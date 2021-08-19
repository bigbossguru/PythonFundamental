from typing import List

def string_to_gen(s: str) -> List[str]:
    gene: List[str] = list()
    for i in range(0, len(s), 3):
        if (i+2) >= len(s): return gene
        codon: str = s[i]+s[i+1]+s[i+2]
        gene.append(codon)
    return gene

def binary_search(gene: List[str], key_codon: str) -> bool:
    low: int = 0
    high: int = len(gene)-1
    while low <= high:
        mid: int = (high + low) // 2
        if gene[mid] < key_codon:
            low = mid + 1
        elif gene[mid] > key_codon:
            high = mid - 1
        else:
            return True
    return False

if __name__ == "__main__":
    gen_str = "GGGAGTTATTGATGCTACTGGTGACCTAAGCATTCCACCAGCACGCGCGC"  #gen_genom_string(n=50)
    my_gene: List[str] = string_to_gen(s=gen_str)
    my_sorted_gene: List[str] = sorted(my_gene)


    print(my_gene)
    print(my_sorted_gene)

    print(binary_search(gene=my_gene, key_codon='AAA'))
    
    print(binary_search(gene=my_gene, key_codon='TAT'))
