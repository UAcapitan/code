
import fastapi
import uvicorn

from api import motd
from views import home


main_app = fastapi.FastAPI()

def configure():
    configure_routing()

def configure_routing():
    main_app.include_router(motd.router)
    main_app.include_router(home.router)


if __name__ == "__main__":
    configure()
    uvicorn.run(main_app, host="127.0.0.1", port=8000)
