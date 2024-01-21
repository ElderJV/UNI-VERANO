import math
E = 500
r = 0.6
E0 = (8.854 * 10**-12 )
pi = math.pi

#Qneta = (E *4*pi*r *E0)
Qneta = 1.1126264541953611e-08

CampoElectrico = Qneta/4*pi*(r**2)*E0

print("Carga Neta:",Qneta)
print("Campo Electrico:",CampoElectrico)

