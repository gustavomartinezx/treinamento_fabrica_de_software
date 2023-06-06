import random

numeros = []

def sorteia():
    for x in range(1, 6):
        numero_aleatorio =  random.randint(1, 100)

        numeros.append(numero_aleatorio)
    
    print(numeros)

pares = sorteia()

def pares():
    numeros_pares = 0
    for valor in numeros:        
        if valor % 2 == 0:
            numeros_pares = numeros_pares + valor
    print(numeros_pares)
pares()