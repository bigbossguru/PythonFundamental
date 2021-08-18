# Data structure and algorithms
# Linked List

class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        if self.head is None:
            self.head = Node(data=data)
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = Node(data=data)
        self.size += 1

    def add(self, data):
        new_node = Node(data=data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def get_size(self):
        return self.size

    def display(self):
        if self.size == 0:
            print("Linked List is empty")
        else:
            print('Linked List: [', end='')
            current = self.head
            while current.next != None:
                print(f"{current.data},", end=' ')
                current = current.next
            print(f"{current.data}]")
    
    def find(self, index):
        count = 0
        current = self.head
        while current.next != None:
            if count == index:
                return current.data
            current = current.next
            count += 1
        return None
    
    def insert(self, index, data):
        count = 0
        new_node = Node(data=data)
        current = self.head
        while current.next != None:
            if count == index:
                current.next = new_node
            count += 1
            

def main():
    my_list = LinkedList()
    my_list.append(56)
    my_list.append(5)
    my_list.append(3)
    my_list.append(7)
    my_list.add(6)
    my_list.add("Hello")
    my_list.append("Good job")
    my_list.append("Putin")

    print(f"Length linkedList = {my_list.get_size()}")
    my_list.display()
    print(my_list.find(3))


if __name__ == "__main__":
    main()