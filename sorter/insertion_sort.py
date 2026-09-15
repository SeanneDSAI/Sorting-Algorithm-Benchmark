from sorter.sorter_adt import Sorter


class InsertionSort(Sorter):
    """
    Insertion Sort implementation.

    Builds a sorted sub-list one element at a time by inserting each
    new element into its correct position within the already-sorted
    portion.
    """

    def sort(self, data: list, key=lambda x: x) -> list:
        arr = data.copy()
        for i in range(1, len(arr)):
            current = arr[i]
            j = i - 1
            while j >= 0 and key(arr[j]) > key(current):
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = current
        return arr
