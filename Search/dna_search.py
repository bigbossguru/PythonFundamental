from enum import IntEnum
from typing import List, Tuple
from random import randint

Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
Gene = List[Codon]

def gen_genom_string(n: int) -> str:
    sample: str = 'ACGT'
    genom: str = ""
    for i in range(n):
        genom += sample[randint(0,3)]
    return genom

def string_to_gene(s: str) -> Gene:
    gene: Gene = list()
    for i in range(0, len(s), 3):
        if (i+2) >= len(s): return gene
        codon: Codon = (Nucleotide[s[i]], Nucleotide[s[i+1]], Nucleotide[s[i+2]])
        gene.append(codon)
    return gene

def linear_search_contains(gene: Gene, key_codon: Codon) -> bool:
    for codon in gene:
        if codon == key_codon:
            return True
    return False

def binary_search_contains(gene: Gene, key_codon: Codon) -> bool:
    low: int = 0
    high: int = len(gene)-1
    while low <= high:
        mid: int = (low + high) // 2
        if gene[mid] < key_codon:
            low = mid+1
        elif gene[mid] > key_codon:
            high = mid-1
        else:
            return True
    return False

if __name__ == "__main__":
    gene_str: str = "CGGAACATCCTTGAAGCTTCGGTAACCAGGGTAGTTCGAGACATGTCCAC"    # gen_genom_string(n=50)
    my_gene: Gene = string_to_gene(s=gene_str)

    # print(my_gene)
    gac: Codon = (Nucleotide.G, Nucleotide.A, Nucleotide.C)
    tga: Codon = (Nucleotide.T, Nucleotide.G, Nucleotide.A)

    print(linear_search_contains(gene=my_gene, key_codon=gac))  # True
    print(linear_search_contains(gene=my_gene, key_codon=tga))  # False

    my_sorted_gene: Gene = sorted(my_gene)
    print(binary_search_contains(gene=my_gene, key_codon=gac))  # True
    print(binary_search_contains(gene=my_gene, key_codon=tga))  # False

    print(my_gene)
    print()
    print(my_sorted_gene)