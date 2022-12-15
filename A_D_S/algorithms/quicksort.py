
import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])

def quicksort(values):

    if len(values) <= 1:
        return values

    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]

    for values in values[1:]:
        if values <= pivot:
            less_than_pivot.append(values)
        else:
            greater_than_pivot.append(values)
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

sorted_numbers = quicksort(numbers)
print(sorted_numbers)

