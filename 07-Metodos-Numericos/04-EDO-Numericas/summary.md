# Resumen: EDO Numéricas

## Problema de Valor Inicial (PVI)
$$\frac{dy}{dx} = f(x, y), \quad y(x_0) = y_0$$

---

## Fórmulas Principales

### Método de Euler (Explícito)
$$y_{n+1} = y_n + h \cdot f(x_n, y_n)$$
- **Error local:** $O(h^2)$
- **Error global:** $O(h)$

### Método de Heun (Euler Mejorado)
$$\tilde{y}_{n+1} = y_n + h \cdot f(x_n, y_n)$$
$$y_{n+1} = y_n + \frac{h}{2}[f(x_n, y_n) + f(x_{n+1}, \tilde{y}_{n+1})]$$
- **Error local:** $O(h^3)$
- **Error global:** $O(h^2)$

### Runge-Kutta 4 (RK4)
$$y_{n+1} = y_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)$$
donde:
- $k_1 = f(x_n, y_n)$
- $k_2 = f(x_n + h/2, y_n + hk_1/2)$
- $k_3 = f(x_n + h/2, y_n + hk_2/2)$
- $k_4 = f(x_n + h, y_n + hk_3)$
- **Error local:** $O(h^5)$, **Error global:** $O(h^4)$

---

## Tabla Comparativa

| Método | Evaluaciones $f$ | Orden | Error local | Estabilidad |
|--------|-----------------|-------|-------------|-------------|
| Euler | 1 | 1 | $O(h^2)$ | Limitada |
| Heun | 2 | 2 | $O(h^3)$ | Mejor |
| RK2 | 2 | 2 | $O(h^3)$ | Similar Heun |
| RK4 | 4 | 4 | $O(h^5)$ | Buena |
| Adams-Bashforth 4 | 1* | 4 | $O(h^5)$ | Limitada |
| Adams-Moulton 4 | 1* | 5 | $O(h^6)$ | Mejor |

*Usan valores anteriores ya calculados.

---

## Métodos Multipaso

### Adams-Bashforth (Explícito, 4 pasos)
$$y_{n+1} = y_n + \frac{h}{24}(55f_n - 59f_{n-1} + 37f_{n-2} - 9f_{n-3})$$

### Adams-Moulton (Implícito, 3 pasos)
$$y_{n+1} = y_n + \frac{h}{24}(9f_{n+1} + 19f_n - 5f_{n-1} + f_{n-2})$$

---

## Sistemas de EDO

Para $\mathbf{y}' = \mathbf{f}(x, \mathbf{y})$:

$$\mathbf{y}_{n+1} = \mathbf{y}_n + h \cdot \mathbf{f}(x_n, \mathbf{y}_n)$$

EDO de orden superior → Sistema de primer orden.

---

## Diagrama de Selección

```
¿Qué precisión necesitas?
│
├── BAJA (visualización) → Euler
│
├── MEDIA → Heun o RK2
│
├── ALTA → RK4 (estándar)
│
└── MUY ALTA/MUCHOS PASOS → Adams-Bashforth/Moulton
```

---

## Región de Estabilidad

Para EDO lineal $y' = \lambda y$ con $\lambda < 0$:
- **Euler explícito:** Estable si $|1 + h\lambda| < 1$, es decir $h < \frac{2}{|\lambda|}$
- **Euler implícito:** Incondicionalmente estable
- **RK4:** Estable para $h|\lambda| \lesssim 2.78$
