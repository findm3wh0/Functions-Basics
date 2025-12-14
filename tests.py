import sys
from io import StringIO
from main import print_numbers

# Test cases: (n, expected_output)
test_cases = [
    (1, "1"),
    (3, "123"),
    (5, "12345"),
    (10, "12345678910"),
    (15, "123456789101112131415"),
    (20, "1234567891011121314151617181920"),  # Extra one for practice~
]

print("Starting local tests... Nya~! 🐾\n")

all_passed = True

for n, expected in test_cases:
    # Capture what the function prints
    old_stdout = sys.stdout
    sys.stdout = captured_output = StringIO()
    
    print_numbers(n)
    
    output = captured_output.getvalue().strip()
    sys.stdout = old_stdout
    
    if output == expected:
        print(f"Test n={n}: PASSED! ✨💖")
    else:
        print(f"Test n={n}: Failed... 😿")
        print(f"   Got:      '{output}'")
        print(f"   Expected: '{expected}'\n")
        all_passed = False

print("=" * 35)
if all_passed:
    print("All tests passed!! You're super ready to submit~! 🎉🐍💕")
else:
    print("Some tests failed... Keep trying, you can do it! 🥺❤️")
print("=" * 35)
