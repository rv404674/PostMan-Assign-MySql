import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user="sysadmin",
        passwd="sysadmin",
        database="testdb"
        )

mycursor = mydb.cursor()


mycursor.execute("DROP TABLE customers")
mycursor.execute("DROP TABLE animals")
mycursor.execute("DROP TABLE frameworks")

#Create a table customers with auto_increment id value

mycursor.execute("CREATE TABLE customers (id TINYINT UNSIGNED AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255),\
        address VARCHAR(255))")

sql = "INSERT INTO customers (name,address) VALUES (%s,%s)"
val = [
        ('Rahul','Himachal 174101'),
        ('Sumedha', 'Sumedha Sagar'),
        ]

mycursor.executemany(sql,val)
mydb.commit()

# print all rows of customers table
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)


#Create a table animals with auto_increment id value
mycursor.execute("CREATE TABLE animals (id MEDIUMINT AUTO_INCREMENT PRIMARY KEY,\
        name VARCHAR(50))")

sql = "INSERT INTO animals (name) VALUES ('dog'),('cat')"
mycursor.execute(sql)
mycursor.execute("INSERT INTO animals (id,name) VALUES (100043,'rabbit')")
mydb.commit()

#print all rows of animal 
mycursor.execute("SELECT * FROM animals")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)


#create a table "frameworks" WITHOUT auto_increment id
mycursor.execute("CREATE TABLE frameworks (id MEDIUMINT PRIMARY KEY,\
        name VARCHAR(50))")

sql = "INSERT INTO frameworks (id,name) VALUES (1005,'django')"
mycursor.execute(sql)
mydb.commit()

#print all rows
mycursor.execute("SELECT * FROM frameworks")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)


