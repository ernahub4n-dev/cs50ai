
#EJERCICIOS DE CADENAS.
#Ejercicio 6
frase = input("Introduzca una frase:")
vocal = input("Introduzca una vocal")
frase_modificada = frase.replace(vocal, vocal.upper()) # Aqui estamos reemplazando la vocal que haya escrito con la vocal en mayúculas, dentro de la frase
print(f"Aquí esta su combinación: {frase_modificada}")
 
#Ejercicio 7
correo = input("Introduce tu correo electrónico: ")
nombre = correo.split("@")[0]  
    #Esto es lo mismo que hacer esto
    #partes = correo.split("@")
    #nombre = partes[0]
nuevo_correo = nombre + "@uax.es"
print("Tu nuevo correo es:", nuevo_correo)


#EJERCICIOS DE CONDICIONALES.
#Ejercicio 6
name = input("¿Cómo te llamas? ")
gender = input("¿Cuál es tu sexo (M o H)? ").upper()
first_letter = name[0].lower()
if (gender == "M" and first_letter < 'm') or (gender == "H" and first_letter > 'n'):
    group = "A"
else:
    group = "B"

print("Tu grupo es " + group)

#  while sexo != "MUJER" or sexo != "HOMBRE":
#MAL!!, ES:
# while sexo != "MUJER" and sexo != "HOMBRE":


#Ejercicio 10
# 1️⃣ Elegir tipo de menú
decision = None

while decision not in (1, 2):
    try:
        decision = int(input("Elige una opción (1- Vegetariana | 2- No vegetariana): "))
        if decision not in (1, 2):
            print("Debes elegir 1 o 2.\n")
    except ValueError:
        print("Introduce solo números.\n")


# 2️⃣ Configurar menú e ingredientes
if decision == 1:
    menu = "vegetariano"
    ingredientes = {
        "1": "Pimiento",
        "2": "Tofu"
    }
else:
    menu = "no vegetariano"
    ingredientes = {
        "1": "Peperoni",
        "2": "Jamón",
        "3": "Salmón"
    }


# 3️⃣ Elegir ingrediente (bucle limpio)
opcion = None

while opcion not in ingredientes:
    print(f"\nIngredientes disponibles:")
    for k, v in ingredientes.items():
        print(f"{k}- {v}")

    opcion = input("Elige un ingrediente: ") #the user must type only the number ("1", "2", "3").

    if opcion not in ingredientes:  
        print("Opción inválida, vuelve a intentarlo.\n")


decision_ingrediente = ingredientes[opcion]


# 4️⃣ Resumen final
print("\n--- RESUMEN DE TU PEDIDO ---")
print(f"Pizza {menu}")
print(f"Ingredientes: Mozzarella, Tomate y {decision_ingrediente}")







#EJERCICIOS DE BUCLES.   #range(1,5) empieza desde el 1 y acaba en 4)

#Ejercicio 4

#Otra version, si te fijas al final del 0 imprimiria una ,   esto lo corrige.
numero = int(input("Introduce un entero positivo: "))

while numero < 0:
    numero = int(input("INCORRECTO, introduce un entero positivo: "))

for x in range(numero, -1, -1): #fin es -1 , es decir 0.
    if x == 0:
        print(x)
    else:
        print(x, end=", ")

#Ejercicio 5
amount = float(input("¿Cantidad a invertir? "))
interest = float(input("¿Interés porcentual anual? "))   #user types 10%
years = int(input("¿Años?"))
for i in range(years):
    amount *= 1 + interest / 100 
    print("Capital tras " + str(i+1) + " años: " + str(round(amount, 2)))


#Ejercicio 7
for i in range(1,11):
    print(f"Tabla del {i}:")
    for j in range(1,11):
        print(f"{i} x {j} = {i * j}")
    print("")    

#Ejercicio 9
key = "contraseña"
password = ""
while password != key:
    password = input("Introduce la contraseña: ")
print("Contraseña correcta")

#Ejercicio 10

numero = int(input("Introduce un número entero: "))
if numero <= 1:
    print("No es un número primo")
      #Sabemos que de 1 para abajo no nay numeros primos
else:
    es_primo = True
    for i in range(2, numero):  #va del rango del 2 al numero, sin contar numero.
        if numero % i == 0:     #Primo es si es divisible entre 1 y el mismo. Es decir que si un número de entre. YA ENTIENDO, A LA MINIMA QUE ENCUENTRE 
            #un numero que % == 0, break, x ej si es 8 a la minima en el 2 ya romperia el bucle
            es_primo = False     #el rango es divisible se invalidaria(divisible entre otro numero)
            break
    if es_primo:
        print("Es un número primo")
    else:
        print("No es un número primo")


#Ejercicio 12
frase = input("Introduce una frase: ")
letra = input("Introduce una letra: ")
veces_aparece = frase.lower().count(letra.lower())

print(f"La letra '{letra}' aparece {veces_aparece} veces en la frase.")


#EJERCICIOS DE LISTAS Y TUPLAS.

#Ejercicio 4
numeros = []
           # Preguntar al usuario 6 números ganadores . Y ordenarlos de menos a mayor.
for i in range(6):
    numero = int(input(f"Introduce el número ganador {i+1}: "))
    numeros.append(numero)

print("Números ganadores ordenados:", numeros.sort())


#Ejercicio 5
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(1, 11):
    print(numbers[-i], end=", ")

#Ejercicio 6
#Acuerdate que no podemos remover objetos de una lista que estamos recorriendo mientras. si hicieses eso, tendrías que poner []
# O no modificar la lista original mientras la recorres.
#Ejercicio 9
palabra = input("Introduce una palabra: ").lower()  
vocales = "aeiou"

for vocal in vocales:
    contador = palabra.count(vocal)
    print(f"La vocal '{vocal}' aparece {contador} veces")

#Ejercicio 10

lista = [50, 75, 46, 22, 80, 65, 8]
lista_ordenada = lista.sort()     #el método .sort() ordena la lista in situ y no devuelve nada
#si quieres que devuelva tienes que usar lista_ordenada = sorted(lista)
print(f"Aquí la lista ordenada {lista_ordenada}")

#Lo correcto sería :
lista = [50, 75, 46, 22, 80, 65, 8]
print(f"Aquí la lista ordenada {lista.sort()}")

#Métodos con punto (objeto.método()) como lista.sort() o lista.reverse() modifican la lista directamente y no devuelven nada → devuelven None.
#Funciones externas sin punto como min(lista), max(lista) o sorted(lista) devuelven un valor (un número o una nueva lista) y no modifican la original.

precios = [50, 75, 46, 22, 80, 65, 8]
precio_minimo = min(precios)
precio_maximo = max(precios)
print(f"El precio menor es: {precio_minimo}")
print(f"El precio mayor es: {precio_maximo}")

#Ejercicio 12
#Primero como seleccionamos los elementos de una fila o columna? 
a = (
    (1, 2, 3),
    (4, 5, 6)
)
a[i] → fila i
a[i][k] → elemento de la fila i, columna k
Ejemplos:
a[0]      # (1, 2, 3)  → fila 0
a[1]      # (4, 5, 6)  → fila 1
a[0][2]   # 3          → fila 0, columna 2 OJO, aqui no te da la columna entera(de la fila 0, agarramos el elemento 2)

#SEGUNDO, ahora como se calcula el producto matricial? 
# Cada número del resultado se obtiene multiplicando una FILA de A por una COLUMNA de B y sumando.
# Y asi obviamente el resultado será un 2X2.
Resultado =  ( ?  ? )
             ( ?  ? )

#TERCERO Vamos a calcular el primer número. FILA 1 X COLUMNA 1 . 
    # Fila 1 de A → (1, 2, 3)        # Columna 1 de B → (-1, 0, 1)
#1 × (-1)
#2 × 0
#3 × 1                  #y sumas los resultados , resultado = 2
#Fácil pues ahora con el siguiente : Posición (fila 1, columna 2)    Fila 1 de A → (1, 2, 3)     Columna 2 de B → (0, 1, 1)
#piensa en los numeros para identificar posiciones en la matriz

a = ((1, 2, 3),
     (4, 5, 6))
b = ((-1, 0),
     (0, 1),
     (1,1))
result = [[0,0],
          [0,0]]
for i in range(len(a)): # filas de A. len de A es 2 elementos                ->           i = 0(1era fila) i = 1, 
    for j in range(len(b[0])): # columnas de B, SIMPLEMENTE len(b[0]) para saber el nºcolumnas  j = 0 j= 1
        #una vez tenemos el nº de filas/columnas, tenemos que colocar los numeros en result[][] de tal manera que matchee la posición y operar
        for k in range(len(b)): #len b ahora normal te daria  k=0 k=1 k=2, k es para recorrer los 3 elementos de fila y columna . Piensa en 1 2 3    
            result[i][j] += a[i][k] * b[k][j]  
#vale y repetir el proceso ahora loopeando k, a[0][1] * b[1][0]. Y vamos sumando ese resultado a result.
#Cuando acabe con el loop de k, empezará con otro de j(1) y repetir asi el mismo proceso. result[0][1] += ...


#So let´s tuple the list [[0,0]],[[0,0]]
for i in range(len(result)):  #len(result) -> 0 , 1 or [], []
    result[i] = tuple(result[i]) #we tuple both filas,  0 and 1
result = tuple(result)  #finally we have [(0,0),(0,0)], so we need to tuple the entire matrix -> ((0,0),(0,0))
for i in range(len(result)): #and finally we show each fila tupllezied
    print(result[i])


#Ejercicio 13
entrada = input("Introduce números separados por comas: ")

numeros_str = entrada.split(",")   #Las , introducidas por el usuario las CORTAMOS, y .split devuelve los trozos restantes en una lista.
numeros = []

for n in numeros_str:   #But that is a list of strings yet. So we need to convert each element, and add it to a new list
    numeros.append(float(n))


media = sum(numeros) / len(numeros)    #sum(numeros) will sum each number of the list, instead of doing a for trough each element and sum it in another variabl

suma = 0       
for n in numeros:      #Basic formula to get standard deviation.
    suma += (n - media) ** 2

desviacion = (suma / len(numeros)) ** 0.5

print("Media:", media)
print("Desviación típica:", desviacion)



#EJERCICIOS DE DICCIONARIOS,
#Cuando usas in con un diccionario, Python SOLO mira las claves (keys)
#MIS ERRORES: keys() no se llama con un argumento, devuelve todas las claves del diccionario. lo mismo con value()

#Exercise 5
#Otra version con el .items(), Te evitas repetir asignaturas[asignatura]: 
asignaturas = {
    'Matemáticas': 6,
    'Física': 4,
    'Química': 5
}
total_creditos = 0
for asignatura, creditos in asignaturas.items(): #asignaturas.items() devuelve algo así ->  [('Matemáticas', 6), ('Física', 4), ('Química', 5)]
    print(f"{asignatura} tiene {creditos} créditos") #si fuese for asignatura in asignaturas, aqui tendrías que poner asignaturas[asignatura] para obtener los créditos
    total_creditos += creditos  # vamos sumando los créditos
print(f"El número total de créditos del curso es {total_creditos}")

#Exercise 7

cesta = {}

while True:
    articulo = input("Artículo (fin para terminar): ").lower()
    if articulo == "fin":
        break
    cesta[articulo] = float(input("Precio: "))

print("\nLista de la compra")
total = 0

for articulo, precio in cesta.items():
    print(f"{articulo}: {precio} €")
    total += precio

print(f"Total: {total} €")
# Or u can do: total = sum(cesta.values())
            #print(f"Coste total: {total}")


            
#Exercise 8
entrada = input("Introduce palabras y traducciones (es:en separadas por comas): ")

diccionario = {}

for par in entrada.split(","):
    esp, eng = par.split(":")
    diccionario[esp] = eng

frase = input("Introduce una frase en español: ")
traduccion = [] # 4. Traducimos palabra a palabra

for palabra in frase.split(): #Por defecto, split() separa la cadena por espacios en blanco:
    if palabra in diccionario:
        traduccion.append(diccionario[palabra]) #we r going to append the value of palabra(traducida)
    else:
        traduccion.append(palabra) #If a word is not in the dictionary we must leave it without traduction.
print(" ".join(traduccion)) # 5. Mostramos el resultado.  “Join all elements of the list into one string, putting a space between each word”

       
#Exercise 9     
#Mi código mejorado. SI CON EL CONTINUE VUELVE AL LOOP INICIAL
#CONTINUE SOLO SE PUEDE USAR CON FOR O WHILE.         #if decision != 1, 2, 3:       # if decision not in (1, 2, 3)!! 
diccionario_facturas = {}
cobrado = 0

while True:
    decision_usuario = input(
        "Introduzca decisión de factura (AÑADIR, PAGAR, TERMINAR): "
    ).upper()

    if decision_usuario == "AÑADIR":
        numero_factura = int(input("¿Cuál es el número de factura? "))
        coste = float(input("¿Cuál es el coste de la factura? "))
        diccionario_facturas[numero_factura] = coste

    elif decision_usuario == "PAGAR":
        factura_eliminada = int(input("¿Cuál es el número de factura a pagar? "))
        if factura_eliminada in diccionario_facturas:
            cobrado += diccionario_facturas[factura_eliminada]
            del diccionario_facturas[factura_eliminada] # en diccionarios no existe .remove()
        else:
            print("Esa factura no existe.")

    elif decision_usuario == "TERMINAR":
        break  #That break exits the while True loop, not just the elif.

    else:
        print("Opción no válida.") #Yo aqui pondria un continue ya el texto siguiente se printeraria
        continue
        
    pendiente = sum(diccionario_facturas.values())
    
    print("Cobrado hasta ahora:", cobrado)
    print("Pendiente de cobro:", pendiente)
    print("-" * 30)

#EJERCICIOS DE FUNCIONES.
#Exercise 3
def factorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado


numero = int(input("Introduce un número entero positivo: "))

while numero <= 0:
    numero = int(input("Debe ser positivo. Introduce otro: "))
    
print("El factorial es:", factorial(numero))
        


#12
def a(cadena):
    diccionario = {}

    for x in cadena:
        if x not in diccionario:
            diccionario[x] = 1
        else:
            diccionario[x] += 1
    return diccionario

def b(diccionario):
    palabra_masrepe = None
    frecuencia_masrepe = 0
#ahhh ya entiendo, Lo que pasa es que se va guardando siempre la mayor que hemos encontrado hasta ese momento.
    for palabra, frecuencia in diccionario.items():
        if frecuencia > frecuencia_masrepe
            frecuencia_masrepe = frecuencia
            palabra_masrepe = palabra
    return palabra_masrepe, frecuencia_masrepe




cadena = input("Introduce una frase: ").split()
diccionario = a(cadena)
resultado = b(diccionario)

print(diccionario)
print("La palabra más repetida es:", resultado[0])
print("Con frecuencia:", resultado[1])






