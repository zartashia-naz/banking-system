import os
import re
import json
import random



def accountcreation():
    data = load_data()
    user_credentials={}
    create_account=input("Do you want to create a new account?")
    checklower =  create_account.lower()
    if checklower == 'yes':
        name=input("Enter your full name: ")
        user_credentials["Name"]=name

        while True:
         CNIC= input("Enter your CNIC: ")
         if CNIC .isdigit and len(CNIC)==13:
           user_credentials["CNIC"]=CNIC
           break
         else:
           print("Enter a valid CNIC")
        
      
        while True:
         Phone_number=input("Enter your phone number: ")
         if Phone_number.isdigit  and len(Phone_number)==11:
          user_credentials["Phone Number"]=Phone_number
          break
         else:
           print("Enter a correct phone number!") 
    
        Address=input("Enter your full address: ")
        user_credentials["Address"]=Address

        while True:
         password=input("Create a password for your account: ")
         if len(password)==8 and re.search("[0-9]",password) and re.search("[a-zA-Z]",password) and ("[!@#$%&+<>?/_-=:;]",password):
          user_credentials["password"]=password
          break
         else:
           print("Enter the correct password!")

        birth_date=input("Enter your date of birth: ")
        user_credentials["Date of Birth"]=birth_date

        while True:
         email_address=input("Enter a  valid email address: ")
         if re.search("[@]",email_address) and re.search("[.com]",email_address):
          user_credentials["Email Address"]=email_address
          break
         else: 
           print("Entered email address does not exist!")

        while True:
         initial_deposit_amount=int(input("Enter the amount you want to deposit in order to open your account: "))
         
         if initial_deposit_amount<1000:
          print("Minimun deposit amount should not be less  than Rs1000")
          continue
         else:
           print(str(initial_deposit_amount) + " Added to your account successfully!")
           user_credentials["Initial deposit amount"]=initial_deposit_amount
           break
         
        customer_account_number=generate_account_number()
        data[customer_account_number] = user_credentials
        print(f"Your Account Created Sucessfully, this is your account number {customer_account_number}")
        save_data(data)
    else: 
        print("Existing")

def generate_account_number():
  user_data = load_data()

  while True:
   account_number=str(random.randint(1000,5000))
   if account_number not in user_data.keys():
    return account_number
  
   
     

 
# accountcreation() 
  
# {     
# "1001":{'Name': 'fgvybh', 'Phone Number': '567', 'Address': 'erfgth'},
# "1002":{'Name': 'fgvybh', 'Phone Number': '567', 'Address': 'erfgth'}} 
def load_data():
    if os.path.exists("data.json"):
        with open("data.json", "r") as file:
            return json.load(file) 
    return {} 
    
def save_data(user_data):
  with open("data.json","a") as file:
    json.dump(user_data,file, indent=4)

def login_account():
  account_number=input("Enter your account number: ")
  user_data= load_data()
  if account_number not in user_data.keys():
    print("Invalid account number!")
  
  eachUserData = user_data.get(account_number)
    
  
          
  password=input("Enter your password: ")
  if password not in eachUserData["password"]:
    print("Incorrect password!")
  else:
    return eachUserData

 
def deposit_amount():
  user_data=login_account()
  
  add_amount=int(input("Enter the amount you want to deposit: "))
  initial_amount=user_data.get("Initial deposit amount")
  after_adding_amount=initial_amount+add_amount
  user_data["Initial deposit amount"]=after_adding_amount
  print(user_data)
  
def withdraw_amount():
  user_data=login_account()
  subtract_amount=int(input("Enter the amount you want to withdraw: "))
  before_withdrawl=user_data.get("Initial deposit amount")
  after_withdrawl=before_withdrawl-subtract_amount
  user_data["Initial deposit amount"]=after_withdrawl
  print(user_data)

def check_balance():
  user_data=login_account()
  balance=user_data.get("Initial deposit amount")
  print(balance)




def main():
  print("------------------------WELCOME TO GLOBAL HORIZON BANK!----------------------------")
  print("DO YOU WANT TO:")
  print("       1.CREATE ACCOUNT")
  print("       2.DEPOSIT AMOUNT")
  print("       3.WITHDRAW AMOUNT")
  print("       4.CHECK BALANCE")
  service=input("Press 1,2,3 or 4: ")

  if service==1:
    accountcreation()
  if service==2:
    deposit_amount()
  if service==3:
    withdraw_amount()    
  if service==4:
    check_balance()

  # accountcreation()
  # login_account() 
  deposit_amount()
  # withdraw_amount()
  # check_balance()
  # print("Showing data")
  # load_data()
  
main()

  



 
 