import csv
from models.vehicle import Vehicle


class VehicleDataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.__vehicles = []
        self.load_data()

    def load_data(self):
        """Read the CSV and populate the internal vehicle list."""
        with open(self.file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                vehicle = Vehicle(
                    vehicle_id=row['Vehicle_ID'],
                    brand=row['Brand'],
                    model=row['Model'],
                    year=row['Year'],
                    mileage=row['Mileage'],
                    engine_size=row['Engine_Size'],
                    price=row['Price']
                )
                self.__vehicles.append(vehicle)

    def get_all_data(self):
        """Return a copy of all loaded vehicles (preserves encapsulation)."""
        return self.__vehicles.copy()

    def get_data_by_size(self, size):
        """Return the first 'size' records. Raises ValueError for negative size."""
        if size < 0:
            raise ValueError("Size must be non-negative")
        return self.__vehicles[:size]

    def get_by_year(self, year):
        """Return all vehicles matching the given year."""
        results = []
        for vehicle in self.__vehicles:
            if vehicle.year == year:
                results.append(vehicle)
        return results

    def get_by_brand(self, brand_name):
        """Return all vehicles matching the given brand."""
        results = []
        for vehicle in self.__vehicles:
            if vehicle.brand == brand_name:
                results.append(vehicle)
        return results

    def get_total_count(self):
        """Return total number of loaded vehicles."""
        return len(self.__vehicles)
