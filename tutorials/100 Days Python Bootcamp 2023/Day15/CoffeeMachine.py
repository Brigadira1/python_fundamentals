from Espresso import Espresso
from Capuccinno import Capuccinno
from Latte import Latte


class CoffeeMachine:
    def __init__(self):
        self.__water = 300
        self.__milk = 200
        self.__coffee = 100
        self.__money = 0

    def get_water(self):
        return self.__water

    def get_milk(self):
        return self.__milk

    def get_coffee(self):
        return self.__coffee

    def get_money(self):
        return self.__money

    def add_money(self, money):
        self.__money += money

    def subract_water(self, quantity):
        self.__water = self.__water - quantity

    def subtract_milk(self, quantity):
        self.__milk = self.__milk - quantity

    def subtract_coffee(self, quantity):
        self.__coffee = self.__coffee - quantity

    def make_coffee(self, coffee_type):
        if not self.validate_ingredients(coffee_type.water, coffee_type.coffee, coffee_type.milk):
            return
        user_input = self.calculate_coins()
        print(f"User put ${user_input:.02f} in the machine!")
        if user_input < coffee_type.cost:
            print("Sorry that's not enough money! Money refunded.")
            return
        elif user_input > coffee_type.cost:
            print(f"Here is ${(user_input - coffee_type.cost):.02f} in change")
            print("Enjoy your coffee")
        self.add_money(coffee_type.cost)
        self.subract_water(coffee_type.water)
        self.subtract_coffee(coffee_type.coffee)
        self.subtract_milk(coffee_type.milk)

    def validate_ingredients(self, water, coffee, milk):
        is_valid = True

        if water > self.get_water():
            print("Sorry, not enough water!")
            is_valid = False
        elif coffee > self.get_coffee():
            print("Sorry, not enough coffee!")
            is_valid = False
        elif milk != 0 and milk > self.get_milk():
            print("Sorry, not enough milk!")
            is_valid = False

        return is_valid

    def print_report(self):
        print(f"Water: {self.get_water()}")
        print(f"Milk: {self.get_milk()}")
        print(f"Coffee: {self.get_coffee()}")
        print(f"Money: {self.get_money()}")

    def calculate_coins(self):
        quarters = int(input("How many quarters: "))
        dimes = int(input("How many dimes: "))
        nickels = int(input("How many nickels: "))
        pennies = int(input("How many pennies: "))

        return quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
