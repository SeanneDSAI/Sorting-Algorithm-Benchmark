import time
from data_loader.vehicle_data_loader import VehicleDataLoader
from business.vehicle_collection import VehicleCollection
from sorter.bubble_sort import BubbleSort

if __name__ == "__main__":
    print("=" * 42)
    print("  Car Dealership Sorting Demo")
    print("=" * 42)

    # --------------------------------------------------
    # 1. Load Data
    # --------------------------------------------------
    loader = VehicleDataLoader("data/source/vehicles.csv")
    vehicle_data = loader.get_data_by_size(1000)
    print(f"Loaded {len(vehicle_data)} vehicle records.\n")

    # --------------------------------------------------
    # 2. Create VehicleCollection
    # --------------------------------------------------
    dealership = VehicleCollection("Irish Auto Ltd", vehicle_data)
    print("Dealership Summary:")
    print(f"  Total Vehicles : {dealership.total_vehicle_count()}")
    print(f"  Inventory Value: €{dealership.total_inventory_value():,.2f}")
    print(f"  Average Price  : €{dealership.average_price():,.2f}\n")

    # --------------------------------------------------
    # 3. Create Sorter (Strategy Pattern)
    # --------------------------------------------------
    bubble_sort = BubbleSort()

    # --------------------------------------------------
    # 4. Time Sorting by Price
    # --------------------------------------------------
    start = time.perf_counter()
    sorted_by_price = dealership.sort_vehicles(
        bubble_sort,
        key_function=lambda v: v.price
    )
    end = time.perf_counter()
    print(f"BubbleSort by Price – Time: {end - start:.6f} seconds\n")

    # --------------------------------------------------
    # 5. Display Top 10 by Price
    # --------------------------------------------------
    print("Top 10 Most Expensive Vehicles:\n")
    top_10 = dealership.get_top_vehicles(bubble_sort, attribute='price', n=10)
    for vehicle in top_10:
        print(f"  {vehicle}")

    print("\nDemo Complete.")
