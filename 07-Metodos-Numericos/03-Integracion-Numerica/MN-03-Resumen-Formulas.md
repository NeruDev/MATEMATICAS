<!--
---
title: Resumen de Fórmulas - [Integración Numérica](../../glossary.md#integracion-numerica)
type: cheatsheet
topic: integracion-numerica
tags: [métodos-numéricos, integración, fórmulas, cheatsheet]
created: 2025-12-20
updated: 2025-12-20
---
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../glossary.md)

---

# Resumen de Fórmulas: Integración Numérica

## 1. Regla del Trapecio

### Fórmula Simple
$$\int_a^b f(x)\,dx \approx \frac{h}{2}[f(a) + f(b)]$$

donde $h = b - a$.

### Regla del Trapecio Compuesta
$$\int_a^b f(x)\,dx \approx \frac{h}{2}\left[f(x_0) + 2\sum_{i=1}^{n-1}f(x_i) + f(x_n)\right]$$

donde $h = \frac{b-a}{n}$ y $x_i = a + ih$.

### Error del Trapecio Simple
$$E_T = -\frac{h^3}{12}f''(\xi), \quad \xi \in [a,b]$$

### Error del Trapecio Compuesto
$$E_T = -\frac{(b-a)h^2}{12}f''(\xi) = -\frac{(b-a)^3}{12n^2}f''(\xi)$$

**[Orden](../../glossary.md#orden) de precisión:** $O(h^2)$

---

## 2. Regla de Simpson 1/3

### Fórmula Simple
$$\int_a^b f(x)\,dx \approx \frac{h}{3}[f(x_0) + 4f(x_1) + f(x_2)]$$

donde $h = \frac{b-a}{2}$ y $x_1 = \frac{a+b}{2}$.

### Regla de Simpson 1/3 Compuesta
$$\int_a^b f(x)\,dx \approx \frac{h}{3}\left[f(x_0) + 4\sum_{i=1,3,5,...}^{n-1}f(x_i) + 2\sum_{i=2,4,6,...}^{n-2}f(x_i) + f(x_n)\right]$$

donde $n$ debe ser **par**.

### Forma Alternativa (más clara)
$$\int_a^b f(x)\,dx \approx \frac{h}{3}\left[f_0 + 4(f_1 + f_3 + \cdots) + 2(f_2 + f_4 + \cdots) + f_n\right]$$

### Error de Simpson Simple
$$E_S = -\frac{h^5}{90}f^{(4)}(\xi) = -\frac{(b-a)^5}{2880}f^{(4)}(\xi)$$

### Error de Simpson Compuesto
$$E_S = -\frac{(b-a)h^4}{180}f^{(4)}(\xi)$$

**[Orden](../../glossary.md#orden) de precisión:** $O(h^4)$

---

## 3. Regla de Simpson 3/8

### Fórmula Simple
$$\int_a^b f(x)\,dx \approx \frac{3h}{8}[f(x_0) + 3f(x_1) + 3f(x_2) + f(x_3)]$$

donde $h = \frac{b-a}{3}$.

### Error
$$E_{3/8} = -\frac{3h^5}{80}f^{(4)}(\xi)$$

**Orden de precisión:** $O(h^4)$ (igual que Simpson 1/3)

---

## 4. Fórmulas de Newton-Cotes (Resumen)

### Forma General
$$\int_a^b f(x)\,dx \approx \sum_{i=0}^{n} w_i f(x_i)$$

### Coeficientes de Newton-Cotes

| n | Nombre | Coeficientes | Error |
|---|--------|--------------|-------|
| 1 | Trapecio | $\frac{h}{2}[1, 1]$ | $O(h^3)$ |
| 2 | Simpson 1/3 | $\frac{h}{3}[1, 4, 1]$ | $O(h^5)$ |
| 3 | Simpson 3/8 | $\frac{3h}{8}[1, 3, 3, 1]$ | $O(h^5)$ |
| 4 | Boole | $\frac{2h}{45}[7, 32, 12, 32, 7]$ | $O(h^7)$ |

---

## 5. Cuadratura de Gauss-Legendre

### Fórmula General (en $[-1, 1]$)
$$\int_{-1}^{1} f(x)\,dx \approx \sum_{i=1}^{n} w_i f(x_i)$$

### Cambio de Variable (para $[a, b]$)
$$\int_a^b f(x)\,dx = \frac{b-a}{2}\int_{-1}^{1} f\left(\frac{b-a}{2}t + \frac{a+b}{2}\right)\,dt$$

### Nodos y Pesos (2 puntos)
$$x_1 = -\frac{1}{\sqrt{3}}, \quad x_2 = \frac{1}{\sqrt{3}}, \quad w_1 = w_2 = 1$$

### Nodos y Pesos (3 puntos)
$$x_1 = -\sqrt{\frac{3}{5}}, \quad x_2 = 0, \quad x_3 = \sqrt{\frac{3}{5}}$$
$$w_1 = w_3 = \frac{5}{9}, \quad w_2 = \frac{8}{9}$$

---

## 6. Estimación de Errores

### Error Relativo
$$\varepsilon_r = \left|\frac{I_{exacta} - I_{aproximada}}{I_{exacta}}\right| \times 100\%$$

### Regla de Runge (Extrapolación de Richardson)
$$I \approx I_{2n} + \frac{I_{2n} - I_n}{2^p - 1}$$

donde $p$ es el orden del método (2 para trapecio, 4 para Simpson).

### Mejora con Trapecio
$$I \approx I_{2n} + \frac{I_{2n} - I_n}{3}$$

### Mejora con Simpson
$$I \approx I_{2n} + \frac{I_{2n} - I_n}{15}$$

---

## Tabla Comparativa

| Método | Orden | Subintervalos | Mejor para |
|--------|-------|---------------|------------|
| Trapecio | $O(h^2)$ | Cualquier $n$ | Funciones suaves, cálculo rápido |
| Simpson 1/3 | $O(h^4)$ | $n$ par | Mayor precisión |
| Simpson 3/8 | $O(h^4)$ | $n$ múltiplo de 3 | Combinar con 1/3 |
| Gauss-Legendre | $O(h^{2n})$ | Variable | Alta precisión, pocos puntos |

---

## Fórmulas de Memoria Rápida

| Método | Recuerda |
|--------|----------|
| Trapecio | $\frac{h}{2}(f_0 + f_n) + h\sum f_i$ |
| Simpson | $\frac{h}{3}(1-4-2-4-2-\cdots-4-1)$ |
| Error Trap. | $\propto h^2 f''$ |
| Error Simp. | $\propto h^4 f^{(4)}$ |
