from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    text = db.Column(db.Text, nullable=True)
    mark = db.Column(db.Integer, default=5)

    def __repr__(self):
        return self.title


@app.route('/')
def index():
    tasks = Task.query.order_by(Task.id).all()
    context = {
        'tasks': tasks
    }
    return render_template('index.html', **context)

@app.route('/page')
def page():
    return render_template('page.html')

@app.route('/create', methods=["POST", "GET"])
def create():
    if request.method == "POST":
        title = request.form["title"]
        text = request.form["text"]
        mark = request.form["mark"]
        
        task = Task(title=title, text=text, mark=mark)

        try:
            db.session.add(task)
            db.session.commit()
        except:
            return redirect('/create')

        return redirect('/')
    else:
        return render_template('create.html')

@app.route('/page/<int:id>')
def page_num(id):
    return render_template('page_num.html', id=id)


if __name__ == '__main__':
    app.run(debug=True, port=3000)