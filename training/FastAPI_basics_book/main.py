
import fastapi
import uvicorn

from environs import Env
from starlette.staticfiles import StaticFiles

from api import motd
from views import home


main_app = fastapi.FastAPI()

def configure():
    configure_routing()
    configure_env_vars()

def configure_routing():
    main_app.mount("/static", StaticFiles(directory="static"), name="static")
    main_app.include_router(motd.router)
    main_app.include_router(home.router)

def configure_env_vars():
    env = Env()
    env.read_env()
    if not env("TOKEN"):
        raise Exception("There is no token")
    else:
        home.token = env("TOKEN")


if __name__ == "__main__":
    configure()
    uvicorn.run(main_app, host="127.0.0.1", port=8000)
