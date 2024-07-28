import mysql.connector
from mysql.connector import errorcode
mydb = mysql.connector.connect(host = "localhost",user = "root",passwd = "1234")
mycursor = mydb.cursor()
try:
    mycursor.execute('CREATE DATABASE IF NOT EXISTS alx_book_store')
except mysql.connector.Error as e:
    if e.errno == errorcode.ER_DB_CREATE_EXISTS:
        print("Database 'alx_book_store' already exists.")
else:
    print("Database 'alx_book_store' created successfully!")
mycursor.close()
mydb.close()
