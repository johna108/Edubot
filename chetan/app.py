from flask import Flask, render_template, request, jsonify
import os
import sys

# Add the project directory to the sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the chatbot module from scripts.js
from scripts import chatbot

app = Flask(__name__)

@app.route("/About")
def index():
    return render_template("index.html")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/Course")
def Course():
    return render_template("courses.html")

@app.route("/Feedback")
def Feedback():
    return render_template("feedback.html")

@app.route("/myaccount")
def myaccount():
    return render_template("myaccount.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form.get("userInput")
    response = chatbot.respond(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)