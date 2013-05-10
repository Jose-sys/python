from mano import hand
from carta import carta
from collections import Counter


cont = Counter()

repeticiones =  1000
for i in range(repeticiones):
    mano = hand()
    cont[mano.quees()] += 1

for x,y in cont.most_common():
    print("{0:<20}|  {1:<10}".format(x,y/repeticiones))




