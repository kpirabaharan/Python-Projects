MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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


def report(mon):
    print(f'Water: {resources["water"]}')
    print(f'Milk: {resources["milk"]}')
    print(f'Coffee: {resources["coffee"]}')
    print(f"Money: ${mon}")


def payment():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    pay = 0.25*quarters + 0.1*dimes + 0.05*nickels + 0.01*pennies

    return round(pay, 2)


def check(tot, ch, mon):
    if tot < MENU[ch]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    if resources["water"] < MENU[ch]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
    if resources["coffee"] < MENU[ch]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
    if resources["milk"] < MENU[ch]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
    if tot >= MENU[ch]["cost"] and resources["water"] >= MENU[ch]["ingredients"]["water"] \
            and resources["coffee"] >= MENU[ch]["ingredients"]["coffee"] \
            and resources["milk"] >= MENU[ch]["ingredients"]["milk"]:
        change = total - MENU[ch]["cost"]
        resources["water"] -= MENU[ch]["ingredients"]["water"]
        resources["milk"] -= MENU[ch]["ingredients"]["milk"]
        resources["coffee"] -= MENU[ch]["ingredients"]["coffee"]
        mon += MENU[ch]["cost"]
        print(f"Here is ${change} in change.")
        print(f"Here is your {ch}. Enjoy!")
    return mon


fin = False
money = 0
while not fin:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        fin = True
    if choice == "report":
        report(money)
    if choice == "espresso" or choice == "latte" or choice == "cappuccino":
        total = payment()
        money = check(total, choice, money)

















