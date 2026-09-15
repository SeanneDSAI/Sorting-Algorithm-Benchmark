import time

from data_loader.vehicle_data_loader import VehicleDataLoader
from sorter.bubble_sort import BubbleSort
from sorter.insertion_sort import InsertionSort
from sorter.merge_sort import MergeSort
from sorter.quick_sort import QuickSort
from sorter.selection_sort import SelectionSort


# ---------------------------------------------------------------
# Timing helper (time_sort function)
# ---------------------------------------------------------------

def time_sort(sorter, data, key_function, runs=3):
    """
    Return the average execution time over multiple runs.
    Averaging reduces timing noise from background processes.
    """
    total = 0.0
    for _ in range(runs):
        data_copy = data.copy()
        start = time.perf_counter()
        sorter.sort(data_copy, key=key_function)
        end = time.perf_counter()
        total += (end - start)
    return total / runs


# ---------------------------------------------------------------
# CA1 Table 1 Sort by Price
# ---------------------------------------------------------------

def benchmark_by_price(loader, algorithms):
    """
    CA1 Table 1: Sort all vehicles for a specific range by price.
    Dataset sizes: 250, 500, 1000, 2000, 8000, 16000, 32000, 64000
    """
    dataset_sizes = [250, 500, 1000, 2000, 8000, 16000, 32000, 64000]
    key_function = lambda v: v.price
    results = {name: [] for name in algorithms}

    print("\n" + "=" * 60)
    print("  CA1 TABLE 1 Sort by Price (varying dataset sizes)")
    print("=" * 60)

    for size in dataset_sizes:
        print(f"\nDataset size: {size}")
        data = loader.get_data_by_size(size)
        for name, sorter in algorithms.items():
            elapsed = time_sort(sorter, data, key_function)
            results[name].append(elapsed)
            print(f"  {name:<18}: {elapsed:.6f} seconds")

    print()


# ---------------------------------------------------------------
# CA1 Table 2 Sort by Mileage per year
# ---------------------------------------------------------------

def benchmark_by_year_mileage(loader, algorithms):
    """
    CA1 Table 2: Sort vehicles for each year (2020-2024) by mileage.
    """
    years = [2020, 2021, 2022, 2023, 2024]
    key_function = lambda v: v.mileage

    print("\n" + "=" * 60)
    print("  CA1 TABLE 2 - Sort by Mileage per Year")
    print("=" * 60)

    for year in years:
        data = loader.get_by_year(year)
        print(f"\nYear: {year}  ({len(data)} vehicles)")
        for name, sorter in algorithms.items():
            elapsed = time_sort(sorter, data, key_function)
            print(f"  {name:<18}: {elapsed:.6f} seconds")

    print()


# ---------------------------------------------------------------
# Main
# ---------------------------------------------------------------

def main():
    print("\nLoading vehicle data...")
    loader = VehicleDataLoader("data/source/vehicles.csv")
    print(f"Total records loaded: {loader.get_total_count()}")

    algorithms = {
        "Bubble Sort":    BubbleSort(),
        "Selection Sort": SelectionSort(),
        "Insertion Sort": InsertionSort(),
        "Quick Sort":     QuickSort(),
        "Merge Sort":     MergeSort(),
    }

    print("\nRunning automated performance analysis...")

    benchmark_by_price(loader, algorithms)

    benchmark_by_year_mileage(loader, algorithms)

    print("Performance analysis complete.")


if __name__ == "__main__":
    main()
