import sys
from modules.constants import WELCOME, OPTION_1, OPTION_2, OPTION_3, OPTION_4, FAREWELL, PIZZAS

def header():
  print(20*'*')
  print("* PIZZERIA UCAB *")
  print(20*'*')

def menu():
  print()
  print(WELCOME)
  print()
  print(OPTION_1)
  print(OPTION_2)
  print(OPTION_3)
  print(OPTION_4)
  print()
  option = int(input("Seleccione una opción: "))
  print()
  if option == 1:
    # LLAMAR A FUNCION DE PIZZERIA
    pass
  elif option == 2:
    # LLAMAR A CONSULTA DE COMPRAS
    pass
  elif option == 3:
    # LLAMAR A LIMPIEZA DE REGISTRO
    pass
  elif option == 4:
    print(FAREWELL)
    sys.exit()
    
  print(option)

header()
menu()