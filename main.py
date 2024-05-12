from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    message = ""
    if request.method == "POST":
        number = request.form["number"]
        response = requests.get(url=f"http://numbersapi.com/{number}")
        response.raise_for_status
        message = response.text

        return render_template("index.html", message=message)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")