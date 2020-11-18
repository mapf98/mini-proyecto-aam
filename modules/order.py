from .visuals import header
from .constants import PIZZAS, INGREDIENTS, DELIVERY_COST
from .info import pizzaOptions, ingredientOptions, getOption
from .errors import invalidOption
from .order_extra import addDrinks
from .history import saveOrder
from .delivery import delivery
from os import system

def _getPizzaOptions():
  pizza_option = ""
  pizzaOptions()
  while True:
    pizza_option = getOption(input('Indique el tamaño: '), PIZZAS)
    if pizza_option == None:
      invalidOption()
    else:
      print(f'Tamaño seleccionado: {pizza_option[0]}')
      break
  return pizza_option

def _getPizzaIngredients():
  ingredients = []
  ingredientOptions()
  while True:
    selected_ingredient = input('Indique el ingrediente (enter para terminar): ')
    if selected_ingredient != "":
      ingredient_option = getOption(selected_ingredient, INGREDIENTS)
      if ingredient_option == None:
        invalidOption()
      else:
        ingredients.append(ingredient_option)
    else:
      break
  return ingredients

def _getPizzaType(ingredients):
  pizza_type = ""
  if (len(ingredients) == 0):
    pizza_type = "Margarita"
  else:
    pizza_type = "con "
    for ingredient in ingredients:
      pizza_type = pizza_type + ingredient[0]
      if ingredients.index(ingredient) < len(ingredients)-1:
        pizza_type = pizza_type + ", "
  return pizza_type

def _getPizzaCost(pizza_option, pizza_ingredients):
  pizza_cost = pizza_option[2]
  for ingredient in pizza_ingredients:
    pizza_cost = pizza_cost + ingredient[2]
  return pizza_cost

def _continueOrder():
  continue_order = ""
  while True:
    continue_order = input('¿Desea agregar otra pizza? [s/n]: ')
    if continue_order.capitalize() == 'N' or continue_order.capitalize() == 'S':
      break
  return continue_order.capitalize() == 'S'

def executeOrder():
  pizzas = []
  total_cost = 0

  header()
  while True:
    pizza_number = len(pizzas) + 1

    print(f'Pizza número {pizza_number}\n')
    print('Opciones:')
    pizza_option = _getPizzaOptions()
    print()
    ingredients = _getPizzaIngredients()
    print()
    print(f'Usted seleccionó una pizza {pizza_option[0]} {_getPizzaType(ingredients)}\n')
    pizza_cost = _getPizzaCost(pizza_option, ingredients)
    print(f'Subtotal a pagar por una pizza {pizza_option[0]}: {pizza_cost}')
    print('****************************')
    total_cost = total_cost + pizza_cost
    pizzas.append({
      'size': pizza_option,
      'ingredients': ingredients,
      'cost': pizza_cost
    })
    if _continueOrder():
      print()
      print('****************************')
    else:
      break
  
  total_drinks = addDrinks()
  info_delivery = delivery()
  system("cls")
  total_pizzas = total_cost
  print('RESUMEN DE ORDEN')
  print()
  print('****************************')
  print(f'- EL pedido tiene un total de {len(pizzas)} pizza(s): {total_pizzas}')
  if len(total_drinks[0]) > 0:
    print(f'- EL pedido tiene un total de {len(total_drinks[0])} bebida(s): {total_drinks[1]}')
  if info_delivery != "":
    print(f'- El pedido tiene un delivery de costo: {str(DELIVERY_COST)}')
    total_cost += DELIVERY_COST
  print()
  total_cost += total_drinks[1]
  print(f'Por un monto total de {total_cost}\n')
  print('****************************')
  print('Gracias por su compra, regrese pronto!')
  saveOrder([(total_pizzas, len(pizzas)), (total_drinks[1], len(total_drinks[0]))], total_cost, info_delivery)
  print()
