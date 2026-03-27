def saludar(nombre):
    return f"Hola, {nombre}. Proyecto con GitHub funcionando."

if __name__ == "__main__":
    nombre = input("Ingresa tu nombre: ")
    print(saludar(nombre))