import math

# Datos dados
sigma = 8.0e-6  # C/m^2
radio = 1.22  # m
k = 8.99e9  # N*m^2/C^2

# a) Calcular la carga neta
area_superficie = 4 * math.pi * radio**2
carga_neta = sigma * area_superficie

# b) Calcular el campo eléctrico en la superficie
campo_electrico = k * carga_neta / radio**2

# Resultados
print(f"a) La carga neta en la esfera es: {carga_neta:.2e} C")
print(f"b) El campo eléctrico en la superficie de la esfera es: {campo_electrico:.2e} N/C")
