from flask import Flask
import random

app = Flask(__name__)

texts = [
    "This is your AI-generated poem: Sun shines bright, code runs light.",
    "AI-generated wisdom: Never give up on your learning journey.",
    "Random joke: Why did the developer go broke? Because he used up all his cache!"
]

@app.route("/generate")
def generate():
    return random.choice(texts)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
