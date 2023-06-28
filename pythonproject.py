


class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: +bdt {amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -bdt {amount}")
        else:
            print("Bankrupt: Insufficient funds to withdraw.")

    def transfer(self, recipient, amount):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            self.transactions.append(f"Transfer: - bdt {amount} to {recipient.name}")
            recipient.transactions.append(f"Transfer: + bdt {amount} from {self.name}")
        else:
            print("Bankrupt: Insufficient funds to transfer.")

    def check_balance(self):
        return self.balance

    def check_transaction_history(self):
        return self.transactions

    def take_loan(self):
        loan_amount = self.balance * 2
        self.balance += loan_amount
        self.transactions.append(f"Loan: + bdt {loan_amount}")
        return loan_amount


class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, name):
        user = User(name)
        self.bank.users.append(user)
        return user

    def check_total_balance(self):
        total_balance = sum(user.balance for user in self.bank.users)
        return total_balance

    def check_total_loan_amount(self):
        total_loan_amount = sum(user.balance for user in self.bank.users if user.balance < 0)
        return total_loan_amount

    def enable_loan_feature(self):
        self.bank.loan_feature_enabled = True

    def disable_loan_feature(self):
        self.bank.loan_feature_enabled = False


class Bank:
    def __init__(self):
        self.users = []
        self.loan_feature_enabled = True




bank = Bank()


admin = Admin(bank)

# Create user accounts
user1 = admin.create_account("Rahim")
user2 = admin.create_account("Karim")

user1.deposit(1000)
user1.withdraw(500)
user2.deposit(2000)
user1.transfer(user2, 300)

print(user1.check_balance())  
print(user2.check_balance())  
print(user1.check_transaction_history())  
print(user2.check_transaction_history())  

loan_amount = user1.take_loan()
print(loan_amount)  
print(user1.check_balance())  


print(f'Total balance is : {admin.check_total_balance()}') 
print( user1.take_loan()  ) 
 

