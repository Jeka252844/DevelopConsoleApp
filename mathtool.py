import sys, argparse
import math

from handlers import HANDLERS
from solve import SOLVES
from solve import equations, integration, series, stats
from handlers import equations_hnd, integration_hnd, series_hnd, stats_hnd
from usage import print_help


def main():
    argv = sys.argv[1:]

    if not argv or argv[0] in ['--help', '-h']:
        print_help()
        return 0

    command, rest = sys.argv[0], sys.argv[1:]

    if command not in HANDLERS:
        print(f"ОШИБКА: yеизвестная команда {command}", file=sys.stderr)
        print_help()
        return 2
        
    build_parser, handler = HANDLERS[command]
    solve = SOLVES[command]

    parser = build_parser()
    args, unknown = parser.parse_known_args(rest)

    if unknown:
        print(f'Предупреждение: неизвестные аргументы:{unknown}', file=sys.stderr)

    try: 
        args = handler(args)

        result = solve(args)
        for r in result:
            print(f"{r}", file=sys.stdout)
        return 0
    except ValueError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(e, file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())