# Data structure and algorithms
# Stack
# LIFO Last In First Out

class Stack(object):
    def __init__(self, stack=[]):
        self.stack = stack

    def is_empty(self):
        return self.stack == []
    
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        self.stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.stack[len(self.stack)-1]
    
    def __str__(self):
        return str(self.stack)
    
    def __len__(self):
        return len(self.stack)

def main():
    test_stack = Stack()
    print(test_stack.peek())

if __name__ == "__main__":
    main()