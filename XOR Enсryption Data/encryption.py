from secrets import token_bytes
from typing import Tuple

def random_key(lenght: int) -> int:
    random_token: bytes = token_bytes(lenght)
    return int.from_bytes(random_token, "big")

def encrypt(original: str) -> Tuple:
    original_bytes: bytes = original.encode()
    secret_key: int = random_key(len(original_bytes))
    original_key: int = int.from_bytes(original_bytes, "big")
    encrypted: int = secret_key ^ original_key
    return secret_key, encrypted

def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^ key2
    decrypt_original_bytes: bytes = decrypted.to_bytes((decrypted.bit_length()+7)//8, "big")
    return decrypt_original_bytes.decode()

if __name__ == "__main__":
    IN_FILE: bool = False
    string: str = "This message will be encryption and decryption"

    # Encryption string and return two keys 
    key1, key2 = encrypt(original=string)
    keys_string: str = "key1: "+str(key1)+"\nkey2: "+str(key2)

    # Decryption message for help two keys
    decrypt_string: str = decrypt(key1=key1, key2=key2)

    if IN_FILE:
        with open("encryption.txt", "w") as f:
            f.write(keys_string)
            f.write('\n')
            f.write(decrypt_string)
