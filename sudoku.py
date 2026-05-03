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
    base_row = list(range(1, 10))
    for band_start in range(3): #repeat 3 times (3 rows per loop) to complete the set of 9 rows total
        row = base_row[band_start:] + base_row[:band_start]
        for _ in range(3): #repeat 3 times (1 row per loop) to complete the set of 3 rows
            grid.append(row[:])
            front = row[:3]
            back = row[3:]
            row = back + front
    #Random algo 1: Simple repalce
    for _ in range(10):
        a, b = random.sample(range(1, 10), 2)
        for r in range(9):
            for c in range(9):
                if grid[r][c] == a:
                    grid[r][c] = b
                elif grid[r][c] == b:
                    grid[r][c] = a
    #Random algo 2: row swap
    bands = [[0, 1, 2],[3, 4, 5],[6, 7, 8]]
    b1, b2 = random.sample([0, 1, 2], 2)
    for i in range(3):
        r1 = bands[b1][i]
        r2 = bands[b2][i]
        grid[r1], grid[r2] = grid[r2], grid[r1]
    #Random algo 3: column swap
    stacks = [[0, 1, 2],[3, 4, 5],[6, 7, 8]]
    s1, s2 = random.sample([0, 1, 2], 2)
    for i in range(3):
        c1 = stacks[s1][i]
        c2 = stacks[s2][i]
        for r in range(9):
            grid[r][c1], grid[r][c2] = grid[r][c2], grid[r][c1]
    return grid

def grid_to_string(grid):
    return "".join(str(cell) for row in grid for cell in row)

def string_to_grid(s):
    grid = []
    for i in range(0, 81, 9):
        row = [int(ch) for ch in s[i:i+9]]
        grid.append(row)
    return grid

def check_grid(grid):
    # Check rows
    for r in range(9):
        seen = {}
        for c in range(9):
            val = grid[r][c]
            if val == 0:
                continue
            if val in seen:
                return StringConstants.exist_row(chr(ord('A') + r), str(val))
            seen[val] = True
    # Check columns
    for c in range(9):
        seen = {}
        for r in range(9):
            val = grid[r][c]
            if val == 0:
                continue
            if val in seen:
                return StringConstants.exist_col(str(c + 1), str(val))
            seen[val] = True
    # Check 3x3 subgrids
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            seen = {}
            for r in range(box_row, box_row + 3):
                for c in range(box_col, box_col + 3):
                    val = grid[r][c]
                    if val == 0:
                        continue
                    if val in seen:
                        return StringConstants.exist_subgrid(str(val))
                    seen[val] = True
    return StringConstants.GOOD

def get_hint(grid):
    for r in range(9):
        for c in range(9):
            if grid[r][c] != 0:
                continue
            for num in range(1, 10):
                # simulate placing number
                grid[r][c] = num
                if check_grid(grid) == StringConstants.GOOD:
                    grid[r][c] = 0
                    return r, c, num
                grid[r][c] = 0
    return None

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
    elif command == StringConstants.CHECK_INPUT:
        print(check_grid(usergrid))
        return
    elif command == StringConstants.HINT_INPUT:
        if check_grid(usergrid) == StringConstants.GOOD:
            hint = get_hint(usergrid)
            if hint is None:
                print(StringConstants.DEAD_END)
                return
            r, c, num = hint
            cell = chr(ord('A') + r) + str(c + 1)
            print(StringConstants.hint(cell, str(num)))
            return
        else:
            print(StringConstants.HINT_BLOCKED)
            return
    elif command.endswith(StringConstants.CLEAR_INPUT):
        cell = command[:-5]
        row_char = cell[0]
        col_char = cell[1]
        if row_char not in StringConstants.ROWS or col_char not in StringConstants.COLS:
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
        print(StringConstants.CURRENT)
        print_grid(usergrid)
        return
    elif len(command) == 3: # handle fill command
        cell = command[:2]
        value = command[2]
        row_char = cell[0]
        col_char = cell[1]
        if row_char not in StringConstants.ROWS or col_char not in StringConstants.COLS: # validate cell
            print(StringConstants.invalid_cell(cell))
            return
        if value not in StringConstants.COLS: # validate value
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
        print(StringConstants.CURRENT)
        print_grid(usergrid)
        if check_grid(usergrid) == StringConstants.GOOD and all(0 not in row for row in usergrid):
            reset_game()
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

def reset_game():
    global usergrid
    input(StringConstants.SUCCESS)
    print(StringConstants.WELCOME)
    grid = generate_grid()
    usergrid = ensure_only_30_filled(grid)
    print_grid(usergrid)

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
