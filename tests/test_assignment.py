import subprocess
import sys
import json  # <-- 1. Import json at the top!

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

# --- NEW CODE FOR CYBERFLIX ---
# 2. Calculate percentage (e.g. 1/2 becomes 50)
percentage_score = int((score / total) * 100)

# 3. Save it to score.json
with open('score.json', 'w') as f:
    json.dump({'score': percentage_score}, f)
