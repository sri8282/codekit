import ollama
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

real = [
    "def add(a,b): return a+b",
    "def square(n): return n*n",
    "def even(n): return n%2==0",
    "def maximum(a,b): return max(a,b)"
]

prompts = [
    "Write a Python function to subtract two numbers.",
    "Write a Python function to multiply two numbers.",
    "Write a Python function to check odd number.",
    "Write a Python function to calculate cube."
]

fake = []

for p in prompts:
    r = ollama.generate(
        model="qwen2.5-coder:3b",
        prompt=p + " Return only Python code."
    )
    fake.append(r["response"])

print("Generated code:")
print(fake[0])

# Prepare dataset
X = real + fake
y = [1] * len(real) + [0] * len(fake)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X)

model = LogisticRegression()
model.fit(X, y)

sample = [real[0], fake[0]]
prediction = model.predict(vectorizer.transform(sample))

for p in prediction:
    print("Prediction:", "Real" if p == 1 else "Generated")
