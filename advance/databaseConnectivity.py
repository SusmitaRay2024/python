import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', password='Hello5@123')

if conn.is_connected():
    print("Connection Established....")