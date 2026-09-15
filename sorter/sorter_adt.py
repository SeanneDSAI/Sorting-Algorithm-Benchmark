from abc import ABC, abstractmethod


class Sorter(ABC):
    """
    Abstract Data Type: Sorter

    Defines the interface for all sorting algorithms.
    """

    @abstractmethod
    def sort(self, data: list, key=lambda x: x) -> list:
        """
        Sorts the given list using the provided key function.

        :param data: List of elements to sort
        :param key:  Function that extracts the comparison value
        :return:     New sorted list (original is not modified)
        """
        pass
