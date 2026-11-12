import ollama

code = """
def factorial(n):
"""

prompt = f"""
Complete this Python code:
{code}
Return only the completed code.
"""

response = ollama.generate(
    model="qwen2.5-coder:3b",
    prompt=prompt
)

print(response["response"])
