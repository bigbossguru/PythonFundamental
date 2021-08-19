from enum import IntEnum
from typing import List, Tuple, TypeVar
from random import randint
from generic_search import linear_search, Comparable

T = TypeVar('T')

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

if __name__ == "__main__":
    gene_str: str = "CGGAACATCCTTGAAGCTTCGGTAACCAGGGTAGTTCGAGACATGTCCAC"    # gen_genom_string(n=50)
    my_gene: Gene = string_to_gene(s=gene_str)

    # print(my_gene)
    gac: Codon = (Nucleotide.G, Nucleotide.A, Nucleotide.C)
    tga: Codon = (Nucleotide.T, Nucleotide.G, Nucleotide.A)

    print(linear_search(my_gene, gac))  # True
    print(linear_search(my_gene, tga))  # False

    my_sorted_gene: Gene = sorted(my_gene)
    print(Comparable.binary_search(my_sorted_gene, gac))
    print(Comparable.binary_search(my_sorted_gene, tga))

    print(my_gene)
    print()
    print(my_sorted_gene)