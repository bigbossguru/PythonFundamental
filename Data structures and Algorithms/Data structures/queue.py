# Data structure and algorithms
# Queue
# FIFO First In First Out

class Queue(object):
    def __init__(self, queue=[]):
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
    test_queue = Queue()
    print(test_queue.peek())

if __name__ == "__main__":
    main()