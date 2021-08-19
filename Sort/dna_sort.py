from generic_sort import bubble_sort
from typing import List

def string_to_gen(s: str) -> List[str]:
    gene: List[str] = list()
    for i in range(0, len(s), 3):
        if (i+2) >= len(s): return gene
        codon: str = s[i]+s[i+1]+s[i+2]
        gene.append(codon)
    return gene

if __name__ == "__main__":
    gene_str: str = "CGGAACATCCTTGAAGCTTCGGTAACCAGGGTAGTTCGAGACAT"
    my_gene: List[str] = string_to_gen(gene_str)
    print(my_gene)
    
    print(bubble_sort(my_gene))
    print(sorted(my_gene))