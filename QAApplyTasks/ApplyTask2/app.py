import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

connection = create_connection("localhost", "root", "password", "projectCars")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        rows_as_lists = [list(row) for row in result]
        for row_list in rows_as_lists:
            print(row_list)
    except Error as e:
        print(f"The error '{e}' occurred")


select_query = "SELECT * FROM Cars"
table_data = execute_read_query(connection, select_query)

# Printing the data
