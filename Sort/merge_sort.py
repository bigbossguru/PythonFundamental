# Data structure and algorithms
# Merge Sort
import random
from typing import List

def mergeSort(list: list) -> List[int]:
	size: int = len(list)
	if size > 1:
		mid: int = size // 2
		left: list = mergeSort(list[:mid])
		right: list = mergeSort(list[mid:])

		i = j = k = 0
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				list[k] = left[i]
				i += 1
			else:
				list[k] = right[j]
				j += 1
			k += 1

		while i < len(left):
			list[k] = left[i]
			i += 1
			k += 1

		while j < len(right):
			list[k] = right[j]
			j += 1
			k += 1
	return list


def main() -> None:
	arr: List[int] = [random.randint(0, 95) for _ in range(random.randint(5, 27))]
	print('Unsorted list of integers: ', arr)
	mergeSort(arr)
	print('Sorted list of integers: ', arr)


if __name__ == "__main__":
	main()
