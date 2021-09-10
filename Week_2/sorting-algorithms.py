import time

values_selection = [2, 9, 7, 5, 8, 3, 1, 6, 4]
values_bubble = values_selection.copy()
values_bubble_e = values_selection.copy()


def time_algorithm(f):
    def _time(*args, **kwargs):
        start = time.time() * 1000
        f(*args, **kwargs)
        end = time.time() * 1000
        print('Algorithm took {} ms'.format(end - start))

    return _time


@time_algorithm
def selection_sort(values):
    # Iteration in the main list
    for i in range(len(values)):
        smallest = i
        # Iteration in the sub-list after i
        for j in range(i, len(values)):
            if values[j] < values[smallest]:
                smallest = j
        swap(i, smallest, values)


@time_algorithm
def bubble_sort(values):
    # Iteration over all the items
    for _ in values:
        # Comparison of neighbours - largest will end at the end
        for j in range(len(values) - 1):
            if values[j] > values[j + 1]:
                swap(j, j + 1, values)


@time_algorithm
def bubble_sort_enhanced(values):
    is_sorted = False
    last_unsorted_item = len(values) - 1

    # Iterate until the list is sorted
    while not is_sorted:
        # Assume the list is sorted
        is_sorted = True
        # Iterate comparing neighbours
        for i in range(last_unsorted_item):
            if values[i] > values[i + 1]:
                # If we had to swap, the list was not sorted
                swap(i, i + 1, values)
                is_sorted = False
        # Finished a full list pass, so we can assume the last item is now sorted
        last_unsorted_item -= 1


def swap(idx1, idx2, list_ref):
    print("swapping {} for {}".format(list_ref[idx1], list_ref[idx2]))
    list_ref[idx1], list_ref[idx2] = list_ref[idx2], list_ref[idx1]


if __name__ == "__main__":
    # Selection sort
    selection_sort(values_selection)
    print(values_selection)
    print()

    # Bubble sort
    bubble_sort(values_bubble)
    print(values_bubble)
    print()

    # Bubble sort enhanced
    bubble_sort_enhanced(values_bubble_e)
    print(values_bubble_e)
    print()
