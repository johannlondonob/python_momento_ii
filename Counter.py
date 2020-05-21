class Counter:

    def __init__(self, counter=0):
        self.counter = counter

    def __str__(self):
        return self.counter

    def set_counter(self, counter=0):
        self.counter = counter

    def get_counter(self):
        return self.counter

    def increase(self, increase=1):
        counter = self.counter + increase
        self.set_counter(counter)

    def decrease(self, decrease=1):
        counter = self.counter - decrease
        self.set_counter(counter)


counter = Counter(5)
print('Valor inicial:', counter.__str__())
counter.increase(8)
print('Valor luego de incrementarse:', counter.__str__())
counter.decrease(5)
print('Valor luego de decrementarse:', counter.__str__())
