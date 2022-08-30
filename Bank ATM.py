import sys

#Backend
class cust:
    '''HDFC bank code wire class'''
    bankname = 'HDFC'
    pincode = 100


    def __init__(self,name,balance = 0.0):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance + amount
        print("Current balance of your HDFC account is Rs:", self.balance)

    def withdraw(self,amount):
        if amount > self.balance:
            print("Your bank balance is to low. Please recharge your bank account.")
            sys.exit()
        self.balance = self.balance - amount
        print("Current balance of your HDFC account is Rs:", self.balance)

#Frontend
print("Welcome to",cust.bankname)
name = input('Pls enter your name:')
C = cust(name)

for i in range(3,0,-1):
    pin = int(input('Enter your HDFC bank pin:'))
    if pin == cust.pincode:
         break
    else:
        sys.exit

while True:
    print(' D/d = Deposit\n W/w = Withdraw\n B/b = Balace\n E/e = Exit' )
    option = input("Enter your option:")
    if option == 'd' or option == 'D':
        amount = float(input("Enter amount:"))
        C.deposit(amount)
    elif option == 'w' or option == 'W':
        amount = float(input('Enter amount:'))
        C.withdraw(amount)
    elif option == 'e' or option == 'E':
        sys.exit()
    else:
        print('Invalid option.Thank you for banking with HDFC.')



