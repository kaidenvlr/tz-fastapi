import uvicorn
from fastapi import FastAPI

from logger.logger import logger
from routers import mailer

app = FastAPI()
app.include_router(mailer.router)


@app.get('/')
async def root():
    logger.info("Hello world")
    return {'message': 'hello world'}
