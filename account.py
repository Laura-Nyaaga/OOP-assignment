class Account:
    def __init__(self, number, pin, owner_name="Unknown"):
        self.number = number
        self.__pin = pin
        self.__owner_name = owner_name
        self.__balance = 0
        self.__overdraft = None
        self.__minimum_balance = None
        self.__is_frozen = False
        self.__transaction_history = []
    def view_account_details(self, pin):
        if pin == self.__pin:
            return f"Account Number: {self.number}Owner Name: {self.__owner_name}Current Balance: {self.__balance}"
        else:
            return "Wrong PIN"
    def change_owner(self, new_owner_name, pin):
        if pin == self.__pin:
            self.__owner_name = new_owner_name
            return f"Account owner changed to {new_owner_name}."
        else:
            return "Wrong PIN"
    def account_statement(self, pin):
        if pin == self.__pin:
            transactions = ["Deposit $800", "Withdrawal $100"]
            return self.__transaction_history.append(transactions)
        else:
            return "Wrong PIN"
    def overdraft_limit(self, amount, pin):
        if pin == self.__pin:
            self.__overdraft = amount
            return f"Overdraft limit set to ${amount}."
        else:
            return "Wrong PIN"
    def calculate_interest(self, rate, time, pin):
        if pin == self.__pin:
            interest_amount = self.__balance * time * rate / 100
            self.__balance += interest_amount
            return f"Interest calculated. New balance: ${self.__balance}"
        else:
            return "Wrong PIN"
    def freeze_account(self, pin):
        if pin == self.__pin:
            self.__is_frozen = True
            return "Your Account is frozen."
        else:
            return "Wrong PIN"
    def unfreeze_account(self, pin):
        if pin == self.__pin:
            self.__is_frozen = False
            return "Your Account is unfrozen."
        else:
            return "Wrong PIN"
    def transaction_history(self, pin):
        if pin == self.__pin:
            return self.__transaction_history
        else:
            return "Wrong PIN"
    def set_minimum_balance(self, min_balance, pin):
        if pin == self.__pin:
            self.__minimum_balance = min_balance
            return f"Minimum balance requirement set to ${min_balance}."
        else:
            return "Wrong PIN"
    def transfer_funds(self, money, recipient_number, pin):
        if pin == self.__pin:
            if self.__balance >= money:
                self.__balance -= money
                self.__transaction_history.append(f"Withdrawal: ${money} to {recipient_number}")
                return f"Funds transferred successfully. New balance: ${self.__balance}"
            else:
                return "Insufficient funds."
        else:
            return "Wrong PIN"
    def close_account(self, pin):
        if pin == self.__pin:
            return "Your is Account closed."
        else:
            return "Wrong PIN"
        
bank = Account(112345, 4444, "Laura Nyaaga")
# print(transfer_funds(money=120,recipient_number=76543, pin=444))

        