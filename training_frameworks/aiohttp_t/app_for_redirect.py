from flask import Flask, redirect


app = Flask(__name__)

@app.route('/')
def main():
    return redirect('/test')

@app.route('/test')
def test():
    return redirect('/pages')

@app.route('/pages')
def pages():
    return redirect('/page')

@app.route('/page')
def page():
    return redirect('/comments')

@app.route('/comments')
def comments():
    return 'Work'


if __name__ == '__main__':
    app.run(debug=True)