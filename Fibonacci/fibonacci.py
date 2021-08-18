from typing import Dict, Generator
from functools import lru_cache

memo: Dict[int, int] = {0:0, 1:1}
def fibo_recursive_v1(n: int) -> int:
    if n not in memo:
        memo[n] = fibo_recursive_v1(n - 1) + fibo_recursive_v1(n - 2)
    return memo[n]

@lru_cache(maxsize=None)
def fibo_recursive(n: int) -> int:
    if n < 2:
        return n
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)

def fibo_generator(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0: yield 1
    last: int = 0
    next: int = 1

    for _ in range(1, n):
        last, next = next, last+next
        yield next

if __name__ == "__main__":
    number_from_sequence_fibo_v1 = fibo_recursive_v1(n=50)
    number_from_sequence_fibo = fibo_recursive(n=50)
    sequence_fibonacci = [i for i in fibo_generator(n=50)]
