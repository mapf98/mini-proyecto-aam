from .constants import PIZZAS, INGREDIENTS, DRINKS
from .data import pizzas, ingredients, drinks 

# Obtener lista de elementos con sus precios
def _getListOfElements(name):
  if name == PIZZAS:
    return pizzas
  if name == INGREDIENTS:
    return ingredients
  if name == DRINKS:
    return drinks

# Obtener tamaños de pizzas
def pizzaOptions():
  print('Tamaños: ', end="")
  for option in pizzas:
    for clave, valor in pizzas[option].items():
      if clave == 'symbol':
        print(f'{option} ({valor})', end=" ")
  print("")

# Obtener posibles ingredientes extra en una pizza
def ingredientOptions():
  print('Ingredientes: ')
  for option in ingredients:
    for clave, valor in ingredients[option].items():
      if clave == 'symbol':
        print(f'- {option} ({valor})')

# Obtener posibles bebidas
def drinkOptions():
  print('Bebidas: ')
  for option in drinks:
    for clave, valor in drinks[option].items():
      if clave == 'symbol':
        print(f'- {option} ({valor})')

# Validar y obtener opción seleccionada por un usuario
def getOption(symbol, listOfElements):
  elements = _getListOfElements(listOfElements)
  for option in elements:
    for clave, valor in elements[option].items():
      if clave == 'symbol' and valor == symbol:
        return (option, elements[option]['symbol'], elements[option]['price'])
        
