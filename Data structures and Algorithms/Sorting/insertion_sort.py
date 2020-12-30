# Data structure and algorithms
# Insertion Sort

def insertion_sort(arr: list, decrease=False) -> None:
    n = len(arr)

    for i in range(n-1):
        key = arr[i+1]
        for j in range(i,0,-1):
            if arr[j] > key:
                

    if decrease:
        for i in range(n//2):
            tmp = arr[i]
            arr[i] = arr[n-1-i]
            arr[n-1-i] = tmp

def main():
    arr = [2,5,1,3,0]
    print('Before\n'+'-'*30)
    print(arr)
    #selection_sort(arr)
    print('After\n'+'-'*30)
    print(arr)

if __name__ == "__main__":
    main()