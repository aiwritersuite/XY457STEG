from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def index():
    # Load messages from the JSON file
    with open("messages.json", "r", encoding="utf-8") as f:
        messages = json.load(f)
    # Pass messages to the template for server-side rendering
    return render_template("index.html", messages=messages)

if __name__ == "__main__":
    app.run(debug=True)
