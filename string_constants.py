
class StringConstants:

    APP_NAME = "Sudoku"
    PROMPT = "Enter command (e.g., A3 4, C5 clear, hint, check, quit):\n"

    @staticmethod
    def user_greeting(username: str) -> str:
        return f"Hello, {username}! Welcome to {StringConstants.APP_NAME}."
