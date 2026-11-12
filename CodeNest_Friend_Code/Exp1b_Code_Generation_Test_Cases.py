import ollama

prompt = """
Write a Python function named n_nat_numbers(n)
that returns numbers from 0 to n as a list.
Return only Python code.
"""

response = ollama.chat(
    model="qwen2.5-coder:3b",
    messages=[{"role": "user", "content": prompt}]
)

code = response["message"]["content"]
code = code.replace("```python", "").replace("```", "").strip()

print("Generated Code:")
print(code)

namespace = {}
exec(code, namespace)

# Test cases
tests = [
    (0, [0]),
    (3, [0, 1, 2, 3]),
    (5, [0, 1, 2, 3, 4, 5])
]

for n, expected in tests:
    actual = namespace["n_nat_numbers"](n)

    if actual == expected:
        print("PASS:", n, actual)
    else:
        print("FAIL:", n, actual)
