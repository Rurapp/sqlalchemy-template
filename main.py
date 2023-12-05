from fastapi import FastAPI
from sqlalchemy import text

from infrastructure.db.connection import DatabaseConnection
from infrastructure.db.models.sales import Sales
from infrastructure.db.models.user import User
import datetime as dt
import uvicorn
import pandas as pd

db_connection = DatabaseConnection()
db_connection.initialize_db()

app = FastAPI()


def add_template_users():
    db_session = db_connection.get_session()
    diego = User('nico', 202035)
    db_session.add(diego)
    print(diego.id)

    carlos = User('jose', 202038)
    db_session.add(carlos)
    print(carlos.id)

    db_session.commit()
    db_session.close()
    print('done')


def query_examples():
    db_session = db_connection.get_session()

    # filtrar por id
    id_numer = 5
    id_1 = db_session.query(User).get(id_numer)
    print(f'el cliente que tiene id = {id_numer} es: {id_1.name}')

    # query por nombre
    diego = db_session.query(User).filter_by(name='diego').first()
    print(diego.name)
    print(diego.created_at)

    query = db_session.query(User).filter_by(name='diego').statement
    df = pd.read_sql(query, db_session.bind)
    print(df)

    # leer y transformar a df
    costs_query = db_session.query(User).filter(User.name.in_(["diego", "nico"])).statement
    df = pd.read_sql(costs_query, db_session.bind)
    print(df)


def execute_query():
    db_session = db_connection.get_session()
    query = text("""
        SELECT * FROM user_table;
    """)
    result = db_session.execute(query)
    # due
    for row in result:
        print(row.name)

    df = pd.read_sql_query(query, db_session.bind)
    print(df)


def inert_batch_of_orders():
    db_session = db_connection.get_session()

    sales_reg = [(1, 300), (1, 5000), (5, 500), (6, 1000)]

    try:
        for sale in sales_reg:
            user_id = sale[0]
            price = sale[1]

            temp_sale = Sales(user_id, price)
            db_session.add(temp_sale)

        db_session.commit()

    except Exception as ex:

        db_session.rollback()

    db_session.close()


if __name__ == '__main__':
    inert_batch_of_orders()
    uvicorn.run(app, host="0.0.0.0", port=8080)
