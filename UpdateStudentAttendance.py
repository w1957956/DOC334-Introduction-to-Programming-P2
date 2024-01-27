import mysql.connector
mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="",
                               database="icw")
mycursor = mydb.cursor()

def Update():
      def UpdateMenu():
            print('1. Update Attendance')
            print('2. Update Course Level')
            return
      decision = True
      while decision == True:
            ID = int(input("Enter Student ID : "))
            Date = str(input("Enter Date(yyyy-mm-dd) : "))
            UpdateMenu()
            option = int(input("Select an option : "))
            if option == 1:
                Attendance = input("Enter Attendance(1/ab) : ")
                update ="UPDATE Attendance SET Attendance= %s WHERE Student_ID = %s and Date = %s"
                value = (Attendance, ID, Date)
                mycursor.execute(update,value)
                mydb.commit()
                print('')
                Choice = input('Would you like to go back to update menu(y/n) : ')
                if Choice == 'y':
                      decision = True
                      print('')
                else:
                      decision = False
                      print('<<<<<<Returning back to main menu>>>>>>')
                      print('')

            elif option == 2:
                CourseLevel = input ("Enter Course Level : ")      
                update ="UPDATE Attendance SET Course_Level = %s WHERE Student_ID = %s and Date = %s"
                value = (CourseLevel,ID,Date)
                mycursor.execute(update,value)
                mydb.commit()
                print('')
                Choice = input('Would you like to go back to update menu(y/n) : ')
                if Choice == 'y':
                      decision = True
                      print('')
                else:
                      decision = False
                      print('<<<<<<Returning back to main menu>>>>>>')
                      print('')
Update()
