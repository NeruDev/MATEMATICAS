<!--
::METADATA::
type: problem_set
topic_id: ed-01-[edo](../../..](../../../glossary.md)#edo)-primer-[orden](../../..](../../../glossary.md)#orden)
file_id: ED-01-Problemas
status: stable
audience: student
total_problems: 28
difficulty_distribution: {basic: 10, intermediate: 12, advanced: 6}
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../WIKI_INDEX.md) | [📚 Glosario](../../../glossary.md)

---

# Problemas: EDO de Primer Orden

---

## 1.1 Conceptos Fundamentales

### [Prob-01] Clasificación de EDOs por orden y grado ⭐

Clasificar las siguientes ecuaciones por [orden](../../..](../../../glossary.md)#orden) y grado:

a) $\frac{dy}{dx} + xy = e^x$

b) $\left(\frac{d^2y}{dx^2}\right)^2 + \frac{dy}{dx} = x$

c) $y''' + (y')^3 = \sin x$

> 📁 Solución: `solutions/prob-01/`

---

### [Prob-02] Verificación de solución general (lineal) ⭐

Verificar que $y = Ce^{-x} + x - 1$ es [solución general](../../..](../../../glossary.md)#solucion-general) de $\frac{dy}{dx} + y = x$.

> 📁 Solución: `solutions/prob-02/`

---

### [Prob-03] Verificación de solución general (no lineal) ⭐

Para $\frac{dy}{dx} = y^2$, verificar que $y = -\frac{1}{x+C}$ es [solución general](../../..](../../../glossary.md)#solucion-general).

> 📁 Solución: `solutions/prob-03/`

---

## 1.2 Ecuaciones Separables

### [Prob-04] Ecuaciones separables básicas ⭐⭐

Resolver las siguientes ecuaciones separables:

a) $\frac{dy}{dx} = \frac{x^2}{y}$

b) $\frac{dy}{dx} = y\sin x$

c) $(1+y^2)dx + (1+x^2)dy = 0$

> 📁 Solución: `solutions/prob-04/`

---

### [Prob-05] PVI con ecuación separable ⭐⭐

Resolver el PVI: $\frac{dy}{dx} = \frac{y^2}{x}$, $y(1) = 1$

> 📁 Solución: `solutions/prob-05/`

---

### [Prob-06] Separable con exponencial ⭐

Resolver: $\frac{dy}{dx} = e^{x+y}$

> 📁 Solución: `solutions/prob-06/`

---

### [Prob-07] Separable con funciones trigonométricas inversas ⭐⭐

Resolver: $\frac{dy}{dx} = \frac{1+y^2}{1+x^2}$

> 📁 Solución: `solutions/prob-07/`

---

## 1.3 Ecuaciones Lineales

### [Prob-08] Ecuaciones lineales de primer orden ⭐⭐

Resolver las siguientes ecuaciones lineales:

a) $\frac{dy}{dx} + 2y = e^{-x}$

b) $\frac{dy}{dx} - \frac{y}{x} = x^2$

c) $x\frac{dy}{dx} + 2y = x^3$

> 📁 Solución: `solutions/prob-08/`

---

### [Prob-09] PVI con ecuación lineal ⭐

Resolver el PVI: $\frac{dy}{dx} + y = e^x$, $y(0) = 1$

> 📁 Solución: `solutions/prob-09/`

---

### [Prob-10] Lineal con funciones trigonométricas ⭐⭐

Resolver: $\frac{dy}{dx} + y\tan x = \sec x$

> 📁 Solución: `solutions/prob-10/`

---

### [Prob-11] Lineal tipo Euler ⭐⭐

Resolver: $\frac{dy}{dx} + \frac{3}{x}y = \frac{1}{x^2}$

> 📁 Solución: `solutions/prob-11/`

---

## 1.4 Ecuaciones Exactas

### [Prob-12] Verificación y resolución de exactas ⭐⭐

Verificar si son exactas y resolver:

a) $(2xy + 3)dx + (x^2 - 1)dy = 0$

b) $(3x^2 + 6xy)dx + (3x^2 + 4y)dy = 0$

c) $(ye^{xy} + 2x)dx + (xe^{xy} + 2y)dy = 0$

> 📁 Solución: `solutions/prob-12/`

---

### [Prob-13] Ecuación exacta con polinomios ⭐⭐

Resolver: $(2xy - 3x^2)dx + (x^2 + 2y)dy = 0$

> 📁 Solución: `solutions/prob-13/`

---

### [Prob-14] PVI con ecuación exacta ⭐⭐⭐

Resolver el PVI: $(y\cos x + 2xe^y)dx + (\sin x + x^2e^y)dy = 0$, $y(0) = 0$

> 📁 Solución: `solutions/prob-14/`

---

## 1.5 Factor Integrante

### [Prob-15] Factor integrante básico ⭐⭐

Encontrar el [factor integrante](../../..](../../../glossary.md)#factor-integrante) y resolver:

a) $(y + 1)dx - xdy = 0$

b) $(x + y)dx + x\,dy = 0$

c) $ydx + (2xy - e^{-2y})dy = 0$

> 📁 Solución: `solutions/prob-15/`

---

### [Prob-16] Factor integrante con homogénea ⭐⭐⭐

Resolver: $(y^2 + xy)dx - x^2dy = 0$

> 📁 Solución: `solutions/prob-16/`

---

### [Prob-17] Determinación de factor integrante $\mu(x)$ ⭐⭐⭐

Encontrar $\mu(x)$ para: $(2y - 6x)dx + (3x - 4x^2y^{-1})dy = 0$

> 📁 Solución: `solutions/prob-17/`

---

## 1.6 Ecuaciones de Bernoulli

### [Prob-18] Ecuaciones de Bernoulli clásicas ⭐⭐

Resolver las ecuaciones de Bernoulli:

a) $\frac{dy}{dx} + y = y^2$

b) $\frac{dy}{dx} - y = xy^3$

c) $x\frac{dy}{dx} + y = y^2\ln x$

> 📁 Solución: `solutions/prob-18/`

---

### [Prob-19] PVI con Bernoulli ⭐⭐

Resolver el PVI: $\frac{dy}{dx} + \frac{y}{x} = xy^2$, $y(1) = 1$

> 📁 Solución: `solutions/prob-19/`

---

### [Prob-20] Bernoulli con trigonométricas ⭐⭐⭐

Resolver: $\frac{dy}{dx} + y\cot x = y^3\csc x$

> 📁 Solución: `solutions/prob-20/`

---

## 1.7 Ecuaciones Homogéneas

### [Prob-21] Ecuaciones homogéneas estándar ⭐⭐

Resolver las ecuaciones homogéneas:

a) $\frac{dy}{dx} = \frac{x + y}{x}$

b) $(x^2 + y^2)dx - 2xy\,dy = 0$

c) $\frac{dy}{dx} = \frac{y^2 - x^2}{xy}$

> 📁 Solución: `solutions/prob-21/`

---

### [Prob-22] PVI con ecuación homogénea ⭐⭐

Resolver el PVI: $\frac{dy}{dx} = \frac{x + 2y}{x}$, $y(1) = 0$

> 📁 Solución: `solutions/prob-22/`

---

### [Prob-23] Homogénea simétrica ⭐⭐

Resolver: $(x - y)dx + (x + y)dy = 0$

> 📁 Solución: `solutions/prob-23/`

---

## 1.8 Aplicaciones

### [Prob-24] Decaimiento Radiactivo ⭐

La cantidad de un material radiactivo decrece según $\frac{dN}{dt} = -kN$. Si inicialmente hay 100g y después de 10 años quedan 60g, ¿cuánto quedará después de 25 años?

> 📁 Solución: `solutions/prob-24/`

---

### [Prob-25] Ley de Enfriamiento de Newton ⭐⭐

Un objeto a 90°C se coloca en un ambiente a 20°C. Después de 10 minutos está a 60°C. ¿Cuándo estará a 30°C?

> 📁 Solución: `solutions/prob-25/`

---

### [Prob-26] Circuito RL ⭐⭐

En un circuito RL con $L = 2H$, $R = 4\Omega$ y $E = 12V$, la corriente satisface:

$$L\frac{di}{dt} + Ri = E$$

Si $i(0) = 0$, encontrar $i(t)$.

> 📁 Solución: `solutions/prob-26/`

---

### [Prob-27] Problema de Mezcla ⭐⭐⭐

Un tanque contiene 100L de agua con 10kg de sal. Entra solución a 3L/min con concentración 0.2 kg/L, y sale mezcla a 3L/min. Encontrar la cantidad de sal en el tanque en [función](../../..](../../../glossary.md)#funcion) del tiempo.

> 📁 Solución: `solutions/prob-27/`

---

### [Prob-28] Modelo de Población Logística ⭐⭐⭐

La población sigue el modelo logístico:

$$\frac{dP}{dt} = rP\left(1 - \frac{P}{K}\right)$$

con $r = 0.1$, $K = 1000$, $P(0) = 100$. Resolver para $P(t)$.

> 📁 Solución: `solutions/prob-28/`
