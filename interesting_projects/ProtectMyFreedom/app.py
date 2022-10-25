
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/reg")
def reg():
    return render_template("reg.html")

@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(port=3000)
