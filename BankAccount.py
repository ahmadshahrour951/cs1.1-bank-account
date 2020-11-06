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

