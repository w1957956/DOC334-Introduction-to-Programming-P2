import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="icw")

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE Student_Information ( Student_ID INT NOT NULL,First_Name VARCHAR(15),\
Last_Name VARCHAR(15),Age INT,Gender ENUM('M','F'),PRIMARY KEY (Student_ID)")

#mycursor.execute("CREATE TABLE Attendance( Student_ID INT NOT NULL, Date DATE, Attendance ENUM('1','ab'),\
Course_Level VARCHAR(15),FOREIGN KEY(Student_ID) REFERENCES Student_Information(Student_ID))")


import Sub.MainMenu

decision = True
while decision == True:
    Sub.MainMenu.Menu()
    option = int(input("Select an option : "))
    print('')
    if option == 1:
        import Sub.ViewStudentInfo
        Sub.ViewStudentInfo.View()
        print('')
        Choice = input('Would you like to go back to main menu(y/n) : ')
        if Choice == 'y':
               decision = True
               print('')
        else: decision = False

    elif option == 2:
        import Sub.ViewStudentAttendance
        Sub.ViewStudentAttendance.View()
        print('')
        Choice = input('Would you like to go back to main menu(y/n) : ')
        if Choice == 'y':
                decision = True
                print('')
        else: decision = False

    elif option == 3:
        import Sub.StudentInfo
        Sub.StudentInfo.StudentInfo()
        print('')
        Choice = input('Would you like to go back to main menu(y/n) : ')
        if Choice == 'y':
                decision = True
                print('')
        else: decision = False

    elif option == 4:
        import Sub.StudentAttendance
        Sub.StudentAttendance.Attendance()
        print('')
        Choice = input('Would you like to go back to main menu(y/n) : ')
        if Choice == 'y':
                decision = True
                print('')
        else: decision = False
        
    elif option == 5:
        import Sub.NewStudent
        Sub.NewStudent.NewStudent()
        print('')
        Choice = input('Would you like to go back to main menu(y/n) : ')
        if Choice == 'y':
                decision = True
                print('')
        else: decision = False

    elif option == 6:
        import Sub.NewAttendance
        Sub.NewAttendance.Attendance()
        print('')
        Choice = input('Would you like to go back to main menu(y/n) : ')
        if Choice == 'y':
                decision = True
                print('')
        else: decision = False

    elif option == 7:
        import Sub.UpdateStudentInfo
        Sub.UpdateStudentInfo.Update()
        print('')
        Choice = input('Would you like to go back to main menu(y/n) : ')
        if Choice == 'y':
                decision = True
                print('')
        else: decision = False


    elif option == 8:
        import Sub.UpdateStudentAttendance
        Sub.UpdateStudentAttendance.Update()
        print('')
        Choice = input('Would you like to go back to main menu(y/n) : ')
        if Choice == 'y':
                decision = True
        else: decision = False
        
    elif option == 9:
        import Sub.DeleteStudent
        Sub.DeleteStudent.Delete()
        print('')
        Choice = input('Would you like to go back to main menu(y/n) : ')
        if Choice == 'y':
                decision = True
                print('')
        else: decision = False

        
    elif option == 10:
        import Sub.DeleteAttendance
        Sub.DeleteAttendance.Delete()
        print('')
        Choice = input('Would you like to go back to main menu(y/n) : ')
        if Choice == 'y':
                decision = True
                print('')
        else: decision = False

    
