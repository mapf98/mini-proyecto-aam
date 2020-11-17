import sys
from modules.constants import BASIC_RESPONSE, WELCOME, OPTION_1, OPTION_2, OPTION_3, OPTION_4, FAREWELL, PIZZAS, INGREDIENTS, DRINKS, SELECT_OPTION, NUMBER_ERROR
from modules.visuals import header
from modules.order import executeOrder

def menu():
  print()
  print(WELCOME)
  print()
  print(OPTION_1)
  print(OPTION_2)
  print(OPTION_3)
  print(OPTION_4)
  print()
  while True:
    try:
      option = int(input(SELECT_OPTION))
    except ValueError:
      print()
      print(NUMBER_ERROR)
      print()
      continue
    print()
    if option == 1:
      executeOrder()
      break
    elif option == 2:
      # LLAMAR A CONSULTA DE COMPRAS
      print("LLAMAR A CONSULTA DE COMPRAS")
      break
    elif option == 3:
      # LLAMAR A LIMPIEZA DE REGISTRO
      print("LLAMAR A LIMPIEZA DE REGISTRO")
      break
    elif option == 4:
      print(FAREWELL)
      sys.exit()

header()
menu()
