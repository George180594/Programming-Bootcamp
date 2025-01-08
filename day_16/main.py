# # import turtle
# from turtle import Turtle,Screen
# # timy=turtle.Turtle()
# timy=Turtle()
# timy.shape('turtle')
# timy.color('red','green')
# timy.forward(100)

# my_screen= Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column("Pokemon",["pikachu",'Squirtle'])
# table.add_column("Type",["eletric",'water'])
# table.align= "l"
# print(table)
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from menu import MenuItem, Menu  
#Print report
money_machine= MoneyMachine()
coffee_maker= CoffeeMaker()
menu= Menu()
is_on= True

#Check resourcers
while is_on:
    options=menu.get_items()
    choice=input(f'What would you like? {options}\n')
    if choice=='off':
        is_on= False
    elif choice=='report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink= menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)