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
    "money":0
}
def check(a):
    if any(resources[item] < MENU[choice]['ingredients'][item] for item in MENU[choice]['ingredients']) :
        print(f"Sorry, there is not enough of resources")
        return  False
    else:
        return True
status=True
while status:
    choice=input("What would you like? (espresso/latte/cappuccino):")
    if choice=="off":
        status=False
    elif choice=="report":
        print(f"Water:{resources['water']}\n Milk:{resources['milk']}\nCoffee:{resources['coffee']}\nMoney:${resources['money']}")
    else:
        if check(choice):
            print("Please insert coins.")
            a=int(input("how many quarters?:"))
            b=int(input("how many dimes?:"))
            c=int(input("how many nickles?:"))
            d=int(input("how many pennies?:"))
            cash=((a*0.25)+(b*0.1)+(c*0.05)+(d*0.01))
            if cash>=MENU[choice]['cost']:
                money_return=round(cash-MENU[choice]['cost'],2)
                print(f"Here is ${money_return} in change")
                print(f"Here is your {choice} ☕.")
                resources['water']-=MENU[choice]['ingredients']['water']
                resources['milk']-=MENU[choice]['ingredients']['milk']
                resources['coffee']-=MENU[choice]['ingredients']['coffee']
            else:
                print("Sorry! that's not enough money.Money refunded")
