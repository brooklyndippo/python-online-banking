'''
INITIALIZE empty dictionary banking_customers
IMPORT text files
'''

banking_customers = {
    #'username': ("password", "customer_name", "account_balance")
}
customer_data_file = "data.txt"
bank_file = "pythonbank.txt"

'''
Fucntion LOAD ART loads the ascii art file.
It removes the line break at the end of each line and prints each line to show the art.
'''

def load_art(filename):
    file = open(filename, "r")
    lines = file.readlines()
    for line in lines:
        art_line = line.replace("\n", "")
        print (art_line)

'''
Function LOAD DATA loads the user data and returns a dictionary with account info.
>> Note: uncomment print values to confirm if data import & sort is working
'''
def load_data(filename):
    file = open(filename, "r")
    lines = file.readlines()
    for line in lines:
        #print ("========================")
        #print(line)
        value = line.split(',')
        #print (value)
        #print ("========================")
        username = value[0]
        #print (f"username: {username}")
        password = value[1]
        #print (f"password: {password}")
        name = value[2]
        #print (f"name: {name}")
        balance = int(value[3]) #convert the balance from a string to an integer
        #print (f"balance: {balance}")

        banking_customers[username]=password, name, balance
        #print (banking_customers)
        #print ("========================")

    file.close()
    return banking_customers

'''
Function DISPLAY ACCOUNT INFO displays the customer's account information, including the current balance.
'''
def display_account_info(username):
    customer_account = banking_customers[username]
    
    customer_name = customer_account[1] #get the customer name from the account
    account_balance = customer_account[2] #get the customer name from the account

    print ("")
    print (f"Hi {customer_name}, welcome back!")
    print (f"Your account balance is:")
    print ("")
    print (f"${account_balance}")
    print ("")

'''
Function LOGIN takes in a customers username and password to validate the account.
    *If the login information is accurate, it displays account information.
    *If it's not accurate, it reprompts for a username & password. 
'''
def login():

    user_input = input("Username:")
    user_password = input("Password:")

    #check to see if the username is valid
    if user_input in banking_customers:
        account_match = banking_customers[user_input]
        correct_password = account_match[0]
        #print (correct_password) - only do this to test the program

        #check to see if the password matches
        if user_password == correct_password:
            display_account_info(user_input)

    else:
        print ("")
        print("Username and password not found.")
        print("Please try again.")
        print("")
        login()


'''
Run the online banking app! 
'''

#Load the customer data first
load_data(customer_data_file)

#Display the bank & welcome message
print ("")
load_art(bank_file)
print ("")
print ("Welcome to Bank of Python")
print ("To get started, please login below:")
print ("")

#Run the login function
login()