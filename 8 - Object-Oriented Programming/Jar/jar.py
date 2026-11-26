class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0


    def __str__(self):
        return("🍪" * self.size)


    def deposit(self, deposit):
        space = self.capacity - self.size
        if type(deposit) != int:
            raise ValueError("Deposit value is not an integer")
        if deposit > space:
            raise ValueError("Deposit value is greater than available space")
        if deposit < 0:
            raise ValueError("Deposit value is negative")
        self.size = self.size + deposit


    def withdraw(self, withdrawal):
        if type(withdrawal) != int:
            raise ValueError("Withdrawal value is not an integer")
        if withdrawal > self.size:
            raise ValueError("Withdrawal value is greater than available cookies")
        if withdrawal < 0:
            raise ValueError("Withdrawal value is negative")
        self.size = self.size - withdrawal


    @property
    def capacity(self):
        return self._capacity


    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Negative capacity")
        if type(capacity) != int:
            raise ValueError("Capacity is not an integer")
        self._capacity = capacity


    @property
    def size(self):
        return self._size


    @size.setter
    def size(self, size):
        if size < 0:
            raise ValueError("Negative balance")
        if size > self.capacity:
            raise ValueError("Balance is greater than capacity")
        if type(size) != int:
            raise ValueError("Balance is not an integer")
        self._size = size


def main():
    cookie = Jar()
    cookie.deposit("co")
    while True:
        choice = selection_menu()
        if choice == 1:
            print(cookie)
        if choice == 2:
            try:
                deposit_amount = int(input("How many cookies would you like to deposit? "))
                cookie.deposit(deposit_amount)
                print(f"{deposit_amount} cookies succesfully deposited")
            except ValueError:
                print("Invalid deposit amount")

        if choice == 3:
            try:
                withdrawal_amount = int(input("How many cookies would you like to deposit? "))
                cookie.withdraw(withdrawal_amount)
                print(f"{withdrawal_amount} cookies succesfully deposited")
            except ValueError:
                print("Invalid withdrawal amount")
        if choice == 4:
            break
        if choice == 5:
            while True:
                answer = input("""WARNING: Changing capacity will create a new cookie jar!
Do you still want to change capacity yes or no? """)
                if answer == "yes" or answer == "no":
                    break
                else:
                    print("Please choose a valid option")
            if answer == "yes":
                while True:
                    try:
                        new_capacity = int(input("New capacity: "))
                    except ValueError:
                        print("Invalid new capacity")
                        continue
                    break
            if answer == "no":
                print("No changes made")
                cookie = Jar(new_capacity)


def selection_menu():
    while True:
        print("""
    ===Cookie Jar Menu===
    1. Cookie Balance
    2. Deposit Cookies
    3. Withdraw Cookies
    4. Exit
    =====================
    """)
        choice = input("Please select an option(1-4): ")
        try:
            if choice == "Change Capacity":
                return 5
            elif 1 <= int(choice) <= 4:
                return int(choice)
            else:
                print("Please choose a valid option")
                continue
        except ValueError:
            print("""
            Please choose a valid option""")
            continue


if __name__ == "__main__":
    main()