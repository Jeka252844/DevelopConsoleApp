import sys
import random

MIN_VALUE = -100
MAX_VALUE = 100
MAX_COUNT = 1_000_000
MAX_SEARCH = 1000

def read_array(path=None):
    """Читает массив из файла или stdin."""
    if path:
        with open(path, encoding="utf-8-sig") as f:
            text = f.read()
    else:
        print("Введите числа (пустая строка для завершения):", file=sys.stderr)
        lines = []
        while True:
            try:
                line = input()
                if not line.strip():
                    break
                lines.append(line)
            except EOFError:
                break
        text = " ".join(lines)
    
    text = text.replace(",", " ")
    words = text.split()
    
    try:
        values = [int(w) for w in words]
    except ValueError:
        raise ValueError("Ошибка: найдены не целые числа")
    
    if not (1 <= len(values) <= MAX_COUNT):
        raise ValueError(f"Ошибка: количество элементов вне диапазона 1..{MAX_COUNT}")
    for v in values:
        if not (MIN_VALUE <= v <= MAX_VALUE):
            raise ValueError(f"Ошибка: значение {v} вне диапазона {MIN_VALUE}..{MAX_VALUE}")
            
    return values

def write_array(values, path=None):
    """Записывает массив в файл или возвращает строку для вывода."""
    result_str = " ".join(str(x) for x in values)
    if path:
        with open(path, "w", encoding="utf-8") as f:
            f.write(result_str + "\n")
        return f"Записано элементов: {len(values)} в файл {path}"
    return result_str

def fill_array(count, low=MIN_VALUE, high=MAX_VALUE, seed=None):
    """Генерирует список случайных чисел."""
    random.seed(seed)
    return [random.randint(low, high) for _ in range(count)]

def binary_search(arr, target):
    """Двоичный поиск. Возвращает индекс или None."""
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None
