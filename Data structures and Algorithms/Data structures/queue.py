# Data structure and algorithms
# Queue
# FIFO First In First Out
import random

class Queue(object):
    def __init__(self, queue):
        self.queue = queue
    
    def is_empty(self):
        return self.queue == []
    
    def enqueue(self, value):
        self.queue.append(value)
    
    def dequeue(self):
        self.queue.remove(self.queue[0])

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
    
    def __str__(self):
        return str(self.queue)
    
    def __len__(self):
        return len(self.queue)

def main():
    arr = [random.randint(0, 95) for _ in range(random.randint(5, 15))]
    print('Original list of integers: ', arr)
    queue = Queue(arr)
    print('Peek method: ', queue.peek())
    queue.dequeue()
    print('After used Dequeue method: ', arr)
    queue.enqueue(9999)
    print('After used Enqueue method: ', arr)
    print('Control is empty queue: ', queue.is_empty())

if __name__ == "__main__":
    main()