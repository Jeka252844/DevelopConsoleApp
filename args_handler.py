import argparse
ARGS_LIST = ['a', 'b', 'c', 'd', 'e']
MIN_VALUE = -10000
MAX_VALUE = 10000

def handler(self):
    parser = argparse.ArgumentParser(
        description=('Программа для решения математических задач'),
        epilog='Примеры использования: ' \
        '\nРешение квадратных уравнений - ' \
        '"python mathtool.py quadratic -a 3 -b 2 -c -12"' \
        '\n' \
        '""'
    )
    
    subparser = parser.add_subparsers(dest='command', help='Доступные комманды')
    return 
    
def quadratic_args(parser, subparser):
    quadratic_parser = subparser.add_parser(
        'quadratic', help='Команда для решения квадратных уравнений'
    )
    quadratic_parser.add_argument('-a', default=None, help='число a')
    quadratic_parser.add_argument('-b', default=None, help='число b')
    quadratic_parser.add_argument('-c', default=None, help='число c')
    args, unknown = parser.parser_known_args()

    return validator(3, unknown, {"a": args.a, 'b': args.b, 'c': args.c})

def validator(cnt:int, unknown:list, values:dict):
    arg_err = 'a'
    names = ARGS_LIST[0:cnt-1]
    nums = {}        
    try:
        for name in names:
            arg_err = name
            if values[name]:
                nums[name] = int(values[name])
            else:
                nums[name] = int(input(f'введите число {name}'))
    except:
        raise ValueError(
            f"Ошибка папаметра {arg_err}: надо ввести ЦЕЛЫЕ числа от {MIN_VALUE} до {MAX_VALUE}"
            )

    if min(list(vars(nums).values())) < MIN_VALUE or max(list(vars(nums).values())) > MAX_VALUE:
        raise ValueError(f"ОШИБКА: числа не должны быть меньше {MIN_VALUE} или превышать {MAX_VALUE}")

    return nums, unknown
