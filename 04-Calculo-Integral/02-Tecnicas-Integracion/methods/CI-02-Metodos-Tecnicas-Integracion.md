<!--
HUMANO:
Métodos de [técnicas de integración](../../../glossary.md#tecnicas-de-integracion).

IA:
Procedimientos paso a paso para cada técnica.

---
content_type: methods
expected_output:
  default: markdown
audience: self-study
---
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../WIKI_INDEX.md) | [📚 Glosario](../../../glossary.md)

---

# Métodos de Técnicas de Integración

> **Objetivo:** Dominar las técnicas avanzadas de integración con explicaciones detalladas, cálculos intermedios y ejemplos clásicos paso a paso.

---

## Método 1: Sustitución Simple

### Cuándo Usar
- Se identifica una [función](../../../glossary.md#funcion) y su [derivada](../../../glossary.md#derivada) (o múltiplo) en el integrando
- Hay una "[función](../../../glossary.md#funcion) interna" compuesta

### Algoritmo de Resolución

| Paso | Acción | Verificación |
|------|--------|--------------|
| 1 | Identificar $u = g(x)$ (función "interna") | ¿Está $g'(x)$ en el integrando? |
| 2 | Calcular $du = g'(x) dx$ | Derivar $u$ |
| 3 | Expresar $dx$ en términos de $du$ | Despejar $dx$ |
| 4 | Sustituir completamente | No debe quedar ninguna $x$ |
| 5 | Integrar en términos de $u$ | Aplicar reglas básicas |
| 6 | Regresar a variable $x$ | Sustituir $u = g(x)$ |

### Ejemplo Detallado

**Problema:** Calcular $\int \frac{x}{x^2+1} \, dx$

**Paso 1:** Identificamos la función interna:
$$u = x^2 + 1$$
Observamos que $x$ (que está en el numerador) es proporcional a la [derivada](../../../glossary.md#derivada) de $u$.

**Paso 2:** Calculamos $du$:
$$du = 2x \, dx$$

**Paso 3:** Despejamos $x \, dx$:
$$x \, dx = \frac{du}{2}$$

**Paso 4:** Sustituimos en la integral:
$$\int \frac{x}{x^2+1} \, dx = \int \frac{1}{u} \cdot \frac{du}{2} = \frac{1}{2}\int \frac{du}{u}$$

**Paso 5:** Integramos:
$$= \frac{1}{2}\ln\lvert u \rvert + C$$

**Paso 6:** Regresamos a $x$:
$$\int \frac{x}{x^2+1} \, dx = \frac{1}{2}\ln(x^2+1) + C$$

> **Nota:** No necesitamos valor absoluto porque $x^2+1 > 0$ siempre.

---

## Método 2: Integración por Partes

### Cuándo Usar
- Producto de funciones de diferentes tipos
- Integrales de $\ln x$, funciones trigonométricas inversas
- Cuando la [sustitución](../../../glossary.md#sustitucion) simple no funciona

### Fórmula Fundamental
$$\int u \, dv = uv - \int v \, du$$

### Regla LIATE (prioridad para elegir $u$)
| Prioridad | Tipo de función | Ejemplo |
|-----------|-----------------|---------|
| 1 | **L**ogarítmica | $\ln x$, $\log x$ |
| 2 | **I**nversa trigonométrica | $\arctan x$, $\arcsin x$ |
| 3 | **A**lgebraica | $x^2$, $x$, $\sqrt{x}$ |
| 4 | **T**rigonométrica | $\sin x$, $\cos x$ |
| 5 | **E**xponencial | $e^x$, $2^x$ |

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Elegir $u$ usando LIATE | La función más alta en la lista |
| 2 | El resto es $dv$ | Todo lo que queda incluyendo $dx$ |
| 3 | Calcular $du$ | Derivar $u$ |
| 4 | Calcular $v$ | Integrar $dv$ |
| 5 | Aplicar la fórmula | $uv - \int v \, du$ |
| 6 | Resolver la nueva integral | Puede requerir repetir |

### Ejemplo Detallado

**Problema:** Calcular $\int x \ln x \, dx$

**Paso 1:** Usando LIATE, elegimos $u$:
- $\ln x$ es Logarítmica (L)
- $x$ es Algebraica (A)
- L tiene mayor prioridad, entonces: $u = \ln x$

**Paso 2:** El resto es $dv$:
$$dv = x \, dx$$

**Paso 3:** Calculamos $du$:
$$du = \frac{1}{x} \, dx$$

**Paso 4:** Calculamos $v$ (integrando $dv$):
$$v = \int x \, dx = \frac{x^2}{2}$$

**Paso 5:** Aplicamos la fórmula $uv - \int v \, du$:
$$\int x \ln x \, dx = \ln x \cdot \frac{x^2}{2} - \int \frac{x^2}{2} \cdot \frac{1}{x} \, dx$$

$$= \frac{x^2}{2}\ln x - \frac{1}{2}\int x \, dx$$

**Paso 6:** Resolvemos la integral restante:
$$= \frac{x^2}{2}\ln x - \frac{1}{2} \cdot \frac{x^2}{2} + C$$

$$\int x \ln x \, dx = \frac{x^2}{2}\ln x - \frac{x^2}{4} + C$$

**Verificación:** Derivando el resultado debe dar $x \ln x$.

---

## Método 3: Potencias de Seno y Coseno (caso impar)

### Cuándo Usar
- $\int \sin^m x \cos^n x \, dx$ donde $m$ o $n$ es impar

### Estrategia
Si $n$ es impar: separar un $\cos x$ y usar $\cos^2 x = 1 - \sin^2 x$
Si $m$ es impar: separar un $\sin x$ y usar $\sin^2 x = 1 - \cos^2 x$

### Algoritmo de Resolución (caso $n$ impar)

| Paso | Acción | Propósito |
|------|--------|-----------|
| 1 | Separar un factor $\cos x$ | Reservar para $du$ |
| 2 | Convertir $\cos^{n-1} x$ usando identidad | $\cos^2 x = 1 - \sin^2 x$ |
| 3 | Sustituir $u = \sin x$ | $du = \cos x \, dx$ |
| 4 | Integrar el [polinomio](../../../glossary.md#polinomio) en $u$ | Expandir y aplicar regla de potencia |
| 5 | Regresar a $x$ | $u = \sin x$ |

### Ejemplo Detallado

**Problema:** Calcular $\int \sin^2 x \cos^3 x \, dx$

**Paso 1:** Identificamos que $n = 3$ es impar. Separamos un $\cos x$:
$$\int \sin^2 x \cos^3 x \, dx = \int \sin^2 x \cos^2 x \cdot \cos x \, dx$$

**Paso 2:** Convertimos $\cos^2 x$ usando la identidad pitagórica:
$$= \int \sin^2 x (1 - \sin^2 x) \cos x \, dx$$

**Paso 3:** Hacemos la [sustitución](../../../glossary.md#sustitucion):
$$u = \sin x \implies du = \cos x \, dx$$

**Paso 4:** Sustituimos completamente:
$$= \int u^2(1-u^2) \, du = \int (u^2 - u^4) \, du$$

**Paso 5:** Integramos el [polinomio](../../../glossary.md#polinomio):
$$= \frac{u^3}{3} - \frac{u^5}{5} + C$$

**Paso 6:** Regresamos a $x$:
$$\int \sin^2 x \cos^3 x \, dx = \frac{\sin^3 x}{3} - \frac{\sin^5 x}{5} + C$$

---

## Método 4: Potencias de Seno y Coseno (ambos pares)

### Cuándo Usar
- $\int \sin^m x \cos^n x \, dx$ donde $m$ y $n$ son ambos pares

### Identidades de Reducción de Potencia
$$\sin^2 x = \frac{1-\cos 2x}{2} \qquad \cos^2 x = \frac{1+\cos 2x}{2}$$

### Algoritmo de Resolución

| Paso | Acción | Resultado |
|------|--------|-----------|
| 1 | Aplicar identidades de reducción | Reducir exponentes a la mitad |
| 2 | Expandir el producto | Obtener términos con $\cos 2x$, $\cos^2 2x$, etc. |
| 3 | Si aparecen potencias pares, repetir | Aplicar identidades nuevamente |
| 4 | Integrar cada término | Funciones lineales en $\cos$ |

### Ejemplo Detallado

**Problema:** Calcular $\int \sin^2 x \, dx$

**Paso 1:** Aplicamos la identidad de reducción:
$$\sin^2 x = \frac{1-\cos 2x}{2}$$

**Paso 2:** Sustituimos en la integral:
$$\int \sin^2 x \, dx = \int \frac{1-\cos 2x}{2} \, dx$$

**Paso 3:** Separamos:
$$= \frac{1}{2}\int 1 \, dx - \frac{1}{2}\int \cos 2x \, dx$$

**Paso 4:** Integramos cada parte:
- $\int 1 \, dx = x$
- $\int \cos 2x \, dx = \frac{\sin 2x}{2}$ (sustitución con $u = 2x$)

**Paso 5:** Combinamos:
$$\int \sin^2 x \, dx = \frac{x}{2} - \frac{1}{2} \cdot \frac{\sin 2x}{2} + C = \frac{x}{2} - \frac{\sin 2x}{4} + C$$

---

## Método 5: Sustitución Trigonométrica para $\sqrt{a^2 - x^2}$

### Cuándo Usar
- Expresiones con $\sqrt{a^2 - x^2}$

### Sustitución y Relaciones
$$x = a\sin\theta \implies dx = a\cos\theta \, d\theta$$
$$\sqrt{a^2 - x^2} = \sqrt{a^2 - a^2\sin^2\theta} = a\sqrt{1-\sin^2\theta} = a\cos\theta$$

### Triángulo de Referencia
```
        /|
       / |
    a /  | x = a sin θ
     /   |
    /θ   |
   /_____|
   √(a²-x²)
```

### Algoritmo de Resolución

| Paso | Acción | Cálculo |
|------|--------|---------|
| 1 | Identificar $a$ | $a^2 = $ constante bajo la raíz |
| 2 | Sustituir $x = a\sin\theta$ | $dx = a\cos\theta \, d\theta$ |
| 3 | Simplificar $\sqrt{a^2-x^2} = a\cos\theta$ | Usar identidad pitagórica |
| 4 | Integrar en $\theta$ | Métodos trigonométricos |
| 5 | Regresar a $x$ usando triángulo | $\theta = \arcsin(x/a)$ |

### Ejemplo Detallado

**Problema:** Calcular $\int \sqrt{9-x^2} \, dx$

**Paso 1:** Identificamos $a = 3$ (porque $a^2 = 9$)

**Paso 2:** Hacemos la sustitución:
$$x = 3\sin\theta \implies dx = 3\cos\theta \, d\theta$$

**Paso 3:** Simplificamos la raíz:
$$\sqrt{9-x^2} = \sqrt{9-9\sin^2\theta} = 3\sqrt{1-\sin^2\theta} = 3\cos\theta$$

**Paso 4:** Sustituimos en la integral:
$$\int \sqrt{9-x^2} \, dx = \int 3\cos\theta \cdot 3\cos\theta \, d\theta = 9\int \cos^2\theta \, d\theta$$

**Paso 5:** Usamos la identidad de potencia par:
$$= 9\int \frac{1+\cos 2\theta}{2} \, d\theta = \frac{9}{2}\int (1+\cos 2\theta) \, d\theta$$

**Paso 6:** Integramos:
$$= \frac{9}{2}\left(\theta + \frac{\sin 2\theta}{2}\right) + C = \frac{9\theta}{2} + \frac{9\sin 2\theta}{4} + C$$

**Paso 7:** Usamos $\sin 2\theta = 2\sin\theta\cos\theta$:
$$= \frac{9\theta}{2} + \frac{9 \cdot 2\sin\theta\cos\theta}{4} + C = \frac{9\theta}{2} + \frac{9\sin\theta\cos\theta}{2} + C$$

**Paso 8:** Regresamos a $x$ usando el triángulo:
- $\sin\theta = \frac{x}{3}$, entonces $\theta = \arcsin\frac{x}{3}$
- $\cos\theta = \frac{\sqrt{9-x^2}}{3}$

$$= \frac{9}{2}\arcsin\frac{x}{3} + \frac{9}{2} \cdot \frac{x}{3} \cdot \frac{\sqrt{9-x^2}}{3} + C$$

$$\int \sqrt{9-x^2} \, dx = \frac{9}{2}\arcsin\frac{x}{3} + \frac{x\sqrt{9-x^2}}{2} + C$$

---

## Método 6: Sustitución Trigonométrica para $\sqrt{a^2 + x^2}$

### Cuándo Usar
- Expresiones con $\sqrt{a^2 + x^2}$

### Sustitución y Relaciones
$$x = a\tan\theta \implies dx = a\sec^2\theta \, d\theta$$
$$\sqrt{a^2 + x^2} = \sqrt{a^2 + a^2\tan^2\theta} = a\sqrt{1+\tan^2\theta} = a\sec\theta$$

### Triángulo de Referencia
```
        /|
       / |
√(a²+x²)/ | x = a tan θ
       /  |
      /θ  |
     /____|
       a
```

### Algoritmo de Resolución

| Paso | Acción | Cálculo |
|------|--------|---------|
| 1 | Identificar $a$ | $a^2 = $ constante |
| 2 | Sustituir $x = a\tan\theta$ | $dx = a\sec^2\theta \, d\theta$ |
| 3 | Simplificar $\sqrt{a^2+x^2} = a\sec\theta$ | Usar identidad $1+\tan^2\theta = \sec^2\theta$ |
| 4 | Integrar en $\theta$ | Métodos trigonométricos |
| 5 | Regresar a $x$ usando triángulo | $\theta = \arctan(x/a)$ |

### Ejemplo Detallado

**Problema:** Calcular $\int \frac{1}{\sqrt{4+x^2}} \, dx$

**Paso 1:** Identificamos $a = 2$

**Paso 2:** Sustituimos:
$$x = 2\tan\theta, \quad dx = 2\sec^2\theta \, d\theta$$

**Paso 3:** Simplificamos:
$$\sqrt{4+x^2} = 2\sec\theta$$

**Paso 4:** Sustituimos en la integral:
$$\int \frac{1}{\sqrt{4+x^2}} \, dx = \int \frac{2\sec^2\theta}{2\sec\theta} \, d\theta = \int \sec\theta \, d\theta$$

**Paso 5:** Integramos (fórmula conocida):
$$= \ln|\sec\theta + \tan\theta| + C$$

**Paso 6:** Regresamos a $x$:
- $\tan\theta = \frac{x}{2}$
- $\sec\theta = \frac{\sqrt{4+x^2}}{2}$

$$\int \frac{1}{\sqrt{4+x^2}} \, dx = \ln\left|\frac{\sqrt{4+x^2}}{2} + \frac{x}{2}\right| + C = \ln\left|\sqrt{4+x^2} + x\right| + C'$$

---

## Método 7: Fracciones Parciales (factores lineales distintos)

### Cuándo Usar
- Función racional $\frac{P(x)}{Q(x)}$ donde $\deg P < \deg Q$
- Denominador factoriza en factores lineales diferentes

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Verificar que $\deg P < \deg Q$ | Si no, dividir primero |
| 2 | [Factorizar](../../../glossary.md#factorizar) el denominador | Obtener $(x-r_1)(x-r_2)\cdots$ |
| 3 | Escribir la descomposición | $\frac{A}{x-r_1} + \frac{B}{x-r_2} + \cdots$ |
| 4 | Multiplicar por denominador común | Eliminar fracciones |
| 5 | Sustituir raíces para hallar constantes | $x = r_1, r_2, \ldots$ |
| 6 | Integrar cada fracción | $\int \frac{A}{x-r} dx = A\ln\lvert x-r \rvert$ |

### Ejemplo Detallado

**Problema:** Calcular $\int \frac{2x+3}{x^2-x-2} \, dx$

**Paso 1:** Verificamos grados: numerador grado 1, denominador grado 2. ✓

**Paso 2:** Factorizamos el denominador:
$$x^2-x-2 = (x-2)(x+1)$$

**Paso 3:** Escribimos la descomposición:
$$\frac{2x+3}{(x-2)(x+1)} = \frac{A}{x-2} + \frac{B}{x+1}$$

**Paso 4:** Multiplicamos por $(x-2)(x+1)$:
$$2x+3 = A(x+1) + B(x-2)$$

**Paso 5:** Encontramos $A$ y $B$ sustituyendo raíces:

Para $x = 2$:
$$2(2)+3 = A(2+1) + B(0) \implies 7 = 3A \implies A = \frac{7}{3}$$

Para $x = -1$:
$$2(-1)+3 = A(0) + B(-1-2) \implies 1 = -3B \implies B = -\frac{1}{3}$$

**Paso 6:** Integramos:
$$\int \frac{2x+3}{x^2-x-2} \, dx = \int \frac{7/3}{x-2} \, dx + \int \frac{-1/3}{x+1} \, dx$$

$$= \frac{7}{3}\ln\lvert x-2\rvert - \frac{1}{3}\ln\lvert x+1\rvert + C$$

---

## Método 8: Fracciones Parciales (factor cuadrático irreducible)

### Cuándo Usar
- Denominador tiene factor $ax^2 + bx + c$ con discriminante $b^2 - 4ac < 0$

### Forma de la Descomposición
Para un factor cuadrático irreducible:
$$\frac{Ax + B}{ax^2+bx+c}$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Escribir descomposición con $Ax + B$ | Numerador lineal para cuadráticos |
| 2 | Encontrar $A$ y $B$ | Sistema de ecuaciones |
| 3 | Separar la integral | Parte logarítmica + parte arcotangente |

### Ejemplo Detallado

**Problema:** Calcular $\int \frac{x+1}{x^2+4} \, dx$

**Paso 1:** Notamos que $x^2+4$ es irreducible (discriminante $= -16 < 0$)

**Paso 2:** Separamos el numerador de forma estratégica:
$$\frac{x+1}{x^2+4} = \frac{x}{x^2+4} + \frac{1}{x^2+4}$$

**Paso 3:** Primera integral (produce logaritmo):
$$\int \frac{x}{x^2+4} \, dx$$

Hacemos $u = x^2+4$, $du = 2x\,dx$:
$$= \frac{1}{2}\int \frac{du}{u} = \frac{1}{2}\ln(x^2+4)$$

**Paso 4:** Segunda integral (produce arcotangente):
$$\int \frac{1}{x^2+4} \, dx = \int \frac{1}{2^2+x^2} \, dx = \frac{1}{2}\arctan\frac{x}{2}$$

**Paso 5:** Combinamos:
$$\int \frac{x+1}{x^2+4} \, dx = \frac{1}{2}\ln(x^2+4) + \frac{1}{2}\arctan\frac{x}{2} + C$$

---

## Método 9: Completar el Cuadrado

### Cuándo Usar
- Integrando con $ax^2 + bx + c$ en denominador que no factoriza fácilmente
- Para convertir a forma que permita usar arcotangente o arcoseno

### Fórmula para Completar el Cuadrado
$$ax^2 + bx + c = a\left(x + \frac{b}{2a}\right)^2 + \left(c - \frac{b^2}{4a}\right)$$

### Algoritmo de Resolución

| Paso | Acción | Cálculo |
|------|--------|---------|
| 1 | Identificar $a$, $b$, $c$ | Coeficientes del trinomio |
| 2 | Calcular $(x + \frac{b}{2a})^2$ | El cuadrado perfecto |
| 3 | Calcular el término constante | $c - \frac{b^2}{4a}$ |
| 4 | Sustituir $u = x + \frac{b}{2a}$ | Simplifica la expresión |
| 5 | Aplicar fórmula de arctan o arcsin | Según el signo |

### Ejemplo Detallado

**Problema:** Calcular $\int \frac{dx}{x^2 + 6x + 13}$

**Paso 1:** Identificamos: $a=1$, $b=6$, $c=13$

**Paso 2:** Completamos el cuadrado:
$$x^2 + 6x + 13 = (x^2 + 6x + 9) + 4 = (x+3)^2 + 4$$

**Paso 3:** Reescribimos la integral:
$$\int \frac{dx}{x^2 + 6x + 13} = \int \frac{dx}{(x+3)^2 + 4}$$

**Paso 4:** Hacemos $u = x + 3$, $du = dx$:
$$= \int \frac{du}{u^2 + 4} = \int \frac{du}{u^2 + 2^2}$$

**Paso 5:** Aplicamos la fórmula de arcotangente:
$$= \frac{1}{2}\arctan\frac{u}{2} + C$$

**Paso 6:** Regresamos a $x$:
$$\int \frac{dx}{x^2 + 6x + 13} = \frac{1}{2}\arctan\frac{x+3}{2} + C$$

$= \int \frac{du}{u^2 + 4} = \frac{1}{2}\arctan\frac{u}{2} + C = \frac{1}{2}\arctan\frac{x+3}{2} + C$

---

## Método 10: Partes Tabular (Derivadas Repetidas)

### Cuándo Usar
- $\int x^n e^{ax} dx$, $\int x^n \sin(ax) dx$, $\int x^n \cos(ax) dx$

### Pasos
1. Crear tabla con [derivadas](../../../glossary.md#derivadas) sucesivas de $x^n$ y primitivas de la otra función
2. Alternar signos: $+, -, +, -, \ldots$
3. Multiplicar diagonalmente

### Ejemplo
$$\int x^2 e^x dx$$

| [Derivadas](../../../glossary.md#derivadas) de $x^2$ | Primitivas de $e^x$ | Signo |
|-------------------|---------------------|-------|
| $x^2$ | $e^x$ | $+$ |
| $2x$ | $e^x$ | $-$ |
| $2$ | $e^x$ | $+$ |
| $0$ | $e^x$ | |

$= x^2 e^x - 2x e^x + 2e^x + C = e^x(x^2 - 2x + 2) + C$
