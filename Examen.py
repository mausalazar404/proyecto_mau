import random

#caracteres = int(input("numero de caracteres para tu contraseña"))

"""def crear_numero(num1,num2,num3,num4,num5,num6,num7,num8,num9,num10):

    random_num = random(num1,num2,num3,num4,num5,num6,num7,num8,num9,num10)
    return random_num

llamada = crear_numero(1,2,3,4,5,6,7,8,9,0)
print(llamada)"""


num = '1234567890'
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYz'
esp = '!@#$%&/()='

longitud = int(input("Elige la longitud de tu contraseña (maximo 10 caracteres)"))

if longitud > 10:
    return 0
else:
    return 1


def contraseña(num,lower,upper,esp):
    res = num + lower + upper + esp
    return res



