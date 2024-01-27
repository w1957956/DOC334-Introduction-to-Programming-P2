import mysql.connector

mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="",
                               database="icw")
mycursor = mydb.cursor()

def View():
    mycursor.execute("SELECT * FROM Attendance")
    result = mycursor.fetchall()
    for x in result:
        print(x)
        print("\n")
        print('<<<<<<Returning back to main menu>>>>>>')
        print('')
    return

View()
