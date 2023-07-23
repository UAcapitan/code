
import fastapi
import uvicorn


api = fastapi.FastAPI()


@api.get("/")
def message():
    return {
        "message": "Hello world!",
    }


if __name__ == "__main__":
    uvicorn.run(api, host="127.0.0.1", port=8000)
