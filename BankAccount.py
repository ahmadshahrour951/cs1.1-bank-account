class BankAccount:
    def __init__(self, full_name, account_number, routing_number, balance=0):
        """
        This method creates the bank account's instance variables from the given four parameters.

        Parameters:
          - full_name: STRING - The full name of the user.
          - account_number: STRING - The account number of the bank account.
          - routing_number: STRING - The routing number of the bank account.
          - balance: FLOAT - The latest and current balance of the bank account.

        Return:
          - None.
        """
        self._full_name = full_name
        self._account_number = account_number
        self._routing_number = routing_number
        self.balance = balance

    def deposit(self, amount):
        """
        This method manipulates the self.balance instance variable to reflect a deposit.

        Parameters:
          - amount: FLOAT - The amount the user wants to deposit.

        Return:
          - None.
        """
        self.balance += amount
        print(f'Amount Deposited: ${amount:.2f}')
        self.print_receipt()

    def atm_charge(self):
        """
        This method manipulates the self.balance instance variable to reflect an ATM service charge after a withdraw.

        Return:
          - None.
        """
        self.balance -= 2

    def withdraw(self, amount):
        """
        This method manipulates the self.balance instance variable to reflect a withdraw of cash.
        This requires an atm charge, however if the user doesn't have enought money on the account there will be a $10 penelaty.
        If the balance is positive, there will be a interest gain for the user.

        Parameters:
          - amount: FLOAT - The amount the user wants to withdraw.

        Return:
           - None.
        """
        if amount > self.balance:
          #  Check if the amount requested exceeds the account balance. If so, deduct $10.
            self.balance -= 10
            print("Insufficient funds.")
        else:
          #   Otherwise, charge an atm_charge() and deduct the amount requsted from the current balance.
            self.atm_charge()
            self.balance -= amount
            print(
                f"""
          ATM Charge: $2.00
          Amount Withdrawn: ${amount:.2f}
          """
            )

        if self.balance > 0:
            # Since a positive balance in, everytime the user withdraws, I incur an interest on the balance, since we're using their money to loan to other people lol...
            self.add_interest()

        self.print_receipt()

    def get_balance(self):
        """
        This method only displays the latest and the most current balance of the bank account.

        Parameters:
          - None.

        Return:
          - None.
        """
        print(f'Your Current Balance: ${self.balance:.2f} ')
        return self.balance

    def add_interest(self):
        """
        This method manipulates the balance to incorporate an interest gain for the user.

        Parameters:
          - None.

        Result:
          - None.
        """
        self.balance += self.balance * 0.00083

