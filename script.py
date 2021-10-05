'''
Write a function to load Write a function to load data. Parameter: file name, returns a list of users.
Write a function to display the user information. Parameters: one or more strings, or an array and return a formatted string.
Write a login function that takes username and password as parameters and returns a user dictionary.


INITIALIZE empty dictionary banking_customers
'''

banking_customers = {
    #'username': ("password", "customer_name", "account_balance")
}
customer_data_file = "data.txt"

'''
FUNCTION load_data(filename):
    IMPORT data.txt file
    SPLIT at each comma to create a list
    SET username = key 
    APPEND to dictionary banking_customers
    SET password, name, balance = pairs
    APPEND to dictionary banking_customers

    RETURN banking_customers
'''

def load_data(filename):
    file = open(filename, "r")
    print (file)
    lines = file.readlines()
    print (lines)
    for line in lines:
        print ("========================")
        print(line)
        value = line.split(',')
        print (value)
        print ("========================")
        username = value[0]
        print (f"username: {username}")
        password = value[1]
        print (f"password: {password}")
        name = value[2]
        print (f"name: {name}")
        balance = value[3]
        int(balance)
        print (f"balance: {balance}")

        banking_customers[username]=password, name, balance
        print (banking_customers)
        print ("========================")

    file.close()
    return banking_customers


load_data(customer_data_file)

'''
FUNCTION display_account_info(username):
    SET customer_name = GET dictionary element with key
    SET account_balance = GET dictionary element with key

    DISPLAY ("customer_name: Your account balance is $account_balance")
    RETURN ("customer_name, account_balance")

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

display_account_info("betho")
'''


FUNCTION login(username, password):
    SET correct_password = GET dictionary element with key(username)

    IF the password == correct_password:
        THEN display_account_info(username)
    
    ELSE:
        DISPLAY "Your login information was incorrect. Please try again."


NOTE dictionary format:

banking_customers = {
    'username': [password, customer_name, account_balance],
    'username': [password, customer_name, account_balance]
}
'''
