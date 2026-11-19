from solve.sorting import bubble_sort, insertion_sort, selection_sort, counting_sort
from solve.arrays_solve import measure_time

with open("testpy.txt", "r") as f:
    text = f.read()

data = text.split()
data = [int(x) for x in data]

measure_time("bubble_sort", bubble_sort, [data.copy()])
measure_time("insertion_sort", insertion_sort, [data.copy()])
measure_time("selection_sort", selection_sort, [data.copy()])
measure_time("counting_sort", counting_sort, [data.copy()])