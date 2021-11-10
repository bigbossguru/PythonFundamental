class Node:
	def __init__(self, val) -> None:
		self.value = val
		self.next_ = None
		self.prev_ = None
	
	def __repr__(self):
		return f"Node (value:{self.value}, next: {self.next_}, prev: {self.prev_})"

class DoubleLinkedList:
	def __init__(self) -> None:
		self.head = None
	
	def pop(self):
		pass

	def push(self, val):
		if self.head is None:
			self.head = Node(val)
		else:
			current: Node = self.head
			while current.next_:
				current = current.next_
			current.next_ = Node(val)
			current.next_.prev_ = current

	def popleft(self):
		pass

	def __repr__(self) -> str:
		result = ''
		current = self.head
		while current.next_:
			result += f'({current})'
			current = current.next_
		return f'{DoubleLinkedList.__name__} [{result}]'


if __name__ == "__main__":
	list_t = DoubleLinkedList()
	list_t.push(5)
	list_t.push(7)
	list_t.push(9)
	print(list_t)