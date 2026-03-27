def saludar(nombre):
    return f"Hola, {nombre}. Bienvenido al proyecto con GitHub."

def despedida(nombre):
    return f"Adiós, {nombre}. Gracias por usar el programa."

def validar_nombre(nombre):
    if nombre.strip() == "":
        return False
    return True

if __name__ == "__main__":
    nombre = input("Ingresa tu nombre: ")

    if validar_nombre(nombre):
        print(saludar(nombre))
        print(despedida(nombre))
    else:
        print("Error: Debes ingresar un nombre válido.")