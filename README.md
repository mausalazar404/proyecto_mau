# proyecto_mau
mi proyecto de progra en python

"""Este proyecto se encarga de la creación de una contraseña aleatoria totalmente segura que utiliza números, letras mayúsculas y minúsculas y caracteres especiales. Yo creo que es interesante ya que podrás elegir la longitud de tu contraseña lo cual hace que sea una contraseña totalmente segura. El algoritmo que describe mi proyecto es el siguiente:

 Eo letras_mayusculas = (A-Z)
 letras_minusculas = (a-z)
 numeros = (0-9)
caracteres_esp = ($%!&?¡*)

caracteres = letras_mayusculas ´+ letras_minusculas + numero + caracteres_esp

elección de longitud (no se como hacerlo)

contraseña = selección de carácter aleatorio de caracteres hasta llegar a la longitud deseada.

Ef = contraseña"""

#A partir de aqui:

num = '1234567890'
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYz'
esp = '!@#$%&/()='

longitud = int(input("Elige la longitud de tu contraseña (maximo 10 caracteres)"))

if longitud > 10:
    return 0
else:
    return 1

#No se como hacer para que se quede con la longitud que se decida y tampoco para que se hagan random los caracteres

def contraseña(num,lower,upper,esp):
    res = num + lower + upper + esp
    return res
