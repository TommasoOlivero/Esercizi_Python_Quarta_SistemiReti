def isPrimo(numero):
	ok = True
	divisore = 2
	while(ok == True) & (divisore < numero):
		if (numero % divisore == 0):
			ok = False
		divisore = divisore + 1
	if (divisore == 0):
		ok = False
	return ok


num = int(input("inserisci un numero: "))

if (isPrimo(num)  == True):
	   print("Il numero è primo")
else:
	   print("Il numero non è primo")