class Account:

    quantity = 0.0

    def __init__(self, identification_card, names, expedition_date, quantity=None):
        self.expedition_date = expedition_date
        self.identification_card = identification_card
        self.names = names
        if not (quantity is None):
            self.quantity = quantity

    def set_identification_card(self, identification_card):
        self.identification_card = identification_card

    def get_identification_card(self):
        return self.identification_card

    def set_names(self, names):
        self.names = names

    def get_names(self):
        return self.names

    def set_expedition_date(self, expedition_date):
        self.expedition_date = expedition_date

    def get_expedition_date(self):
        return self.expedition_date

    def set_quantity(self, quantity):
        self.quantity = quantity

    def get_quantity(self):
        return self.quantity

    def deposit(self, quantity):
        if quantity >= 0:
            self.quantity += quantity

    def retire(self, quantity):
        if quantity <= self.quantity:
            self.quantity = self.quantity - quantity
        else:
            self.quantity = 0.0
            print("Hizo un retiro de ", self.quantity)


account = Account(
    "1026154301", "Johan Alexander Londoño Bedoya", "20/09/2010", 10000)

account.retire(2000)
account.deposit(500)
print(account)
