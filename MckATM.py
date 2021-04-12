# register
# - first name,last name, password, email
# - generate user account


#login
# - account number and password


#bank operations

#Initializing the system
import random

database ={} #dictionary

def init():

   isValidOptionSelected = False
   print("Welcome to bankPHP") 

   while isValidOptionSelected == False:

      haveAccount = int(input("Do you have an account with us: 1 (yes) 2 (no) \n"))
    
      if(haveAccount == 1):
         isValidOptionSelected = True
         login()
      elif(haveAccount == 2): 
         isValidOptionSelected = True
         print(register())
      else:
          print("You have selected invalid option")


def login():
    print("Login to your account")

    bankOperation()

def register():

    print("****** Register ******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("create a password \n")

    accountNumber = generateAccountNumber()

    database[accountNumber] = [first_name, last_name, email, password]

    print("Your Account has been created")

    login()

def bankOperation():
    print("some operations")

def generateAccountNumber():
   
    return random.randrange(1111111111,9999999999)



  #### ACTUAL BANKING SYSTEM ####

init()

name = input ("What is your username? \n")
allowedUsers = ['Silvi','Jahsh','Dija']
allowedPassword = ['pwSilvi','pwJahsh','pwDija']



if(name in allowedUsers):
   password = input("Your password? \n")
   userId = allowedUsers.index(name)
   
   if(password == allowedPassword[userId]):
    
    print('Welcome %s \n' % name)

    import datetime
    now = datetime.datetime.now()
    print ("Date and Time :")
    print (now.strftime("%Y-%m-%d %H:%M:%S \n"))
    
    print('These are the available options: \n')
    
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaint \n')
    
    
    selectedOption = int(input('Please select an option:'))
                        
    if(selectedOption == 1):
       print('How much money would you like to withdraw? \n')
       withdraw = int(input("Please enter the amount you want to withdraw:"))

    if(withdraw == 1):
       print("Take your cash \n")
       print('These are the available options:')
       print('1. Withdrawal')
       print('2. Deposit')
       print('3. Complaint')
           
    elif(selectedOption == 2):
       print('How much would you like to deposit? \n')
       deposit = int(input("Enter the amount to deposit: "))

       print("Current balance")
       
       print('These are the available options:')
       print('1. Withdrawal')
       print('2. Cash Deposit')
       print('3. Complaint')
        
    elif(selectedOption == 3):
       int('What issue would you like to report? \n')
       
       print('Thank you for contacting us.')
       print('These are the available options:')
       print('1. Withdrawal')
       print('2. Cash Deposit')
       print('3. Complaint')
        
    else:
       print('Invalid Option selected, please try again')      
    
   else:
       print('Password Incorrect, please try again')
       
 
