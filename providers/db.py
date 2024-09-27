import psycopg2
from psycopg2.extras import DictCursor
import os


def connect_db():
    try:
        # Connection parameters
        conn_params = {
            "host": os.environ.get('DB_HOST'),
            "database": os.environ.get('DB_NAME'),
            "user": os.environ.get('DB_USER'),
            "password": os.environ.get('DB_PASSWORD')
        }

        # Establish a connection
        conn = psycopg2.connect(**conn_params, cursor_factory=DictCursor)
        conn.autocommit = True

        return conn
    except Exception as e:
        raise e


def get_postgresql_cursor():
    try:
        connection = connect_db()
        # Create a cursor
        cur = connection.cursor()

        return cur

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)


def execute_query(query):
    try:
        connection = connect_db()
        # Create a cursor
        cur = connection.cursor()

        cur.execute(query)

        return cur
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)


if __name__ == "__main__":
    get_postgresql_cursor()
