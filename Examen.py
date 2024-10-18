"""
Proyecto python
Generador de contraseñas aleatorias
El programa realiza una serie de contraseñas aleatorias dependiendo
de el número de caracteres que el usuario eliga.
"""

#bibliotecas
import random 



"""
(Uso de ciclos)
Se pide el número de caracteres y si no es un número, te pide que lo sea
"""
caracteres = input("Número de caracteres para la contraseña (9 o más): ")
while not caracteres.isdigit():
    print("Por favor, ingrese un número válido.")
    caracteres = input("Número de caracteres para la contraseña (9 o más): ")

caracteres = int(caracteres)


"""
(ciclos)
Este while es para verificar que la contraseña sea mayor de 9
caracteres
"""
while caracteres < 9:
    print("El número de caracteres debe ser 9 o más.")
    caracteres = input("Número de caracteres para la contraseña (9 o más): ")
    
    while not caracteres.isdigit():
        print("Por favor, ingrese un número válido.")
        caracteres = input("Número de caracteres para la contraseña (9 o más): \
                           ")
    
    caracteres = int(caracteres)  


def crear_numero():
    """
    Devuelve número aleatorio
    """
    return str(random.randint(0,9))


def crear_min():
    """
    Devuelve letras aleatorias en minúscula
    """
    letras = "abcdefghijklmnopqrstuvwxyz"
    a = random.randint(0, (len(letras)-1))
    return letras[a]


def crear_may():
    """
    Devuelve las letras en mayúscula
    """
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    a = random.randint(0, (len(letras)-1))
    return letras[a]


def crear_simb():
    """
    Devuelve los simbolos aleatoriamente
    """
    simbolos = "!#$%&/()=?¡;,.:-_"
    a = random.randint(0, (len(simbolos)-1))
    return simbolos[a]


funciones = [crear_numero,crear_min,crear_may,crear_simb]



"""
======================= Parte principal del programa =====================
"""


def generar_contrasena(longitud_c, funciones):
    """
    (operadores, funciones, ciclos)
    Recibe la longitúd y las funciones anteriores
    Genera contraseña final 
    Devuelve la contraseña final
    """
    contrasena = ""
    for caracteres in range(longitud_c):
        rand_index = random.randint(0, len(funciones)-1)
        llamar_funcion = funciones[rand_index]()
        caracteres = llamar_funcion
        contrasena = contrasena + caracteres
    return contrasena

contrasena_final = generar_contrasena(caracteres, funciones)


"""
Se imprime una vista previa de tu contraseña final
"""
print("tu contraseña final es:", contrasena_final)


"""
========================= función auxiliar ==============================
"""


def guardar_contrasena():
    """
    (funcionees, listas, listas anidadas, ciclos, condicionales)
    Recibe la contraseña final 
    Mete la contraseña a un espacio de guardado
    Devuelve el apartado con tu contraseña
    """
    guardar = str(input("¿Desea ponerle un título a su contraseña? (Y/N): "))
    
    continuar = True  
    while continuar:
        if guardar == "Y" or guardar == "y":
            espacio_de_guardado = []
            lista_cont = []
            nombre = str(input("¿Cómo desea llamar su espacio de contraseña?: "\
                               ))
            espacio_de_guardado.append(nombre)
            lista_cont.append(contrasena_final)
            espacio_de_guardado.append(lista_cont)
            
            otra = str(input("¿Desea generar otra? (Y/N): "))
            if otra == "Y" or otra == "y":
                nueva = generar_contrasena(caracteres, funciones)  
                lista_cont.append(nueva)
            print("Este es tu espacio con tus contraseñas: ", \
                  espacio_de_guardado)
            return espacio_de_guardado
        else:
            print("Contraseña final: ", contrasena_final)
            continuar = False  


guardar_contrasena()
"""
Se manda a llamar a la función
"""

print("Gracias :)")
"""
Se imprime un "Gracias" 
"""
        
