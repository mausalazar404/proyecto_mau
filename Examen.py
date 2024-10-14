import random 
"""Se importó la libreria de python llamada "random". Esta 
proporciona funciones para generar números pseudoaleatorios y realizar 
acciones aleatorias"""


caracteres = int(input("número de caracteres para la contraseña (9 o más): "))
"""Se asigna el valor a los caracteres"""


def crear_numero():
    return str(random.randint(0,9))
"Esta función sirve para devolver numeros aleatorios del 0 al 9"

def crear_min():
    letras = "abcdefghijklmnopqrstuvwxyz"
    a = random.randint(0, (len(letras)-1))
    return letras[a]
"Esta función genera letras aleatorias en minúscula"

def crear_may():
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    a = random.randint(0, (len(letras)-1))
    return letras[a]
"Esta funcion crea genera las letras en mayúscula"

def crear_simb():
    simbolos = "!#$%&/()=?¡;,.:-_"
    a = random.randint(0, (len(simbolos)-1))
    return simbolos[a]
"Esta función genera los simbolos aleatoriamente"

funciones = [crear_numero,crear_min,crear_may,crear_simb]
"""Se crea una variable que llama a las funciones anteriores"""

def generar_contrasena(longitud_c, funciones):
    contrasena = ""
    for caracteres in range(longitud_c):
        rand_index = random.randint(0, len(funciones)-1)
        llamar_funcion = funciones[rand_index]()
        caracteres = llamar_funcion
        contrasena = contrasena + caracteres
    return contrasena


if caracteres < 9:
    while caracteres < 9:
        caracteres = int(input("TE DIJE QUE número de caracteres para la contraseña (9 o más): "))

contrasena_final = generar_contrasena(caracteres, funciones)

print("tu contraseña final es:", contrasena_final)

def guardar_contrasena(contrasena_final):
    guardar = str(input("¿Desea guardar su contraseña? (Y/N): "))
    while True:
        if guardar == "Y":
            espacio_de_guardado = []
            lista_cont = []
            nombre = str(input("¿Cómo desea llamar su espacio de guardado?: "))
            espacio_de_guardado.append(nombre)
            lista_cont.append(contrasena_final)
            espacio_de_guardado.append(lista_cont)
            
            otra = str(input("¿desea generar otra? (Y/N): "))
            if otra == "Y":
                nueva = generar_contrasena(caracteres, funciones)  
                lista_cont.append(nueva)
            print("Este es tu espacio con tus contraseñas: ", espacio_de_guardado)
            return espacio_de_guardado 
        else:
            print("Contraseña final: ", contrasena_final)
            break
"""Se crea una función para guardar la contraseña. Pregunta si quieres guardar
la contraseña, si le pones que sí, se crea una lista para la cual te pide un
nombre. La función agrega la contraseña a una lista y esa lista a la lista
de guardado. Finalmente te pide si quieres crear una contraseña nueva para 
guardarla en el espacio de guardado. Si le pones que no"""

guardar_contrasena(contrasena_final)
"""Se manda a llamar a la función"""

print("Gracias :)")
"""Se imprime un "Gracias" """
        





