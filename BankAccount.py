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

    def print_receipt(self):
        """
        This method prints a recipt of the balance. This is usally displayed in all times where the balance is being manipulated.

        Parameters:
          - None.

        Result:
          - None.
        """
        print(
            f"""
      {self._full_name}
      Account No.: ****{self._account_number[-5:-1:1]}
      Routing No.: {self._routing_number}
      Balance: ${self.balance:.2f}"""
        )


def atm_terminal_intro():
    """
    This function is a helper. It is just used to print a nice welcoming message to translate and communicate instructions for the logic.
    It also creates a bank account stance for the logic to use in the return statement.

    Parameters:
      - None.

    Result:
      - BankAccount Instance - OBJECT - an instance from the BankAccount class using user responses to required inputs.
    """
    # Welcome Message
    print("Welcome to Make School's Virtual Bank!")
    print("Let's get your account sorted.")
    print()

    # Grabbing the inputs to use for the BankAccount Instance
    full_name = input("What's your full name? ")
    account_number = "02105678"
    routing_number = "98765432"
    balance = float(input("Amount of first deposit? "))
    print()

    # Create the instance for the user
    atm_user = BankAccount(full_name, account_number,
                           routing_number, balance)

    print(
        "For security purposes, the following information will only be displayed once.")
    print("Please keep note of them and save it somewhere safe.")
    print("==========================================================")
    print(f"Your assigned Account No.: {account_number}")
    print(f"Your assigned Routing No.: {routing_number}")
    atm_user.get_balance()
    print("==========================================================")
    print()

    # Return the instance for the the logic.
    return atm_user


def atm_interface(user):
    """
    This function is a modularlized version of the logic and navigation for the user.
    Hence, the name function name atm_interface.
    The interface will ask for four options, based on the user's input, the logic will follow using an if conditional.

    Parameters:
      - user: OBJECT - a BankAccount instance for a user.

    Return: 
      - None
    """

    # The flag helps break out of the while loop
    flag = True

    # Ask user for commands indefninitely until E is pressed.
    # Each command lands in a conditional.
    while flag:
        print()
        print("What would you like to do?")
        user_res = input("""
Enter one of the following:
    'D' to deposit money.
    'W' to withdraw money.
    'B' to display your current balance.
    'E' to end your session
""")

        if user_res == 'D':
            amount_deposit = float(input("Amount to deposit? "))
            print()
            user.deposit(amount_deposit)
        elif user_res == 'W':
            amount_withdraw = float(input("Amount to withdraw? "))
            print()
            user.withdraw(amount_withdraw)
        elif user_res == 'B':
            user.get_balance()
            print()
        elif user_res == 'E':
            flag = False
            print(
                "Thank you for your visit. Below is your recepit for your session.")
            user.print_receipt()
        else:
            print("Please enter a correct option.")
            print()


def atm_terminal():
    """
    This function is just mainly the index script to run the atm machine.

    Parameters:
      - None.

    Return:
      - None.
    """
    atm_user = atm_terminal_intro()
    atm_interface(atm_user)


# Invoke the fuinction
atm_terminal()

# Tests:
joi = BankAccount('Joi Anderson', '02105678', '98765432', 100)
joi.deposit(30)
joi.get_balance()
joi.withdraw(20)
joi.print_receipt()

ahmed = BankAccount('Ahmed Shahrour', '05155978', '98765432', 40)
ahmed.deposit(50)
ahmed.withdraw(20)
joi.get_balance()
ahmed.withdraw(600)
ahmed.print_receipt()

omar = BankAccount('Omar Gurashi', '09638698', '98765432', 0)
omar.deposit(0)
omar.withdraw(10)
joi.get_balance()
omar.deposit(120)
omar.print_receipt()
