

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print('User: ' + self.name + ', Saldo: $ ' + str(self.account_balance))

    def transfer_money(self, user_transf, amount):
        self.make_withdrawal(amount)
        user_transf.make_deposit(amount)
        
        #cta_transf.make_deposit(amount)
        self.display_user_balance()
        user_transf.display_user_balance()
        

# Instanciando
jaime = User('Jaime Sepúlveda Aguilera', 'jsepulveda.aguilera@gmail.com')
maria = User('María Paz Lagos', 'm.paz.lagos.r@gmail.com')
maximiliano = User('Maximiliano Riquelme', 'm.paz.lagos.r@gmail.com')

jaime.make_deposit(100)
jaime.make_deposit(150)
jaime.make_deposit(210)
jaime.display_user_balance()

maria.make_deposit(230)
maria.make_deposit(70)
maria.make_withdrawal(100)
maria.make_withdrawal(50)
maria.display_user_balance()

maximiliano.make_deposit(230)
maximiliano.make_withdrawal(30)
maximiliano.make_withdrawal(50)
maximiliano.make_withdrawal(40)
maximiliano.display_user_balance()

jaime.transfer_money(maximiliano,100)

#print('User: ' + jaime.name + ', Saldo: $ ' + str(jaime.account_balance))
#print(maria.account_balance)

