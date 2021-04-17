class Budget:
    """This class lets the user create categories, make deposit, check balance account,
    make transfer between  created categories, from created category"""
    print('Welcome to the Budget app')
    def __init__(self,category):
        self.category = category
        self.balance = 0
    def check_category(self):
        """this method lets the user check the category that was created"""
        print( f'You created {self.category} category')

    def withdraw(self,amount):
        if amount > self.balance:
            print('Insuffient funds')
        else:
            self.balance -= amount
            print( f'You have withdrawn {amount} naira'.format(amount))
    
    def check_balance(self):
        print(f'Your current balance is {self.balance} naira'.format(self.balance))


    def deposit(self,amount):
        #self.deposit = deposit
        #added_amt = self.deposit + self.lists
        #self.lists.append([deposit])
        self.balance += amount
        print(f'You have deposited {amount} to your budget account'.format(amount))
        
    def transfer(self,amount):
          if amount > self.balance:
            print('Insuffient funds')
          else:
            self.balance -= amount
            print( f'You have transfered {amount} naira'.format(amount))
    
        

a = Budget('food')
a.deposit(60000)
a.withdraw(4000)
a.check_balance()
a.transfer(50)
a.check_balance()
a.check_category()


