import logging
import bitwise
from random import randint
from pprint import pprint

DEBUG = 1

def main():
    logging.basicConfig(filename='logger.log', 
                        filemode='w', 
                        format='%(asctime)s - %(levelname)s - %(message)s', 
                        level=logging.INFO)

    register = bitwise.BitWise(123)

    for _ in range(3):
        register.set_bit(random_num())
        logging.info(f'Random set a bit: {register.get_actual_data()}')
        register.unset_bit(random_num())
        logging.info(f'Random unset a bit: {register.get_actual_data()}')
        register.toggle_bit(random_num())
        logging.info(f'Random toggle a bit: {register.get_actual_data()}')
        logging.info(f'Extract random range of bits: {register.extract_range_of_bits(random_num(), random_num())}')

def random_num():
    return randint(1,8)

if __name__ == "__main__":
    main()