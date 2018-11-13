import mysql.connector
import re


mydb = mysql.connector.connect(
        host="localhost",
        user="sysadmin",
        passwd="sysadmin",
        database="testdb"
        )

mycursor = mydb.cursor()

# This dict has limits for various types of unsigned as well as signed int.
limitDict = { 'tinyintsigned':'127', 'tinyintunsigned':'255','smallintsigned':'32767', 'smallintunsigned':'65535', 'mediumintsigned':'8388607', 'mediumintunsigned':'16777215','intsigned':'2147483647','intunsigned':'4294967295','bigintsigned':'9223372036854775807', 'bigintunsigned':'18446744073709551615' }

mycursor.execute("SHOW TABLES")

tables = mycursor.fetchall()

for (table_name,) in tables:
    print(f"TABLE NAME {table_name}")
   
    #This query describes field of a table and tells whether id is associated with 'auto_increment' or not
    mycursor.execute(f"DESCRIBE {table_name}")
    x= mycursor.fetchall()

    print(x)
    print(x[0][1]) # contains int type of id
    print(x[0][5]) # stores whether there is an 'auto_increment' field or not

    if(x[0][5] == 'auto_increment'):
        print(f"{table_name} has a AUTOINCREMENTED id")
        
        #This gives current value for auto incremented id
        mycursor.execute(f"SELECT MAX(id) FROM {table_name}")
        curIdVal = mycursor.fetchall()[0][0]
        print(curIdVal)
        

        # now find the type of id, and whether it is signed or unsigned
        # for signed int x[0][1] is "int(10)" and for unsigned int it is "int(10) unsigned"
        s = x[0][1]
        if 'unsigned' in s:
            flag = True
        else :
            flag = False

        i = s.find('(')
        intType = s[:i]

        for x in limitDict:
            if flag:
                if x.startswith(intType) and 'unsigned' in x:
                    maxLimit = int(limitDict[x])

                    print(f"detected {intType} unsigned")
                    #check whether cur value of id field is just 5 less than threshold value
                    if(maxLimit - curIdVal <=5):
                        print("Send alert to slack")
            else:
                if ( x.startswith(intType) and ( 'unsigned' not in x ) ):
                    print(limitDict[x])
                    maxLimit = int(limitDict[x])

                    print(f"detected {intType} signed")
                    if(maxLimit - curIdVal <=5):
                        print("Send alert to Slack")






