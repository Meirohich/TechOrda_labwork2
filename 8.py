class Bank:
    def __init__(self, balance):
        self.balance = balance

    def addBalance(self, balance):
        self.balance += balance

    def subBalance(self, balance):
        self.balance -= balance

    def convert(self, balance, m1, m2):
        if m1 == 'USD' and m2 == 'KZT':
            print(f'{balance, m1} to {balance * 470, m2}')
        elif m1 == 'RUB' and m2 == 'KZT':
            print(f'{balance, m1} to {balance * 8, m2}')
        elif m1 == 'KZT' and m2 == 'USD':
            print(f'{balance, m1} to {balance / 470, m2}')


bank = Bank(100)
bank.addBalance(123)
bank.subBalance(213)
bank.convert(300, 'USD', 'KZT')
print(bank.balance)
