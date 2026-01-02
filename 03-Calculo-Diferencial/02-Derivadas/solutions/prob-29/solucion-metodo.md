<!--
---
type: solution
problem-id: CD-02-29
topic: [Derivadas](../../../..](../../../../glossary.md)#derivadas)
subtopic: [Regla de la cadena](../../../..](../../../../glossary.md)#regla-de-la-cadena)
difficulty: avanzado
tags: [derivada, cadena-triple, funciones-compuestas, trigonométricas]
created: 2024-12-22
---
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../WIKI_INDEX.md) | [📚 Glosario](../../../../glossary.md)

---

# Solución: Derivada de g(x) = sin(cos(tan x)) (Cadena Triple)

## Problema

Derivar $g(x) = \sin(\cos(\tan x))$ aplicando la [regla de la cadena](../../../..](../../../../glossary.md)#regla-de-la-cadena) tres veces.

---

## Método de Solución: Regla de la cadena anidada

### Paso 1: Identificar la estructura de composición

La [función](../../../..](../../../../glossary.md)#funcion) es una [composición](../../../..](../../../../glossary.md)#composicion) de tres funciones:

$$g(x) = (f \circ h \circ k)(x) = f(h(k(x)))$$

Donde:

| Nivel | [Función](../../../../glossary.md#funcion) | Nombre | [Derivada](../../../../glossary.md#derivada) |
|-------|---------|--------|----------|
| Externa | $f(u) = \sin u$ | [seno](../../../../glossary.md#seno) | $f'(u) = \cos u$ |
| Media | $h(v) = \cos v$ | [coseno](../../../../glossary.md#coseno) | $h'(v) = -\sin v$ |
| Interna | $k(x) = \tan x$ | [tangente](../../../../glossary.md#tangente) | $k'(x) = \sec^2 x$ |

### Paso 2: Establecer la regla de la cadena generalizada

Para una [composición](../../../..](../../../../glossary.md)#composicion) triple $f(h(k(x)))$:

$$\frac{d}{dx}[f(h(k(x)))] = f'(h(k(x))) \cdot h'(k(x)) \cdot k'(x)$$

> **Regla mnemotécnica**: "[Derivada](../../../..](../../../../glossary.md)#derivada) de la externa evaluada en lo de adentro, por derivada de la media evaluada en lo más interno, por derivada de la interna."

### Paso 3: Calcular cada factor

**Factor 1: Derivada de la función externa**
$$f'(u) = \cos u$$
Evaluada en $u = h(k(x)) = \cos(\tan x)$:
$$f'(h(k(x))) = \cos(\cos(\tan x))$$

**Factor 2: Derivada de la función media**
$$h'(v) = -\sin v$$
Evaluada en $v = k(x) = \tan x$:
$$h'(k(x)) = -\sin(\tan x)$$

**Factor 3: Derivada de la función interna**
$$k'(x) = \sec^2 x$$

### Paso 4: Multiplicar los tres factores

$$g'(x) = \cos(\cos(\tan x)) \cdot (-\sin(\tan x)) \cdot \sec^2 x$$

### Paso 5: Simplificar y ordenar

$$g'(x) = -\cos(\cos(\tan x)) \cdot \sin(\tan x) \cdot \sec^2 x$$

---

## Respuesta

$$\boxed{g'(x) = -\sec^2 x \cdot \sin(\tan x) \cdot \cos(\cos(\tan x))}$$

Forma alternativa:
$$\boxed{g'(x) = -\frac{\sin(\tan x) \cdot \cos(\cos(\tan x))}{\cos^2 x}}$$

---

## Verificación

### Método 1: Verificación estructural por capas

Descomponemos paso a paso:

1. Sea $u = \tan x \Rightarrow \dfrac{du}{dx} = \sec^2 x$

2. Sea $v = \cos u = \cos(\tan x) \Rightarrow \dfrac{dv}{du} = -\sin u = -\sin(\tan x)$

3. Sea $g = \sin v = \sin(\cos(\tan x)) \Rightarrow \dfrac{dg}{dv} = \cos v = \cos(\cos(\tan x))$

Aplicando la regla de la cadena:
$$\frac{dg}{dx} = \frac{dg}{dv} \cdot \frac{dv}{du} \cdot \frac{du}{dx}$$

$$= \cos(\cos(\tan x)) \cdot (-\sin(\tan x)) \cdot \sec^2 x \checkmark$$

### Método 2: Verificación numérica en x = π/6

Calculamos valores:
- $\tan(\pi/6) = \dfrac{1}{\sqrt{3}} \approx 0.5774$
- $\cos(\tan(\pi/6)) = \cos(0.5774) \approx 0.8376$
- $\sin(\cos(\tan(\pi/6))) = \sin(0.8376) \approx 0.7431$

Para la derivada:
- $\sec^2(\pi/6) = \dfrac{4}{3} \approx 1.333$
- $\sin(\tan(\pi/6)) = \sin(0.5774) \approx 0.5456$
- $\cos(\cos(\tan(\pi/6))) = \cos(0.8376) \approx 0.5463$

$$g'(\pi/6) \approx -(1.333)(0.5456)(0.5463) \approx -0.397$$

Aproximación numérica con $h = 0.0001$:
$$\frac{g(\pi/6 + h) - g(\pi/6)}{h} \approx -0.397 \checkmark$$

---

## Diagrama de composición

```
x → [tan] → tan(x) → [cos] → cos(tan x) → [sin] → sin(cos(tan x))
     ↓              ↓                    ↓
   sec²x       -sin(tan x)      cos(cos(tan x))
```

$$g'(x) = \sec^2 x \times (-\sin(\tan x)) \times \cos(\cos(\tan x))$$

---

## Notas adicionales

> **[Generalización](../../../..](../../../../glossary.md)#generalizacion)**: Para $n$ funciones compuestas $f_1(f_2(\cdots f_n(x)))$:
> $$\frac{d}{dx} = f_1'(f_2(\cdots)) \cdot f_2'(f_3(\cdots)) \cdots f_n'(x)$$

> **[Dominio](../../../..](../../../../glossary.md)#dominio)**: La derivada existe donde $\cos x \neq 0$, es decir, $x \neq \dfrac{\pi}{2} + k\pi$ para $k \in \mathbb{Z}$.
