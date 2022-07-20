from fastapi import FastAPI
from routes import trabajador

app = FastAPI()

app.include_router(trabajador.router)