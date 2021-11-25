parola = input("inserisci parola: ")

palindorma = lambda parola: True if(parola == parola[::-1]) else None

variabile = palindorma(parola)

if(variabile == True):
    print("la parola è palindroma")
else:
    print("la parola non è palindorma")