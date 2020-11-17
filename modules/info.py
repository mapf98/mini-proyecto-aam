from .constants import PIZZAS, INGREDIENTS, DRINKS
from .data import pizzas, ingredients, drinks 

def _getListOfElements(name):
  if name == PIZZAS:
    return pizzas
  if name == INGREDIENTS:
    return ingredients
  if name == DRINKS:
    return drinks

def pizzaOptions():
  print('Tamaños: ', end="")
  for option in pizzas:
    for clave, valor in pizzas[option].items():
      if clave == 'symbol':
        print(f'{option} ({valor})', end=" ")
  print("")

def ingredientOptions():
  print('Ingredientes: ')
  for option in ingredients:
    for clave, valor in ingredients[option].items():
      if clave == 'symbol':
        print(f'- {option} ({valor})')

def drinkOptions():
  print('Bebidas: ')
  for option in drinks:
    for clave, valor in drinks[option].items():
      if clave == 'symbol':
        print(f'- {option} ({valor})')

def getOption(symbol, listOfElements):
  elements = _getListOfElements(listOfElements)
  for option in elements:
    for clave, valor in elements[option].items():
      if clave == 'symbol' and valor == symbol:
        return (option, elements[option]['symbol'], elements[option]['price'])
        
