perfDisp = []

for cont in range(1000):
    if((cont**2 < 1000) & ((cont**2)%2 == 1)):
        perfDisp.append(cont**2)

print(perfDisp)