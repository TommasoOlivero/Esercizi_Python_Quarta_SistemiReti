num = 1
lista = []
risposta = "si"

while (risposta == "si"):
    num = int(input("Inserisci un numero: "))
    lista.append(num)
    risposta = input("vuoi ancora aggiungere: ")

print(lista[:-1])

