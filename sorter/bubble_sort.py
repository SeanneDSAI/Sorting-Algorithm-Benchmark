from sorter.sorter_adt import Sorter


class BubbleSort(Sorter):
    """
    Bubble Sort implementation.

    Repeatedly compares adjacent elements and swaps them if they are
    in the wrong order.  After each full pass the largest unsorted
    element 'bubbles' to its correct position.

    """

    def sort(self, data: list, key=lambda x: x) -> list:
        arr = data.copy()
        n = len(arr)
        for i in range(n - 1):
            swapped = False                      # early-exit optimisation
            for j in range(0, n - 1 - i):       # shrink inner bound each pass
                if key(arr[j]) > key(arr[j + 1]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:                      # already sorted
                break
        return arr
