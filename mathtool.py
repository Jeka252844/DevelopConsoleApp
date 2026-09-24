import sys, argparse
import math

from handlers import HANDLERS
from solve import SOLVES
from solve import equations, integration, series, stats
from handlers import equations_hnd, integration_hnd, series_hnd, stats_hnd
from usage.py import print_help


def main():
    argv = sys.argv[1:]

    if not argv or argv[0] in ['--help', '-h']:
        print_help()
        return 0

    command, rest = sys.argv[0], sys.argv[1:]

    if command not in HANDLERS:
        print(f"Неизвестная команда {command}", file=sys.stderr)
        return 2
        
    build_parser, handler = HANDLERS[command]
    solve = SOLVES[command]

    parser = build_parser()
    args, unknown = parser.parse_known_args(rest)

    if unknown:
        print(f'Неизвестные аргументы:{unknown}', file=sys.stderr)

    args = handler(args)

    try: 
        name, cond, res = solve(args)
        print(f"  {name} \n {cond} \n {res}")
        return 0
    except ValueError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())