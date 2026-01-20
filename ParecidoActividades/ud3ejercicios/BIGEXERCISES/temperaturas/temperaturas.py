    #El archivo temperaturas.txt contiene:
#18
#21
#20
#xx (mal)
#23
    #Debemos: :

#1️⃣ Pedir ruta del archivo
#2️⃣ Comprobar si existe (os + excepciones)
#3️⃣ Leer valores
#4️⃣ Ignorar datos incorrectos con try/except
#5️⃣ Calcular:
    #temperatura media
    #máxima
    #mínima
#6️⃣ Guardar resultados en  rsultado_temperaturas.txt
#7️⃣ Usar logging para registrar errores


import os
import logging
#How is this related to logging.error() ? In that line we will log  a level ERROR (40) (value)
#Since my level config is INFO (20) -> it passes the filter so it´s written, otherwise not. (levels, above 20)
logging.basicConfig(level=logging.INFO, filename="log_temperaturas.log",
                    format="%(levelname)s - %(message)s") #ERROR(40root:Valor no válido ignorado: abc

ruta = input("Introduce ruta del archivo de temperaturas: ")

if not os.path.isfile(ruta):
    print("❌ El archivo no existe")
else:
    temperaturas = []

    with open(ruta, "r") as f: 
        for linea in f: #PYTHON detecta f as an _io.TextIOWrapper
            try:  
                numero = float(linea.strip())#We´d get "18\n" .strip removes spaces beggining and end, tabs and NEWLINE chracters 
                temperaturas.append(numero)
            except ValueError: 
                logging.error(f"Valor no válido ignorado: {linea.strip()}") 

    assert len(temperaturas) > 0, "No hay temperaturas válidas" #Checks a condition, if it´s false program STOPS with AssertionError.

    media = sum(temperaturas)/len(temperaturas)
    maxima = max(temperaturas)
    minima = min(temperaturas)

    with open("resultado_temperaturas.txt", "w") as f:
        f.write(f"Media: {media}\nMax: {maxima}\nMin: {minima}\n")

    print("✔️ Resultados guardados")


########NOTES... As u see in your university notes, Loggins is not required in an except.
    # 1- Ejemplo con la Excepción ZERODIVISIONERROR (no manejada)
    #As a result, our program would stop. and show a traceback.
    def division(dividendo, divisor):   # (10 , 0)
        print(dividendo/divisor)
    # 2. NO stopping program. We capture that excepcion with TRY/EXCEPT
    def division(dividendo, divisor):
        try:
            print(dividendo,divisor)
        except ZeroDivisionError:
            print("No es posible dividir entre 0")
        finally:
            print("Fin")

    #Inside the EXCEPT, u can choose what to do: (if u don´t handle an EXcepcion error with TRY & EXCEPT , it will stop the program):

    #print() show the message to the user. OFC my teacher used this because it´s basic exercise. but we can also add a logging here
    #raise , Stop the program
    #pass,  Ignore it
    #LOGGING , RECORD IT SOMEWHERE.  Here´s what we did in our temperatures. Record errors in a file.
#Here the levels in logging, from minor to major. logging.debug(), logging.info() logging.warning(), logging.error(), logging.critical()

    
#SO WE DID SEE LOT OF STUFF. BUT WHAT IS DEBUGGING AND HOW IS CORRELATED TO ALL OF ABOVE?
# WHY  do exceptions, asserts, tracebacks, and logging belong together?
#Because they are different weapons in the same battle:  TO DEBUG!!





# 
# 
# 
# 
# 
# 
# 
# 
# """


