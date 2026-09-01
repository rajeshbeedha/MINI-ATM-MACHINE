# ------ATM MACHINE PROJECT------#
balance=1000

while True:
    pin = input(" ENTERYOUR 4 DIGIT PIN: ")
       
    if len(pin) == 4 and pin.isdigit():
        pin = int(pin)
        print("PIN successfully!")
        break
    else:
        print("ERROR: PIN must contain exactly 4 digits!")
while True:
    print("\n1.CHECK BALANCE")
    print("2.DEPOSITE")
    print("3.WITHDRAW")
    print("4.EXIT")

    choice= int(input("Enter an option:"))

    if(choice==1):
                print("BALANCE:",balance)
    elif(choice==2):
                amount=int(input("Enter deposite amount:"))
                balance+=amount
                print("After deposite amount:",balance)
    elif(choice==3):
        Withdraw_amount=int(input("Enter Withdraw amount amount:"))
        if balance>=Withdraw_amount:
            balance-=Withdraw_amount
            print("Remaining balance after withdraw:",balance)
        else:
            print("insufficient balance you have only",balance)
    elif(choice==4):
            print("THANK YOU FOR CHOICING THIS ATM")
            break
    else:
            print("INVALID CHOICE !")
                
                

    