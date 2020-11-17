import sys
from modules.constants import WELCOME, OPTION_1, OPTION_2, OPTION_3, OPTION_4, FAREWELL, PIZZAS, INGREDIENTS, DRINKS, SELECT_OPTION, NUMBER_ERROR
from modules.visuals import header
from modules.order import executeOrder
from modules.history import deleteHistory
from modules.order_history import getOrderHistory
from os import system

def menu():
  while True:
    system("cls")
    header()
    print()
    print(WELCOME)
    print()
    print(OPTION_1)
    print(OPTION_2)
    print(OPTION_3)
    print(OPTION_4)
    print()
    try:
      option = int(input(SELECT_OPTION))
    except ValueError:
      print()
      print(NUMBER_ERROR)
      print()
      continue
    print()
    if option == 1:
      system("cls")
      executeOrder()
      input("Presione enter para finalizar: ")
    elif option == 2:
      system("cls")
      getOrderHistory()
      input("Presione enter para finalizar: ")
    elif option == 3:
      system("cls")
      deleteHistory()
      input("Presione enter para finalizar: ")
    elif option == 4:
      print(FAREWELL)
      sys.exit()

menu()
