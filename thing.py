import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd

load_dotenv()

server = os.getenv("DB_SERVER")
database = os.getenv("DB_NAME")
username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

# Defining the connection string globally

connection_string = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"


def test_connection():
    try:
        engine = create_engine(connection_string)
        with engine.connect() as connection:
        
            query = "SELECT * FROM Homes"

            df = pd.read_sql(query, connection)
            print(df)
            print("Success")


    except Exception as e:
        print(f"An error occurred... {e}")

test_connection()

