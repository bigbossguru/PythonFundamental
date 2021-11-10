from typing import NamedTuple
from collections import deque
from types import SimpleNamespace
import heapq

class Car(NamedTuple):
    model: str
    color: str
    spz: str

class OwnIterator:
    def __init__(self, val, max_size) -> None:
        self.val = val
        self.max_size = max_size
        self.count = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.max_size:
            raise StopIteration
        self.count += 1
        return self.val

lada = Car('VAZ2110', 'blue', '5CZ7654')
vasa = SimpleNamespace(name='Vasa', age=29)

LIFO = deque([4,7,0,2,3,5,8])
FIFO = deque([9,8,1,5,8,3,2])

q = []

heapq.heappush(q, (2, 'sleep'))
heapq.heappush(q, (3, 'drink'))
heapq.heappush(q, (1, 'coding'))



LIFO.append(2)
FIFO.append(3)

print(LIFO.pop())
print(FIFO.popleft())

print(lada.color, lada.model, lada.spz)

vasa.last = 'Bodrov'
print(vasa)

while q:
    print(heapq.heappop(q))

for i in OwnIterator('Hello', 3):
    print(i)