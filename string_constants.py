
class StringConstants:

    APP_NAME = "Sudoku"

    @staticmethod
    def user_greeting(username: str) -> str:
        return f"Hello, {username}! Welcome to {StringConstants.APP_NAME}."
