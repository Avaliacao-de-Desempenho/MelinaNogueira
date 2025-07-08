from databases import Database
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

database = Database(DATABASE_URL)
metadata = MetaData()

notas_fiscais = Table(
    "notas_fiscais",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("cnpj", String(20)),
    Column("data_emissao", Date),
    Column("valor_total", String(20)),
)

engine = create_engine(DATABASE_URL)
metadata.create_all(engine)
 