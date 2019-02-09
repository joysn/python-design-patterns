class MakeMeal:

    def buy_ingredients(self, money):
        if money < self.cost:
            assert 0, 'Not enough money to buy ingredients!'

    def prepare(self):
        pass

    def cook(self):
        pass

    def go(self, money):
        self.buy_ingredients(money)
        self.prepare()
        self.cook()

class MakePizza(MakeMeal):
    def __init__(self):
        self.cost = 3

    def prepare(self):
        print("Prepare Pizza - make the dough and add toppings")

    def cook(self):
        print("Cook Pizza - cook in the oven on gas mark 8 for 10 minutes")

class MakeCake(MakeMeal):
    def __init__(self):
        self.cost = 2

    def prepare(self):
        print("Prepare Cake - mix ingredients together and pour into a cake tin")

    def cook(self):
        print("Cook Cake - bake in the oven on gas mark 6 for 20 minutes")

		
p = MakePizza()
p.go(5)
c = MakeCake()
c.go(3)
p.go(2)
c.go(2)

# Output
# (base) D:\>python dp18_template.py
# Prepare Pizza - make the dough and add toppings
# Cook Pizza - cook in the oven on gas mark 8 for 10 minutes
# Prepare Cake - mix ingredients together and pour into a cake tin
# Cook Cake - bake in the oven on gas mark 6 for 20 minutes
# Traceback (most recent call last):
  # File "dp18_template.py", line 43, in <module>
    # p.go(2)
  # File "dp18_template.py", line 14, in go
    # self.buy_ingredients(money)
  # File "dp18_template.py", line 5, in buy_ingredients
    # assert 0, 'Not enough money to buy ingredients!'
# AssertionError: Not enough money to buy ingredients!