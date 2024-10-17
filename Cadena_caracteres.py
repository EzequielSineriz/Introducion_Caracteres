""" Ejercicio 1: Desarrollar una función que reciba una letra y una cadena.
Debe retornar las veces que la letra está incluida en el texto. """

def contar_letra(letra:str, cadena:str)->int:
    contador = 0
    for caracter in cadena:
        if caracter == letra:
            contador += 1
    return contador

#texto = "la mejor materia del mundo"
#letra_buscada = "a"

#resultado = contar_letra(letra_buscada, texto)
#print(f"la letra '{letra_buscada}', aparece {resultado}, en el texto '{texto}' ")


""" Ejercicio 2: Desarrollar una función que reciba una cadena y dos índices.
Se debe retornar la cadena que va entre las posiciones indicadas por los índices.
Si las posiciones no son válidas se debe informar. """

def subcadena_entre_indices(cadena:str, indice_inicio:int, indice_fin:int):
    if indice_inicio < 0 or indice_fin >= len(cadena) or indice_inicio > indice_fin:
        print("Los i    ndices no son validos.")
    return cadena[indice_inicio:indice_fin+1]

#cadena = "La mejor materia in the word"
#indice_inicio = 0
#indice_fin = 2
#resultado = subcadena_entre_indices(cadena, indice_inicio, indice_fin)
#print(resultado)


""" Ejercicio 3: Desarrollar una función “char_at” que recibe una cadena y un número.
Se debe retornar el caracter en la posición indicada por el número si ésta es válida.
**IMPORTANTE: **Las posiciones de los caracteres en un string van del 0 hasta el
<número de caracteres> - 1. """

def char_at(cadena, indice):
    if indice < 0 or indice >= len(cadena):
        print("Indice invalido!!")
    return cadena[indice]


#cadena = "Buen dia Argentina"
#indice = 1
#resultado = char_at(cadena, indice-1)
#print(f"El caracter en la posicion {indice} es: '{resultado}'")
         

""" 4) Crear una función que reciba como parámetro una cadena y determine la
cantidad de vocales que hay de cada una (individualmente). La función
retornará una matriz indicando en la columna 1 cada vocal, y en la columna 2
la cantidad.
 """

def contar_vocales(cadena):
    vocales = ['a', 'e', 'i', 'o', 'u']
    conteos = [0] * 5  
    for caracter in cadena.lower():
        if caracter == 'a':
            conteos[0] += 1
        elif caracter == 'e':
            conteos[1] += 1
        elif caracter == 'i':
            conteos[2] += 1
        elif caracter == 'o':
            conteos[3] += 1
        elif caracter == 'u':
            conteos[4] += 1
    return [[vocales[i], conteos[i]]for i in range(5)]
    

#cadena = "murcielaguito"
#resultado = contar_vocales(cadena)

#for fila in resultado:
  #  print(f'{fila[0]} {fila[1]}')

""" 
5) Crear una función que reciba una cadena y un caracter. La función deberá
devolver el índice en el que se encuentre la primera incidencia de dicho
caracter, o -1 en caso de que no esté.
 """

def cadena_caracter(cadena:str, caracter:str):
    for i in range(len(cadena)):
        if cadena[i] == caracter:
            return i
    return -1

#cadena_1 = "Esto es una buena idea"
#caracter_1 = "s"
#resultado = cadena_caracter(cadena_1, caracter_1)
#print (resultado)

""" 6) Crear una función que reciba como parámetro una cadena y determine si la
misma es o no un palíndromo. Deberá retornar un valor booleano indicando
lo sucedido. """

def es_palindromo(cadena: str) -> bool:
    izquierda = 0
    derecha = len(cadena) - 1
    
    while izquierda < derecha:
        if cadena[izquierda] == " ":
            izquierda += 1
        elif cadena[derecha] == " ":
            derecha -= 1
        elif cadena[izquierda].lower() != cadena[derecha].lower():
            return False
        else:
            izquierda += 1
            derecha -= 1
    
    return True

#cadena_2 = "radar"
#resultado_2 = es_palindromo(cadena_2)
#print(resultado_2)

""" 7) Crear una función que reciba como parámetro una cadena y suprima los
caracteres repetidos.Ej: Si recibe como parámetro la cadena “Hooola” debe devolver “Hola”
 """
def suprimir_caracter_repetido(cadena: str) -> str:
    cadena_nueva = ""
    
    for i in range(len(cadena)):
        repetido = False
        for j in range(len(cadena_nueva)):
            if cadena[i] == cadena_nueva[j]:
                repetido = True
                break
        while repetido == False:
            cadena_nueva += cadena[i]
            repetido = True
    
    return cadena_nueva

#cadena1 = "hooola"

#retorno = suprimir_caracter_repetido(cadena1)
#print(retorno)

""" 8) Crear una función que reciba una cadena por parámetro y suprima las
vocales de la misma.
Ej: Si recibe como parámetro la cadena “Hola” debe devolver “Hl”.  """


def suprimir_vocales_de_cadenas(cadena:str):
    vocales = ["a","e","i","o","u"]
    cadena_nueva = ""
    for i in range(len(cadena)):
        repetido = False
        for j in range(len(vocales)):
            if cadena[i] == vocales [j]:
                repetido = True
                break
        while repetido == False:
            cadena_nueva += cadena[i]
            repetido = True
    return cadena_nueva

#cadena_vocales = "hola pedro"
#retorno_nuevo = suprimir_vocales_de_cadenas(cadena_vocales)
#print(retorno_nuevo)

""" 9) Crear una función para contar cuántas veces aparece una subcadena dentro
de una cadena.
Ej: Si recibe la cadena “El pan del panadero” y la subcadena “pan” deberá
retornar el valor 2. """

def sub_cadena_en_cadena(cadena:str, sub_cadena:str)->int:
    contador = 0
    longitud_cadena = len(cadena)
    longitud_sub_cadena = len(sub_cadena)
    for i in range(longitud_cadena - longitud_sub_cadena +1):
        if cadena[i:i+longitud_sub_cadena] == sub_cadena:
            contador += 1
    return contador

#sub_cadena1 = "pan"
#cadena = "el panadero hace muchos panes"
#resultado = sub_cadena_en_cadena(cadena, sub_cadena1)
#print(resultado)



                

