#!/usr/bin/python3
import mysql.connector

def stream_users():
    """Generator to stream rows from user_data table one by one."""
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_mysql_password",  # Replace with your password
        database="ALX_prodev"
    )
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")

    for row in cursor:
        yield row

    cursor.close()
    connection.close()
