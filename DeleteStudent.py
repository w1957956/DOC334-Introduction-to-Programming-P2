import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="icw")

mycursor = mydb.cursor()
def Delete():
        decision = True
        while decision == True:                
                id = (input("Enter Student ID : "))
                mycursor.execute("DELETE FROM Attendance WHERE Student_ID = "+id+"")
                mycursor.execute("DELETE FROM Student_Information WHERE Student_ID = "+id+"")
                mydb.commit()
                print('')
                Choice = input('Would you like to enter a new student(y/n)? : ')
                if Choice == 'y':
                        decision = True
                        print('')

                else:
                        decision = False
                        print('<<<<<<Returning back to main menu>>>>>>')
                        print('')


Delete()

