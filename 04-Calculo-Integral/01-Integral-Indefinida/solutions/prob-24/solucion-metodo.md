<!--
---
title: "Solución - Integral de Binomio Exponencial al Cuadrado"
type: solution
topic: integral-indefinida
problem_id: CI-01-024
techniques:
  - expansion-binomial
  - integracion-exponencial
  - funciones-hiperbolicas
difficulty: intermedio
tags:
  - exponenciales
  - binomio-cuadrado
  - cosh
created: 2025-12-22
---
-->

# Solución: $\int(e^x + e^{-x})^2 \, dx$

## Problema

Calcular la [integral indefinida](../../../../glossary.md#integral-indefinida):
$$\int(e^x + e^{-x})^2 \, dx$$

---

## Método de Solución: Expansión del Binomio

### Paso 1: Expandir el binomio al cuadrado

Aplicamos $(a + b)^2 = a^2 + 2ab + b^2$:

$$(e^x + e^{-x})^2 = (e^x)^2 + 2(e^x)(e^{-x}) + (e^{-x})^2$$

Simplificando cada término:
- $(e^x)^2 = e^{2x}$
- $2(e^x)(e^{-x}) = 2e^{x-x} = 2e^0 = 2$
- $(e^{-x})^2 = e^{-2x}$

Por lo tanto:
$$(e^x + e^{-x})^2 = e^{2x} + 2 + e^{-2x}$$

### Paso 2: Reescribir la integral

$$\int(e^x + e^{-x})^2 \, dx = \int(e^{2x} + 2 + e^{-2x}) \, dx$$

### Paso 3: Integrar término a término

Separamos la integral:
$$\int e^{2x} \, dx + \int 2 \, dx + \int e^{-2x} \, dx$$

**Para $\int e^{2x} \, dx$:**

Usando la fórmula $\int e^{ax} \, dx = \frac{1}{a}e^{ax} + C$ con $a = 2$:
$$\int e^{2x} \, dx = \frac{1}{2}e^{2x}$$

**Para $\int 2 \, dx$:**
$$\int 2 \, dx = 2x$$

**Para $\int e^{-2x} \, dx$:**

Usando la misma fórmula con $a = -2$:
$$\int e^{-2x} \, dx = \frac{1}{-2}e^{-2x} = -\frac{1}{2}e^{-2x}$$

### Paso 4: Combinar resultados

$$\int(e^x + e^{-x})^2 \, dx = \frac{1}{2}e^{2x} + 2x - \frac{1}{2}e^{-2x} + C$$

Factorizando $\frac{1}{2}$:
$$= \frac{1}{2}(e^{2x} - e^{-2x}) + 2x + C$$

---

## Respuesta Final

$$\boxed{\int(e^x + e^{-x})^2 \, dx = \frac{e^{2x}}{2} + 2x - \frac{e^{-2x}}{2} + C}$$

**Forma alternativa:**
$$\boxed{\int(e^x + e^{-x})^2 \, dx = \frac{e^{2x} - e^{-2x}}{2} + 2x + C}$$

---

## Verificación por Derivación

Derivamos el resultado:
$$\frac{d}{dx}\left(\frac{e^{2x}}{2} + 2x - \frac{e^{-2x}}{2} + C\right)$$

Derivando término a término:
- $\frac{d}{dx}\left(\frac{e^{2x}}{2}\right) = \frac{1}{2} \cdot 2e^{2x} = e^{2x}$
- $\frac{d}{dx}(2x) = 2$
- $\frac{d}{dx}\left(-\frac{e^{-2x}}{2}\right) = -\frac{1}{2} \cdot (-2)e^{-2x} = e^{-2x}$
- $\frac{d}{dx}(C) = 0$

Resultado de la derivación:
$$e^{2x} + 2 + e^{-2x}$$

Verificamos que esto es igual a $(e^x + e^{-x})^2$:
$$(e^x + e^{-x})^2 = e^{2x} + 2 + e^{-2x} \quad \checkmark$$

**La solución es correcta.**

---

## Conexión con Funciones Hiperbólicas

### Relación con $\cosh(x)$

Recordemos que el [coseno](../../../../glossary.md#coseno) hiperbólico se define como:
$$\cosh(x) = \frac{e^x + e^{-x}}{2}$$

Por lo tanto:
$$(e^x + e^{-x})^2 = (2\cosh x)^2 = 4\cosh^2 x$$

### Identidad hiperbólica

Usando $\cosh^2 x = \frac{1 + \cosh(2x)}{2}$:
$$4\cosh^2 x = 4 \cdot \frac{1 + \cosh(2x)}{2} = 2 + 2\cosh(2x)$$

### Integral en términos hiperbólicos

$$\int 4\cosh^2 x \, dx = \int(2 + 2\cosh(2x)) \, dx = 2x + \sinh(2x) + C$$

Dado que $\sinh(2x) = \frac{e^{2x} - e^{-2x}}{2}$, esto coincide con nuestra respuesta:
$$2x + \frac{e^{2x} - e^{-2x}}{2} + C \quad \checkmark$$

---

## Notas Adicionales

> **Patrón Importante:** El producto $e^x \cdot e^{-x} = e^0 = 1$ siempre simplifica a una constante.

> **Fórmula General:** $\int e^{ax} \, dx = \frac{1}{a}e^{ax} + C$ para $a \neq 0$

> **Identidades Hiperbólicas Útiles:**
> - $\cosh x = \frac{e^x + e^{-x}}{2}$
> - $\sinh x = \frac{e^x - e^{-x}}{2}$
> - $\cosh^2 x - \sinh^2 x = 1$
