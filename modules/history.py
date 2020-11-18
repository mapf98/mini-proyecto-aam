import os
from datetime import datetime
from .constants import SEPARATOR, DELIVERY_COST, PATH, DATA_FOLDER

# Abrir archivo de órdenes
def _openFile(value):
  return open(PATH, value)

# Crear carpeta data en caso de que no exista
def _createDataFolder():
  try:
    os.stat(DATA_FOLDER)
  except:
    os.mkdir(DATA_FOLDER)

# Salvar ordenes con el formato establecido
def saveOrder(prices, total, info):
  _createDataFolder()
  file = _openFile("a")
  file.write(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
  file.write(SEPARATOR)
  for price in prices:
    file.write(f'{str(price[0])}-{str(price[1])}')
    file.write(SEPARATOR)
  file.write(str(total))
  file.write(SEPARATOR)
  file.write(str(info))
  file.write(SEPARATOR)
  file.write(str(DELIVERY_COST))
  file.write("\n")
  file.close()

# Eliminar las ordenes registradas
def deleteHistory():
  while True:
    response = input("¿Desea borrar el registro de todas las compras de manera permanente? [s/n]")
    if response.capitalize() == 'N' or response.capitalize() == 'S':
      break
  
  if response.capitalize() == 'S':
    if os.path.isfile(PATH):
      os.remove(PATH)
      print()
      print("Datos borrados satisfactoriamente!")
      print()
    else:
      print()
      print("No hay datos actualmente registrados!")
      print()

# Obtener historico de ordenes
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
