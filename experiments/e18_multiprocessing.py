
import multiprocessing


with multiprocessing.Pool() as pool:
    pool.apply(print, args=["Hello, world!"])
