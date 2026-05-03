import subprocess, sys

SUDOKU_SCRIPT = "sudoku.py"

def run_test(name, grid, cmds, exp):
    print(f"\nTEST NAME: {name}")
    cmd = f'python {SUDOKU_SCRIPT} {grid} ' + " ".join(cmds)
    out = subprocess.run(cmd, capture_output=True, text=True, shell=True).stdout

    print("\n--- RAW COMMAND ---")
    print(cmd)

    print("\n--- COMMANDS ---")
    for c in cmds: print(c)

    print("\n--- EXPECTED ---")
    for e in exp: print(e)

    print("\n--- ACTUAL ---")
    print(out)

    print("\n--- RESULT ---")
    print("PASS" if all(e in out for e in exp) else "FAIL")
    print("="*80)


def main():

    run_test("Check valid grid","123456789456789123789123456234567891567891234891234567345678912678912345912345678",["CHECK"],["No rule violations detected"])
    run_test("Fill A15","000000000000000000000000000000000000000000000000000000000000000000000000000000000",["A15"],["Move accepted"])
    run_test("Invalid cell","000000000000000000000000000000000000000000000000000000000000000000000000000000000",["Z95"],["Cell Z9 doesn't exist"])
    run_test("Invalid value","000000000000000000000000000000000000000000000000000000000000000000000000000000000",["A10"],["Number 0 isn't between 1-9"])
    run_test("Clear empty cell","000000000000000000000000000000000000000000000000000000000000000000000000000000000",["A1CLEAR"],["Cell A1 is not filled"])
    run_test("Hint","123456789456789123789123456234567891567891234891234567345678912678912345912345678",["HINT"],["Hint: Cell"])
    run_test("Quit","123456789456789123789123456234567891567891234891234567345678912678912345912345678",["QUIT"],["Quitting the game"])
    run_test("Clear successfully","000000000000000000000000000000000000000000000000000000000000000000000000000000000",["A11","A1CLEAR"],["Input accepted"])
    run_test("Double fill","000000000000000000000000000000000000000000000000000000000000000000000000000000000",["A11","A12"],["A1 is filled"])

if __name__ == "__main__":
    main()
