import random


def partition(values, left, right, rng):
    """Разбиение Ломуто. Возвращает окончательный индекс опорного."""
    q = rng.randint(left, right)
    values[q], values[right] = values[right], values[q]
    pivot = values[right]
    i = left
    for j in range(left, right):
        if values[j] <= pivot:
            values[i], values[j] = values[j], values[i]
            i += 1
    values[i], values[right] = values[right], values[i]
    return i

def statistic(values, k, seed=None):
    """k-я порядковая статистика (quickselect, циклическая версия)."""
    if not isinstance(k, int) or isinstance(k, bool):
        raise ValueError("k должно быть целым числом")
    if not (1 <= k <= len(values)):
        raise ValueError(f"k вне диапазона 1..{len(values)}")

    rng = random.Random(seed)
    target = k - 1
    left = 0
    right = len(values) - 1

    while left < right:
        p = partition(values, left, right, rng)
        if target == p:
            return values[p]
        if target < p:
            right = p - 1
        else:
            left = p + 1

    return values[left]