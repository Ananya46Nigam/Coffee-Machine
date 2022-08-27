from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo 

print(logo)


money_machine=MoneyMachine()
cofee_maker=CoffeeMaker()
# print(money_machine.report())



is_on=True
while is_on:
    menu=Menu()
    print("* * * * *      MENU       * * * * * * ")
    print(menu.get_items())
    drink=input("What would you like to order?").lower().strip()
    if drink=="off":
        is_on=False
    elif drink=="report":
        cofee_maker.report()
        money_machine.report()
    else:
        is_available=menu.find_drink(drink)
        if cofee_maker.is_resource_sufficient(is_available)==True and money_machine.make_payment(is_available.cost):
                # money_machine.make_payment(is_available)
                cofee_maker.make_coffee(is_available)
                
            
            
