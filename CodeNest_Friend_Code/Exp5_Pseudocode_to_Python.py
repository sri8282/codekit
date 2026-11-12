import ollama

pseudo = """
Read two numbers a and b.
If a is greater than b, print a.
Otherwise, print b.
"""

prompt = f"""
Convert this pseudocode into Python code:
{pseudo}
Return only Python code.
"""

response = ollama.generate(
    model="qwen2.5-coder:3b",
    prompt=prompt
)

code = response["response"]
print(code)
