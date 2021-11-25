import math

x1 = int(input("Inserisci x prima coordinata: "))
y1 = int(input("Inserisci y prima coordinata: "))
x2 = int(input("Inserisci x seconda coordinata: "))
y2 = int(input("Inserisci y seconda coordinata: "))

a = (x1, y1)
b = (x2, y2)

distanza = math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
print(a, b)
print(f"distanza: {distanza}")

