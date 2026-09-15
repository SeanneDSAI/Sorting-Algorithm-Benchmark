class VehicleCollection:
    """
    Represents a collection of Vehicle objects for a car dealership.

    """

    def __init__(self, name, vehicles=None):
        self.name = name
        self.__vehicles = vehicles if vehicles is not None else []

    def add_vehicle(self, vehicle):
        """Add a single Vehicle to the collection."""
        self.__vehicles.append(vehicle)

    def get_vehicles(self):
        """Return a copy of the vehicle list (encapsulation)."""
        return self.__vehicles.copy()

    def total_vehicle_count(self):
        """Return the total number of vehicles in the collection."""
        return len(self.__vehicles)

    def total_inventory_value(self):
        """Calculate and return the sum of all vehicle prices."""
        total = 0.0
        for vehicle in self.__vehicles:
            total += vehicle.price
        return total

    def average_price(self):
        """Return the average price of all vehicles."""
        if not self.__vehicles:
            return 0.0
        return self.total_inventory_value() / len(self.__vehicles)

    def sort_vehicles(self, sorter, key_function=lambda x: x):
        """
        Sort the vehicle collection using the provided sorter (Strategy Pattern).

        :param sorter:       Any object implementing the Sorter ADT
        :param key_function: Lambda that extracts the sort key from a Vehicle
        :return:             New sorted list of vehicles
        """
        return sorter.sort(self.__vehicles, key=key_function)

    def get_top_vehicles(self, sorter, attribute='price', n=10):
        """
        Return the top N vehicles sorted by the given attribute (descending).

        :param sorter:    Sorter object (Strategy Pattern)
        :param attribute: Vehicle attribute to sort by ('price','mileage','year','engine_size')
        :param n:         Number of top results to return
        :return:          List of top N vehicles
        """
        key_fn = lambda v: getattr(v, attribute)
        sorted_vehicles = sorter.sort(self.__vehicles, key=key_fn)

        # Collect top N by traversing backwards (ascending -> descending)
        top = []
        index = len(sorted_vehicles) - 1
        while index >= 0 and len(top) < n:
            top.append(sorted_vehicles[index])
            index -= 1
        return top
