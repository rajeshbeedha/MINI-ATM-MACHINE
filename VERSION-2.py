
# -------------VERSION-2 OF MINI ATM---------------

import random
balance=1000
correct_pin="1234"
transactions=[]
# INSERT ATM CARD
print("PLEASE INSERT YOUR ATM CARD")
print("PLEASE WAIT WHILE TRANSCATION")

# DOMESTIC OR INTERNATONAL
print("\n------ATM CARD-----")
print("1.DOMESTIC")
print("2.INTERNATIONAL")
card_type=int(input("Enter card type:"))
if card_type==1:
    print("Welcome OUR ATM")
elif card_type==2:
    print("HI THERE WELCOME TO OUR ATM")
else:
    print("INVALID CARD TYPE")

# PIN ATTEMPTS
attempts=3

while attempts>0:
    pin = input("ENTER YOUR 4 DIGIT PIN: ")

    if len(pin) == 4 and pin.isdigit():
        if pin == correct_pin:
            print("PIN SUCCESSFULLY VERIFIED!")
            break
        else:
            attempts -= 1
            print("WRONG PIN!")
            print("Attempts remaining:", attempts)

    else:
        attempts -= 1
        print("ERROR: PIN must contain exactly 4 digits!")
        print("Attempts remaining:", attempts)


else:
    print("TOO MANY WRONG ATTEMPTS!")
    print("YOUR ACCOUNT IS LOCKED.")
    exit()

# ATM MENU
while True:
    print("\n--------ATM MEMU----------")
    print("1.CHECK BALANCE")
    print("2.DEPOSITE")
    print("3.WITHDRAW")
    print("4.FAST CASH")
    print("5.PIN CHANGE")
    print("6.MINI STATEMENT")
    print("7.EXIT")

    choice= int(input("Enter an option:"))

# BALANCE CHECK

    if(choice==1):
        print("BALANCE:",balance)

# DEPOSITE

    elif(choice==2):
            amount=int(input("Enter deposite amount:"))
            if amount>0:
                balance+=amount
                transactions.append("deposite:"+str(amount))
                print("Deposite sucessful")
                print("After deposite amount: ₹",balance)
            else:
                print("Please enter valid amount !")

# WITHDRAW

    elif(choice==3):
        Withdraw_amount=int(input("Enter Withdraw amount amount:"))
        if balance>=Withdraw_amount:
            balance-=Withdraw_amount
            transactions.append("Withdraw:"+str(Withdraw_amount))
            print("Remaining balance: ₹",balance)
        elif Withdraw_amount<=0:
            print("ERROR: enter a valid amount")
        else:
            print("insufficient balance") 
            print("you have only: ₹",balance)
# FAST WITHDRAW

    elif(choice==4):
        print("\n====== FAST WITHDRAW ======") 
        print("1. ₹500") 
        print("2. ₹1000") 
        print("3. ₹2000")
        print("4. ₹5000") 
        fast_choice = int(input("SELECT AN AMOUNT: ")) 
        if fast_choice == 1: 
            amount = 500 
        elif fast_choice == 2: 
            amount = 1000
        elif fast_choice == 3: 
            amount = 2000
        elif fast_choice == 4: 
            amount = 5000 
        else: 
            print("INVALID CHOICE!")
            continue 
        if balance >= amount: 
            balance -= amount 
            transactions.append("Fast Withdraw ₹" + str(amount)) 
            print("PLEASE COLLECT YOUR CASH.") 
            print("WITHDRAWN: ₹", amount) 
            print("REMAINING BALANCE: ₹", balance) 
        else: 
            print("INSUFFICIENT BALANCE!") 
            print("YOU HAVE ONLY ₹", balance)

# PIN CHANGE
    elif (choice==5):
        current_pin = input("ENTER CURRENT PIN: ")
        if current_pin == correct_pin: 
            new_pin = input("ENTER NEW 4 DIGIT PIN: ") 
            confirm_pin = input("CONFIRM NEW PIN: ") 
            if len(new_pin) != 4 or not new_pin.isdigit():
                print("ERROR: PIN MUST CONTAIN EXACTLY 4 DIGITS!") 
            elif new_pin != confirm_pin: 
                print("ERROR: NEW PIN AND CONFIRM PIN DO NOT MATCH!") 
            elif new_pin == correct_pin: 
                print("ERROR: NEW PIN CANNOT BE SAME AS CURRENT PIN!") 
            else: 
                correct_pin = new_pin
                print("PIN CHANGED SUCCESSFULLY!") 
                print("PLEASE REMEMBER YOUR NEW PIN.") 
        else: 
            print("ERROR: CURRENT PIN IS INCORRECT!")

# MINI STATEMENT/TRANSCATION HISTORY

    elif(choice==6):
        print("\n========== MINI STATEMENT ==========")
        if len(transactions)==0:
            print(" No Transcatons ")
        else:
            for transaction in transactions:
                print(transaction)
        print("------------------------------------") 
        print("CURRENT BALANCE: ₹", balance) 
        print("====================================")

# EXIT

    elif choice == 5: 
        print("\nTHANK YOU FOR USING THIS ATM!") 
        print("PLEASE COLLECT YOUR CARD.") 
        break
    else:
        print("invalid choice")



