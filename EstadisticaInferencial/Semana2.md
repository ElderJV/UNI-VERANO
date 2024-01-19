# Intervalo de confianza para la media

**Estimacion:**
Usar los estadisticos para estimar los parametros
### Tipos:

* **Puntual:** Se obtiene el parametro a partir de un solo numero obtenido de la muestra.
Cuando tenemos una media aritmetica a partir de una muestra (estadístico), esta puede ser empleada como estimador puntual para el valor de la media poblacional (parámetro). Análogamente con los demás estadísticos.

* **Por intervalos:** Se cuenta con un determinado rango de valores en los que se espera que esté el parametro (confianza) de que se encuentre el verdadero valor de $\theta$ (parámetro).
$$
P(\widehat{\theta}-\varepsilon<{\theta}<\widehat{\theta}+\varepsilon)={1-\alpha}
$$

# Intervalo de confianza de la media con varianza conocida

**Coeficiente o grado de confianza =** $1-\alpha$ 

Es la probabilidad de que la media $\mu$ este contenida en el **intervalo de confianza**

**Desconfianza o nivel de insignificancia** ( $\alpha$ )

Tambien llamado **error de tipo I** son sucesos fortuitos o extraños que pueden ocurrir.

---
![Confianza](../Images/Confianza.png)

# Intervalo de confianza de la media con varianza conocida

**Emplearemos Z cuando:**

* $n\geq30$ y $\sigma^2$ conocida
* $n<30$ y $\sigma^2$ conocida

**Intervalo de confianza IC**

$$
IC{:}\quad\bar{X}-Z_{(1-\frac\alpha2)}\cdot\frac\sigma{\sqrt{n}}\leq\mu\leq\bar{X}+Z_{(1-\frac\alpha2)}\cdot\frac\sigma{\sqrt{n}}
$$

**Erorr** ( $\epsilon$ )

$$
|\bar{X}-\mu|\leq\frac{Z_{1-\frac\alpha2}\cdot\sigma}{\sqrt{\mathrm{n}}}
$$
