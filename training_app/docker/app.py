from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/next')
def another_page():
    return render_template('another_page.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')