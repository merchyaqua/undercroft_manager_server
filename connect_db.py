from dotenv import load_dotenv
import psycopg
import os
from psycopg.rows import dict_row

def connect():
    '''Return a connection object for the database.'''
    # Get connection details from a separate file
    load_dotenv()
    USER = os.getenv("user")
    PASSWORD = os.getenv("password")
    HOST = os.getenv("host")
    PORT = os.getenv("port")
    DBNAME = os.getenv("dbname")
    # Connect to the database
    try:
        conn = psycopg.connect(host=HOST, user=USER, password=PASSWORD, port=PORT, dbname=DBNAME, row_factory=dict_row) # specifies the return format of queries is a Python dict
        print("Connection successful!")
        conn.autocommit = True

        return conn

    except Exception as e:
        print(f"Failed to connect: {e}")

def test_cursor(cur):
    # Only run once at initialisation of the DB
    cur.execute("SELECT NOW();")
    result = cur.fetchone()
    print("Current Time:", result)
    # Executes DDL
    with open('schema.sql', 'r') as f:
        schema = f.read()
        cur.execute(schema)
    # Test query
    record = cur.execute('''INSERT INTO prop (name, description, categoryID, isBroken, locationID, photoPath)
                VALUES (%s,%s,%s,%s,%s,%s)
                RETURNING propID;''', ('Sword', 'Odyssiad prop', 1, False, 1, 'test')).fetchone()
    print(record)
    select_query = '''SELECT name FROM prop WHERE name = %s''', ['Sword']
    record = cur.execute(select_query).fetchone() 
    print(record)

# test_cursor(cur)