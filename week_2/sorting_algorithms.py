from utils.utils import time_algorithm, data, big_data


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
    list_ref[idx1], list_ref[idx2] = list_ref[idx2], list_ref[idx1]


if __name__ == "__main__":
    # Selection sort
    values_selection = data.copy()
    selection_sort(values_selection)
    print(values_selection)
    print()

    # Bubble sort
    values_bubble = data.copy()
    bubble_sort(values_bubble)
    print(values_bubble)
    print()

    # Bubble sort enhanced
    values_bubble_e = data.copy()
    bubble_sort_enhanced(values_bubble_e)
    print(values_bubble_e)
    print()

    # Selection sort - large dataset
    big_data_selection = big_data.copy()
    selection_sort(big_data_selection)
    print()

    # Bubble sort - large dataset
    big_data_bubble = big_data.copy()
    bubble_sort(big_data_bubble)
    print()

    # Bubble sort enhanced - large dataset
    big_data_bubble_e = big_data.copy()
    bubble_sort_enhanced(big_data_bubble_e)
    print()
