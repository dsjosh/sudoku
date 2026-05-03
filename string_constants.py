
class StringConstants:

    WELCOME = "Welcome to Sudoku!\n\nHere is your puzzle:"
    PROMPT = "Enter command (e.g., A3 4, C5 clear, hint, check, quit):\n"
    ACCEPT_MOVE = "\nMove accepted.\n"
    ACCEPT_INPUT = "Input accepted.\n"
    GOOD = "No rule violations detected.\n"
    UNRECOGNISED = "Unrecognised keyboard input. Please try again.\n"
    CURRENT = "Current grid:"
    SUCCESS = "You have successfully completed the Sudoku puzzle!\nPress any key to play again...\n"
    QUIT = "Quitting the game!\nHave a nice day...\n"
    CHECK_INPUT = "CHECK"
    HINT_INPUT = "HINT"
    QUIT_INPUT = "QUIT"
    CLEAR_INPUT = "CLEAR"
    ROWS = "ABCDEFGHI"
    COLS = "123456789"
    HINT_BLOCKED = "You can only get a hint after fixing all rule violations. Check rule violations via the check command.\n"
    DEAD_END = "You have reached a dead end. Do some backtracking by clearing some cells.\n"

    @staticmethod
    def not_filled(cell: str) -> str:
        return f"\nInvalid move. Cell {cell} is not filled.\n"

    @staticmethod
    def prefilled(cell: str) -> str:
        return f"\nInvalid move. {cell} is pre-filled.\n"

    @staticmethod
    def filled(cell: str) -> str:
        return f"\nInvalid move. {cell} is filled. You may choose to clear it.\n"

    @staticmethod
    def invalid_cell(cell: str) -> str:
        return f"\nInvalid move. Cell {cell} doesn't exist.\n"

    @staticmethod
    def invalid_value(value: str) -> str:
        return f"\nInvalid move. Number {value} isn't between 1-9.\n"

    @staticmethod
    def hint(cell: str, number: str) -> str:
        return f"Hint: Cell {cell} = {number}\n"

    @staticmethod
    def exist_row(row: str, number: str) -> str:
        return f"Number {number} already exists in Row {row}.\n"

    @staticmethod
    def exist_col(col: str, number: str) -> str:
        return f"Number {number} already exists in Column {col}.\n"

    @staticmethod
    def exist_subgrid(number: str) -> str:
        return f"Number {number} already exists in the same 3×3 subgrid.\n"
