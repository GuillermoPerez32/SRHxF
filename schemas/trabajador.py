from pydantic import BaseModel

class TrabajadorIn(BaseModel):
  nombre: str
  ci: str

class TrabajadoroOut(BaseModel):
  id: int
  nombre: str
  ci: str

class TrabajadorUpdate(BaseModel):
  id: int
  nombre: str
  ci: str