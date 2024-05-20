# -*- coding: utf-8 -*-
"""
Created on Mon May 20 15:41:34 2024

@author: juger
"""

def validar_credenciales(usuario, clave):
    with open("usuario.txt", "r") as file_usuario, open("claves.txt", "r") as file_claves:
        logins = file_usuario.read().splitlines()
        claves = file_claves.read().splitlines()
        # Verificar si el usuario y la clave coinciden
        if usuario in logins and clave == claves[logins.index(usuario)]:
            return True
        else:
            return False

intentos = 0
while intentos < 2:
    usuario = input("Ingrese su login: ")
    clave = input("Ingrese su clave: ")
    if validar_credenciales(usuario, clave):
        print("DATOS PRODUCTO")
        print("Menú:")
        print("1. Listar")
        print("2. Agregar")
        print("3. Salir")
        break
    else:
        print("Usuario o contraseña incorrectos")
        intentos += 1
else:
    print("Ha excedido el número de intentos permitidos. El programa finalizara.")