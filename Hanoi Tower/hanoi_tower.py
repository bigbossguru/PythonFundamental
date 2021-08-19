from typing import Generic, List, TypeVar

T = TypeVar('T')
class Stack(Generic[T]):
    def __init__(self) -> None:
        self.__container: List[T] = list()
    
    def push(self, item: T) -> None:
        self.__container.append(item)

    def pop(self) -> T:
        return self.__container.pop()

    def __repr__(self) -> str:
        return repr(self.__container)


def hanoi_tower(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:
    if n == 1: end.push(begin.pop())
    else:
        hanoi_tower(begin, temp, end, n-1)
        hanoi_tower(begin, end, temp, 1)
        hanoi_tower(temp, end, begin, n-1)

if __name__ == "__main__":
    numbers_of_discs: int = 10
    tower_a: Stack[int] = Stack()
    tower_b: Stack[int] = Stack()
    tower_c: Stack[int] = Stack()

    for i in range(1, numbers_of_discs+1):
        tower_a.push(i)

    hanoi_tower(tower_a, tower_b, tower_c, numbers_of_discs)
    print(tower_a)
    print(tower_b)
    print(tower_c)