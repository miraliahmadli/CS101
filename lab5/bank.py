balance = 0

def deposit(money) :
    # Input : (Integer) The amount of money that a user wants to deposit
    # Output : (None) No Output
    
    # Add the money to the current balance
    
    #################
    ### implement ###
    #################
    # Do something on here !
    global balance
    balance += money    
    #################

def withdrawal(money) :
    # Input : (Integer) The amount of money that a user wants to withdraw
    # Output : (None) No Output
    
    # Withdraw the money from the current balance

    #################
    ### implement ###
    #################
    # Do something on here !
    global balance
    if money > balance:
        print("Not enough balance")
        return
    balance -= money
    #################


def bank() :
    # Input : (None) No Input
    # Output : (None) No Output
    global balance
    while True:
        process = input("Deposit(d) or withdrawal(w) or balance check(c)? ")
        
        # If a user's input is empty string (''), then quit this function.
        # If a user's input is 'd', then ask the amount of money to deposit and deposit it.
        # If a user's input is 'w', then ask the amount of money to withdraw and withdraw it.
        # If a user's input is 'c', then check the current balance.

        #################
        ### implement ###
        #################
        # Do something on here !
        if process == "d":
            money = int(input("How much do you want to deposit?: "))
            while money <= 0:
                money = int(input("Please input positive amount: "))
            deposit(money)
        elif process == "w":
            money = int(input("How much do you want to withdraw?: "))
            while money <= 0:
                money = int(input("Please input positive amount: "))
            withdrawal(money)
        elif process == "c":
            print("Current balance: ", balance)
        elif process == "":
            break
        else:
            print("Could not recognize the process")
        #################

bank()
