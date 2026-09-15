class Vehicle:
    """
    Represents a single row from the vehicles CSV file.
    Mirrors the Sale/Student model pattern from Labs 5 and 6.
    """

    def __init__(self, vehicle_id, brand, model, year, mileage, engine_size, price):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.year = int(year)
        self.mileage = int(mileage)
        self.engine_size = float(engine_size)
        self.price = float(price)

    def __repr__(self):
        return (
            f"Vehicle({self.vehicle_id}, {self.brand} {self.model}, "
            f"Year={self.year}, Mileage={self.mileage}, "
            f"Engine={self.engine_size}L, Price=€{self.price:,.0f})"
        )
