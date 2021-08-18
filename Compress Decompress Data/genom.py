from random import randint
from typing import Dict
from sys import getsizeof

class GenomCompressDecompress:
    __nucleotides: Dict[str, int] = {"A": 0b00, "C": 0b01, "G": 0b10, "T": 0b11}

    def __init__(self, genom: str) -> None:
        self.genom = genom
    
    def compressed(self) -> int:
        self.bits_string: int = 1
        for nucleotide in self.genom:
            if nucleotide in self.__nucleotides:
                self.bits_string <<= 2
                self.bits_string |= self.__nucleotides[nucleotide]
            else:
                raise ValueError("Invalid Nucleotide: {}".format(nucleotide))
        return self.bits_string
    
    def decompressed(self) -> str:
        decompress_genom: str = ""
        for i in range(0, self.bits_string.bit_length()-1, 2):
            bits: int = self.bits_string >> i & 0b11
            for nucleotide, bit in self.__nucleotides.items():
                if bits == bit: 
                    decompress_genom += nucleotide
                    break
        return decompress_genom[::-1]

def generate_GenomDNA(lenght: int) -> str:
    sample: str = "ATGC"
    genom: str = ""
    for _ in range(lenght):
        genom += sample[randint(0,3)]
    return genom

if __name__ == "__main__":
    IN_FILE: bool = True
    genom: str = generate_GenomDNA(lenght=5000)
    genom_manipulation: GenomCompressDecompress = GenomCompressDecompress(genom=genom)
    compress_genom: int = genom_manipulation.compressed()
    decompress_genom: str = genom_manipulation.decompressed()
    compare_genom: bool = genom == decompress_genom

    if IN_FILE:
        with open("genom.txt", "w") as f:
            f.write(genom)
            f.write("\n------------------------------------\n")
            f.write(f"Original string: {getsizeof(genom)} bytes")
            f.write("\n------------------------------------\n")
            f.write(bin(compress_genom))
            f.write("\n------------------------------------\n")
            f.write(f"Compressed bits string: {getsizeof(compress_genom)} bytes")
            f.write("\n------------------------------------\n")
            f.write(decompress_genom)
            f.write("\n------------------------------------\n")
            f.write(f"Compare: {compare_genom}")
