from string_constants import StringConstants
import sys
from collections import deque
import random

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
    global usergrid, initial_usergrid
    if len(command) == 0:
        print(StringConstants.UNRECOGNISED)
        return
    command = command.replace(" ", "").upper()
    if command == StringConstants.QUIT_INPUT:
        print(StringConstants.ACCEPT_INPUT)
        print(StringConstants.QUIT)
        sys.exit(0)
    if command.endswith("CLEAR"):
        cell = command[:-5]
        row_char = cell[0]
        col_char = cell[1]
        if row_char not in "ABCDEFGHI" or col_char not in "123456789":
            print(StringConstants.invalid_cell(cell))
            return
        row = ord(row_char) - ord('A')
        col = int(col_char) - 1
        if initial_usergrid[row][col] != 0:
            print(StringConstants.prefilled(cell))
            return
        if usergrid[row][col] == 0:
            print(StringConstants.not_filled(cell))
            return
        usergrid[row][col] = 0
        print(StringConstants.ACCEPT_INPUT)
        print_grid(usergrid)
        return
    elif len(command) == 3: # handle fill command
        cell = command[:2]
        value = command[2]
        row_char = cell[0]
        col_char = cell[1]
        if row_char not in "ABCDEFGHI" or col_char not in "123456789": # validate cell
            print(StringConstants.invalid_cell(cell))
            return
        if value not in "123456789": # validate value
            print(StringConstants.invalid_value(value))
            return
        row = ord(row_char) - ord('A')
        col = int(col_char) - 1
        if initial_usergrid[row][col] != 0:
            print(StringConstants.prefilled(cell))
            return
        if usergrid[row][col] != 0:
            print(StringConstants.filled(cell))
            return
        usergrid[row][col] = int(value)
        print(StringConstants.ACCEPT_MOVE)
        print_grid(usergrid)
        return
    else:
        print(StringConstants.UNRECOGNISED)
        return

def ensure_only_30_filled(grid):
    global initial_usergrid
    # Flatten all positions (row, col)
    positions = [(r, c) for r in range(9) for c in range(9)]
    # Randomly pick 30 unique positions to KEEP
    keep_positions = set(random.sample(positions, 30))
    # Set everything else to 0
    for r in range(9):
        for c in range(9):
            if (r, c) not in keep_positions:
                grid[r][c] = 0
    initial_usergrid = [row[:] for row in grid]
    return grid

def print_grid(grid):
    print("    " + " ".join(str(i) for i in range(1, 10))) # Column header
    for idx, row in enumerate(grid):
        row_label = chr(ord('A') + idx)
        formatted_row = []
        for cell in row:
            if cell == 0:
                formatted_row.append("_")
            else:
                formatted_row.append(str(cell))
        print(f"  {row_label} " + " ".join(formatted_row))
    print("")

def main():
    global usergrid
    print(StringConstants.WELCOME)
    grid_raw, commands = parse_args()
    interactive = grid_raw is None
    if interactive: #For actual user
        grid = generate_grid()
        usergrid = ensure_only_30_filled(grid)
        print_grid(usergrid)
        while True:
            command = input(StringConstants.PROMPT).strip()
            process_single_sudoku_command(command)
    else: #For TDD
        grid = string_to_grid(grid_raw)
        usergrid = ensure_only_30_filled(grid)
        print_grid(usergrid)
        while commands:
            process_single_sudoku_command(commands.popleft())

if __name__ == "__main__":
    main()
