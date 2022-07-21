from app import app
from config.db import conn
from schemas.trabajador import TrabajadorIn, TrabajadorUpdate
from models.trabajador import trabajadores

@app.get('/trabajadores')
async def get_trabajadores():
  return conn.execute(trabajadores.select()).fetchall()

@app.post('/trabajadores')
async def create_trabajador(trabajador: TrabajadorIn):
  return conn.execute(trabajadores.insert(trabajador.dict()))

@app.put('/trabajadores/{id}')
async def update_trabajador(id: int, trabajador: TrabajadorUpdate):
  return conn.execute(trabajadores.insert(trabajador.dict()))