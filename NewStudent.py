import mysql.connector

mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="",
                               database="icw")
mycursor = mydb.cursor()

def NewStudent():
    decision = True
    while decision == True:
        ID = int(input("Enter Student ID : "))
        FirstName = input("Enter First Name : ")
        LastName = input("Enter Last Name : ")
        Age = input("Enter Age : ")
        Gender = input("Enter Gender(M/F) : ")
        mycursor.execute("INSERT INTO student_information(Student_ID,First_Name,Last_Name,Age,Gender)\
                         VALUES(%s,%s,%s,%s,%s)",(ID,FirstName,LastName,Age,Gender))
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




NewStudent()
