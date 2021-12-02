from flask import Flask

app = Flask(__name__)

@app.route('/')
def main_page():
    return '<h1>To do</h1>'

if __name__ == '__main__':
    app.run(debug=True)