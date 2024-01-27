import mysql.connector

mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="",
                               database="icw")
mycursor = mydb.cursor()

def Update():
      def UpdateMenu():
            print('1. Update First Name')
            print('2. Update Last Name')
            print('3. Update Age')
            print('4. Update Gender')
            return
      decision = True
      while decision == True:
            ID = int(input("Enter Student ID : "))
            UpdateMenu()
            option = int(input("Select an option : "))
            if option == 1:
                         FirstName = input ("Enter First Name : ")      
                         update ="UPDATE Student_Information SET First_Name= %s WHERE Student_ID = %s"
                         value = (FirstName, ID)
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
                         LastName = input ("Enter Last Name : ")      
                         update ="UPDATE Student_Information SET Last_Name= %s WHERE Student_ID = %s"
                         value = (LastName,ID)
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
                               
            elif option == 3:
                         Age = input ("Enter Age : ") 
                         update ="UPDATE Student_Information SET Age= %s WHERE Student_ID = %s"
                         value = (Age,ID)
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

            elif option == 4:
                         Gender = input ("Enter Gender : ") 
                         update ="UPDATE Student_Information SET Gender= %s WHERE Student_ID = %s"
                         value = (Gender,ID)
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

