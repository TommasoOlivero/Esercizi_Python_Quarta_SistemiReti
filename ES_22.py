#moduli corrispondono alle librerie
#due tipi di moduli :
    #nativi -> gia presenti in python
    #non nativi che sono le librerie esterne

import random

alice = random. randint(1,6)
Bob = random. randint(1, 6)
print(alice, Bob)

if (alice == Bob):
    print(f"parimerito")
elif(alice > Bob):
    print(f"vincitrice : Alice")
else:
    print(f"vincitore: Bob")
