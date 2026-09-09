import sys
import argparse
import traceback

MAX_VALUE = 10_000
MIN_VALUE = -10_000

def main():
    parser, args = get_command()

    if args.command == 'solve':
        if args.a is not None and args.b is not None and args.c is not None:
            try:
                a, b, c = validator(args.a, args.b, args.c)

                return solve(a, b, c)
            except ValueError as e:
                traceback.print_exc(file=sys.stderr)
                return 1
        else:
            try:
                a, b, c = get_input_data(args.a, args.b, args.c)

                return solve(a, b, c)
            except ValueError as e:
                print(e, )
                return 1
    else:
        parser.print_help()

def get_command():
    parser = argparse.ArgumentParser(
        description='Программа для решения уравнений вида a*x**2 + b*x + c = 0',
        epilog='Пример: "python mathtool.py solve -a 3 -b 2 -c -12"'
    )
    subparsers = parser.add_subparsers(dest='command', help='Доступные команды')
    solve_parser = subparsers.add_parser('solve', help='Решать')

    solve_parser.add_argument('-a', default=None, help='Число a')
    solve_parser.add_argument('-b', default=None, help='Число b')
    solve_parser.add_argument('-c', default=None, help='Число c')

    args = parser.parse_args()
    return parser, args 

def validator(a, b, c):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
    except:
        raise ValueError("Ошибка: надо ввести ЦЕЛЫЕ числа(1, -8, 12, 4)")

    if min([a, b, c]) < -MIN_VALUE or max([a, b, c]) > MAX_VALUE:
        raise ValueError(f"ОШИБКА: числа не должны быть меньше {MIN_VALUE} или превышать {MAX_VALUE}")

    print(f"Введены a = {a}, b = {b}, c = {c}\n")
    return a, b, c

def get_input_data(a=None, b=None, c=None):
    print(f"Введите целые числа не от {MIN_VALUE} до {MAX_VALUE}")

    # nums = [a, b, c] #Не удобно ):
    # names = ['a', 'b', 'c']

    # for i in range(3):
    #     if nums[i] is None:
    #         nums[i] = int(input(f'{names[i]} : '))
    #     else:
    #         print(f'Число {names[i]} уже введено')

    # return validator(*nums)

    a = int(input('Введите a : ')) if a is None else print(f'Число a уже введено') or a
    b = int(input('Введите b : ')) if b is None else print('Число b уже введено') or b
    c = int(input('Введите c : ')) if c is None else print('Число c уже введено') or c

    return validator(a, b, c)

def solve(a, b, c):
    if a==0 and b==0:
        raise ValueError("Ошика: a и b равны нулю. Не уравнение")
    elif a == 0:
        print("Линейное уравнение\n")
        x = -c / b
        print(f"x = {x:.3f}")
        return 0
    else:
        print("Квадратное уравнение\n")

        D = b**2 - (4 * a * c)
        if D < 0:
            print(f" D = {D} < 0 \n Действительных корней нет")
            return 0
        elif D == 0:
            x = -b / (2*a)
            print(f" D = 0 \n x = {x:.2f}")
            return 0
        else:
            x1 = (-b + D**(1/2)) / (2*a)
            x2 = (-b - D**(1/2)) / (2*a)
            print(f" D = {D} > 0 \n x1 = {x1:.3f} \n x2 = {x2:.3f}")

    

if __name__ == "__main__":
    main()