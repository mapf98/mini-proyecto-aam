import os
from datetime import datetime
from .constants import SEPARATOR

def _openFile():
  return open("data/orders.txt", "a")

def saveOrder(prices, total, info):
  file = _openFile()
  file.write(str(datetime.now()))
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


