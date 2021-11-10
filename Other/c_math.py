import ctypes
import pathlib

libpath = pathlib.Path().absolute().joinpath('adder.so').as_posix()
adder = ctypes.CDLL(libpath)

print(adder.add_int(2,3))
print(adder.add_float(ctypes.c_float(2.5), ctypes.c_float(4.6)))
print(adder.range_(10))