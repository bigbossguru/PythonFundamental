import random

def main():
	lenght = input("enter lenght of the list >> ")
	gen_list = [random.randrange(1, 99) for _ in range(int(lenght))]
	print(f"Before sorting list: {gen_list}")
	print(f"After sorting list: {mergeSort(gen_list)}")

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

if __name__ == "__main__":
	main()

