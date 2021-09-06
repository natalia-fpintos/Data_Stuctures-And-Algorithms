values = [2, 9, 7, 5, 8, 3, 1, 6, 4]

def selection_sort(values):
  for i in range(len(values)):
    smallest = i
    for j in range(i, len(values)):
      if values[j] < values[smallest]:
        smallest = values[j]
    print("swapping {} for {}".format(values[i], values[smallest]))
    values[i], values[smallest] = values[smallest], values[i]
    
if __name__ == "__main__":
    selection_sort(values)
    print(values)
