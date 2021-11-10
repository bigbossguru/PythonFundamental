import time
from analyzer import Analyzer
import PythonFundamental.Sort.generic_sort as sort_

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter() - start
        print(f"spend time: {end:.3f} sec")
    return wrapper

if __name__ == "__main__":
    algo_test = Analyzer(length=5000, step=500)
    algo_test.analyze(sort_.selection_sort)
    algo_test.display_plot()
    algo_test.to_file()