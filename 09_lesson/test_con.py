# IMPORT THE SQALCHEMY LIBRARY's CREATE_ENGINE METHOD
from sqlalchemy import create_engine, inspect

# DEFINE THE DATABASE CREDENTIALS
user = 'postgres'
password = '0000'
host = 'localhost'
port = 5432
database = 'postgres'
client_encoding='?client_encoding=utf8'

# PYTHON FUNCTION TO CONNECT TO THE POSTGRESQL DATABASE AND
# RETURN THE SQLACHEMY ENGINE OBJECT
def get_connection():
    return create_engine(
        url="postgresql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database, client_encoding
        )
    )

engine = get_connection()

def test_db_connection():
    inspector = inspect(engine)
    names = inspector.get_table_names()
    # просто проверяем, что таблица есть в списке
    assert 'places' in names
    
