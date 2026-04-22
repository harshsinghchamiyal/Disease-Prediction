import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="harsh123@#",
    database="mediscope"
)

cursor = conn.cursor()