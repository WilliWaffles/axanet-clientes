import os
import json

# Carpeta donde se almacenarán los archivos
DATA_FOLDER = "clientes"

# Asegurar que la carpeta exista
os.makedirs(DATA_FOLDER, exist_ok=True)

# Diccionario para mapear clientes a sus archivos
clientes = {}

# Cargar clientes existentes
def cargar_clientes():
    for archivo in os.listdir(DATA_FOLDER):
        if archivo.endswith(".json"):
            nombre = archivo.replace(".json", "")
            clientes[nombre] = os.path.join(DATA_FOLDER, archivo)

# Crear nuevo cliente
def crear_cliente(nombre, servicio):
    if nombre in clientes:
        print("El cliente ya existe.")
        return
    datos = {"nombre": nombre, "servicios": [servicio]}
    ruta = os.path.join(DATA_FOLDER, f"{nombre}.json")
    with open(ruta, "w") as f:
        json.dump(datos, f, indent=4)
    clientes[nombre] = ruta
    print(f"Cliente '{nombre}' creado con servicio: {servicio}")

# Actualizar cliente existente
def actualizar_cliente(nombre, nuevo_servicio):
    if nombre not in clientes:
        print("Cliente no encontrado.")
        return
    with open(clientes[nombre], "r+") as f:
        datos = json.load(f)
        datos["servicios"].append(nuevo_servicio)
        f.seek(0)
        json.dump(datos, f, indent=4)
        f.truncate()
    print(f"Servicio agregado a cliente '{nombre}': {nuevo_servicio}")

# Consultar cliente
def consultar_cliente(nombre):
    if nombre not in clientes:
        print("Cliente no encontrado.")
        return
    with open(clientes[nombre], "r") as f:
        datos = json.load(f)
        print(f"Información del cliente '{nombre}':\n{json.dumps(datos, indent=4)}")

# Eliminar cliente
def eliminar_cliente(nombre):
    if nombre in clientes:
        os.remove(clientes[nombre])
        del clientes[nombre]
        print(f"Cliente '{nombre}' eliminado.")
    else:
        print("Cliente no encontrado.")

# Mostrar lista de clientes
def listar_clientes():
    if not clientes:
        print("No hay clientes registrados.")
        return
    print("Clientes registrados:")
    for nombre in clientes:
        print(f"- {nombre}")

# Menú de opciones
def menu():
    cargar_clientes()
    while True:
        print("\n--- Menú ---")
        print("1. Crear cliente")
        print("2. Actualizar cliente")
        print("3. Consultar cliente")
        print("4. Eliminar cliente")
        print("5. Listar clientes")
        print("6. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del cliente: ")
            servicio = input("Servicio solicitado: ")
            crear_cliente(nombre, servicio)
        elif opcion == "2":
            nombre = input("Nombre del cliente: ")
            servicio = input("Nuevo servicio: ")
            actualizar_cliente(nombre, servicio)
        elif opcion == "3":
            nombre = input("Nombre del cliente: ")
            consultar_cliente(nombre)
        elif opcion == "4":
            nombre = input("Nombre del cliente: ")
            eliminar_cliente(nombre)
        elif opcion == "5":
            listar_clientes()
        elif opcion == "6":
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
