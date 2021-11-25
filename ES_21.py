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

conta = 0
for numero in range(2,1001):
	if (isPrimo(numero) == True):
	   conta = conta + 1

print(conta)

