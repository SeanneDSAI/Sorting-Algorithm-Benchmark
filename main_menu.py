import time
from data_loader.vehicle_data_loader import VehicleDataLoader
from business.vehicle_collection import VehicleCollection
from sorter.bubble_sort import BubbleSort
from sorter.insertion_sort import InsertionSort
from sorter.merge_sort import MergeSort
from sorter.quick_sort import QuickSort
from sorter.selection_sort import SelectionSort


def print_menu():
    print("\n========== Car Dealership Menu ==========")
    print("1. Show total vehicle count")
    print("2. Show total inventory value")
    print("3. Choose sorting algorithm")
    print("4. Sort vehicles (using selected algorithm)")
    print("5. Show Top N vehicles")
    print("6. Exit")
    print("=========================================")


def choose_sorter():
    print("\nChoose Sorting Algorithm:")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Quick Sort")
    print("5. Merge Sort")
    choice = input("Enter choice: ")

    match choice:
        case "1":
            return BubbleSort()
        case "2":
            return SelectionSort()
        case "3":
            return InsertionSort()
        case "4":
            return QuickSort()
        case "5":
            return MergeSort()
        case _:
            print("Invalid choice. Defaulting to Quick Sort.")
            return QuickSort()


def choose_attribute():
    """Allow the user to choose which vehicle attribute to sort by."""
    print("\nSort by which attribute?")
    print("1. Price")
    print("2. Mileage")
    print("3. Year")
    print("4. Engine Size")
    choice = input("Enter choice: ")

    match choice:
        case "1":
            return 'price',      lambda v: v.price
        case "2":
            return 'mileage',    lambda v: v.mileage
        case "3":
            return 'year',       lambda v: v.year
        case "4":
            return 'engine_size', lambda v: v.engine_size
        case _:
            print("Invalid. Defaulting to Price.")
            return 'price', lambda v: v.price


def main():
    # Load data
    loader = VehicleDataLoader("data/source/vehicles.csv")
    vehicle_data = loader.get_data_by_size(10000)

    # Create dealership collection
    dealership = VehicleCollection("Irish Auto Ltd", vehicle_data)

    # Default sorter 
    current_sorter = QuickSort()
    current_attr, current_key = 'price', lambda v: v.price

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                print(f"Total Vehicle Records: {dealership.total_vehicle_count()}")

            case "2":
                print(f"Total Inventory Value: €{dealership.total_inventory_value():,.2f}")

            case "3":
                current_sorter = choose_sorter()
                current_attr, current_key = choose_attribute()
                print(f"Algorithm: {current_sorter.__class__.__name__}  |  "
                      f"Sort key: {current_attr}")

            case "4":
                start = time.perf_counter()
                sorted_vehicles = dealership.sort_vehicles(
                    current_sorter,
                    key_function=current_key
                )
                end = time.perf_counter()
                print(f"\nSorting completed in {end - start:.6f} seconds.")
                print("First 5 results (ascending):")
                for v in sorted_vehicles[:5]:
                    print(f"  {v}")

            case "5":
                n = int(input("Enter N: "))
                print(f"Retrieving top {n} vehicles using "
                      f"{current_sorter.__class__.__name__} on {current_attr}...")
                top = dealership.get_top_vehicles(current_sorter,
                                                  attribute=current_attr, n=n)
                print(f"\nTop {n} Vehicles by {current_attr}:")
                for v in top:
                    print(f"  {v}")

            case "6":
                print("Exiting program...")
                break

            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
