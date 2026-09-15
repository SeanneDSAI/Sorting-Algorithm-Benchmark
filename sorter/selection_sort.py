from sorter.sorter_adt import Sorter


class SelectionSort(Sorter):
    """
    Selection Sort implementation.

    Divides the list into a sorted and an unsorted region.  On each
    pass it selects the minimum element from the unsorted region and
    moves it to the end of the sorted region.
    """

    def sort(self, data: list, key=lambda x: x) -> list:
        arr = data.copy()
        n = len(arr)
        for i in range(n - 1):
            min_idx = i
            for j in range(i + 1, n):
                if key(arr[j]) < key(arr[min_idx]):
                    min_idx = j
            if min_idx != i:
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
