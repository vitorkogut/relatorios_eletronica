import math
import matplotlib.pyplot as pp

IS = 1*(10**-16)
Vt = 0.025
Id = []
passo = 0.001
Vd = []
contador = 0.0
id = []
Vcc = 10
rs = 2000

# Calculo de Id
while contador <= 0.8:
    Id.append(IS * ( math.exp(contador/Vt)-1 ) )
    Vd.append(contador)
    contador = contador + passo
pp.plot(Vd,Id, label="Vd Id")
#pp.show()
   
# calculo de reta da carga
for point in range(len(Vd)):
    id.append( (-Vd[point] + Vcc )/rs )
pp.plot(Vd,id, label="Vd id")
pp.show()


