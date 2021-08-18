# Data structure and algorithms
# Linked List

from typing import Any


class Node:
    def __init__(self, data: Any, next: int = None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head: Node = None
        self.size: int = 0

    def append(self, data: Any) -> None:
        if self.head is None:
            self.head = Node(data=data)
        else:
            current: Node = self.head
            while current.next != None:
                current = current.next
            current.next = Node(data=data)
        self.size += 1

    def add(self, data: Any) -> None:
        new_node = Node(data=data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def get_size(self) -> int:
        return self.size

    def display(self) -> None:
        if self.size == 0:
            print("Linked List is empty")
        else:
            print('Linked List: [', end='')
            current = self.head
            while current.next != None:
                print(f"{current.data},", end=' ')
                current = current.next
            print(f"{current.data}]")
    
    def find(self, index) -> None:
        count: int = 0
        current: Node = self.head
        while current.next != None:
            if count == index:
                return current.data
            current = current.next
            count += 1
    
    def insert(self, index: int, data: Any) -> None:
        count: int = 0
        new_node: Node = Node(data=data)
        current: Node = self.head
        while current.next != None:
            if count == index:
                current.next = new_node
            count += 1
            

def main() -> None:
    my_list: LinkedList = LinkedList()
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