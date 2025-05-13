from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn

from settings.constants import PROD
from settings.database import engine, Base

from api.router import router as api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    with engine.begin() as conn:
        Base.metadata.create_all(conn)
    yield


app = FastAPI(
    lifespan=lifespan,
    title="Registration Territory",
    description="https://github.com/DimaFyodorov/reg_territory",
    version="0.0.0",
)


app.include_router(
    router=api_router,
    prefix="/api",
)


@app.get("/")
def main_page():
    """Страница заглушка на /"""
    return {
        "message": "Hello  Territory!",
    }


# Запуск
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=(not PROD), workers=2)