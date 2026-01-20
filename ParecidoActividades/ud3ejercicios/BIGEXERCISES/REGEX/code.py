#Estás desarrollando un pequeño buscador de patrones en textos.
#Dispones de un archivo texto.txt con contenido libre (frases, números, emails, etc.).
# Extraer información concreta del texto usando expresiones regulares.

import re

#No uso search() + group() porque el objetivo del ejercicio es encontrar todas las coincidencias
#findall devuelve una lista con todas las coincidencias encontradas.
#Los apuntes dice: Especificar la cadena que quieres buscar en el objeto Regex con el método search()
#Lo que devolvería un objeto tipo match. Finalmente .group() para obtener la cadena encontrada.
try:
    with open("texto.txt") as f:
        texto = f.read()

    patron_numeros = re.compile(r"\d+")
    patron_mayus = re.compile(r"\b[A-Z][a-zA-Z]*")
    patron_email = re.compile(r"\b\w+@\w+\.\w+\b")

    numeros = patron_numeros.findall(texto)
    palabras_mayus = patron_mayus.findall(texto)
    emails = set(patron_email.findall(texto))

    print(f"Números encontrados: {numeros}")
    print(f"Palabras con mayúscula: {palabras_mayus}")
    print(f"Emails encontrados: {emails}")

except FileNotFoundError:
    print("El archivo texto.txt no existe")