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


def quick_sort(arr, descending=False):
    stack = [(0, len(arr) - 1)]
    while stack:
        lo, hi = stack.pop()
        if lo >= hi:
            continue
        pivot = arr[(lo + hi) // 2]
        i, j = lo, hi
        while i <= j:
            while is_out_of_order(pivot, arr[i], descending):
                i += 1
            while is_out_of_order(arr[j], pivot, descending):
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        if lo < j:
            stack.append((lo, j))
        if i < hi:
            stack.append((i, hi))
    return arr


def merge_sort(arr, descending=False):
    n = len(arr)
    width = 1
    while width < n:
        for lo in range(0, n, 2 * width):
            mid = min(lo + width, n)
            hi  = min(lo + 2 * width, n)
            left  = arr[lo:mid]
            right = arr[mid:hi]
            i = j = 0
            k = lo
            while i < len(left) and j < len(right):
                if is_out_of_order(left[i], right[j], descending):
                    arr[k] = right[j]; j += 1
                else:
                    arr[k] = left[i];  i += 1
                k += 1
            while i < len(left):
                arr[k] = left[i];  i += 1; k += 1
            while j < len(right):
                arr[k] = right[j]; j += 1; k += 1
        width *= 2
    return arr

def heap_sort(arr, descending=False):
    n = len(arr)

    # 1. Построение кучи (bottom-up)
    for start in range((n - 2) // 2, -1, -1):
        root, last = start, n - 1
        while 2 * root + 1 <= last:
            child = 2 * root + 1
            swap = root
            if is_out_of_order(arr[child], arr[swap], descending):
                swap = child
            if child + 1 <= last and is_out_of_order(arr[child + 1], arr[swap], descending):
                swap = child + 1
            if swap == root:
                break
            arr[root], arr[swap] = arr[swap], arr[root]
            root = swap

    # 2. Извлечение корня в конец
    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        root, last = 0, end - 1
        while 2 * root + 1 <= last:
            child = 2 * root + 1
            swap = root
            if is_out_of_order(arr[child], arr[swap], descending):
                swap = child
            if child + 1 <= last and is_out_of_order(arr[child + 1], arr[swap], descending):
                swap = child + 1
            if swap == root:
                break
            arr[root], arr[swap] = arr[swap], arr[root]
            root = swap

    return arr

METHODS = {
    "bubble": bubble_sort,
    "selection": selection_sort,
    "insertion": insertion_sort,
    "counting": counting_sort,
    "quick": quick_sort,
    "merge": merge_sort,
    "heap": heap_sort,
}