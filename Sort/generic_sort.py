from typing import Iterable, TypeVar
from copy import copy

T = TypeVar('T')

def bubble_sort(container: Iterable[T]) -> Iterable[T]:
    """ Bubble Sort Algorithm """

    l: int = len(container)
    sorted: Iterable[T] = copy(container)

    for i in range(l-1):
        for j in range(l-1-i):
            if sorted[j] > sorted[j+1]:
                sorted[j], sorted[j+1] = sorted[j+1], sorted[j]
    return sorted