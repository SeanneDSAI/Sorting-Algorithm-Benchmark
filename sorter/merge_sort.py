from sorter.sorter_adt import Sorter


class MergeSort(Sorter):
    """
    Merge Sort implementation.

    Divide-and-conquer algorithm that recursively splits the list in
    half, sorts each half, then merges them back in sorted order.
    """

    def sort(self, data: list, key=lambda x: x) -> list:
        arr = data.copy()
        return self._merge_sort(arr, key)

    def _merge_sort(self, arr, key):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self._merge_sort(arr[:mid], key)
        right = self._merge_sort(arr[mid:], key)
        return self._merge(left, right, key)

    def _merge(self, left, right, key):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if key(left[i]) <= key(right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
