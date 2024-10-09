import random


caracteres = int(input("número de caracteres para la contraseña (9 o más): "))



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

guardar_contrasena(contrasena_final)

print("Gracias :)")

        





