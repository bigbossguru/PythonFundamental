import logging
import bitwise
from random import randint

def main() -> None:
    logging.basicConfig(filename='logger.log', 
                        filemode='w', 
                        format='%(asctime)s - %(levelname)s - %(message)s', 
                        level=logging.INFO)

    register: bitwise.BitWise = bitwise.BitWise(value=123)

    for _ in range(3):
        register.set_bit(bit=random_num())
        logging.info(f'Random set a bit: {register.get_actual_data()}')
        register.unset_bit(bit=random_num())
        logging.info(f'Random unset a bit: {register.get_actual_data()}')
        register.toggle_bit(bit=random_num())
        logging.info(f'Random toggle a bit: {register.get_actual_data()}')
        logging.info(f'Extract random range of bits: {register.extract_range_of_bits(random_num(), random_num())}')

def random_num() -> int:
    return randint(1,8)

if __name__ == "__main__":
    main()