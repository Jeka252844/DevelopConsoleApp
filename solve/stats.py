import math

def total(args):
    # return sum(args)
    res = 0
    for a in args:
        res += a
    return res

def mean(args):
    return total(args) / len(args)

def sum_squares(values):
    result = 0
    for v in values:
        result += v ** 2
    return result

def rms(values):
    return math.sqrt(sum_squares(values) / len(values))


# -------отклонения-------

def sum_sq_deviations(values):
    m = mean(values)
    result = 0
    for v in values:
        result += (v - m) ** 2
    return result

def variance(values):
    return sum_sq_deviations(values) / len(values)

def std_dev(values):
    return math.sqrt(variance(values))

def sample_std(values):
    if len(values) < 2:
        return None
    return math.sqrt(sum_sq_deviations(values) / (len(values) - 1))

# -----экстремумы---------

def minimum(values):
    result = values[0]
    for v in values:
        if v < result:
            result = v
    return result

def maximum(values):
    res = values[0]
    for v in values:
        if v > res:
            res = v
    return res

# ------подсчёты----

def count_positive(values):
    res = 0
    for v in values:
        if v > 0:
            res += 1
    return res

def count_negative(values):
    res = 0
    for v in values:
        if v < 0:
            res += 1
    return res


REPORT = [
    ("Количество",    len,            "d"),
    ("Сумма",         total,          ".3f"),
    ("Ср. арифм.",    mean,           ".3f"),
    ("Сумма кв.",     sum_squares,    ".3f"),
    ("Ср. кв.",       rms,            ".3f"),
    ("Дисперсия",     variance,       ".3f"),
    ("СКО",           std_dev,        ".3f"),
    ("Станд. откл.",  sample_std,     ".3f"),
    ("Наименьшее",    minimum,        ".3f"),
    ("Наибольшее",    maximum,        ".3f"),
    ("Положительных", count_positive, "d"),
    ("Отрицательных", count_negative, "d"),
]

def solve_stats(args):
    lines = []
    for name, func ,cl in REPORT:
        value = func(args)
        if value is None:
            lines.append(f"{name}: НЕ СУЩЕСТВУЕТ")
        else:
            lines.append(f"{name}: {value:{cl}}")
    return lines

COMMANDS = {
    "stats": solve_stats,
}