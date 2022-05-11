from dict import MENU
from dict import resources

loop = True
money = 0

quarter = 0.25
dime = 0.1
nickle = 0.05
penny = 0.01


def funding(choice):
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    wallet = round((quarter * quarters) + (dime * dimes) + (nickle * nickles) + (penny * pennies), 2)

    if wallet > int(MENU[choice]['cost']):
        wallet -= int(MENU[choice]['cost'])
        print(f"Here is your {choice}!")
        print(f"${wallet} is your change.")
        again = input("Would you like to order again? Y/N: ").lower()
        if again == "n":
            print("Thank you! Come again!")
            loop = False
        resources['water'] -= MENU[choice]['ingredients']['water']
        resources['coffee'] -= MENU[choice]['ingredients']['coffee']
        if choice != "espresso":
            resources['milk'] -= MENU[choice]['ingredients']['milk']

    else:
        print("Sorry that's not enough money. Money refunded.")



while loop:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        loop = False
        print("Powering Down")

    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")

# def resource_check(water, milk, coffee):
    elif choice == "espresso":
        if resources['water'] < MENU['espresso']['ingredients']['water']:
            print("Sorry there is not enough water.")

        elif resources['coffee'] < MENU['espresso']['ingredients']['coffee']:
            print("Sorry there is not enough coffee.")

        else:
            print("Espressos are $1.5. Please insert coins")
            funding(choice)


    elif choice == "latte":
        if resources['water'] < MENU['latte']['ingredients']['water']:
            print("Sorry there is not enough water.")

        elif resources['milk'] < MENU['latte']['ingredients']['milk']:
            print("Sorry there is not enough milk.")

        elif resources['coffee'] < MENU['latte']['ingredients']['coffee']:
            print("Sorry there is not enough coffee.")

        else:
            print("Lattes are $2.5. Please insert coins.")
            funding(choice)
            # transaction(choice)

    elif choice == "cappuccino":
        if resources['water'] < MENU['cappuccino']['ingredients']['water']:
            print("Sorry there is not enough water.")

        elif resources['milk'] < MENU['cappuccino']['ingredients']['milk']:
            print("Sorry there is not enough milk.")

        elif resources['coffee'] < MENU['cappuccino']['ingredients']['coffee']:
            print("Sorry there is not enough coffee.")

        else:
            print("Cappuccinos are $3.0. Please insert coins.")
            funding(choice)
            # transaction(choice)
    else:
        print("That is not a valid input, please try again.")

    print(resources['coffee'])