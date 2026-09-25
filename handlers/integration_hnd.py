import argparse
import math
from solve.integration import FORMULS

ARGS_LIST = ['a', 'b', 'c', 'd', 'e']
MAX_STEPS = 500

def integrate_parser():
    p = argparse.ArgumentParser(
        prog="mathtool integrate",
        description="Решение интегралов",
        epilog="Пример: python mathtool.py integral --func root --from 1 --to 7 --steps 9",
        allow_abbrev=False,
    )
    p.add_argument("--func", required=True, choices=sorted(FORMULS), help="Функция интеграла")
    p.add_argument('--from', required=True, dest='start', type=int, help='число начала')
    p.add_argument('--to', required=True, dest="end", type=int, help='число конца')
    p.add_argument('--steps', default=1, type=int, help='шаг интегрирования')

    return p 
    
def handle_integrate(args):
    func = args.func
    start = args.start
    end = args.end
    steps = args.steps
    return validator(func, start, end, steps)



def validator(func, start, end, steps):
    if start >= end:
        raise ValueError("начальный предел должен быть меньше конечного")

    if not (math.isfinite(start) and math.isfinite(end)):
        raise ValueError("пределы должны быть конечными числами")

    if not 1 <= steps <= MAX_STEPS:
        raise ValueError(f"шагов должно быть от1 до{MAX_STEPS}")

    f, str_f, low, high, strict = FORMULS[func]

    if strict:
        if start <= low or end >= high:
            raise ValueError(f"пределы должны быть ({low}; {high})")
    else:
        if start < low or end > high:
            raise ValueError(f"пределы должны быть [{low}; {high}]")

    return {"func": f, "str_f":str_f, "start": start, "end": end, "steps": steps}

HANDLERS = {
    "integrate": (integrate_parser, handle_integrate),
}