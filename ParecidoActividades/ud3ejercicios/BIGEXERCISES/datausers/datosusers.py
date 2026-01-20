# Tienes datos_usuarios.txt, con datos desordenados
#   Ana, 25, Madrid
# LUIS,30,barcelona
# Marta , 17 , Valencia
# Pedro,abc,Sevilla

#OBJETIVO:
#LEER , LIMPIAR, VALIDAR Y OBTENER INFORMACIÓN ÚTIL.


import logging


logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


usuarios_validos = set()
usuarios_descartados = 0


try:
    with open("datos_usuarios.txt") as f:
        for linea in f:
            try:
                linea = linea.strip()   #Ana, 25, Madrid 
                nombre, edad, ciudad = [x.strip() for x in linea.split(",")] #Logically once the loop ends, we get 3 elements. SO
                                                                            # We can unpack the looped list into 3 variables directly
                if not nombre.isalpha(): #if not only letters
                    raise ValueError("Nombre inválido")
                if not edad.isdecimal(): #if not only decimals
                    raise ValueError("Edad inválida")

                usuarios_validos.add(nombre.title()) #pone la primera mayus y las demas minus
                logging.info(f"Usuario válido: {nombre}")

            except ValueError as e: #The errors above are reasons to stop the program. See them as apart.
                                    #If a line doesn´t have exactly 3 elements, we log the problem.
                usuarios_descartados += 1
                logging.warning(f"Línea descartada: {linea} → {e}") #as e -> the message of the exception raised
except FileNotFoundError: #If the file does not exist
    logging.error("El archivo datos_usuarios.txt no existe")


print(f"Usuarios válidos: {usuarios_validos}")
print(f"Usuarios descartados: {usuarios_descartados}")

