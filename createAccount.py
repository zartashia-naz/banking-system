import re

user_credentials=[{}]

def accountcreation():
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

        # 
        while True:
         initial_deposit_amount=int(input("Enter the amount you want to deposit in order to open your account: "))
         
         if initial_deposit_amount<1000:
          print("Minimun deposit amount should not be less  than Rs1000")
          continue
         else:
           print(str(initial_deposit_amount) + " Added to your account successfully!")
           break

        import random
        account_number=random.randint(1000,2000)
        print("Your account number is:", account_number )
        user_credentials["Account Number"]=account_number
             
        

        print(user_credentials)
        print("Congratulations! Your account has successfully been created.")
    else: 
        print("Existing")
    
 
accountcreation() 
   
# {     
# "1001":{'Name': 'fgvybh', 'Phone Number': '567', 'Address': 'erfgth'},
# "1002":{'Name': 'fgvybh', 'Phone Number': '567', 'Address': 'erfgth'}} 