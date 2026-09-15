from sorter.sorter_adt import Sorter


class QuickSort(Sorter):
    """
    Quick Sort implementation.

    Divide-and-conquer algorithm that picks the last element as the
    pivot, partitions the list into elements less than and greater
    than the pivot, then recursively sorts each partition.
    """

    def sort(self, data: list, key=lambda x: x) -> list:
        arr = data.copy()
        self._quick_sort(arr, 0, len(arr) - 1, key)
        return arr

    def _quick_sort(self, arr, low, high, key):
        if low < high:
            pivot_idx = self._partition(arr, low, high, key)
            self._quick_sort(arr, low, pivot_idx - 1, key)
            self._quick_sort(arr, pivot_idx + 1, high, key)

    def _partition(self, arr, low, high, key):
        pivot = key(arr[high])   # use last element as pivot
        i = low - 1
        for j in range(low, high):
            if key(arr[j]) <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
