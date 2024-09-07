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

#No se como juntar las variables para que al momento de elegir la londitud acomode las variables aleatoriamente.


if caracteres < 8:
    print("no valido")
else:
    print("tu contraseña final es")

