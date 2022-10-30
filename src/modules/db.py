# Import the required modules.
import mysql.connector
from mysql.connector import Error
# Database functions

# Connect to the database
def stdb():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="",
            database='startrek'
        )
        # print("Connection to MySQL DB successful")
    except Error as e:
        # print(f"The error '{e}' occurred")
        connection = "FALSE"

    return connection

# Execute the query
def query(connection, query):
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(query)
        # print("Query run successfully")
        result = cursor.fetchall()
    except Error as e:
        # print(f"The error '{e}' occurred")
        result = "FALSE"

    connection.commit()
    connection.close()
    return result

# Execute many queries.
def querymany(connection, query, data):
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.executemany(query, data)
        #print("Query run successfully")
        result = cursor.fetchall()
    except Error as e:
        #print(f"The error '{e}' occurred")
        result = "FALSE"
    connection.commit()
    connection.close()
    return result

# Return the rowcount
def rowcount(connection, query):
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(query)
        # print("Query run successfully")
        result = cursor.fetchall()
        result = cursor.rowcount
    except Error as e:
        # print(f"The error '{e}' occurred")
        result = "FALSE"

    connection.commit()
    connection.close()
    return result
