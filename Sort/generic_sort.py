from typing import Iterable, TypeVar
from copy import copy

T = TypeVar('T')

def merge_sort(container: Iterable[T]) -> Iterable[T]:
    """ Merge Sort Algorithm """
    
    length: int = len(container)
    sorted: int = copy(container)

    if length > 1:
        mid: int = length // 2

        left: Iterable[T] = merge_sort(sorted[:mid])
        right: Iterable[T] = merge_sort(sorted[mid:])

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted[k] = left[i]
                i += 1
            else:
                sorted[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            sorted[k] = left[i]
            i += 1
            k += 1
            
        while j < len(right):
            sorted[k] = right[j]
            j += 1
            k += 1
    return sorted

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


def quick_sort(container: Iterable[T]) -> Iterable[T]:
    """ Quick Sort Algorithm """

    length: int = len(container)
    sorted: Iterable[T] = copy(container)

    left: int = 0
    right: int = length - 1

    def _qs(container: Iterable[T], left: int, right: int) -> None:
        def partition(container: Iterable[T], left: int, right: int) -> int:
            pivot: int = container[right]
            i = left - 1

            for j in range(left, right):
                if container[j] <= pivot:
                    i += 1
                    container[i], container[j] = container[j], container[i]
            container[i+1], container[right] = container[right], container[i+1]
            return i+1
        
        if left < right:
            part_idx = partition(container, left, right)
            _qs(container, left, part_idx-1)
            _qs(container, part_idx+1, right)

    _qs(sorted, left, right)

    return sorted



