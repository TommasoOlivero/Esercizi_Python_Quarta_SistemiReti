lista_operazioni = []

n1 = int(input("Primo numero"))
n2 = int(input("Secondo numero"))

lista_operazioni.append((n1**2) + (n2**2))
lista_operazioni.append((n1+n2)**2)
lista_operazioni.append((n1**2) - (n2**2))
lista_operazioni.append((n1-n2)**2)

print(lista_operazioni)
