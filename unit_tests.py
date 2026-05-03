import subprocess
import sys

SUDOKU_SCRIPT = "sudoku.py"


def run_test(test_name, grid_string, commands, expected_outputs):
    print(f"\n=== TEST: {test_name} ===")

    # Build command string (shell=True mode)
    cmd = f'python {SUDOKU_SCRIPT} {grid_string} ' + " ".join(commands)

    result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    output = result.stdout

    print("\n--- Raw Command ---")
    print(cmd)

    print("\n--- Commands ---")
    for c in commands:
        print(c)

    print("\n--- Expected (partial match) ---")
    for exp in expected_outputs:
        print(f"- {exp}")

    print("\n--- Actual Output ---")
    print(output)

    print("\n--- Result ---")
    passed = all(exp in output for exp in expected_outputs)
    print("PASS" if passed else "FAIL")


def main():
    solved_grid = (
        "123456789"
        "456789123"
        "789123456"
        "234567891"
        "567891234"
        "891234567"
        "345678912"
        "678912345"
        "912345678"
    )

    # Test CHECK
    run_test(
        "Check valid grid",
        solved_grid,
        ["CHECK"],
        ["No rule violations detected."]
    )

    # Test fill move using A15 format (no space)
    empty_grid = "0" * 81

    run_test(
        "Fill cell A15 format",
        empty_grid,
        ["A15"],
        ["Move accepted", "Current grid"]
    )

    # Test invalid cell
    run_test(
        "Invalid cell",
        empty_grid,
        ["Z95"],
        ["doesn't exist"]
    )

    # Test invalid value
    run_test(
        "Invalid value",
        empty_grid,
        ["A10"],
        ["isn't between 1-9"]
    )

    # Test clear
    run_test(
        "Clear cell",
        empty_grid,
        ["A1CLEAR"],
        ["is not filled"]
    )

    # Test hint
    one_empty = list(solved_grid)
    one_empty[0] = "0"
    one_empty = "".join(one_empty)

    run_test(
        "Hint test",
        one_empty,
        ["HINT"],
        ["Hint: Cell"]
    )

    # Test quit
    run_test(
        "Quit",
        solved_grid,
        ["QUIT"],
        ["Quitting the game"]
    )


if __name__ == "__main__":
    main()
