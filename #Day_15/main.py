MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# machine resources
# think of making these variables as a dictionary
machineMoney = 0
machineWater = 500
machineMilk = 500
machineCoffee = 500


# TODO : 1. Print a report of all coffe machine resources
def printResources():
    print(f"Water: {machineWater}ml")
    print(f"Milk: {machineMilk}ml")
    print(f"Coffee: {machineCoffee}g")
    print(f"Money: ${machineMoney}")


def processOrder(drink):

    # These variables should be declared as global because it's overriden with new values
    global machineCoffee
    global machineMilk
    global machineWater
    global machineMoney

    requiredDrink = MENU[drink]

    cost = requiredDrink["cost"]
    requiredWater = requiredDrink["ingredients"]["water"]
    requiredCoffee = requiredDrink["ingredients"]["coffee"]

    if drink != "espresso":
        requiredMilk = requiredDrink["ingredients"]["milk"]
    else:
        requiredMilk = 0

    # TODO : 2. Check that resources are sufficient to make the drink
    if (
            machineWater < requiredWater or
            machineMilk < requiredMilk or
            machineCoffee < requiredCoffee
    ):
        print("Sorry there is not enough water.")
        return 0
    else:
        machineWater -= requiredWater
        machineCoffee -= requiredCoffee
        machineMilk -= requiredMilk

        print("please insert coins.")
        quarters = int(input("How many quarters?"))
        dimes = int(input("How many dimes?"))
        nickels = int(input("How many nickles?"))
        pennies = int(input("How many pennies?"))
        totalMoney = (quarters * 25 + dimes * 10 + nickels * 5 + pennies) / 100

        if totalMoney < cost:
            print("Sorry there is not enough money.")
        else:
            machineMoney += cost
            print(f"Here is ${round(totalMoney - cost, 3)} dollars in change.")
            print(f"Here is your {drink}. Enjoy")


order = True
while order:
    drink = input("What would you like? (espresso/latte/cappuccino): ")
    if drink == 'off':
        order = False
    elif drink == 'report':
        printResources()
    else:
        processOrder(drink)

print("Thank you!")