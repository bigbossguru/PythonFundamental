class BitWise:
    def __init__(self, value):
        self.value = value
    
    def set_bit(self, bit):
        self.value |= (1 << (bit-1))
    
    def unset_bit(self, bit):
        self.value &= ~(1 << (bit-1))
    
    def toggle_bit(self, bit):
        self.value ^= (1 << (bit-1))

    def extract_range_of_bits(self, start, stop):
        mask = sum(map(lambda x: 2**x, list(range(start-1, stop))))
        int_val = (self.value & mask) >> (start-1)
        return {'dec': int_val,
                'bin': bin(int_val),
                'hex': hex(int_val),
                'mask': bin(mask)}

    def get_actual_data(self):
        return {'dec': self.value,
                'bin': bin(self.value),
                'hex': hex(self.value)}