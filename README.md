# Vehicle Sorting and Inventory Analysis

A Python application that loads a large vehicle dataset, models it as a dealership inventory, and sorts it using five classic sorting algorithms that are implemented from scratch. It also measures and compares how long each algorithm takes as the dataset grows.

## What it does

- Reads vehicle records from a CSV file and turns each row into a `Vehicle` object
- Groups those objects into a `VehicleCollection` that can report inventory totals and averages
- Sorts the collection by price, mileage, year or engine size using any of five sorting algorithms
- Returns the top N vehicles for a chosen attribute
- Times each algorithm across a range of dataset sizes so their performance can be compared directly

All sorting logic is written by hand. No built-in sorting functions are used.

## Project structure

```
C24384533_CA1_Code/
├── main.py                 Simple demo run
├── main_menu.py            Interactive menu program
├── main_tester.py          Automated performance benchmarks
├── models/
│   └── vehicle.py          Vehicle object, one per CSV row
├── data_loader/
│   └── vehicle_data_loader.py   Reads the CSV and filters records
├── business/
│   └── vehicle_collection.py    Inventory logic and sorting entry points
├── sorter/
│   ├── sorter_adt.py       Abstract Sorter interface
│   ├── bubble_sort.py
│   ├── selection_sort.py
│   ├── insertion_sort.py
│   ├── quick_sort.py
│   └── merge_sort.py
└── data/
    └── source/vehicles.csv Dataset
```

## Design

The code is split into layers so each part has one job:

- **Model layer** holds the `Vehicle` class, which converts raw CSV strings into typed fields (year and mileage as integers, engine size and price as floats).
- **Data layer** holds `VehicleDataLoader`, which reads the CSV once at startup and keeps the records private. It exposes methods to fetch all records, the first N records, or records filtered by year or brand. Every getter returns a copy so the internal list cannot be modified from outside.
- **Business layer** holds `VehicleCollection`, which knows about inventory totals, average price and top-N queries, but knows nothing about how sorting works.
- **Sorting layer** defines an abstract `Sorter` class with a single `sort(data, key)` method. Each algorithm subclasses it.

`VehicleCollection.sort_vehicles()` accepts any object that implements `Sorter`, so the sorting algorithm can be swapped at runtime without changing the collection code. This is the strategy pattern.

Every sorter copies the input list before sorting, so the original data is never changed and repeated benchmark runs all start from the same unsorted order.

Sorting is driven by a key function rather than fixed comparisons, so the same algorithm can sort by any attribute:

```python
dealership.sort_vehicles(QuickSort(), key_function=lambda v: v.price)
```

## Algorithms

| Algorithm | Average time | Notes |
|---|---|---|
| Bubble sort | O(n²) | Includes an early-exit flag that stops once a pass makes no swaps |
| Selection sort | O(n²) | Always scans the full unsorted region, so the swap count stays low |
| Insertion sort | O(n²) | Fast on data that is already close to sorted |
| Quick sort | O(n log n) | Last element used as the pivot, in-place partitioning |
| Merge sort | O(n log n) | Recursive split and merge, stable, uses extra memory |

## Running it

Python 3.10 or later is required. The menu program uses `match` statements. No external packages are needed.

Run from inside the `C24384533_CA1_Code` folder so the relative path to the dataset resolves:

```bash
python main.py          # short demo: loads 1000 records, sorts by price, shows the top 10
python main_menu.py     # interactive menu over 10,000 records
python main_tester.py   # full benchmark suite
```

### Demo (`main.py`)

Loads 1000 vehicles, prints the inventory summary, sorts by price with bubble sort, reports the elapsed time and lists the ten most expensive vehicles.

### Menu (`main_menu.py`)

An interactive loop over 10,000 records. Options:

1. Show total vehicle count
2. Show total inventory value
3. Choose a sorting algorithm and a sort attribute
4. Sort with the current selection and report the time taken
5. Show the top N vehicles
6. Exit

Quick sort on price is the default until something else is chosen.

### Benchmarks (`main_tester.py`)

Runs all five algorithms and prints two sets of results:

- **By dataset size:** sorting by price at 250, 500, 1000, 2000, 8000, 16000, 32000 and 64000 records
- **By year:** sorting by mileage within each model year from 2020 to 2024

Each measurement is the average of three runs on a fresh copy of the data, which smooths out timing noise from other processes on the machine. Times are taken with `time.perf_counter()`.

Note that the quadratic algorithms get slow quickly at the larger sizes, so the full run takes a while to finish.

## Dataset

`data/source/vehicles.csv` with the columns:

`Vehicle_ID`, `Brand`, `Model`, `Year`, `Mileage`, `Engine_Size`, `Price`

To use a different dataset, keep the same column names and point the loader at the new file path.
