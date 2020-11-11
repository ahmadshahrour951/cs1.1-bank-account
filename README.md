# cs1.1-bank-account

Language Used: **Python 3.8.6 64-bit**

In this project, I'm creating a BankAccount class that instantiates bank account objects. Each bank account has a many-to-one relationship with users. So that means bank accounts are inherintily related to users, therefore information about the user will be required to be initiatlized.

Within the class, we create instance variables that hold key information about the user's Bank Account. I've made a few of those variables protected to indiciate to the developer to tread lightly in the **init** terrain.

Then, each method was created to manipulate the instance variables and display useful information to the user. It acts as a interface for the user, a form of abstraction we call the black box.

Finally, I created a abstract terminal that communicates with the user for basic logic instructions for their Bank Account.
