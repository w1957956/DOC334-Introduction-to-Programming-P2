import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="icw")

mycursor = mydb.cursor()

def Attendance():
    decision = True
    while decision == True:
        id = input("Enter Student ID : ") 
        mycursor.execute("SELECT* FROM Attendance WHERE Student_ID = {0}".format(id))
        row = mycursor.fetchone()
        if(row):
         print("Date:",row[1])
         print("Attendance(1/0):", row[2])
         print("Course Level:", row[3])
        else:
         print("Record Not Found....")
         print('<<<<<<Returning back to main menu>>>>>>')
        print('')
        Choice = input('Would you like to search another attendance(y/n)? : ') 
        if Choice == 'y':
            decision = True
            print('')
        else:
            decision = False
            print('<<<<<<Returning back to main menu>>>>>>')
            print('')


Attendance()

