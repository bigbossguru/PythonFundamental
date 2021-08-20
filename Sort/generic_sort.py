from typing import Iterable, TypeVar
from copy import copy

T = TypeVar('T')

def merge_sort(container: Iterable[T]) -> Iterable[T]:
    """ Merge Sort Algorithm """
    pass

def selection_sort(container: Iterable[T]) -> Iterable[T]:
    """ Selection Sort Algorithm """

    length: int = len(container)
    sorted: Iterable[T] = copy(container)

    for i in range(length):
        min_idx: int = i
        for j in range(i+1, length):
            if sorted[j] < sorted[min_idx]:
                min_idx = j
        sorted[i], sorted[min_idx] = sorted[min_idx], sorted[i]
    return sorted

def insertion_sort(container: Iterable[T]) -> Iterable[T]:
    """ Insertion Sort Algorithm """

    length: int = len(container)
    sorted: Iterable[T] = copy(container)

    for i in range(1, length):
        key: T = sorted[i]
        j: int = i-1

        while j>=0 and key<sorted[j]:
            sorted[j+1] = sorted[j]
            j -= 1
        sorted[j+1] = key
    return sorted

def bubble_sort(container: Iterable[T]) -> Iterable[T]:
    """ Bubble Sort Algorithm """

    length: int = len(container)
    sorted: Iterable[T] = copy(container)

    for i in range(length-1):
        for j in range(length-1-i):
            if sorted[j] > sorted[j+1]:
                sorted[j], sorted[j+1] = sorted[j+1], sorted[j]
    return sorted