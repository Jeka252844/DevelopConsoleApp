import argparse
from solve.series import FORMULAS

ARGS_LIST = ['a', 'b', 'c', 'd', 'e']
MIN_VALUE = -10000
MAX_VALUE = 10000

def series_parser():
    p = argparse.ArgumentParser(
        prog="mathtool series",
        description="",
        epilog="Пример: python mathtool.py series --func third --eps 0.001",
        allow_abbrev=False,
    )

    p.add_argument('--func', required=True, choices=sorted(FORMULAS), help='')

    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument('--eps', type=float, help='число b')
    group.add_argument('--terms', type=int, help='число c')

    return p  
    
def handle_series(args):
    return {
        "func": args.func,
        "eps": args.eps,
        "terms": args.terms,
    }


HANDLERS = {
    "series": (series_parser, handle_series),
}