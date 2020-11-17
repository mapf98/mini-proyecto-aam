import os
from datetime import datetime
from .constants import SEPARATOR

PATH = "data/orders.txt"

def _openFile(value):
  return open(PATH, value)

def saveOrder(prices, total, info):
  file = _openFile("a")
  file.write(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
  file.write(SEPARATOR)
  for price in prices:
    file.write(f'{str(price[0])}-{str(price[1])}')
    file.write(SEPARATOR)
  file.write(str(total))
  file.write(SEPARATOR)
  file.write(str(info))
  file.write("\n")
  file.close()

def deleteHistory():
  while True:
    response = input("¿Desea borrar el registro de todos los archivos de manera permanente? [s/n]")
    if response.capitalize() == 'N' or response.capitalize() == 'S':
      break
  
  if response.capitalize() == 'S':
    os.remove("data/orders.txt")
    print()
    print("Datos borrados satisfactoriamente! (enter para continuar)", end="")
    input()

def getHistory():
  try:
    file = _openFile("r")
    file_orders = file.read().rsplit('\n')
    if file_orders == None:
      return None
    orders = []
    for order in file_orders:
      if order != "":
        orders.append(order.rsplit(SEPARATOR))
    file.close()
    return orders
  except:
    return None
