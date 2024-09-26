import psycopg2
from psycopg2.extras import DictCursor


def connect_db():
    # Connection parameters
    conn_params = {
        "host": "localhost",
        "database": "mydb",
        "user": "myuser",
        "password": "mypassword"
    }

    try:
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


if __name__ == "__main__":
    get_postgresql_cursor()
