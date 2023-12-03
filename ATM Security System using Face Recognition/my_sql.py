import mysql.connector as mysql
from datetime import datetime

class my_sql():
    
    def __init__(self, filename, entry_time):
        date=None
        mycursor=None
        mydb = mysql.connect(
                host="localhost",
                user="root",
                password="1234",
                database="minor_project"
                )
        if(mydb):
            print("Connection Successfull")
        else:
            print("Connection Failed")  
        mycursor=mydb.cursor()
        today=datetime.now()
        date= str(today.year)+"-"+str(today.month)+"-"+str(today.day)

        with open(filename, "rb") as file:
             photo = file.read()
        SqlStatement="INSERT INTO atm_machine(photo, date, entry_time) VALUES (%s,%s,%s)"
        mycursor.execute(SqlStatement, (photo, date, entry_time))
        mydb.commit()

