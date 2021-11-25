Parole = ["Ciao", "anna", "otto", "tavolo", "Chiave"]
maiuscole = []
palindrome = []

for parola in Parole:
    palindorma = lambda parola: True if(parola == parola[::-1]) else None
    palind = palindorma(parola)
    if(palind == True):
        palindrome.append(parola)


    isMaiuscolo = lambda parola: True if ((parola[0] >= 'A') & (parola[0] <= 'Z')) else None

    maiusc = isMaiuscolo(parola)

    if(maiusc == True):
        maiuscole.append(parola)

print(maiuscole)
print(palindrome)
    








