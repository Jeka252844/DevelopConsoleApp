import argparse
import sys

ARGS_LIST = ['a', 'b', 'c', 'd', 'e']
MIN_VALUE = -10000
MAX_VALUE = 10000

def quadratic_parser():
    p = argparse.ArgumentParser(
        prog="mathtool quadratic",
        description="Решение квадратного уравнения",
        epilog="Пример: python mathtool.py quadratic -a 1 -b -3 -c 2",
        allow_abbrev=False,
    )

    p.add_argument('-a', type=int, help='число a')
    p.add_argument('-b', type=int, help='число b')
    p.add_argument('-c', type=int, help='число c')

    return p 
    
def handle_quadratic(args):
    return validator(3, {"a": args.a, 'b': args.b, 'c': args.c})

def validator(cnt:int, values:dict):
    names = ARGS_LIST[0:cnt]
    nums = {}

    for name in names:        
        if values[name] is not None:
            nums[name] = values[name]
        else:   
            try:
                nums[name] = int(input(f'введите целое число {name}'))
            except ValueError:
                raise ValueError(
                    f"Ошибка папаметра {name}: надо ввести ЦЕЛЫЕ числа от {MIN_VALUE} до {MAX_VALUE}"
                )

    if min(list(nums.values())) < MIN_VALUE or max(list(nums.values())) > MAX_VALUE:
        raise ValueError(f"ОШИБКА: числа не должны быть меньше {MIN_VALUE} или превышать {MAX_VALUE}")

    return nums


HANDLERS = {
    "quadratic": (quadratic_parser, handle_quadratic),
}