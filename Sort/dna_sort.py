from generic_sort import insertion_sort, selection_sort
from typing import List


if __name__ == "__main__":
    list_of_numbers: List[int] = [3,7,2,1,5,4]
    original_list_of_codons: List[str] = ['CGG', 'AAC', 'ATC', 'CTT', 'GAA', 'GCT', 'TCG', 'GTA', 'ACC', 'AGG', 'GTA', 'GTT']

    print("Original Genom:\t\t\t", original_list_of_codons)
    print("Standart sort in Python:\t", sorted(original_list_of_codons))
    print("Original Genom:\t\t\t", original_list_of_codons)
    print("Insertion sort custom:\t\t", insertion_sort(original_list_of_codons))
    print("Original Genom:\t\t\t", original_list_of_codons)
    print("Selection sort custom:\t\t", selection_sort(original_list_of_codons))
    print("Original Genom:\t\t\t", original_list_of_codons)