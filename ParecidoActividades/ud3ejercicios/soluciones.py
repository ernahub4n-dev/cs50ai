!!!!!!!!ANKIIII + MNEMOTECNIAS!!!
########################TEMA 1. ESTRUCTURAS DE DATOS########################
############################1. Sets#################################
#__________________________1______________________ Creación y propiedades
s = {1, 2, 2, 3, 4, 4, 5}
print(s)
# A set doesn´t allow duplicated elements, so the output will be: {1, 2, 3, 4, 5}
#we cannot print(s[0]) because sets are unordered collections (TypeError )


#__________________________2______________________ Métodos básicos de set           ,                   AÚR-De

s = {1, 2, 3} #Given this set...     

s.add(4)    
s.update([3.5, 6])
#Both of them just work to remove the element.
s.remove(10)  # This will raise a KeyError because 10 is not in the set. BUT....
s.discard(10)  # This will NOT raise an error even though 10 is not in the set.

#__________________________3______________________ Operaciones entre conjuntos.                         UIDD
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
A | B # Unión      {1, 2, 3, 4, 5, 6}
A & B # Intersección   {3, 4}
A - B # Diferencia   {1, 2} solo elementos unicos al primer conjunto. (Solo A)
A ^ B # Diferencia simétrica {1, 2, 5, 6}

###########################2. Compresión de listas##########################
#__________________________4______________________ Lista comprimida básica

lista_num20 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

pares = [x for x in lista_num20 if x % 2 == 0]
lista_con_mayores_10 = [x for x in lista_num20 if x > 10]
#Obviosly u can also create an empty list and use a for loop with an if statement to append the even numbers.

#__________________________5______________________ Compresión con condición.
palabras = ["sol", "luna", "estrella", "cielo", "mar"]

palabras_mayores_4 = [x for x in palabras if len(x) > 4] 
set_palabras_mayores_4 = {x for x in palabras if len(x) > 4} 
#or
set_palabras_mayores_4 = set(palabras_mayores_4)

#__________________________6______________________ Compresión de sets y diccionarios.
set_cadenas = {"abc", "rst"}
print({letra.upper() for letra in set_cadenas})  # Output: {"RST", "ABC"}

diccnotas = {"Ana": 9, "Luis": 4, "Marta": 7, "Pedro": 3}
aprobados = {alumno: nota for alumno, nota in diccnotas.items() if nota >= 5} #u can also nota: alumno so it would reverse the key value
subir_1_usandocompresion = {alumno: nota + 1 for alumno, nota in diccnotas.items()}


###########################3. Carácteres de escape########################
#__________________________7______________________ Uso de escapes
print("Nombre:\tAna\nEdad:\t25\nCiudad:\tMadrid")

#__________________________8______________________ Raw strings
print(r"Hola\nBienvenidos\nPython")  # Si queremos ignorar las barras y los caracteres de escape: r

###########################4. Métodos de strings#########################
#__________________________9______________________ Métodos booleanos     ,                   SALUDAT 
texto = "Python123"

print(texto.isspace()) #True if all the characters in the string are whitespace characters (spaces, tabs, newlines)
print(texto.isalpha())  # False.     True would be if it only contained letters
print(texto.islower())  # False, because there are uppercase letters
print(texto.isupper())  # False, because there are lowercase letters 
print(texto.isdecimal()) #True if all the characters in the string are decimal characters (0-9)
print(texto.isalnum())  # True, because it contains only letters and numbers
print(texto.istitle()) #True if first letter of each word capitalized and the rest lowercase

#_________________________10______________________ Startswith y endswith
archivo = "programacion.py"
archivo.startswith("pro") #It returns True
archivo.endswith(".py") #It returns True
#_________________________11______________________ Split and join
texto = "Aprender Python es divertido" 
palabras = texto.split() # ['Aprender', 'Python', 'es', 'divertido']
nuevo = "-".join(palabras)  # "Aprender-Python-es-divertido"

########################TEMA 2. EXPRESIONES REGULARES########################
#_________________________16______________________ Regex básico          1. patron     2. resultado     3. findall solo reemplaza .search
#Busca la palabra "python" dentro de: "Estoy aprendiendo Python"
import re
patron = re.compile("python") 
resultado = patron.search("Estoy aprendiendo Python") #ponemos el texto donde buscar
print(resultado.group()) #y esa busqueda/resultado la ponemos en un grupo    #python


#_________________________17______________________ Símbolos regex
#Crear una expresión regular para:            Van dentro de re.compile(r"\d{3}"), re.search, re.match, re.findall
#. Números de **3 cifras**    cualquier digito 0-9, 3 veces
r"\d{3}" 
#. Palabras que empiecen por `"a"`
r"^a\w*"
#. Correos electrónicos simples
r"\w+@\w+\.\w+"
#. Cadenas que **terminen en `.txt`**
r"\.txt$"

########################TEMA 3. ARCHIVOS Y DIRECTORIOS########################          1. os.getcwd()   2. os.makedirs("")  3. if ruta.is_absolute()
#_________________________19______________________ Directorio de trabajo
import os 
print("Directorio actual:", os.getcwd()) 

#_________________________20______________________Crear carpetas
os.makedirs("C:\\CarpetaEjemplo\\NuevaCarpeta") 
#_________________________21______________________Rutas absolutas y relativas
from pathlib import Path
ruta = Path("datos/archivo.txt")
#esto de arriba es linux y el nombre de las funciones de abajo varian dependiendo si linux /windows

#1. Comprueba si una ruta es absoluta
if ruta.is_absolute(): #Obvio devuelve true false
    print("Es absoluta") #"C:/Users/Nahuel/file.txt"        Linux Mac "/home/user/file.txt"
else:
    print("Es relativa") #"datos/archivo.txt"


#_________________________22______________________Validez de archivos                         EFD , aqui si usamos os.path 
#1. Comprueba si un ARCHIVO o DIRECTORIO existe .       Dentro de () se pone la ruta
os.path.exists("archivo.txt")  
#2. Comprueba si un elemento es un archivo 
os.path.isfile("archivo.txt")
#3. Comprobar si un elemento es un directorio
os.path.isdir("mi_carpeta")

#4. Obtén su tamaño
os.path.getsize("archivo.txt")
#5. Lista el contenido de un directorio
contenido = os.listdir(".") #Lista archivos y carpetas en el directorio actual. Si la ruta no existe evidentenement error
contenido = os.listdir("..") #Lista archivos y carpetas en el directorio padre
print(os.listdir("../directorio/micarpeta")) #también se puede poner una ruta concreta

 
#_________________________23______________________ Lectura de archivos           read, readlines, for linea in f
#Leer un archivo.
with open("C:Users\\Nahuel\\archivo.txt") as f:  #Por defecto open abre el archivo en modo "r"
    contenido = f.read()
#Leer obteniendo lista
with open("C:Users\\Nahuel\\archivo.txt") as f:
    f.readlines()  #Cada línea del archivo es un elemento de la lista 
#Iterar línea a línea.
with open("C:Users\\Nahuel\\archivo.txt") as f:
    for linea in f:
        print(linea.strip())  # .strip() para eliminar saltos de línea y espacios en blanco


#_________________________24______________________Escritura de archivos            f.write directamente 
with open("C:Users\\Nahuel\\archivo_salida.txt", "w") as f:  
    f.write("Primera línea\n") 
    f.write("Segunda línea\n")

#_________________________25______________________JSON
#Lectura de un fichero JSON.
import json
with open("datos.json", "r") as f:
    datos = json.load(f.read()) 
#Escritura de un fichero JSON.
import json
contenido = {"nombre": "Ana", "edad": 30, "ciudad": "Madrid"}
with open("datos.json", "w") as f:
    json.dump(contenido, f)

########################TEMA 4.  MANEJO DE EXCEPCIONES.########################
#_________________________26______________________ TRY & EXCEPT basic
#_________________________27______________________Múltiples excepciones
try:
    int("a")
except (ValueError, ZeroDivisionError):
    print("Error controlado")
#_________________________28______________________Finally, very easy, try:  except ... finally
#_________________________29______________________Excepción personalizada
class AgeError(Exception):  #normal exception like ValueError for example
    pass #this means nothing, just empty block-placeholder
 #Decide WHEN TO TRIGGER IT:   RAISE!
age = int(input("Enter age: "))
if age < 0:
    raise AgeError("Age cannot be negative") #like a normal exception, it stops the program and shows a traceback

########################TEMA 5 DEBUGGING########################
#_________________________30______________________Traceback
#_________________________31______________________Assertions
x = -1
assert x > 0, "El número debe ser positivo" #If x <= 0, raises AssertionError with the message and shows a traceback
#_________________________32______________________Logging . Si eso poner aqui el ejemplo de la calculadora ejercicio.
#Ejercicio1: Generar una Calculadora en Python que realiza 
#operaciones de suma, resta, multiplicación y división, con control de 
#excepciones para manejar situaciones como la división por cero o 
#entradas no válidas


import logging

logging.basicConfig(level=logging.INFO)

class Calculadora:
    def sumar(self, a, b):
        try:
            resultado = a + b
            logging.info(f"Suma exitosa: {a} + {b} = {resultado}")
            return resultado
        except Exception as e:
            logging.error(f"Error en la suma: {e}")
            return None

    def restar(self, a, b):
        try:
            resultado = a - b
            logging.info(f"Resta exitosa: {a} - {b} = {resultado}")
            return resultado
        except Exception as e:
            logging.error(f"Error en la resta: {e}")
            return None

    def multiplicar(self, a, b):
        try:
            resultado = a * b
            logging.info(f"Multiplicación exitosa: {a} * {b} = {resultado}")
            return resultado
        except Exception as e:
            logging.error(f"Error en la multiplicación: {e}")
            return None

    def dividir(self, a, b):
        try:
            if b == 0:
                raise ValueError("No se puede dividir por cero.")
            resultado = a / b
            logging.info(f"División exitosa: {a} / {b} = {resultado}")
            return resultado
        except Exception as e:
            logging.error(f"Error en la división: {e}")
            return None



# Ejemplo de uso
calculadora = Calculadora()

# Operaciones válidas
resultado_suma = calculadora.sumar(10, 5)
resultado_resta = calculadora.restar(10, 5)
resultado_multiplicacion = calculadora.multiplicar(10, 5)
resultado_division = calculadora.dividir(10, 2)

# Operación inválida (división por cero)
resultado_division_invalida = calculadora.dividir(10, 0)

# Verificación de resultados
print("Resultado de la suma:", resultado_suma)
print("Resultado de la resta:", resultado_resta)
print("Resultado de la multiplicación:", resultado_multiplicacion)
print("Resultado de la división:", resultado_division)
print("Resultado de la división inválida:", resultado_division_invalida)








#debugging.

import logging
logging.basicConfig(level=logging.DEBUG, format=" %(asctime)......")
logging.debug("Inicio del programa")

def suma(numero1, numero2):
    loggin.debug("Inicio del programa suma(%)" %(numero1))
                
            