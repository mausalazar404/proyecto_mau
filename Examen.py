import random

num_de_contrasenas = int(input("¿cuantas contraseñas quieres generar?"))

cont = 0
while cont < num_de_contrasenas:
    contrasena = generar_contrasena()
    cont = cont + 1


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

def generar_contrasena():
#Aquí va cuando se gnera la contraseña con los demás datos que no se como poner. 
#No se como juntar las variables para que al momento de elegir la londitud acomode las variables aleatoriamente.

if caracteres < 9:
    ValueError 
    print("no valido")
else:
    print("tu contraseña final es")



