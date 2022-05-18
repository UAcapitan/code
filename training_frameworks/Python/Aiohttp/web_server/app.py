from asyncio import tasks
from aiohttp import web
import aiohttp_jinja2
import jinja2
from aiohttp_jinja2 import template
import sqlalchemy
from sqlalchemy.orm import declarative_base, Session, sessionmaker
from sqlalchemy_utils import database_exists, create_database

db_engine = sqlalchemy.create_engine('sqlite:///tasks.db')
Base = declarative_base()

class Task(Base):
    __tablename__ = "task"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    title = sqlalchemy.Column(sqlalchemy.String(50), nullable=False)
    text = sqlalchemy.Column(sqlalchemy.Text, default="None")
    mark = sqlalchemy.Column(sqlalchemy.Integer, default=5)


    def __repr__(self):
        return self.title

@template('index.html')
async def index(request):
    with Session(db_engine) as session:
        query = session.query(Task)
        all_tasks = query.all()
    return {"tasks": all_tasks}

@template('page.html')
async def page(request):
    return {}

@template('create.html')
async def create(request):
    return {}

@template('create.html')
async def create_post(request):
    data = await request.post()
    title = data['title']
    text = data['text']
    mark = data['mark']
    print(f"{title} {text} {mark}")
    with Session(db_engine) as session:
        task = Task(title=title, text=text, mark=mark)
        session.add(task)
        session.commit()
    raise web.HTTPFound('/')

@template('success.html')
async def success(request):
    return {}


def app_launch():
    app = web.Application()
    add_jinja(app)
    all_routes(app)
    return app

def add_jinja(app):
    aiohttp_jinja2.setup(app,
        loader = jinja2.PackageLoader('app', 'templates')
    )

def all_routes(app):
    app.router.add_get("/", index)
    app.router.add_get("/page", page)
    app.router.add_get("/create", create)
    app.router.add_post("/create", create_post)
    app.router.add_get("/success", success)

def start_database():
    if not database_exists(db_engine.url):
        create_database(db_engine.url)
    session = sessionmaker()
    session.configure(bind=db_engine)
    Base.metadata.create_all(db_engine)

if __name__ == '__main__':
    start_database()
    web.run_app(app_launch(), host='127.0.0.1', port=3000)