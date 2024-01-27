import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="icw")

mycursor = mydb.cursor()

def StudentInfo():
    decision = True
    while decision == True:
        id = input("Enter Student ID : ") 
        mycursor.execute("SELECT* FROM Student_Information WHERE Student_ID = {0}".format(id))
        row = mycursor.fetchone()
        if(row):
         print("First Name:",row[1])
         print("Last Name:", row[2])
         print("Age:", row[3])
         print("Gender:", row[4])
        else:
         print("Record Not Found....")
        print('')
        Choice = input('Would you like to search again(y/n)? : ')
        print('')
        if Choice == 'y':
            decision = True
        else:
            decision = False
            print('<<<<<<Returning back to main menu>>>>>>')
            print('')

StudentInfo()
