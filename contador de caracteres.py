vocal = 0
consonante = 0
espacio = 0
num = 0
cant = 1 
z=0
y = input("Ingrese texto a contar\n")
for char in y:
    if char == " ":
        z = z
    else:
         z = z + 1
    cant = cant + 1
    if char == "a" or char == "e" or  char == "i" or  char == "o" or  char == "u" or char == "á" or char == "é" or  char == "í" or  char == "ó" or  char == "ú" or char == "A" or char == "E" or  char == "I" or  char == "O" or  char == "U":
        vocal = vocal + 1
    elif char == " ":
        espacio = espacio + 1
    elif char == "1" or char == "2" or  char == "3" or  char == "4" or  char == "5" or char == "6" or char == "7" or  char == "8" or  char == "9" or  char == "0":
        num = num + 1
    else:
        consonante = consonante + 1
print(f"Usted ingresó {cant-1} de caracteres\nde las cuales {vocal} son letras vocales\n{consonante} son letras consonantes\n{num} son numeros\ny {espacio} espacios")