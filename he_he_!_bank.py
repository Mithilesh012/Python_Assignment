import random
from time import *

beg,end=1,1000
r1=random.randint(beg, end)

Accounts={ }

def creat_account():
    account_number = int(input("Enter account number: "))
    name = input("Enter account holder name: ")
    in_balance = float(input("Enter in balance: "))

    if account_number in Accounts:
        print("account number already exist hee hee!")
    else:
        Accounts[account_number]={
            'Name': name,
            'Balance':in_balance
        }
        #print(f"Account created for {name} with balance {in_balance}")
        print(f"Account created for {name} with balance {in_balance} hee hee! ")
        print(Accounts)

def withdraw_blance():
    print("otp of this",r1)
    account_number = int(input("Enter account number: "))
    amount = float(input("Enter amount to withdraw: "))
    print("\n tpyes of payment")
    print("1. g-pay")
    print("2. payment")
    print("3.  phone pay")
    mg = int(input("Enter payemnt type: "))


    if account_number in Accounts:
        if mg == 1:
            r2 = int(input("Enter otp number: "))
            if r1 == r2:
                if Accounts[account_number]['Balance'] >= amount:
                    Accounts[account_number]['Balance'] -= amount
                    print(f"Withdrew {amount} new balance is {Accounts[account_number]['Balance']} hee hee!")
                    print("your payment is done by g-pay")
                    h = ctime()
                    print(h)
                    print(Accounts)
                else:
                    print("Insufficient funds. hee hee!")
            else:
                print("Invalid credential")
        elif mg == 2:
            r2 = int(input("Enter otp number: "))
            if r1 == r2:
                if Accounts[account_number]['Balance'] >= amount:
                    Accounts[account_number]['Balance'] -= amount
                    print(f"Withdrew {amount} new balance is {Accounts[account_number]['Balance']} hee hee!")
                    print("your payment is done by paytem")
                    h = ctime()
                    print(h)
                    print(Accounts)
                else:
                    print("Insufficient funds. hee hee!")
            else:
                print("Invalid credential")
        elif mg == 3:
            r2 = int(input("Enter otp number: "))
            if r1 == r2:
                if Accounts[account_number]['Balance'] >= amount:
                    Accounts[account_number]['Balance'] -= amount
                    print(f"Withdrew {amount} new balance is {Accounts[account_number]['Balance']} hee hee!")
                    print("your payment is done by phonem pay")
                    h = ctime()
                    print(h)
                    print(Accounts)
                else:
                    print("Insufficient funds. hee hee!")
            else:
                print("Invalid credential")



    else:
        print("Account number is not exist hee hee!")

def deposit_blance():
    account_number = int(input("Enter account number: "))
    amount = float(input("Enter amount to Deposit : "))

    if account_number in Accounts:
        Accounts[account_number]['Balance']+=amount
        print(f"Deposit {amount} new balance is {Accounts[account_number]['Balance']} hee hee!")
        print(Accounts)
    else:
        print("Account number is not exist hee hee!")
def check_blance():
    account_number = int(input("Enter account number: "))
    if account_number in Accounts:
        print(f"Balance for account {account_number} is {Accounts[account_number]['Balance']} hee hee!")
        print(Accounts)
    else:
        print("Account number is not exist hee hee!")

def main():
    while True:
        print("\nhee hee! Bank Management System ")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")
       # print(random())


        choice = int(input("hee hee! Enter your choice: "))

        if choice == 1:
            creat_account()
        elif choice == 2:
            deposit_blance()
        elif choice == 3:
            withdraw_blance()
        elif choice == 4:
            check_blance()
        elif choice == 5:
            print("Exiting the system. Goodbye! hee hee!")
            break
        else:
            print("Invalid choice. Please try again. hee hee!")

if __name__ == "__main__":
    main()