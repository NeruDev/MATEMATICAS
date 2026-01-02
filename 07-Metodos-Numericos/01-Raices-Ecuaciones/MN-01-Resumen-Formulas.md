<!--
---
title: Resumen de Fórmulas - [Raíces de Ecuaciones](../../glossary.md#raices-de-ecuaciones)
type: cheatsheet
topic: raices-ecuaciones
tags: [métodos-numéricos, raíces, fórmulas, cheatsheet]
created: 2025-12-20
updated: 2025-12-20
---
-->

# Resumen de Fórmulas: Raíces de Ecuaciones

## 1. Método de Bisección

### Fórmula Principal
$$x_m = \frac{a + b}{2}$$

### Algoritmo
1. Verificar que $f(a) \cdot f(b) < 0$
2. Calcular $x_m = \frac{a + b}{2}$
3. Si $f(a) \cdot f(x_m) < 0$: $b = x_m$
4. Si $f(a) \cdot f(x_m) > 0$: $a = x_m$
5. Repetir hasta [convergencia](../../glossary.md#convergencia)

### Error y Convergencia
$$\varepsilon_n = \frac{b - a}{2^n}$$

**Iteraciones necesarias:**
$$n \geq \frac{\ln(b-a) - \ln(\varepsilon)}{\ln 2}$$

---

## 2. Método de Newton-Raphson

### Fórmula Principal
$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

### Condiciones de Aplicación
- $f'(x_n) \neq 0$
- $x_0$ suficientemente cercano a la raíz

### Orden de Convergencia
**[Convergencia](../../glossary.md#convergencia) cuadrática** ([orden](../../glossary.md#orden) 2):
$$|e_{n+1}| \approx C|e_n|^2$$

### Error Aproximado
$$\varepsilon_a = \left|\frac{x_{n+1} - x_n}{x_{n+1}}\right| \times 100\%$$

---

## 3. Método de la Secante

### Fórmula Principal
$$x_{n+1} = x_n - f(x_n) \cdot \frac{x_n - x_{n-1}}{f(x_n) - f(x_{n-1})}$$

### Características
- No requiere [derivada](../../glossary.md#derivada)
- Necesita dos valores iniciales $x_0$ y $x_1$
- [Orden de convergencia](../../glossary.md#orden-de-convergencia): $\phi = \frac{1 + \sqrt{5}}{2} \approx 1.618$

---

## 4. Método de Punto Fijo

### Fórmula Principal
$$x_{n+1} = g(x_n)$$

donde $f(x) = 0 \Rightarrow x = g(x)$

### Condición de Convergencia
$$|g'(x)| < 1 \quad \text{en el intervalo que contiene la raíz}$$

### Error
$$|e_{n+1}| \leq \frac{k}{1-k}|x_{n+1} - x_n|$$

donde $k = \max|g'(x)|$ en el intervalo.

---

## 5. Método de Regla Falsa (Falsa Posición)

### Fórmula Principal
$$x_r = b - \frac{f(b)(a - b)}{f(a) - f(b)}$$

o equivalentemente:
$$x_r = \frac{a \cdot f(b) - b \cdot f(a)}{f(b) - f(a)}$$

---

## Tabla Comparativa

| Método | Convergencia | Evaluaciones/iter | Requiere |
|--------|-------------|-------------------|----------|
| Bisección | Lineal | 1 | Intervalo $[a,b]$ |
| Newton-Raphson | Cuadrática | 2 ($f$, $f'$) | $f'(x)$, $x_0$ |
| Secante | Superlineal (~1.618) | 1 | $x_0$, $x_1$ |
| Punto Fijo | Lineal | 1 | $g(x)$, $x_0$ |
| Regla Falsa | Superlineal | 1 | Intervalo $[a,b]$ |

---

## Criterios de Convergencia

### Error Absoluto
$$|x_{n+1} - x_n| < \varepsilon$$

### Error Relativo
$$\left|\frac{x_{n+1} - x_n}{x_{n+1}}\right| < \varepsilon$$

### Residuo
$$|f(x_n)| < \varepsilon$$

---

## Fórmulas de Error

### Teorema de Taylor (base teórica)
$$f(x) = f(x_n) + f'(x_n)(x - x_n) + \frac{f''(\xi)}{2!}(x - x_n)^2$$

### Error en Newton-Raphson
$$e_{n+1} = -\frac{f''(\xi)}{2f'(x_n)}e_n^2$$
