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

def generate_grid():
    grid = []
    base_row = [1,2,3,4,5,6,7,8,9]
    for band_start in range(3):
        # create the first row of this band
        row = base_row[band_start:] + base_row[:band_start]
        # now generate 3 rows in this band (all shifts of 3)
        for _ in range(3):
            grid.append(row[:])
            # shift by 3 every time (your rule)
            front = row[:3]
            back = row[3:]
            row = back + front
    return grid

def grid_to_string(grid):
    return "".join(str(cell) for row in grid for cell in row)

def string_to_grid(s):
    if len(s) != 81:
        raise ValueError("String must be exactly 81 characters")
    grid = []
    for i in range(0, 81, 9):
        row = [int(ch) for ch in s[i:i+9]]
        grid.append(row)
    return grid

def process_single_sudoku_command(command: str):
    if command == StringConstants.QUIT_INPUT:
        print(StringConstants.QUIT)
    else:
        print(f"Processing command: {command}")

def main():
    print(StringConstants.WELCOME)
    grid, commands = parse_args()
    interactive = grid is None
    if interactive: #For actual user
        grid = generate_grid()
        while True:
            command = input(StringConstants.PROMPT).strip()
            if command:
                process_single_sudoku_command(command)
    else: #For TDD
        while commands:
            process_single_sudoku_command(commands.popleft())

if __name__ == "__main__":
    main()
