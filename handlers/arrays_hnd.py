import argparse
import sys
from solve.arrays import MIN_VALUE, MAX_VALUE, MAX_COUNT, MAX_SEARCH
from solve.sorting import METHODS

def fill_parser():
    p = argparse.ArgumentParser(prog="mathtool fill", allow_abbrev=False)
    p.add_argument('-c', '--count', type=int, required=True, help='количество элементов')
    p.add_argument('--min', type=int, default=MIN_VALUE, help='минимум')
    p.add_argument('--max', type=int, default=MAX_VALUE, help='максимум')
    p.add_argument('--seed', type=int, help='зерно генератора')
    p.add_argument('-o', '--output', help='файл для записи')
    return p

def handle_fill(args):
    if not (1 <= args.count <= MAX_COUNT):
        raise ValueError(f"ОШИБКА: количество элементов вне диапазона 1..{MAX_COUNT}")
    if args.min > args.max:
        raise ValueError("ОШИБКА: min не может быть больше max")
    if args.min < MIN_VALUE or args.max > MAX_VALUE:
        raise ValueError(f"ОШИБКА: границы должны быть в диапазоне {MIN_VALUE}..{MAX_VALUE}")
    
    return {
        "count": args.count, "min": args.min, "max": args.max, 
        "seed": args.seed, "output": args.output
    }

def sort_parser():
    p = argparse.ArgumentParser(prog="mathtool sort", allow_abbrev=False)
    p.add_argument('-m', '--method', choices=sorted(METHODS), required=True, help='метод сортировки')
    p.add_argument('--order', choices=['asc', 'desc'], default='asc', help='направление')
    p.add_argument('-i', '--input', help='входной файл')
    p.add_argument('-o', '--output', help='выходной файл')
    return p

def handle_sort(args):
    return {
        "method": args.method,
        "descending": (args.order == "desc"),
        "input": args.input,
        "output": args.output
    }

def search_parser():
    p = argparse.ArgumentParser(prog="mathtool search", allow_abbrev=False)
    p.add_argument('-v', '--value', type=int, required=True, help='искомое значение')
    p.add_argument('-i', '--input', help='входной файл')
    return p

def handle_search(args):
    if abs(args.value) > MAX_SEARCH:
        raise ValueError(f"ОШИБКА: модуль значения не должен превышать {MAX_SEARCH}")
    return {"value": args.value, "input": args.input}

HANDLERS = {
    "fill": (fill_parser, handle_fill),
    "sort": (sort_parser, handle_sort),
    "search": (search_parser, handle_search),
}