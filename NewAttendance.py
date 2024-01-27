import datetime 
import mysql.connector
mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="",
                               database="icw")
mycursor = mydb.cursor()

def NewAttendance():
    decision = True
    while decision == True:
        ID = int(input("Enter Student ID : "))
        Date = str(input("Enter Date(yyyy-mm-dd) : " ))
        Attendance = input("Enter Attendance(1/ab)) : ")
        CourseLevel= input("Enter Course Level : ")
        insert = "INSERT INTO Attendance(Student_ID,Date,Attendance,Course_Level) VALUES(%s,%s,%s,%s)"
        value = (ID,Date,Attendance,CourseLevel)
        mycursor.execute(insert,value)
        mydb.commit()
        print('')
        Choice = input('Would you like to enter another attendance(y/n)? : ')
        if Choice == 'y':
            decision = True
            print('')
        else:
            decision = False
            print('<<<<<<Returning back to main menu>>>>>>')
            print('')



NewAttendance()
