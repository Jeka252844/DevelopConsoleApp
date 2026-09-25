import math

# ---------- подынтегральные функции ----------

def f_ratio(x):
    """x / (x + 1)"""
    return x / (x + 1)


def f_root(x):
    """sqrt(x^2 + 1)"""
    return math.sqrt(x * x + 1)

FORMULS = {
    "ratio": (f_ratio, "F(x) = x / (x + 1)", 0, 20, False),
    "root":  (f_root, "F(x) = sqrt(x^2 + 1)", -5,  5, True),
}

def solve_integrate(values):
    """values = {"func": ..., "str_f": ... "start": ..., "end": ..., "steps": ...}.
    Возвращает [formula, data, result]."""
    result = integral(values['func'], values["start"], values["end"], values["steps"])
    return [
        f"формула: {values['str_f']}", 
        f"начало: {values['start']}, конец: {values['end']}, шагов: {values['steps']}", 
        f"результат: {result}"]

def integral(f, a, b, steps):
    """Метод левых прямоугольников."""
    dx = (b - a) / steps
    total = 0
    for i in range(steps):
        x = a + i * dx
        total += f(x) * dx
    return total


COMMANDS = {
    "integrate": solve_integrate
}