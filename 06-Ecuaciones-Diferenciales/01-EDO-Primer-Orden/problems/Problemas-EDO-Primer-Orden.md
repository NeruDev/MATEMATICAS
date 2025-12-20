<!--
content_type: problems
topic: EDO de Primer Orden
difficulty: graduated
---
-->

# Problemas: EDO de Primer Orden

---

## 1.1 Conceptos Fundamentales

### Problema 1
Clasificar las siguientes ecuaciones por orden y grado:
a) $\frac{dy}{dx} + xy = e^x$
b) $\left(\frac{d^2y}{dx^2}\right)^2 + \frac{dy}{dx} = x$
c) $y''' + (y')^3 = \sin x$

### Problema 2
Verificar que $y = Ce^{-x} + x - 1$ es solución general de $\frac{dy}{dx} + y = x$.

### Problema 3
Para $\frac{dy}{dx} = y^2$, verificar que $y = -\frac{1}{x+C}$ es solución general.

---

## 1.2 Ecuaciones Separables

### Problema 4
Resolver las siguientes ecuaciones separables:
a) $\frac{dy}{dx} = \frac{x^2}{y}$
b) $\frac{dy}{dx} = y\sin x$
c) $(1+y^2)dx + (1+x^2)dy = 0$

### Problema 5
Resolver el PVI: $\frac{dy}{dx} = \frac{y^2}{x}$, $y(1) = 1$

### Problema 6
Resolver: $\frac{dy}{dx} = e^{x+y}$

### Problema 7
Resolver: $\frac{dy}{dx} = \frac{1+y^2}{1+x^2}$

---

## 1.3 Ecuaciones Lineales

### Problema 8
Resolver las siguientes ecuaciones lineales:
a) $\frac{dy}{dx} + 2y = e^{-x}$
b) $\frac{dy}{dx} - \frac{y}{x} = x^2$
c) $x\frac{dy}{dx} + 2y = x^3$

### Problema 9
Resolver el PVI: $\frac{dy}{dx} + y = e^x$, $y(0) = 1$

### Problema 10
Resolver: $\frac{dy}{dx} + y\tan x = \sec x$

### Problema 11
Resolver: $\frac{dy}{dx} + \frac{3}{x}y = \frac{1}{x^2}$

---

## 1.4 Ecuaciones Exactas

### Problema 12
Verificar si son exactas y resolver:
a) $(2xy + 3)dx + (x^2 - 1)dy = 0$
b) $(3x^2 + 6xy)dx + (3x^2 + 4y)dy = 0$
c) $(ye^{xy} + 2x)dx + (xe^{xy} + 2y)dy = 0$

### Problema 13
Resolver: $(2xy - 3x^2)dx + (x^2 + 2y)dy = 0$

### Problema 14
Resolver el PVI: $(y\cos x + 2xe^y)dx + (\sin x + x^2e^y)dy = 0$, $y(0) = 0$

---

## 1.5 Factor Integrante

### Problema 15
Encontrar el factor integrante y resolver:
a) $(y + 1)dx - xdy = 0$
b) $(x + y)dx + x\,dy = 0$
c) $ydx + (2xy - e^{-2y})dy = 0$

### Problema 16
Resolver: $(y^2 + xy)dx - x^2dy = 0$

### Problema 17
Encontrar $\mu(x)$ para: $(2y - 6x)dx + (3x - 4x^2y^{-1})dy = 0$

---

## 1.6 Ecuaciones de Bernoulli

### Problema 18
Resolver las ecuaciones de Bernoulli:
a) $\frac{dy}{dx} + y = y^2$
b) $\frac{dy}{dx} - y = xy^3$
c) $x\frac{dy}{dx} + y = y^2\ln x$

### Problema 19
Resolver el PVI: $\frac{dy}{dx} + \frac{y}{x} = xy^2$, $y(1) = 1$

### Problema 20
Resolver: $\frac{dy}{dx} + y\cot x = y^3\csc x$

---

## 1.7 Ecuaciones Homogéneas

### Problema 21
Resolver las ecuaciones homogéneas:
a) $\frac{dy}{dx} = \frac{x + y}{x}$
b) $(x^2 + y^2)dx - 2xy\,dy = 0$
c) $\frac{dy}{dx} = \frac{y^2 - x^2}{xy}$

### Problema 22
Resolver el PVI: $\frac{dy}{dx} = \frac{x + 2y}{x}$, $y(1) = 0$

### Problema 23
Resolver: $(x - y)dx + (x + y)dy = 0$

---

## Aplicaciones

### Problema 24 (Decaimiento Radiactivo)
La cantidad de un material radiactivo decrece según $\frac{dN}{dt} = -kN$. Si inicialmente hay 100g y después de 10 años quedan 60g, ¿cuánto quedará después de 25 años?

### Problema 25 (Enfriamiento de Newton)
Un objeto a 90°C se coloca en un ambiente a 20°C. Después de 10 minutos está a 60°C. ¿Cuándo estará a 30°C?

### Problema 26 (Circuito RL)
En un circuito RL con $L = 2H$, $R = 4\Omega$ y $E = 12V$, la corriente satisface:
$$L\frac{di}{dt} + Ri = E$$
Si $i(0) = 0$, encontrar $i(t)$.

### Problema 27 (Mezcla)
Un tanque contiene 100L de agua con 10kg de sal. Entra solución a 3L/min con concentración 0.2 kg/L, y sale mezcla a 3L/min. Encontrar la cantidad de sal en el tanque en función del tiempo.

### Problema 28 (Población Logística)
La población sigue el modelo logístico:
$$\frac{dP}{dt} = rP\left(1 - \frac{P}{K}\right)$$
con $r = 0.1$, $K = 1000$, $P(0) = 100$. Resolver para $P(t)$.
