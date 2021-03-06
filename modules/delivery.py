from .constants import DELIVERY_COST, NUMBER_ERROR

# Función para agregar el delivery a una orden y registrar los datos necesarios para realizar el mismo
def delivery():
  info = ""
  # Preguntar al usuario si desea delivery
  while True:
    response = input('¿Desea qué le enviemos su pedido? Esto tiene un costo adicional de ' + str(DELIVERY_COST) + ' [s/n]: ')
    print()
    if response.capitalize() == 'N' or response.capitalize() == 'S':
      break

  # Si el usuario desea delivery registrar sus datos
  if response.capitalize() == 'S':
    monto = DELIVERY_COST
    name = input("Ingresa el nombre del remitente: ")
    lastname = input("Ingresa el apellido del remitente: ")
    address = input("Ingresa la dirección de entrega: ")
    while True:
      try:
        phone = int(input("Ingresa un número de celular (solo números): "))
      except ValueError:
        print()
        print(NUMBER_ERROR)
        print()
        continue
      break

    info = "Nombre y apellido de remitente: " + name + ' ' + lastname + '. ' + "Dirección: " + address + '. ' + 'Celular: ' + str(phone)

  return info
