import subprocess
import sys

score = 0
total = 2

def run_test(input_data, expected_output):
    result = subprocess.run(
        [sys.executable, "main.py"],
        input=input_data,
        text=True,
        capture_output=True
    )

    return result.stdout.strip() == expected_output

def test_case_1():
    global score
    if run_test("5\n", "25"):
        score += 1
    else:
        print("❌ Test 1 failed")

def test_case_2():
    global score
    if run_test("3\n", "9"):
        score += 1
    else:
        print("❌ Test 2 failed")

test_case_1()
test_case_2()

print(f"\nScore: {score}/{total}")
