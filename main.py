import sys
from modules.constants import WELCOME, OPTION_1, OPTION_2, OPTION_3, OPTION_4, FAREWELL, PIZZAS
from modules.info import ingredientOptions
from modules.visuals import header

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
      option = int(input("Seleccione una opción: "))
    except ValueError:
      print()
      print('Debes ingresar un número')
      print()
      continue
    print()
    if option == 1:
      # LLAMAR A FUNCION DE PIZZERIA
      print("LLAMAR A FUNCION DE PIZZERIA")
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
