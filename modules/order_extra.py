from .info import drinkOptions, getOption
from .constants import DRINKS

# Obtener cantidad de bebidas seleccionadas con su precio
def _totalDrinks(drinks):
  total = 0
  listOfDrinks = []
  if len(drinks) > 0:
    for drink in drinks:
      total += drink[2]
      listOfDrinks.append(drink[0])
    return (listOfDrinks, total)
  else:
    return (listOfDrinks, total)

# Añadir bebidas a una orden
def addDrinks():
  drinks = []
  hasDrinks = True

  # Preguntar al usuario si desea bebidas
  while True:
    response = input('¿Desea incluir bebidas a su pedido? [s/n]: ')
    if response.capitalize() == 'N' or response.capitalize() == 'S':
      break

  # Si el usuario desea bebidas, registrar todas las bebidas deseadas
  if response.capitalize() == 'S':
    while hasDrinks:
      print()
      isDone = True
      drinkOptions()
      option = getOption(input("Indique la bebida a deseada: "), DRINKS)
      if option != None:
        drinks.append(option)
        print(f'Subtotal a pagar por una bebida {option[0]}: {option[2]}')
        print()
        while isDone:
          response = input("¿Quiere incluir otra bebida? [s/n]: ")
          if response.capitalize() == 'N' or response.capitalize() == 'S':
            if not (response.capitalize() == 'S'):
              hasDrinks = False
            isDone = False
      else:
        invalidOption()
  return _totalDrinks(drinks)