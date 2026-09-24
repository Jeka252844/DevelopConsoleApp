import argparse

ARGS_LIST = ['a', 'b', 'c', 'd', 'e']
MIN_VALUE = -10000
MAX_VALUE = 10000

def series_parser():
    p = argparse.ArgumentParser(
        prog="mathtool series",
        description="",
        epilog="Пример: python mathtool.py quadratic -a 1 -b -3 -c 2",
        allow_abbrev=False,
    )

    p.add_argument('--func', required=True, help='')

    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument('--eps', type=int, help='число b')
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