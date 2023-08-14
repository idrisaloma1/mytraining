class Customer:
    '''This mini Bank Application is developed by Idris'''

    bankname='HalalBank01'

    def __init__(self,name,phonenumber, balance=0.0):
        self.name=name
        self.phonenumber=phonenumber
        self.balance=balance
        
    def deposit(self,amount):
        self.balance = self.balance + amount
        print('Net Amount : ',self.balance)

    def withdraw(self,amount):

        if amount > self.balance:
            print('Sorry insufficient Balance')
        else:
            self.balance=self.balance-amount
            print('Net Balance : ',self.balance)

print(' Welcome to ',Customer.bankname)

name=input('Enter the Name: ')
phonenumber=eval(input('Enter the phonenumber: '))
c1 = Customer(name,phonenumber)



while True:
    print(' D - Deposit \n W - Withdraw \n E - exit ')
    optio = input('Enter the option : ')
    opt = optio.lower()
    if opt == 'd':
        amt = eval(input('Enter the amount : '))
        c1.deposit(amt)
    elif opt == 'w':
        amnt = eval(input('Enter the amount to withdraw : '))
        c1.withdraw(amnt)

    elif opt == 'e':
        print(' Thank you for banking with us')
        break
    else:
        print('Enter the valid option :')

