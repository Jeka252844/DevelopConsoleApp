import sys, argparse
import math
from solve.equations import quadratic, integral
from args_handler import handler

# Глобальные перменнные
MAX_VALUE = 10_000
MIN_VALUE = -10_000

COMMANDS = {
    'quadratic': quadratic,
    'integral': integral,
}

def main():
    command = sys.argv[0]
    if command in COMMANDS:
        args = handler(command)
        
    else:
        print(f'Неизвестная комманда {command}')
        # argparse
        sys.exit(1)

if __name__ == "__main__":
    main()