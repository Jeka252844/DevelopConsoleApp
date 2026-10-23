import sys
import time
from solve.arrays import read_array, write_array, fill_array, binary_search
from solve.sorting import METHODS

def solve_fill(args):
    arr = fill_array(args['count'], args['min'], args['max'], args['seed'])
    result = write_array(arr, args['output'])
    return [result]

def measure_time(name, operation, params):
    """Замер времени выполнения операции."""
    start = time.perf_counter()
    result = operation(*params)
    elapsed = time.perf_counter() - start
    print(f"Время операции {name}: {elapsed:.6f} с", file=sys.stderr)
    return result

def solve_sort(args):
    arr = read_array(args['input'])
    method_name = args['method']
    method_func = METHODS[method_name]
    descending = args['descending']
    
    # Замеряем только сортировку
    measure_time(f"sort ({method_name})", method_func, [arr, descending])
    
    result = write_array(arr, args['output'])
    return [result, "Массив отсортирован."]

def solve_search(args):
    arr = read_array(args['input'])
    
    # Проверка на упорядоченность по возрастанию
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            raise ValueError("ОШИБКА: массив не упорядочен по возрастанию")
            
    index = binary_search(arr, args['value'])
    if index is None:
        raise ValueError(f"Значение {args['value']} не найдено.")
    
    return [f"Значение {args['value']} имеет элемент с индексом {index + 1}."]

COMMANDS = {
    "fill": solve_fill,
    "sort": solve_sort,
    "search": solve_search
}