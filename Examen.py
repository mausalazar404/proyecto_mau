import random


caracteres = int(input("número de caracteres para la contraseña (9 o más)"))



def crear_numero():
    return str(random.randint(0,9))

def crear_min():
    letras = "abcdefghijklmnopqrstuvwxyz"
    a = random.randint(0, (len(letras)-1))
    return letras[a]

def crear_may():
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    a = random.randint(0, (len(letras)-1))
    return letras[a]

def crear_simb():
    simbolos = "!#$%&/()=?¡;,.:-_"
    a = random.randint(0, (len(simbolos)-1))
    return simbolos[a]

funciones = [crear_numero,crear_min,crear_may,crear_simb]

def generar_contrasena(longitud_c, funciones):
    contrasena = ""
    for caracteres in range(longitud_c):
        rand_index = random.randint(0, len(funciones)-1)
        llamar_funcion = funciones[rand_index]()
        caracteres = llamar_funcion
        contrasena = contrasena + caracteres
    return contrasena

contrasena_final = generar_contrasena(caracteres, funciones)

if caracteres < 9:
    while caracteres < 9:
        caracteres = int(input("número de caracteres para la contraseña (9 o más)"))

else:
    print("tu contraseña final es", contrasena_final)

#Esta ultima parte no me sirve al 100%, ya que si eligo una contraseña mayor a lo que pide si me sirve, pero si eligo una menor, si sirve el while ya que continua preguntando por un número mayor pero ya cuando lo pones despues de unos intentos, ya no sirve el codigo completo.

