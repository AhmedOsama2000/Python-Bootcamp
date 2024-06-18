from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_off = False

while not is_off:
    order = input(f"What would you like? {menu.get_items()}: ")

    if order == 'off':
        is_off = True
    elif order == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        if not menu.find_drink(order):
            continue
        drink_object = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink_object) and money_machine.make_payment(drink_object.cost):
            coffee_maker.make_coffee(drink_object)

print("Thank you!")
