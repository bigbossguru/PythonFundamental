import multiprocessing
import random

def rand_num():
    print(random.random())

if __name__ == "__main__":
    queue = multiprocessing.Queue()

    processes = [multiprocessing.Process(target=rand_num) for _ in range(4)]

    for p in processes:
        p.start()
    
    for p in processes:
        p.join()