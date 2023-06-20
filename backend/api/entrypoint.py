from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.config.main import container, settings

# FastAPI app
app = FastAPI(
    title="Todo list API",
    description="A simple todo list API",
    version="0.1.0",
    docs_url=settings.API_DOCS_URL,
    redoc_url=settings.API_REDOC_URL,
    openapi_url=settings.API_OPENAPI_URL,
)

app.container = container  # type: ignore


# Routes
@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello World!"}


# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
