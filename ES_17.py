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

#list comprehension crea una lista mettenedo insieme un for e un if o piu istruzioni
primi = [k for k in range(2,1003) if isPrimo(k)]
print(primi)

dispari = [i for i in range(1000) if (i % 2 == 1)]
print(dispari)