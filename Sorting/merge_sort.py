# Data structure and algorithms
# Merge Sort
import random

def mergeSort(list):
	size = len(list)
	if size > 1:
		mid = size // 2
		left = mergeSort(list[:mid])
		right = mergeSort(list[mid:])

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


def main():
	arr = [random.randint(0, 95) for _ in range(random.randint(5, 27))]
	print('Unsorted list of integers: ', arr)
	mergeSort(arr)
	print('Sorted list of integers: ', arr)


if __name__ == "__main__":
	main()
