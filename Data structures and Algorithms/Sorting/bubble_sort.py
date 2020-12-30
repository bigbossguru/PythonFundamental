# Data structure and algorithms
# Bubble Sort
import random

def bubble_sort(arr: list, decrease=False) -> None:
    n = len(arr)

    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
    
    if decrease:
        for i in range(n//2):
            tmp = arr[i]
            arr[i] = arr[n-1-i]
            arr[n-1-i] = tmp
    
def main():
    arr = random.sample(range(-1, 10), 5)    
    print(arr)
    # bubble_sort(arr)
    # print(arr)

    print('Reverse')
    bubble_sort(arr, True)
    print(arr)

if __name__ == "__main__":
    main()