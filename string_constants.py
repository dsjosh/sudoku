
class StringConstants:

    WELCOME = "Welcome to Sudoku!\n\nHere is your puzzle:"
    PROMPT = "Enter command (e.g., A3 4, C5 clear, hint, check, quit):\n"
    ACCEPT_MOVE = "Move accepted.\n"
    ACCEPT_INPUT = "Input accepted.\n"
    GOOD = "No rule violations detected.\n"
    UNRECOGNISED = "Unrecognised keyboard input. Please try again.\n"
    CURRENT = "Current grid:"
    SUCCESS = "You have successfully completed the Sudoku puzzle!\nPress any key to play again..."
    QUIT = "Quitting the game!\nHave a nice day..."
    HINT_INPUT = "hint"
    CHECK_INPUT = "check"
    QUIT_INPUT = "quit"
    CLEAR_INPUT = "clear"

    @staticmethod
    def not_filled(cell: str) -> str:
        return f"Invalid move. Cell {cell} is not filled."

    @staticmethod
    def prefilled(cell: str) -> str:
        return f"Invalid move. {cell} is pre-filled."

    @staticmethod
    def filled(cell: str) -> str:
        return f"Invalid move. {cell} is filled. You may choose to clear it."

    @staticmethod
    def invalid_cell(cell: str) -> str:
        return f"Invalid move. Cell {cell} doesn't exist."

    @staticmethod
    def invalid_value(value: str) -> str:
        return f"Invalid move. Number {value} isn't between 1-9."

    @staticmethod
    def hint(cell: str, number: str) -> str:
        return f"Hint: Cell {cell} = {number}"

    @staticmethod
    def exist_row(row: str, number: str) -> str:
        return f"Number {number} already exists in Row {row}."

    @staticmethod
    def exist_col(col: str, number: str) -> str:
        return f"Number {number} already exists in Column {col}."

    @staticmethod
    def exist_subgrid(number: str) -> str:
        return f"Number {number} already exists in the same 3×3 subgrid."
