import time
import random
from typing import Callable, List
import matplotlib.pyplot as plt
import numpy as np


class Analyzer:

    MAXRANGE: int = 100_000

    def __init__(self, length: int, **kwargs: int) -> None:
        self.length = length
        self.step = kwargs.get('step', 500)
        self.start = kwargs.get('start', 0)
        self.__data_iters = self.__generator_iters_list()
    
    def __generator_iters_list(self) -> List[int]:
        return list(range(self.start, self.length, self.step))

    def analyze(self, func: Callable[[List], None]) -> None:
        self.__data_times = list()
        self.__algo_name = func.__name__.replace('_', ' ').capitalize()

        for iter_ in self.__data_iters:
            list_ = random.sample(range(self.MAXRANGE), iter_)
            start_time = time.perf_counter()
            func(list_)
            end_time = time.perf_counter() - start_time
            self.__data_times.append(end_time)
            end_time = start_time = 0.0

    def to_file(self, name: str = 'logger.txt') -> None:
        with open(name, 'a') as f:
            f.write(f'Algorithm: {self.__algo_name}(max: {self.__data_times[-1]:.2f} sec, length: {self.length})\n')
            f.write('times [sec]: [')
            f.write(', '.join(map(lambda x: f'{x:.2f}', self.__data_times)))
            f.write(']\n')
            f.write('iters [i]: [')
            f.write(', '.join(map(str, self.__data_iters)))
            f.write(']\n')

    def display_plot(self) -> None:
        x = np.array(self.__data_times)
        y = np.array(self.__data_iters)
        
        plt.title(self.__algo_name)
        # plt.plot(x, y, 'o')
        a, b, c = np.polyfit(x, y, 2)
        fit_equation = a * np.square(x) + b * x + c
        plt.plot(fit_equation, x)
        plt.xlabel('Iterations [i]')
        plt.ylabel('Time [sec]')
        plt.show()
