<!--
---
title: "Solución - Integral de Binomio con Radicales al Cuadrado"
type: solution
topic: integral-indefinida
problem_id: CI-01-014
techniques:
  - expansion-binomial
  - integracion-termino-a-termino
difficulty: intermedio
tags:
  - radicales
  - binomio-cuadrado
  - potencias-fraccionarias
created: 2025-12-22
---
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../WIKI_INDEX.md) | [📚 Glosario](../../../../glossary.md)

---

# Solución: $\int(\sqrt{x} + \frac{1}{\sqrt{x}})^2 \, dx$

## Problema

Calcular la [integral indefinida](../../../..](../../../../glossary.md)#integral-indefinida):
$$\int\left(\sqrt{x} + \frac{1}{\sqrt{x}}\right)^2 dx$$

---

## Método de Solución: Expansión del Binomio

### Paso 1: Reescribir en notación exponencial

Expresamos los radicales como potencias fraccionarias:
$$\sqrt{x} = x^{1/2} \quad \text{y} \quad \frac{1}{\sqrt{x}} = x^{-1/2}$$

La integral se convierte en:
$$\int\left(x^{1/2} + x^{-1/2}\right)^2 dx$$

### Paso 2: Expandir el binomio al cuadrado

Aplicamos la identidad $(a + b)^2 = a^2 + 2ab + b^2$:

$$\left(x^{1/2} + x^{-1/2}\right)^2 = \left(x^{1/2}\right)^2 + 2\left(x^{1/2}\right)\left(x^{-1/2}\right) + \left(x^{-1/2}\right)^2$$

Simplificando cada término:
- $(x^{1/2})^2 = x^1 = x$
- $2(x^{1/2})(x^{-1/2}) = 2x^{1/2 - 1/2} = 2x^0 = 2$
- $(x^{-1/2})^2 = x^{-1} = \frac{1}{x}$

Por lo tanto:
$$\left(x^{1/2} + x^{-1/2}\right)^2 = x + 2 + \frac{1}{x}$$

### Paso 3: Integrar término a término

La integral se convierte en:
$$\int\left(x + 2 + \frac{1}{x}\right) dx = \int x \, dx + \int 2 \, dx + \int \frac{1}{x} \, dx$$

Aplicando las fórmulas básicas de integración:

| Término | Integral |
|---------|----------|
| $\int x \, dx$ | $\frac{x^2}{2}$ |
| $\int 2 \, dx$ | $2x$ |
| $\int \frac{1}{x} \, dx$ | $\ln\lvert x \rvert$ |

### Paso 4: Combinar resultados

$$\int\left(\sqrt{x} + \frac{1}{\sqrt{x}}\right)^2 dx = \frac{x^2}{2} + 2x + \ln|x| + C$$

---

## Respuesta Final

$$\boxed{\int\left(\sqrt{x} + \frac{1}{\sqrt{x}}\right)^2 dx = \frac{x^2}{2} + 2x + \ln|x| + C}$$

---

## Verificación por Derivación

Derivamos el resultado para comprobar:

$$\frac{d}{dx}\left(\frac{x^2}{2} + 2x + \ln|x| + C\right)$$

Derivando término a término:
- $\frac{d}{dx}\left(\frac{x^2}{2}\right) = x$
- $\frac{d}{dx}(2x) = 2$
- $\frac{d}{dx}(\ln|x|) = \frac{1}{x}$
- $\frac{d}{dx}(C) = 0$

Resultado de la derivación:
$$x + 2 + \frac{1}{x}$$

Verificamos que esto es igual a $\left(\sqrt{x} + \frac{1}{\sqrt{x}}\right)^2$:
$$\left(\sqrt{x} + \frac{1}{\sqrt{x}}\right)^2 = x + 2 + \frac{1}{x} \quad \checkmark$$

**La solución es correcta.**

---

## Notas Adicionales

> **Concepto Clave:** Siempre que aparezca un binomio al cuadrado en una integral, expandirlo primero simplifica enormemente el cálculo.

> **Dominio:** La función original requiere $x > 0$ debido a $\sqrt{x}$ y $\frac{1}{\sqrt{x}}$. El resultado $\ln|x|$ se reduce a $\ln x$ en este dominio.
