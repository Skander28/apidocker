from fastapi import FastAPI
from uvicorn import Server, Config

from Services.db import create_database
from Apis.router import route
from Configuration.config import config

app = FastAPI()
app.include_router(route)


@app.on_event("startup")
async def create_db():
    return create_database()


if __name__ == '__main__':
    server = Server(Config(app=app, host=config.HOST, port=config.PORT))
    server.run()
