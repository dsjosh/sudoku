from string_constants import StringConstants
import sys
from collections import deque

def parse_args():
    args = sys.argv[1:]
    if args and len(args[0]) == 81:
        grid = args[0]
        commands = deque(args[1:])
    else:
        grid = None
        commands = None
    return grid, commands

def process_single_sudoku_command(command: str):
    print(f"Processing command: {command}")

def main():
    print(StringConstants.WELCOME)
    grid, commands = parse_args()
    interactive = grid is None
    if interactive: #For actual user
        while True:
            command = input(StringConstants.PROMPT).strip()
            if command == StringConstants.QUIT_INPUT:
                print(StringConstants.QUIT)
            if command:
                process_single_sudoku_command(command)
    else: #For TDD
        while commands:
            process_single_sudoku_command(commands.popleft())

if __name__ == "__main__":
    main()
