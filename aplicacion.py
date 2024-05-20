# -*- coding: utf-8 -*-
def validar_credenciales(login, clave):
    with open("usuario.txt", "r") as file_login, open("claves.txt", "r") as file_clave:
        logins = file_login.read().splitlines()
        claves = file_clave.read().splitlines()
        if login in logins and clave in claves:
            return True
        else:
            return False

def listar_personas():
    try:
        with open("codigo.txt", "r") as file_codigo, open("nombre.txt", "r") as file_nombre, open("precio.txt", "r") as file_precio:
            codigos = file_codigo.read().splitlines()
            nombres = file_nombre.read().splitlines()
            precios = file_precio.read().splitlines()
            if len(codigos) == len(nombres) == len(precios):
                print("Datos de las personas:")
                print("{:<10} {:<20} {:<10}".format("CODIGO", "NOMBRE", "PRECIO"))
                for codigo, nombre, precio in zip(codigos, nombres, precios):
                    print("{:<10} {:<20} {:<10}".format(codigo, nombre, precio))
            else:
                print("Error: Los archivos de datos no tienen la misma cantidad de registros.")
    except FileNotFoundError:
        print("Error: No se encontraron los archivos necesarios.")


def agregar_persona(codigos, nombre, precio):
    try:
        # Si el nombre no está presente, agregar la nueva persona
        with open("codigo.txt", "a") as file_codigo, open("nombre.txt", "a") as file_nombre, open("precio.txt", "a") as file_precio:
            file_codigo.write(codigos +"\n")
            file_nombre.write(nombre +"\n")
            file_precio.write(precio +"\n")
        print("Producto agregado exitosamente.")
    except IOError:
        print("Error al escribir en los archivos.")


intentos = 0
while intentos < 2:
    login = input("Ingrese su login: ")
    clave = input("Ingrese su clave: ")
    if validar_credenciales(login, clave):
        print("Bienvenido al programa.")
        while True:
            try:
                print("Menú:")
                print("1. Listar productos")
                print("2. Agregar productos")
                print("3. Salir")
                opcion = input("Seleccione una opción: ")
                if opcion == "1":
                    listar_personas()
                elif opcion == "2":
                    codigos = input("Ingrese el codigo: ")
                    nombre = input("Ingrese el nombre: ")
                    precio = input("Ingrese el precio: ")
                    agregar_persona(codigos, nombre, precio)
                elif opcion == "3":
                    print("Saliendo del programa.")
                    break
                else:
                    print("Opción inválida. Intente nuevamente.")
            except KeyboardInterrupt:
                print("\nSe ha interrumpido la ejecución.")
                break
            except Exception as e:
                print("Error:", e)

        # Reiniciar posición de lectura de los archivos de usuarios y claves
        intentos = 0
    else:
        print("Login o clave incorrectos. Intente nuevamente.")
        intentos += 1
else:
    print("Ha excedido el número de intentos permitidos. El programa terminará.")