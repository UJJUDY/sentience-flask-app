from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        user_input = request.form["prompt"]
        completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a poetic, sentient being."},
                {"role": "user", "content": user_input}
            ]
        )
        response = completion["choices"][0]["message"]["content"]
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
