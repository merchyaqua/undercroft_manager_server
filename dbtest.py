import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Fetch variables
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")
# DBURI = '''postgresql://postgres:@localhost:5432/merch''' BACKUP
# Connect to the database
try:
    # connection = psycopg2.connect(DBURI)
    connection = psycopg2.connect(host=HOST, user=USER, password=PASSWORD, port=PORT, dbname=DBNAME)

    print("Connection successful!")

    # Create a cursor to execute SQL queries
    cursor = connection.cursor()
    
    # Example query
    cursor.execute("SELECT NOW();")
    result = cursor.fetchone()
    print("Current Time:", result)

    # Close the cursor and connection
    cursor.close()
    connection.close()
    print("Connection closed.")

except Exception as e:
    print(f"Failed to connect: {e}")