import time
import numpy


# Small datasets
data = [2, 9, 7, 5, 8, 3, 1, 6, 4]
sorted_data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Large datasets
big_data = numpy.random.randint(0, 101, 1000)  # 1000 random ints between 0-100 inclusive
very_big_data = numpy.random.randint(0, 101, 10000)  # 1000 random ints between 0-100 inclusive

sorted_big_data = list(range(1001))
sorted_very_big_data = list(range(10001))


def time_algorithm(f):
    def _time(*args, **kwargs):
        start = time.time() * 1000
        result = f(*args, **kwargs)
        end = time.time() * 1000
        print('Algorithm took {} ms'.format(end - start))
        return result

    return _time
