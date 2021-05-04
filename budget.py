class Budget():

    def __init__(self, categories, amount):
        self.categories = categories
        self.amount = amount

    def deposit(self, new_amount):
        self.amount += new_amount
        return self.amount

    def withdraw(self, new_amount):
        self.amount -= new_amount
        return self.amount

    def check_balance(self):
        return self.amount

    @staticmethod
    def transfer(obj):
        return obj.check_balance()


obj1 = Budget("Food", 4000)
obj2 = Budget("cloth", 5000)

print(obj1.transfer(obj2))
