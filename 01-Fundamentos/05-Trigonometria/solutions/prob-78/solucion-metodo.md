<!--
---
type: solution
problem_id: FUN-05-PROB-78
title: "Demostración de la identidad arcsin x + arccos x = π/2"
topic: trigonometria
subtopic: funciones-inversas
difficulty: intermedio
tags: [funciones-inversas, arcoseno, arcocoseno, demostracion, identidades]
created: 2025-12-22
---
-->

# Demostración: arcsin x + arccos x = π/2

## 📋 Enunciado del Problema

**Demuestra que para todo $x \in [-1, 1]$:**

$$\arcsin x + \arccos x = \frac{\pi}{2}$$

---

## 🎯 Estrategia de Solución

Presentamos tres enfoques para la demostración:
1. **Demostración algebraica** usando definiciones de funciones inversas
2. **Demostración por [derivadas](../../../../glossary.md#derivadas)** (análisis)
3. **Demostración geométrica** usando un triángulo rectángulo

---

## 📝 Demostración 1: Método Algebraico

### Paso 1: Definir las variables

Sea $\alpha = \arcsin x$ donde $x \in [-1, 1]$

Por la definición de arcoseno:
- $\sin\alpha = x$
- $\alpha \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$

### Paso 2: Encontrar una expresión para arccos x

Necesitamos expresar $\arccos x$ en términos de $\alpha$.

Sabemos que $\sin\alpha = x$.

Usando la identidad cofunction: $\sin\alpha = \cos\left(\frac{\pi}{2} - \alpha\right)$

Por lo tanto:
$$x = \cos\left(\frac{\pi}{2} - \alpha\right)$$

### Paso 3: Verificar el dominio del ángulo

Para que podamos aplicar el arcocoseno, necesitamos que $\frac{\pi}{2} - \alpha$ esté en el rango de $\arccos$, que es $[0, \pi]$.

Como $\alpha \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$:

$$\frac{\pi}{2} - \alpha \in \left[\frac{\pi}{2} - \frac{\pi}{2}, \frac{\pi}{2} - \left(-\frac{\pi}{2}\right)\right] = [0, \pi]$$

✓ El ángulo está en el rango correcto.

### Paso 4: Aplicar arcocoseno

Como $x = \cos\left(\frac{\pi}{2} - \alpha\right)$ y $\frac{\pi}{2} - \alpha \in [0, \pi]$:

$$\arccos x = \frac{\pi}{2} - \alpha$$

### Paso 5: Sustituir y concluir

Recordando que $\alpha = \arcsin x$:

$$\arccos x = \frac{\pi}{2} - \arcsin x$$

Despejando:

$$\arcsin x + \arccos x = \frac{\pi}{2}$$

---

## 📝 Demostración 2: Método de Derivadas

### Paso 1: Definir la función

Sea $f(x) = \arcsin x + \arccos x$ para $x \in [-1, 1]$

### Paso 2: Calcular la derivada

$$f'(x) = \frac{d}{dx}[\arcsin x] + \frac{d}{dx}[\arccos x]$$

Recordando las [derivadas](../../../../glossary.md#derivadas) de las funciones inversas:
- $\frac{d}{dx}[\arcsin x] = \frac{1}{\sqrt{1-x^2}}$
- $\frac{d}{dx}[\arccos x] = -\frac{1}{\sqrt{1-x^2}}$

Por lo tanto:

$$f'(x) = \frac{1}{\sqrt{1-x^2}} + \left(-\frac{1}{\sqrt{1-x^2}}\right) = 0$$

### Paso 3: Conclusión de la derivada

Como $f'(x) = 0$ para todo $x \in (-1, 1)$, la [función](../../../../glossary.md#funcion) $f(x)$ es **constante**.

### Paso 4: Encontrar el valor de la constante

Evaluamos en un punto conveniente, por ejemplo $x = 0$:

$$f(0) = \arcsin(0) + \arccos(0) = 0 + \frac{\pi}{2} = \frac{\pi}{2}$$

### Paso 5: Concluir

Como $f(x)$ es constante y $f(0) = \frac{\pi}{2}$:

$$\arcsin x + \arccos x = \frac{\pi}{2} \quad \forall x \in [-1, 1]$$

---

## 📝 Demostración 3: Método Geométrico

### Paso 1: Construir un triángulo rectángulo

Considere un triángulo rectángulo con:
- Hipotenusa = 1
- Cateto opuesto al ángulo $\alpha$ = $x$ (donde $0 < x < 1$)
- Cateto adyacente = $\sqrt{1-x^2}$

```
                    /|
                   / |
                  /  |
            1   /   | x
               /    |
              /α    |
             /______|
            √(1-x²)
```

### Paso 2: Identificar los ángulos

- $\sin\alpha = \frac{x}{1} = x \implies \alpha = \arcsin x$
- $\cos\alpha = \frac{\sqrt{1-x^2}}{1} = \sqrt{1-x^2}$

El otro ángulo agudo es $\beta = \frac{\pi}{2} - \alpha$

### Paso 3: Relacionar con arcocoseno

Para el ángulo $\beta$:
$$\cos\beta = \frac{x}{1} = x \implies \beta = \arccos x$$

### Paso 4: Usar la suma de ángulos en un triángulo

En un triángulo rectángulo, los dos ángulos agudos suman $\frac{\pi}{2}$:

$$\alpha + \beta = \frac{\pi}{2}$$

Sustituyendo:

$$\arcsin x + \arccos x = \frac{\pi}{2}$$

---

## ✅ Resultado Final

$$\boxed{\arcsin x + \arccos x = \frac{\pi}{2} \quad \text{para todo } x \in [-1, 1]}$$

---

## 🔍 Verificación con Valores Específicos

### Caso 1: x = 0

$$\arcsin(0) + \arccos(0) = 0 + \frac{\pi}{2} = \frac{\pi}{2} \quad ✓$$

### Caso 2: x = 1

$$\arcsin(1) + \arccos(1) = \frac{\pi}{2} + 0 = \frac{\pi}{2} \quad ✓$$

### Caso 3: x = -1

$$\arcsin(-1) + \arccos(-1) = -\frac{\pi}{2} + \pi = \frac{\pi}{2} \quad ✓$$

### Caso 4: x = 1/2

$$\arcsin\left(\frac{1}{2}\right) + \arccos\left(\frac{1}{2}\right) = \frac{\pi}{6} + \frac{\pi}{3} = \frac{\pi}{6} + \frac{2\pi}{6} = \frac{3\pi}{6} = \frac{\pi}{2} \quad ✓$$

### Caso 5: x = √2/2

$$\arcsin\left(\frac{\sqrt{2}}{2}\right) + \arccos\left(\frac{\sqrt{2}}{2}\right) = \frac{\pi}{4} + \frac{\pi}{4} = \frac{\pi}{2} \quad ✓$$

### Caso 6: x = -√3/2

$$\arcsin\left(-\frac{\sqrt{3}}{2}\right) + \arccos\left(-\frac{\sqrt{3}}{2}\right) = -\frac{\pi}{3} + \frac{5\pi}{6}$$

$$= -\frac{2\pi}{6} + \frac{5\pi}{6} = \frac{3\pi}{6} = \frac{\pi}{2} \quad ✓$$

---

## 📊 Casos Especiales y Análisis

### Tabla de Valores Notables

| x | arcsin x | arccos x | Suma |
|---|----------|----------|------|
| -1 | $-\frac{\pi}{2}$ | $\pi$ | $\frac{\pi}{2}$ |
| $-\frac{\sqrt{3}}{2}$ | $-\frac{\pi}{3}$ | $\frac{5\pi}{6}$ | $\frac{\pi}{2}$ |
| $-\frac{\sqrt{2}}{2}$ | $-\frac{\pi}{4}$ | $\frac{3\pi}{4}$ | $\frac{\pi}{2}$ |
| $-\frac{1}{2}$ | $-\frac{\pi}{6}$ | $\frac{2\pi}{3}$ | $\frac{\pi}{2}$ |
| 0 | 0 | $\frac{\pi}{2}$ | $\frac{\pi}{2}$ |
| $\frac{1}{2}$ | $\frac{\pi}{6}$ | $\frac{\pi}{3}$ | $\frac{\pi}{2}$ |
| $\frac{\sqrt{2}}{2}$ | $\frac{\pi}{4}$ | $\frac{\pi}{4}$ | $\frac{\pi}{2}$ |
| $\frac{\sqrt{3}}{2}$ | $\frac{\pi}{3}$ | $\frac{\pi}{6}$ | $\frac{\pi}{2}$ |
| 1 | $\frac{\pi}{2}$ | 0 | $\frac{\pi}{2}$ |

### Análisis de los Extremos

**Para x = 1:**
- $\arcsin(1) = \frac{\pi}{2}$ (máximo del arcoseno)
- $\arccos(1) = 0$ (mínimo del arcocoseno)

**Para x = -1:**
- $\arcsin(-1) = -\frac{\pi}{2}$ (mínimo del arcoseno)
- $\arccos(-1) = \pi$ (máximo del arcocoseno)

En ambos casos extremos, la suma sigue siendo $\frac{\pi}{2}$.

---

## 📚 Identidades Relacionadas

### Otras Identidades de Funciones Inversas

| Identidad | [Dominio](../../../../glossary.md#dominio) |
|-----------|---------|
| $\arcsin x + \arccos x = \frac{\pi}{2}$ | $x \in [-1, 1]$ |
| $\arctan x + \text{arccot } x = \frac{\pi}{2}$ | $x \in \mathbb{R}$ |
| $\text{arcsec } x + \text{arccsc } x = \frac{\pi}{2}$ | $\|x\| \geq 1$ |

### Relación Geométrica

Esta identidad refleja el hecho de que en un triángulo rectángulo, si un ángulo agudo tiene [seno](../../../../glossary.md#seno) $x$, entonces el otro ángulo agudo (que es el complemento a $90°$) tiene [coseno](../../../../glossary.md#coseno) $x$.

> **Nota:** Esta es la razón por la que las funciones [seno](../../../../glossary.md#seno) y [coseno](../../../../glossary.md#coseno) se llaman **cofunciones** — cada una es la [función](../../../../glossary.md#funcion) del ángulo complementario de la otra.
