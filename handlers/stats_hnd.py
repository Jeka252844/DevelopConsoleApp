import argparse
import sys
import math

ARGS_LIST = ['a', 'b', 'c', 'd', 'e']
MIN_VALUE = -10000
MAX_VALUE = 10000
MAX_CNT = 20

def stats_parser():
    p = argparse.ArgumentParser(
        prog="mathtool stats",
        description="Подведение статистики чисел.",
        epilog="Пример: python mathtool.py stats --input data.txt или python mathtool.py stats",
        allow_abbrev=False,
    )

    p.add_argument('--input', help='файл с числами')

    return p 
    
def handle_stats(args):
    if args.input:
        with open(args.input, encoding="utf-8-sig") as f:
            return validator(read(f))
    else:
        print("Введите числа (по одному или в строку через пробел)", file=sys.stderr)
        print("Конец ввода: Ctrl+Z + Enter (Windows) или Ctrl+D (Linux)", file=sys.stderr)
        return validator(read(sys.stdin))

def read(source):
    nums = []
    for line in source:
        for word in line.split():
            try:
                nums.append(float(word))
            except ValueError:
                raise ValueError(f'Ряд должен состоять только из чисел.{word} - Не число')

    return nums

def validator(nums:list):
    if not nums:
        raise ValueError("Числа должны быть")

    if len(nums) > MAX_CNT:
        raise ValueError(f"Чисел должно быть не больше {MAX_CNT}") 

    for n in nums:
        if not math.isfinite(n):
            raise ValueError(f'{n} не конечное число')
        
        if n > MAX_VALUE or n < MIN_VALUE:
            raise ValueError(f"ОШИБКА: числа не должны быть меньше {MIN_VALUE} или превышать {MAX_VALUE}")

    return nums

HANDLERS = {
    "stats": (stats_parser, handle_stats),
}