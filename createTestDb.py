import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user="sysadmin",
        passwd="sysadmin"
        )

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE testdb")
