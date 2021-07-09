# Data structure and algorithms
# Selection Sort
import random

def selection_sort(arr: list) -> None:
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def main():
    arr = [random.randint(0,95) for _ in range(random.randint(5, 27))]
    print('Unsorted list of integers: ', arr)
    selection_sort(arr)
    print('Sorted list of integers: ', arr)


if __name__ == "__main__":
    main()