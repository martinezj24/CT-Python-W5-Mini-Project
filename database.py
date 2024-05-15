import mysql.connector
from mysql.connector import Error

def connect_to_database():
   
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Martinez!1996',
            database='library_management_sys'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
    return None



def execute_query(connection, query, data=None):

    try:
        cursor = connection.cursor()
        cursor.execute(query, data)
        connection.commit()
        return True
    except Error as e:
        print(f"Error executing query: {e}")
        return False
    finally:
        cursor.close()



def fetch_all(connection, query, data=None):
    try:
        cursor = connection.cursor()
        cursor.execute(query, data)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"Error fetching datavfrom MySQL Database: {e}")
        return None
    finally:
        cursor.close()
