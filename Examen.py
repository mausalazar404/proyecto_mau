"""Se importó la librería de python llamada "random". Esta 
proporciona funciones para generar números pseudoaleatorios y realizar 
acciones aleatorias. Esta información fue obtenida de 
random — Generate pseudo-random numbers. (n.d.). Python Documentation. 
https://docs.python.org/es/3/library/random.html"""
import random 


"""Se pidee el número de caracteres y sí no es un número, te pide que 
lo sea"""
caracteres = input("Número de caracteres para la contraseña (9 o más): ")
while not caracteres.isdigit():
    print("Por favor, ingrese un número válido.")
    caracteres = input("Número de caracteres para la contraseña (9 o más): ")

"""Se convierte la entrada a entero después de la validación"""
caracteres = int(caracteres)

"""Este while es para verificar que la contraseña sea mayor de 9
caracteres"""
while caracteres < 9:
    print("El número de caracteres debe ser 9 o más.")
    caracteres = input("Número de caracteres para la contraseña (9 o más): ")
    
    while not caracteres.isdigit():
        print("Por favor, ingrese un número válido.")
        caracteres = input("Número de caracteres para la contraseña (9 o más): ")
    
    caracteres = int(caracteres)  

def crear_numero():
    "Esta función sirve para devolver numeros aleatorios del 0 al 9"
    return str(random.randint(0,9))


def crear_min():
    "Esta función devuelve letras aleatorias en minúscula"
    letras = "abcdefghijklmnopqrstuvwxyz"
    a = random.randint(0, (len(letras)-1))
    return letras[a]


def crear_may():
    "Esta funcion devuelve las letras en mayúscula"
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    a = random.randint(0, (len(letras)-1))
    return letras[a]


def crear_simb():
    "Esta función devuelve los simbolos aleatoriamente"
    simbolos = "!#$%&/()=?¡;,.:-_"
    a = random.randint(0, (len(simbolos)-1))
    return simbolos[a]


funciones = [crear_numero,crear_min,crear_may,crear_simb]
"""Se crea una variable que llama a las funciones anteriores"""

def generar_contrasena(longitud_c, funciones):
    """Esta función recibe la longitúd y las funciones anteriores
    para generar la contraseña final. Devuelve la contraseña final"""
    contrasena = ""
    for caracteres in range(longitud_c):
        rand_index = random.randint(0, len(funciones)-1)
        llamar_funcion = funciones[rand_index]()
        caracteres = llamar_funcion
        contrasena = contrasena + caracteres
    return contrasena


contrasena_final = generar_contrasena(caracteres, funciones)

"""Se imprime una vista previa de tu contraseña final"""
print("tu contraseña final es:", contrasena_final)


def guardar_contrasena(contrasena_final):
    
    """Esta función se crea para guardar la contraseña. La función recibe
    la contraseña final y pregunta si quieres guardar la contraseña para 
    ponerle un nombre al apartado de guardado. Finalmente devuelve el 
    apartado con tu contraseña"""

    guardar = str(input("¿Desea guardar su contraseña? (Y/N): "))
    while True:
        if guardar == "Y" or guardar == "y":
            espacio_de_guardado = []
            lista_cont = []
            nombre = str(input("¿Cómo desea llamar su espacio de guardado?: "))
            espacio_de_guardado.append(nombre)
            lista_cont.append(contrasena_final)
            espacio_de_guardado.append(lista_cont)
            
            otra = str(input("¿desea generar otra? (Y/N): "))
            if otra == "Y" or guardar == "y":
                nueva = generar_contrasena(caracteres, funciones)  
                lista_cont.append(nueva)
            print("Este es tu espacio con tus contraseñas: ", espacio_de_guardado)
            return espacio_de_guardado 
        else:
            print("Contraseña final: ", contrasena_final)
            break


guardar_contrasena(contrasena_final)
"""Se manda a llamar a la función"""

print("Gracias :)")
"""Se imprime un "Gracias" """
        
