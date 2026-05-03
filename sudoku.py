from string_constants import StringConstants
import sys
from collections import deque

def parse_args():
    args = sys.argv[1:]
    if args and len(args[0]) == 81:
        grid_raw = args[0]
        commands = deque(args[1:])
    else:
        grid_raw = None
        commands = None
    return grid_raw, commands

def generate_grid():
    grid = []
    base_row = [1,2,3,4,5,6,7,8,9]
    for band_start in range(3): #repeat 3 times (3 rows per loop) to complete the set of 9 rows total
        row = base_row[band_start:] + base_row[:band_start]
        for _ in range(3): #repeat 3 times (1 row per loop) to complete the set of 3 rows
            grid.append(row[:])
            front = row[:3]
            back = row[3:]
            row = back + front
    return grid

def grid_to_string(grid):
    return "".join(str(cell) for row in grid for cell in row)

def string_to_grid(s):
    grid = []
    for i in range(0, 81, 9):
        row = [int(ch) for ch in s[i:i+9]]
        grid.append(row)
    return grid

def process_single_sudoku_command(command: str):
    if command == StringConstants.QUIT_INPUT:
        print(StringConstants.QUIT)
        sys.exit(0)
    else:
        print(f"Processing command: {command}")

def print_grid(grid):
    pass

def main():
    print(StringConstants.WELCOME)
    grid_raw, commands = parse_args()
    interactive = grid_raw is None
    if interactive: #For actual user
        grid = generate_grid()
        print_grid(grid)
        while True:
            command = input(StringConstants.PROMPT).strip()
            if command:
                process_single_sudoku_command(command)
    else: #For TDD
        grid = string_to_grid(grid_raw)
        print_grid(grid)
        while commands:
            process_single_sudoku_command(commands.popleft())

if __name__ == "__main__":
    main()
