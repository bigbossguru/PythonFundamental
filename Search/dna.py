from typing import List
from generic_search import linear_search, Comparable

def string_to_gen(s: str) -> List[str]:
    gene: List[str] = list()
    for i in range(0, len(s), 3):
        if (i+2) >= len(s): return gene
        codon: str = s[i]+s[i+1]+s[i+2]
        gene.append(codon)
    return gene


if __name__ == "__main__":
    gen_str = "GGGAGTTATTGATGCTACTGGTGACCTAAGCATTCCACCAGCACGCGCGC"  #gen_genom_string(n=50)
    my_gene: List[str] = string_to_gen(s=gen_str)
    my_sorted_gene: List[str] = sorted(my_gene)


    print(my_gene)
    print(my_sorted_gene)

    print(Comparable.binary_search(my_gene, 'AAA'))
    print(Comparable.binary_search(my_gene, 'TAT'))
