from solve.arrays import MIN_VALUE, MAX_VALUE

def is_out_of_order(a, b, descending=False):
    """Проверяет, нарушен ли порядок (по возрастанию или убыванию)."""
    if descending:
        return a < b
    return a > b

def bubble_sort(arr, descending=False):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if is_out_of_order(arr[j], arr[j+1], descending):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

def selection_sort(arr, descending=False):
    n = len(arr)
    for i in range(n - 1):
        best = i
        for j in range(i + 1, n):
            if is_out_of_order(arr[best], arr[j], descending):
                best = j
        arr[i], arr[best] = arr[best], arr[i]

def insertion_sort(arr, descending=False):
    n = len(arr)
    for i in range(1, n):
        current = arr[i]
        j = i
        while j > 0 and is_out_of_order(arr[j-1], current, descending):
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = current

def counting_sort(arr, descending=False):
    counters = [0] * (MAX_VALUE - MIN_VALUE + 1)
    for val in arr:
        counters[val - MIN_VALUE] += 1
    
    k = 0
    indices = range(len(counters))
    if descending:
        indices = reversed(indices)
        
    for idx in indices:
        for _ in range(counters[idx]):
            arr[k] = idx + MIN_VALUE
            k += 1

METHODS = {
    "bubble": bubble_sort,
    "selection": selection_sort,
    "insertion": insertion_sort,
    "counting": counting_sort
}