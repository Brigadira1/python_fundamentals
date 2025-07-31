from Latte import Latte
from Capuccinno import Capuccinno
from Espresso import Espresso
from CoffeeMachine import CoffeeMachine


def make_coffee():
    coffee_machine = CoffeeMachine()
    coffee_types = ("latte", "cappuccino", "espresso", "report")
    while True:
        while True:
            user_selection = input("What would you like? (espresso/latte/cappuccino): ").lower()
            if user_selection not in coffee_types:
                print("The only valid choices are: late, cappuccino or espresso....")
                continue
            break

        if user_selection == "cappuccino":
            coffee_machine.make_coffee(Capuccinno())
        elif user_selection == "latte":
            coffee_machine.make_coffee(Latte())
        elif user_selection == "espresso":
            coffee_machine.make_coffee(Espresso())
        else:
            coffee_machine.print_report()


if __name__ == "__main__":
    make_coffee()
