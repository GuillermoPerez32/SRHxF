from sqlalchemy import create_engine, MetaData

SQLALCHEMY_DATABASE_URL = 'sqlite:///./db.sqlite3'


engine = create_engine(SQLALCHEMY_DATABASE_URL,
 connect_args={"check_same_thread": False})

meta = MetaData()

meta.create_all(engine)

conn = engine.connect()