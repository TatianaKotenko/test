import pytest
from sqlalchemy import create_engine
from sqlalchemy import inspect


from sqlalchemy import create_engine, inspect

engine = create_engine(
    "postgresql://postgres:12345@localhost:5432/postgres",
    connect_args={'options': '-c client_encoding=UTF8'}
)

def test_db_connection():
	inspector = inspect(engine)
	names = inspector.get_table_names()
	assert names[1] == 'plases'


