import mysql.connector
from dotenv import dotenv_values

config = dotenv_values(".env")

conn = mysql.connector.connect(
    host=config['DB_HOST'],
    port=config['DB_PORT'],
    database=config['DB_NAME'],
    user=config['DB_USERNAME'],
    password=config['DB_PASSWORD']
)

cursor = conn.cursor()

with open('appp/dbscript/schema.sql', 'r') as file:
    queries = file.read()

statements = queries.split(';')

for statement in statements:
    if statement.strip():
        cursor.execute(statement)

conn.commit()
conn.close()

print("SQL queries executed successfully!")
