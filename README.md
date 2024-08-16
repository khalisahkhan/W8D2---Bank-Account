# W8D2---Bank-Account

# Overview:
This is a bank account management system implemented in Python using Object Oriented Programming (OOP) principles. The system allows users to create bank accounts, perform deposits and withdrawals, and view account details. 

# Features
- Create bank accounts with account numbers, account owner and initial balances
- Deposit funds
- Withdraw funds and ensuring sufficient funds are available
- View account information

# Bank Account Class
Attributes:

`__accountNumber` (string): Unique identifier for the bank account (private).
`__accountHolder` (string): Name of the account holder (private).
`__balance` (float): Current balance of the account (private).
Methods:

`__init__(self, accountNumber, accountHolder, initialBalance)`: Constructor to initialize the bank account.
`deposit(self, amount)`: Deposits a specified amount into the account if it is positive.
`withdraw(self, amount)`: Withdraws a specified amount from the account if it is positive and there are sufficient funds.
`getBalance(self)`: Returns the current balance of the account.
displayAccountInfo(self): Displays the account number, account holder name, and current balance.

# Clone repository
git clone 



