<!--
::METADATA::
type: cheatsheet
topic_id: ed-01-edo-primer-orden
file_id: ED-01-Resumen-Formulas
status: stable
audience: exam_review
requires: []
-->

# Resumen rápido — EDO de Primer Orden

## Forma general

$$\frac{dy}{dx} = f(x, y) \quad \text{o} \quad F\left(x, y, \frac{dy}{dx}\right) = 0$$

---

## Ecuaciones Separables

**Forma:** $\frac{dy}{dx} = f(x) \cdot g(y)$

**Solución:**
$$\int \frac{dy}{g(y)} = \int f(x)\,dx + C$$

---

## Ecuaciones Lineales de Primer Orden

**Forma estándar:** $\frac{dy}{dx} + P(x)y = Q(x)$

**Factor integrante:**
$$\mu(x) = e^{\int P(x)\,dx}$$

**Solución general:**
$$y = \frac{1}{\mu(x)}\left[\int \mu(x) Q(x)\,dx + C\right]$$

---

## Ecuaciones Exactas

**Forma:** $M(x,y)\,dx + N(x,y)\,dy = 0$

**Condición de exactitud:**
$$\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$$

**Solución:** Encontrar $F(x,y)$ tal que:
$$\frac{\partial F}{\partial x} = M, \quad \frac{\partial F}{\partial y} = N$$

Entonces $F(x,y) = C$ es la solución.

---

## Factor Integrante para Exactas

Si no es exacta, buscar $\mu$:

| Caso | Factor integrante |
|------|-------------------|
| $\frac{1}{N}\left(\frac{\partial M}{\partial y} - \frac{\partial N}{\partial x}\right) = f(x)$ | $\mu = e^{\int f(x)\,dx}$ |
| $\frac{1}{M}\left(\frac{\partial N}{\partial x} - \frac{\partial M}{\partial y}\right) = g(y)$ | $\mu = e^{\int g(y)\,dy}$ |

---

## Ecuación de Bernoulli

**Forma:** $\frac{dy}{dx} + P(x)y = Q(x)y^n$, donde $n \neq 0, 1$

**Sustitución:** $v = y^{1-n}$

**EDO lineal resultante:**
$$\frac{dv}{dx} + (1-n)P(x)v = (1-n)Q(x)$$

---

## Ecuaciones Homogéneas

**Forma:** $\frac{dy}{dx} = f\left(\frac{y}{x}\right)$

**Sustitución:** $y = vx \Rightarrow \frac{dy}{dx} = v + x\frac{dv}{dx}$

**EDO separable resultante:**
$$x\frac{dv}{dx} = f(v) - v$$

---

## Ecuaciones de Variables Reducibles

### Tipo $y' = f(ax + by + c)$

**Sustitución:** $u = ax + by + c$

$$\frac{du}{dx} = a + bf(u)$$

### Tipo $y' = f\left(\frac{a_1x + b_1y + c_1}{a_2x + b_2y + c_2}\right)$

- Si $\frac{a_1}{a_2} = \frac{b_1}{b_2}$: usar sustitución lineal
- Si no: traslación de ejes al punto de intersección

---

## Aplicaciones Comunes

| Modelo | EDO | Solución |
|--------|-----|----------|
| Crecimiento exponencial | $\frac{dP}{dt} = kP$ | $P = P_0 e^{kt}$ |
| Decaimiento | $\frac{dN}{dt} = -\lambda N$ | $N = N_0 e^{-\lambda t}$ |
| Enfriamiento de Newton | $\frac{dT}{dt} = -k(T - T_m)$ | $T = T_m + (T_0 - T_m)e^{-kt}$ |
| Logístico | $\frac{dP}{dt} = kP(M-P)$ | $P = \frac{M}{1 + Ae^{-kMt}}$ |

---

## Verificación de Soluciones

1. Sustituir $y$ y $y'$ en la EDO original
2. Verificar que la identidad se cumple
3. Comprobar condiciones iniciales si existen

---

<!--
IA: Hoja de referencia rápida para EDO de Primer Orden.
Para desarrollo completo: theory/ED-01-Teoria-EDO-Primer-Orden.md
file_id: ED-01-Resumen-Formulas
-->
