class BankAccount:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            return False
        self.balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0:
            return False

        if amount > self.balance:
            return False

        self.balance -= amount
        return True


class ATM:
    def __init__(self):
        self.accounts = {
            "1234": BankAccount("1234", 10000),
            "5678": BankAccount("5678", 5000)
        }

    def authenticate(self, pin):
        return self.accounts.get(pin)

    def run(self):
        print("=" * 40)
        print("       WELCOME TO PYTHON ATM")
        print("=" * 40)

        attempts = 3
        account = None

        while attempts > 0:
            pin = input("Enter your 4-digit PIN: ")

            account = self.authenticate(pin)

            if account:
                print("\nLogin successful!")
                break

            attempts -= 1
            print(f"Invalid PIN. Attempts remaining: {attempts}")

        if account is None:
            print("\nToo many incorrect attempts.")
            print("Your account has been locked.")
            return

        while True:
            print("\n" + "=" * 40)
            print("ATM MENU")
            print("=" * 40)
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")
            print("=" * 40)

            choice = input("Enter your choice: ")

            if choice == "1":
                print(f"\nCurrent balance: ₹{account.check_balance():.2f}")

            elif choice == "2":
                try:
                    amount = float(input("Enter deposit amount: ₹"))

                    if account.deposit(amount):
                        print(f"₹{amount:.2f} deposited successfully.")
                        print(f"New balance: ₹{account.check_balance():.2f}")
                    else:
                        print("Invalid deposit amount.")

                except ValueError:
                    print("Please enter a valid number.")

            elif choice == "3":
                try:
                    amount = float(input("Enter withdrawal amount: ₹"))

                    if amount > account.check_balance():
                        print("Insufficient balance.")

                    elif account.withdraw(amount):
                        print(f"₹{amount:.2f} withdrawn successfully.")
                        print(f"Remaining balance: ₹{account.check_balance():.2f}")

                    else:
                        print("Invalid withdrawal amount.")

                except ValueError:
                    print("Please enter a valid number.")

            elif choice == "4":
                print("\nThank you for using Python ATM.")
                print("Please take your card.")
                break

            else:
                print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    atm = ATM()
    atm.run()class BankAccount:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            return False
        self.balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0:
            return False

        if amount > self.balance:
            return False

        self.balance -= amount
        return True


class ATM:
    def __init__(self):
        self.accounts = {
            "1234": BankAccount("1234", 10000),
            "5678": BankAccount("5678", 5000)
        }

    def authenticate(self, pin):
        return self.accounts.get(pin)

    def run(self):
        print("=" * 40)
        print("       WELCOME TO PYTHON ATM")
        print("=" * 40)

        attempts = 3
        account = None

        while attempts > 0:
            pin = input("Enter your 4-digit PIN: ")

            account = self.authenticate(pin)

            if account:
                print("\nLogin successful!")
                break

            attempts -= 1
            print(f"Invalid PIN. Attempts remaining: {attempts}")

        if account is None:
            print("\nToo many incorrect attempts.")
            print("Your account has been locked.")
            return

        while True:
            print("\n" + "=" * 40)
            print("ATM MENU")
            print("=" * 40)
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")
            print("=" * 40)

            choice = input("Enter your choice: ")

            if choice == "1":
                print(f"\nCurrent balance: ₹{account.check_balance():.2f}")

            elif choice == "2":
                try:
                    amount = float(input("Enter deposit amount: ₹"))

                    if account.deposit(amount):
                        print(f"₹{amount:.2f} deposited successfully.")
                        print(f"New balance: ₹{account.check_balance():.2f}")
                    else:
                        print("Invalid deposit amount.")

                except ValueError:
                    print("Please enter a valid number.")

            elif choice == "3":
                try:
                    amount = float(input("Enter withdrawal amount: ₹"))

                    if amount > account.check_balance():
                        print("Insufficient balance.")

                    elif account.withdraw(amount):
                        print(f"₹{amount:.2f} withdrawn successfully.")
                        print(f"Remaining balance: ₹{account.check_balance():.2f}")

                    else:
                        print("Invalid withdrawal amount.")

                except ValueError:
                    print("Please enter a valid number.")

            elif choice == "4":
                print("\nThank you for using Python ATM.")
                print("Please take your card.")
                break

            else:
                print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    atm = ATM()
    atm.run()