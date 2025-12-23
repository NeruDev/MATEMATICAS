<!--
HUMANO:
Métodos de técnicas de integración.

IA:
Procedimientos paso a paso para cada técnica.

---
content_type: methods
expected_output:
  default: markdown
audience: self-study
---
-->

# Métodos de Técnicas de Integración

---

## Método 1: Sustitución Simple

### Cuándo Usar
- Se identifica una función y su derivada (o múltiplo) en el integrando

### Pasos
1. Identificar $u = g(x)$ (función "interna")
2. Calcular $du = g'(x) dx$
3. Expresar $dx$ en términos de $du$
4. Sustituir completamente
5. Integrar en términos de $u$
6. Regresar a variable $x$

### Ejemplo
$$\int \frac{x}{x^2+1} dx$$

$u = x^2 + 1$, $du = 2x \, dx$, $x \, dx = \frac{du}{2}$

$= \frac{1}{2}\int \frac{du}{u} = \frac{1}{2}\ln\lvert u \rvert + C = \frac{1}{2}\ln(x^2+1) + C$

---

## Método 2: Integración por Partes

### Cuándo Usar
- Producto de funciones de diferentes tipos
- $\int \ln x \, dx$, $\int \arctan x \, dx$, etc.

### Pasos
1. Elegir $u$ usando LIATE (Logarítmica, Inversa trig., Algebraica, Trig., Exponencial)
2. El resto es $dv$
3. Calcular $du$ y $v$
4. Aplicar $\int u \, dv = uv - \int v \, du$
5. Resolver la nueva integral

### Ejemplo
$$\int x \ln x \, dx$$

$u = \ln x$ (L), $dv = x \, dx$
$du = \frac{1}{x} dx$, $v = \frac{x^2}{2}$

$= \frac{x^2}{2}\ln x - \int \frac{x^2}{2} \cdot \frac{1}{x} dx = \frac{x^2}{2}\ln x - \frac{1}{2}\int x \, dx$

$= \frac{x^2}{2}\ln x - \frac{x^2}{4} + C$

---

## Método 3: Potencias de Seno y Coseno (caso impar)

### Cuándo Usar
- $\int \sin^m x \cos^n x \, dx$ con $m$ o $n$ impar

### Pasos (si $n$ es impar)
1. Separar un factor $\cos x$
2. Convertir $\cos^{n-1} x$ usando $\cos^2 x = 1 - \sin^2 x$
3. Sustituir $u = \sin x$

### Ejemplo
$$\int \sin^2 x \cos^3 x \, dx$$

$= \int \sin^2 x \cos^2 x \cos x \, dx = \int \sin^2 x (1 - \sin^2 x) \cos x \, dx$

$u = \sin x$, $du = \cos x \, dx$

$= \int u^2(1-u^2) du = \int (u^2 - u^4) du = \frac{u^3}{3} - \frac{u^5}{5} + C$

$= \frac{\sin^3 x}{3} - \frac{\sin^5 x}{5} + C$

---

## Método 4: Potencias de Seno y Coseno (ambos pares)

### Cuándo Usar
- $\int \sin^m x \cos^n x \, dx$ con $m$ y $n$ pares

### Pasos
1. Usar $\sin^2 x = \frac{1-\cos 2x}{2}$
2. Usar $\cos^2 x = \frac{1+\cos 2x}{2}$
3. Expandir y simplificar
4. Repetir si es necesario

### Ejemplo
$$\int \sin^2 x \, dx = \int \frac{1-\cos 2x}{2} dx = \frac{x}{2} - \frac{\sin 2x}{4} + C$$

---

## Método 5: Sustitución Trigonométrica para $\sqrt{a^2 - x^2}$

### Cuándo Usar
- Expresiones con $\sqrt{a^2 - x^2}$

### Pasos
1. Sustituir $x = a\sin\theta$
2. $dx = a\cos\theta \, d\theta$
3. $\sqrt{a^2 - x^2} = a\cos\theta$
4. Integrar en $\theta$
5. Usar triángulo para regresar a $x$

### Ejemplo
$$\int \sqrt{9-x^2} \, dx$$

$x = 3\sin\theta$, $dx = 3\cos\theta \, d\theta$, $\sqrt{9-x^2} = 3\cos\theta$

$= \int 9\cos^2\theta \, d\theta = \frac{9}{2}\int (1+\cos 2\theta) d\theta = \frac{9}{2}\left(\theta + \frac{\sin 2\theta}{2}\right) + C$

$= \frac{9}{2}\theta + \frac{9}{4}\sin 2\theta + C = \frac{9}{2}\arcsin\frac{x}{3} + \frac{x\sqrt{9-x^2}}{2} + C$

---

## Método 6: Sustitución Trigonométrica para $\sqrt{a^2 + x^2}$

### Cuándo Usar
- Expresiones con $\sqrt{a^2 + x^2}$

### Pasos
1. Sustituir $x = a\tan\theta$
2. $dx = a\sec^2\theta \, d\theta$
3. $\sqrt{a^2 + x^2} = a\sec\theta$
4. Integrar
5. Regresar a $x$

---

## Método 7: Fracciones Parciales (factores lineales distintos)

### Cuándo Usar
- Denominador factoriza en factores lineales diferentes

### Pasos
1. Factorizar denominador
2. Escribir $\frac{P(x)}{(x-a)(x-b)\cdots} = \frac{A}{x-a} + \frac{B}{x-b} + \cdots$
3. Multiplicar por denominador común
4. Sustituir valores de $x$ para hallar constantes
5. Integrar cada fracción

### Ejemplo
$$\int \frac{2x+3}{x^2-x-2} dx = \int \frac{2x+3}{(x-2)(x+1)} dx$$

$\frac{2x+3}{(x-2)(x+1)} = \frac{A}{x-2} + \frac{B}{x+1}$

$x=2$: $7 = 3A \Rightarrow A = \frac{7}{3}$
$x=-1$: $1 = -3B \Rightarrow B = -\frac{1}{3}$

$= \frac{7}{3}\ln\lvert x-2\rvert - \frac{1}{3}\ln\lvert x+1\rvert + C$

---

## Método 8: Fracciones Parciales (factor cuadrático irreducible)

### Cuándo Usar
- Denominador tiene factor $ax^2 + bx + c$ que no factoriza

### Pasos
1. Usar forma $\frac{Ax + B}{ax^2+bx+c}$
2. Encontrar $A$ y $B$
3. Separar en dos integrales:
   - Una que produce logaritmo
   - Otra que produce arcotangente

### Ejemplo
$$\int \frac{x+1}{x^2+4} dx = \int \frac{x}{x^2+4} dx + \int \frac{1}{x^2+4} dx$$

$= \frac{1}{2}\ln(x^2+4) + \frac{1}{2}\arctan\frac{x}{2} + C$

---

## Método 9: Completar el Cuadrado

### Cuándo Usar
- Integrando con $ax^2 + bx + c$ en denominador (sin factorizar fácilmente)

### Pasos
1. Escribir $ax^2 + bx + c = a(x + \frac{b}{2a})^2 + (c - \frac{b^2}{4a})$
2. Sustituir $u = x + \frac{b}{2a}$
3. Usar fórmula de arcotangente o arcoseno

### Ejemplo
$$\int \frac{dx}{x^2 + 6x + 13} = \int \frac{dx}{(x+3)^2 + 4}$$

$u = x + 3$

$= \int \frac{du}{u^2 + 4} = \frac{1}{2}\arctan\frac{u}{2} + C = \frac{1}{2}\arctan\frac{x+3}{2} + C$

---

## Método 10: Partes Tabular (Derivadas Repetidas)

### Cuándo Usar
- $\int x^n e^{ax} dx$, $\int x^n \sin(ax) dx$, $\int x^n \cos(ax) dx$

### Pasos
1. Crear tabla con derivadas sucesivas de $x^n$ y primitivas de la otra función
2. Alternar signos: $+, -, +, -, \ldots$
3. Multiplicar diagonalmente

### Ejemplo
$$\int x^2 e^x dx$$

| Derivadas de $x^2$ | Primitivas de $e^x$ | Signo |
|-------------------|---------------------|-------|
| $x^2$ | $e^x$ | $+$ |
| $2x$ | $e^x$ | $-$ |
| $2$ | $e^x$ | $+$ |
| $0$ | $e^x$ | |

$= x^2 e^x - 2x e^x + 2e^x + C = e^x(x^2 - 2x + 2) + C$
