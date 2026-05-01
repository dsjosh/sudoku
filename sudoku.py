from string_constants import StringConstants
import sys
from collections import deque

print(StringConstants.user_greeting("Josh"))

def process_single_sudoku_command(command: str):
    print(f"Processing command: {command}")

def main():
    commands = deque(sys.argv[1:])
    interactive = not commands
    if interactive:
        while True:
            command = input(StringConstants.PROMPT).strip()
            if command == "quit":
                break
            if command:
                process_single_sudoku_command(command)
    else:
        while commands:
            process_single_sudoku_command(commands.popleft())

if __name__ == "__main__":
    main()
