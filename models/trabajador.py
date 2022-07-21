from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.orm import declarative_base, relationship
from config.db import meta, engine

trabajadores = Table(
  'trabajador',
  meta,
  Column('id', Integer, primary_key = True, autoincrement=True),
  Column('nombre', String),
  Column('ci', String),
)

meta.create_all(engine)