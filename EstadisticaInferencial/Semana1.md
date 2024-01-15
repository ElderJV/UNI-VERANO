# Estadistica Inferencial (Introducción)
Nos proporcionan la teoria a partir de resultados o conclusiones de una muestra para inferir o estimar leyes de una poblacion.

## Parametro
Caracteristica numerica de una poblacion

## Estadistico
Caracteristica numerica de una muestra

## Observaciones 
Valor que toman las variables en cada elemento de la poblacion

## Unidad de analisis
Elemento u objeto indivisible que sera estudiado.

## Marco de muestreo
Relacion de unidades de muestreo

## Muestra
Conjunto de unidades de muestreo obtenidads del marco de muestreo.

---
## Variable 
Es una caracteristica de un objeto que tiende a ser cualitavia o cuantitativa.

---
###     Variable Cualitativa
####    Nominal
No se pueden ordenar
####    Ordinal
Tienen un orden, ya sea mayor que,menor que o igual que.

---
###     Variable Cuantitativa
####    Discreta
Solo se toman valores enteros
####    Continua
Se toman valores reales

---
## Ejemplo 1
La empresa Tecnotic SAC, está constituida por 860 ingenieros de sistemas,
distribuidos en (09) áreas laborales, la edad promedio de los ingenieros es 24
años, el 52% es de sexo masculino. Se tomó una muestra representativa de 100
ingenieros determinándose que 70%, trabajaban en dos turnos, además estos
tienen un sueldo promedio de S/. 4500. Se pide determinar:

**Poblacion:**
N = 860
 
**Muestra:**
 n = 100

**Unidad de analisis:**
Un ingeniero

**Variables:**
X = sueldo del ingeniero (V.Cuantitativa Continua)

**Dato:**
x1 = monto de sueldo de un ingeniero de la muestra

**Parametro:**
µ = Sueldo promedio de todos los ingenieros de la empresa

**Estadistico:**
Sueldo promedio de todos los ingenieros de la empresa

# Tipos de muestreo
* Muestreo aleatorio simple
* Muestreo sistematico
* Muestreo Estratificado

## Muestreo Aleatorio Simple

Simplemente se escoje un dato al azar, se puede uzar la formula +ALEATORIO.entre() en excel

```python 
# Ejemplo de selecion al azar con un arreglo
# Se utilizo el modulo random
import random

# Se crea la lista de numeros
datos = [15,16,4,7,4]

# Se declaran los rangos y se genera el numero al azar
valorMinimo=1
valorMaximo=5
numeroRandom =  random.randint(valorMinimo,valorMaximo)

# Se ubica al dato con el valor generado
datoValor = datos[numeroRandom-1]
print("Numero aleatorio:",numeroRandom)
print("Valor del numero aleatorio:",datoValor)

# Tambien se puede elegir directamente de la lista, si no
# se cuenta con un rango.

elementoAzar = random.choice(datos)
print("Elemento aleatorio directo:",elementoAzar)
```
## Muestreo sistematico

**Se debe definir el tamaño de la poblacion y la muestra**

N -> Poblacion
n -> Muestra

**Se define el valor K**

K -> N/n

**Elejimos un valor aleatorio entre 1 y K**

valorAleatorio = random.randint(1,k)

**Se declaran los siguientes valores**

Primera Seleccion = K
Frecuencia = valorAleatorio
Segunda selecion y posteriores = k + valorAleatorio

## Muestreo Estratificado

**Se debe contar con las varibales en porcentaje**

Ejemplo:
Genero | Masculino | 49%

**Se debe multiplicar el porcentaje por el tamaño de la muestra**

Ejemplo:
n = 30
valorMuestreo = 30 * 0.49 = 14.7 ≈ 15
![cap1](/Images/cap1.png)

## Tablas estadisticas

* **Tabla de distribucion normal:**

    Para utilizar esta tabla se debe tomar los valores y ubicarlos por fila y columna. 
    
    Se hace los mismo con los valores negativos
    
    Ejemplo:

    $$P(Z>-1.37)$$
    Se ubica el valor en la tabla

    $$1.37 = 0.08534$$
    
    Luego se realiza la siguiente operacion:

    $$Z=1-0.8534=0.91466$$

    **Propiedades:**

$$P(Z<a)=P(Z<a)$$
$$P(Z>a)=1-P(Z<=a)$$
$$P(a<Z<b)=P(Z<b)-P(Z<a)$$

* **Tabla T-Student**

Se aproxima a la normal cada vez que aumentan los grados de libertad. 

Se debe tomar en cuenta el tamaño de la muestra **n** para obtener los grados de libertad **gl**
$$gl=n-1$$

**Primera Hipotesis**

Para usar la tabla se debe hallar el valor  **t** , este valor se encontrara en la fila que coincida con el valor **gl** calculado. Se obtendra como resultado el valor de la columna.

**Segunda Hipotesis** (Despues de ver el video)

Se tienen los siguientes datos:

Nivel de Confianza $NC$= 95% | $Tα/2$ | muestra **n=11**

---
Se calcula la probabilidad
$$NC+α=1$$
$$0.95+α=1$$
$$α=0.05$$
Nos piden $α/2$ entonces: 
$$α/2=0.025$$

Ahora $Tα/2$

$$Tα/2=1-α/2$$
$$Tα/2=1-0.025$$
$$Tα/2=0.975$$

Luego se calcula los grados de libertad
$$gl=n-1$$
$$gl=11-1$$
$$gl=10$$
---
Ahora se ubica en la tabla intersectando los grados de libertad y probabilidad.

>Si tenemos controlados los **gl** vamos a controlar tambien la distribucion.

# Tamaño de muestra

![cap2](/Images/cap2.png)

Cada nivel de confianza tiene su equivalencia en calificacion $Z$

Formulas:

![cap3](/Images/cap3.png)

