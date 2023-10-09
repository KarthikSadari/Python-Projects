#Coffee Machine
menu ={
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":25,
        },
        "cost":150
    },
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":20,
        },
        "cost":100
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24,
        },
        "cost":200
    }
}

profit = 0
resources = {
    "water":1000,
    "milk":500,
    "coffee": 250,
       "cost":0}

def check_resource(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            print(f"Sorry ther is not enough {item}")
            return False
    return True

def process_coins():
    print("Please insert the coins:")
    total = 0
    five_coins = int(input("How many 5Rs coins?: "))
    ten_coins = int(input("How many 10Rs coins?: "))
    twenty_coins = int(input("How many 20Rs coins?: "))
    total = five_coins*5 +ten_coins*10 +twenty_coins*20
    return total

def is_payment_successful(money_received,coffee_cost):
    if money_received >= coffee_cost:
        global profit
        profit += coffee_cost
        change = money_received-coffee_cost
        print(f"Here is your RS{change} in Change.")
        return True
    else:
        print("Sorry that's not enough money. Money Refunded.")
        return False

def make_coffee(coffee_name,coffee_ingredients):
    for item in coffee_ingredients:
        resources[item] -= coffee_ingredients[item]
    print(f"Here is your {coffee_name}.")

is_on = True
while is_on:
    choice = input("What would you like to have? (latte/espresso/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water = {resources['water']}ml")
        print(f"Milk = {resources['milk']}ml")
        print(f"Coffe = {resources['coffee']}gm")
        print(f"Money =Rs.{profit}")
    else:
        coffee_type = menu[choice]
        print(coffee_type)
        check_resource(coffee_type["ingredients"])
        payment = process_coins()
        if is_payment_successful(payment,coffee_type['cost']):
            make_coffee(choice,coffee_type['ingredients'])
    
    