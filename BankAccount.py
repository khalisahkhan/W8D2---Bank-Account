class BankAccount:
    def __init__(self, accountNumber, accountHolder, initialBalance):
        self.__accountNumber = accountNumber
        self.__accountHolder = accountHolder
        self.__balance = initialBalance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew {amount}. New balance: {self.__balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def getBalance(self):
        return self.__balance

    def displayAccountInfo(self):
        print(f"Account Number: {self.__accountNumber}")
        print(f"Account Holder: {self.__accountHolder}")
        print(f"Balance: {self.__balance}")
        
def main():
    account1 = BankAccount("004887443", "Khalisah Khan", 500.0)
    account2 = BankAccount("004864021", "Hajra Nawel", 1000.0)

    print("Initial Account Info:")
    account1.displayAccountInfo()
    account2.displayAccountInfo()
    
    print("\nPerforming Transactions:")
    account1.deposit(200)
    account1.withdraw(50)
    account1.withdraw(1000) 
    
    account2.deposit(-100)
    account2.deposit(300)
    account2.withdraw(1500) 
    account2.withdraw(100)

    print("\nUpdated Account Info:")
    account1.displayAccountInfo()
    account2.displayAccountInfo()

if __name__ == "__main__":
    main()