from typing import Iterable, TypeVar

T = TypeVar('T')

def bubble_sort(container: Iterable[T]) -> Iterable[T]:
    """ Bubble Sort Algorithm """

    l: int = len(container)
    sorted: Iterable[T] = list()

    for i in range(l-1):
        for j in range(l-1-i):
            if container[j] > container[j+1]:
                sorted.append(container[j+1], container[j])
    return sorted