# Data structure and algorithms
# Selection Sort

def selection_sort(arr: list, decrease=False) -> None:
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    if decrease:
        for i in range(n//2):
            tmp = arr[i]
            arr[i] = arr[n-1-i]
            arr[n-1-i] = tmp

def main():
    arr = [2,5,1,3,0]
    print('Before\n'+'-'*30)
    print(arr)
    selection_sort(arr)
    print('After\n'+'-'*30)
    print(arr)

if __name__ == "__main__":
    main()