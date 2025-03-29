from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers.scripts import router as scripts_router
from data import databese

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# Инициализация БД
@app.on_event("startup")
async def startup_event():
    databese.initialize_db()


app.include_router(scripts_router, prefix="/api/v1")
