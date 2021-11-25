def minimo(numeri):
    min = 1000
    for numero in numeri:
        if(numero < min):
            min = numero
    return min

def massimo(numeri):
    max = 0
    for numero in numeri:
     if(numero > max):
        max = numero
    return max

listaNumeri = [1,2,3,4,5,6,7,8,9]
max = massimo(listaNumeri)
min = minimo(listaNumeri)

print(f"massimo = {max}     minimo = {min}")