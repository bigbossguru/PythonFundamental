# from __future__ import annotations

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next_ = None

class LinkedList:
    def __init__(self, *args) -> None:
        self.head = None
        for arg in args:
            self.append(arg)
    
    def append(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            current = self.head
            while current.next_:
                current = current.next_
            current.next_ = Node(val)

    def add(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            new_node = Node(val)
            new_node.next_ = self.head
            self.head = new_node

    def insert(self, val, pos):
        if self.head is None:
            self.head = Node(val)
        else:
            current = self.head
            prev: Node = None
            index = 0
            while current:
                if pos == index:
                    new_node = Node(val)
                    prev.next_ = new_node
                    new_node.next_ = current
                prev = current
                current = current.next_
                index += 1

    def sort(self):
        pass

    def popleft(self):
        if self.head is None:
            raise IndexError('pop from empty list')
        prev = self.head
        self.head = self.head.next_
        return prev.value

    def pop(self):
        current = self.head
        prev = None
        while current.next_:
            prev = current
            current = current.next_
        
        last_element = current.value
        prev.next_ = None
        return last_element

    @property
    def is_empty(self):
        return not self.__len__()

    def __repr__(self) -> str:
        result = '['
        result += ', '.join(map(str, self))
        result += ']'
        return result

    def __getitem__(self, position):

        index = 0
        current = self.head

        if isinstance(position, int):
            while current:
                if index == position:
                    return current.value
                current = current.next_
                index += 1
            raise IndexError('Index is out of range')
        elif isinstance(position, slice):
            sublist_ = LinkedList()
            while current:
                if (index >= position.start) and (index <= position.stop):
                    sublist_.append(current.value)
                current = current.next_
                index += 1
            
            if sublist_.is_empty: raise IndexError('Index must be ascending or Index is out of range')
            return sublist_

        raise IndexError('Invalid index')

    def __iter__(self):
        self.__index = 0
        return self
    
    def __next__(self):
        if self.__index < self.__len__():
            res = self.__getitem__(self.__index)
            self.__index += 1
            return res

        raise StopIteration

    def __len__(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next_
        return length


if __name__ == "__main__":

    list_ = LinkedList(1,'python',3,4,5,6,7)
    list_.append('Cool')
    list_.append(2)
    list_.append(3)
    list_.append('Hi')
    print('Length: ',len(list_))
    print('Linked List: ', list_)

    print(list_.popleft())
    print('Linked List: ', list_)

    list_.add(99)
    list_.add(99)
    list_.add(99)
    list_.add(99)
    print('Linked List: ', list_)

    list_.insert(123, 4)
    print('Linked List: ', list_)

    t = [9,3,7, 'Bob', 0,1,2,'Hi']

    t.sort()
    print(t)