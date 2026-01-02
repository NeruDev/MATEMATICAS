<!--
---
type: solution
problem-id: CD-02-04
topic: [Derivadas](../../../../glossary.md#derivadas)
subtopic: Definición de [derivada](../../../../glossary.md#derivada)
difficulty: intermedio
tags: [derivada, definición, [límite](../../../../glossary.md#limite), [función](../../../../glossary.md#funcion)-racional]
created: 2024-12-22
---
-->

# Solución: Derivada de f(x) = 1/x usando la definición

## Problema

Usar la definición de [derivada](../../../../glossary.md#derivada) para calcular $f'(x)$ si $f(x) = \dfrac{1}{x}$.

---

## Método de Solución: Aplicación directa de la definición

### Paso 1: Escribir la definición de derivada

La derivada de una [función](../../../../glossary.md#funcion) $f(x)$ se define como:

$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

### Paso 2: Sustituir f(x) y f(x+h)

Dado que $f(x) = \dfrac{1}{x}$, entonces:

$$f(x+h) = \frac{1}{x+h}$$

Sustituyendo en la definición:

$$f'(x) = \lim_{h \to 0} \frac{\dfrac{1}{x+h} - \dfrac{1}{x}}{h}$$

### Paso 3: Simplificar el numerador (restar fracciones)

Para restar las fracciones en el numerador, encontramos el común denominador:

$$\frac{1}{x+h} - \frac{1}{x} = \frac{x - (x+h)}{x(x+h)} = \frac{x - x - h}{x(x+h)} = \frac{-h}{x(x+h)}$$

### Paso 4: Sustituir el numerador simplificado

$$f'(x) = \lim_{h \to 0} \frac{\dfrac{-h}{x(x+h)}}{h}$$

### Paso 5: Simplificar la fracción compuesta

Dividir por $h$ es equivalente a multiplicar por $\dfrac{1}{h}$:

$$f'(x) = \lim_{h \to 0} \frac{-h}{x(x+h)} \cdot \frac{1}{h}$$

$$f'(x) = \lim_{h \to 0} \frac{-h}{h \cdot x(x+h)}$$

### Paso 6: Cancelar h (válido porque h ≠ 0 en el límite)

$$f'(x) = \lim_{h \to 0} \frac{-1}{x(x+h)}$$

### Paso 7: Evaluar el límite cuando h → 0

$$f'(x) = \frac{-1}{x(x+0)} = \frac{-1}{x \cdot x} = \frac{-1}{x^2}$$

---

## Respuesta

$$\boxed{f'(x) = -\frac{1}{x^2}}$$

---

## Verificación

### Método 1: Usando la regla de la potencia

Reescribimos $f(x) = \dfrac{1}{x} = x^{-1}$

Aplicando la regla de la potencia $\dfrac{d}{dx}[x^n] = nx^{n-1}$:

$$f'(x) = (-1)x^{-1-1} = -x^{-2} = -\frac{1}{x^2} \checkmark$$

### Método 2: Verificación numérica

Para $x = 2$:
- $f'(2) = -\dfrac{1}{4} = -0.25$

Aproximación con $h = 0.001$:
$$\frac{f(2.001) - f(2)}{0.001} = \frac{\frac{1}{2.001} - \frac{1}{2}}{0.001} = \frac{0.49975 - 0.5}{0.001} \approx -0.2499 \approx -0.25 \checkmark$$

---

## Notas adicionales

> **[Dominio](../../../../glossary.md#dominio) de f'(x)**: La derivada $f'(x) = -\dfrac{1}{x^2}$ está definida para todo $x \neq 0$, igual que la función original.

> **Interpretación geométrica**: Como $f'(x) < 0$ para todo $x \neq 0$, la función $f(x) = \dfrac{1}{x}$ es **siempre decreciente** en cada uno de sus intervalos de [dominio](../../../../glossary.md#dominio).
