import math

from utils.utils import time_algorithm, sorted_data, sorted_big_data, sorted_very_big_data, data, big_data, \
    very_big_data


@time_algorithm
def linear_search(item, values):
    """Find `item` in `values` comparing with all items"""

    for i, v in enumerate(values):
        if v == item:
            return "Item {0} found at position {1}".format(v, i)
    return "Item not found"


@time_algorithm
def binary_search(item, sorted_values):
    start = 0
    end = len(sorted_values) - 1
    while True:
        if end < start or end > len(sorted_values) - 1 or start < 0:
            return "Item not found"

        middle = math.floor((start + end) / 2)
        if item > sorted_values[middle]:
            start = middle + 1
            continue
        if item < sorted_values[middle]:
            end = middle - 1
            continue
        return "Item {0} found at position {1}".format(item, middle)


@time_algorithm
def binary_search_recursive(item, sorted_values):
    """Find `item` in a sorted list `sorted_values` using divide and conquer"""

    if not sorted_values:
        return "Item not found"

    middle = math.floor(len(sorted_values) / 2)
    if item > sorted_values[middle]:
        return binary_search_recursive(item, sorted_values[middle + 1:])
    if item < sorted_values[middle]:
        return binary_search_recursive(item, sorted_values[:middle])
    return "Item {0} found at position {1}".format(item, middle)


if __name__ == "__main__":
    print("-------Linear search-------")
    print(linear_search(4, data))
    print(linear_search(23, big_data))
    print(linear_search(120, very_big_data))
    print()

    print("-------Binary search-------")
    print(binary_search(1, sorted_data))
    print(binary_search(5, sorted_data))
    print(binary_search(3, sorted_data))
    print()

    print("-------Binary search - large dataset-------")
    print(binary_search(1, sorted_big_data))
    print(binary_search(5, sorted_very_big_data))
    print()

    print("-------Binary search recursive-------")
    print(binary_search_recursive(1, sorted_data))
    print(binary_search_recursive(5, sorted_data))
    print(binary_search_recursive(3, sorted_data))
    print()

    print("-------Binary search recursive - large dataset-------")
    print(binary_search_recursive(1, sorted_big_data))
    print(binary_search_recursive(5, sorted_very_big_data))
