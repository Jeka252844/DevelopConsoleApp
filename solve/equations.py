import math

def solve_quadratic(args: dict):
    a, b, c = args['a'], args['b'], args['c']

    if a==0 and b==0:
        raise ValueError("Ошика: a и b равны нулю. Не уравнение")
    elif a == 0:
        x = -c / b
        return ["Линейное уравнение",  f"x = {x:.3f}"]
    else:
        D = b**2 - (4 * a * c)
        if D < 0:
            return ["Квадратное уровнение", f"D = {str(D)}", "Действительных корней нет"]
        elif D == 0:
            x = -b / (2*a)
            return ["Квадратное уравнение", "D = 0", f"x = {x:.3f}"]
        else:
            x1 = (-b + math.sqrt(D)) / (2*a)
            x2 = (-b - math.sqrt(D)) / (2*a)
            return[ "Квадратное уровнение", f"D = {str(D)}", f"x1 = {x1:.3f}, x2 = {x2:.3f}"]

COMMANDS = {
    'quadratic': solve_quadratic,
}