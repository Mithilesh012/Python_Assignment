class GPay:
    def __init__(self, user_name, initial_balance=0):
        self.user_name = user_name
        self.balance = initial_balance

    def add_money(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Added {amount} rupees to {self.user_name}'s account. New balance is {self.balance} rupees.")
            print(type(amount))
        else:
            print("Invalid amount. Please enter a positive amount to add.")

    def make_payment(self, amount):
        if amount <= 0:
            print("Invalid amount. Please enter a positive amount to pay.")
        elif amount > self.balance:
            print(f"Insufficient balance. {self.user_name}'s current balance is {self.balance} rupees.")
        else:
            self.balance -= amount
            print(f"{self.user_name} paid {amount} rupees. New balance is {self.balance} rupees.")

    def check_balance(self):
        print(f"{self.user_name}'s current balance is {self.balance} rupees.")

def main():
    user_name = input("Enter your name: ")
    initial_balance = float(input("Enter initial balance: "))
    user = GPay(user_name, initial_balance)

    while True:
        print("\nChoose an option:")
        print("1. Add Money")
        print("2. Make Payment")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount to add: "))
            user.add_money(amount)
        elif choice == '2':
            amount = float(input("Enter amount to pay: "))
            user.make_payment(amount)
        elif choice == '3':
            user.check_balance()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
