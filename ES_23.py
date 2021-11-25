parola = input("inserisci una parola: ")

isMaiuscolo = lambda parola: True if ((parola[0] >= 'A') & (parola[0] <= 'Z')) else None

variabile = isMaiuscolo(parola)

if(variabile == True):
    print("La prima lettera è maiuscola")
else:
    print("La prima lettera è minuscola")