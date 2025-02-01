from contextlib import asynccontextmanager
from dotenv import load_dotenv

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session

from app.db import get_session, init_db
from app.redis import get_redis

load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Inicializa la base de datos
    await init_db()
    yield  # La aplicación está lista para manejar solicitudes


app = FastAPI(lifespan=lifespan)

# Configura CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todos los orígenes
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    redis_client = get_redis()
    redis_client.set("message", "Welcome to Another Wiki!")
    return {"message": redis_client.get("message")}


@app.get("/health")
async def health_check():
    return {"status": "ok"}
