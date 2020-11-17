from .history import getHistory
from .visuals import header

def _transformOrders(orders_data):
  orders = []
  for order_data in orders_data:
    pizza = order_data[1].rsplit('-')
    drink = order_data[2].rsplit('-')
    orders.append({
      'date': order_data[0],
      'pizza': {
        'price': pizza[0],
        'quantity': pizza[1]
      },
      'drink': {
        'price': drink[0],
        'quantity': drink[1]
      },
      'price': order_data[3],
      'info': order_data[4]
    })
  return orders

def _presentOrders(orders):
  for order in orders:
    print('='*15, f'> Orden {orders.index(order)+1}')
    print('Fecha:', order['date'])
    print('Precio:', order['price'])
    if order['info']:
      print('Información:', order['info'])
    print(f"- El pedido tiene un total de {order['pizza']['quantity']} pizza(s): {order['pizza']['price']}")
    if order['drink']['quantity'] != "0":
      print(f"- El pedido tiene un total de {order['drink']['quantity']} bebida(s): {order['drink']['price']}")
    print()

def getOrderHistory():
  header()
  print()
  print(20 * '*', " ORDENES ", 20 * '*')
  print()
  file_data = getHistory()
  if file_data != None:
    _presentOrders(_transformOrders(file_data))
  else:
    print("No existen ordenes registradas")
    print()