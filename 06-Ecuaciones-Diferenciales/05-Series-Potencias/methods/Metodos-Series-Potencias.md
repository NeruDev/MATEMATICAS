<!--
content_type: methods
topic: Series de Potencias para EDO
---
-->

# Métodos: Series de Potencias para EDO

---

## Método 1: Solución en Serie en Punto Ordinario

**Ecuación:** $y'' + P(x)y' + Q(x)y = 0$ con $x_0 = 0$ punto ordinario

### Pasos

1. **Verificar** que $x = 0$ es punto ordinario

2. **Suponer** $y = \sum_{n=0}^{\infty} c_n x^n$

3. **Calcular derivadas:**
   - $y' = \sum_{n=1}^{\infty} n c_n x^{n-1}$
   - $y'' = \sum_{n=2}^{\infty} n(n-1) c_n x^{n-2}$

4. **Sustituir** en la EDO

5. **Reindexar** para que todas las series tengan la misma potencia de $x$

6. **Combinar** series y factorizar

7. **Igualar** coeficientes a cero para cada potencia

8. **Obtener recurrencia** y escribir solución

### Ejemplo Paso a Paso

**Resolver:** $y'' - xy' - y = 0$

**Paso 1:** $P(x) = -x$, $Q(x) = -1$ son analíticas en $x = 0$ ✓

**Paso 2-3:**
$y = \sum_{n=0}^{\infty} c_n x^n$

$y' = \sum_{n=1}^{\infty} n c_n x^{n-1}$

$y'' = \sum_{n=2}^{\infty} n(n-1) c_n x^{n-2}$

**Paso 4:**
$\sum_{n=2}^{\infty} n(n-1) c_n x^{n-2} - x\sum_{n=1}^{\infty} n c_n x^{n-1} - \sum_{n=0}^{\infty} c_n x^n = 0$

**Paso 5:** En $y''$: sea $k = n-2$, entonces $n = k+2$

$y'' = \sum_{k=0}^{\infty} (k+2)(k+1) c_{k+2} x^k$

En $xy'$: $\sum_{n=1}^{\infty} n c_n x^n$

**Paso 6:**
$\sum_{n=0}^{\infty} [(n+2)(n+1)c_{n+2} - nc_n - c_n]x^n = 0$

$\sum_{n=0}^{\infty} [(n+2)(n+1)c_{n+2} - (n+1)c_n]x^n = 0$

**Paso 7:** Para cada $n$: $(n+2)(n+1)c_{n+2} = (n+1)c_n$

**Paso 8:** **Recurrencia:** $c_{n+2} = \frac{c_n}{n+2}$

$n = 0$: $c_2 = \frac{c_0}{2}$

$n = 1$: $c_3 = \frac{c_1}{3}$

$n = 2$: $c_4 = \frac{c_2}{4} = \frac{c_0}{8}$

$n = 3$: $c_5 = \frac{c_3}{5} = \frac{c_1}{15}$

**Solución:**
$$y = c_0\left(1 + \frac{x^2}{2} + \frac{x^4}{8} + \cdots\right) + c_1\left(x + \frac{x^3}{3} + \frac{x^5}{15} + \cdots\right)$$

---

## Método 2: Frobenius - Encontrar Ecuación Indicial

**Ecuación:** $x^2y'' + xp(x)y' + q(x)y = 0$ con punto singular regular en $x = 0$

### Pasos

1. **Identificar** $p(x)$ y $q(x)$ y verificar que son analíticas

2. **Calcular** $p_0 = p(0)$ y $q_0 = q(0)$

3. **Escribir ecuación indicial:**
   $$r(r-1) + p_0 r + q_0 = 0$$

4. **Resolver** para $r_1$ y $r_2$ (con $r_1 \geq r_2$)

5. **Clasificar** el caso:
   - Caso 1: $r_1 - r_2 \notin \mathbb{Z}$
   - Caso 2: $r_1 = r_2$
   - Caso 3: $r_1 - r_2 \in \mathbb{Z}^+$

### Ejemplo

**Encontrar ecuación indicial:** $2x^2y'' + xy' - (x+1)y = 0$

**Paso 1:** Dividir por $2x^2$:
$y'' + \frac{1}{2x}y' - \frac{x+1}{2x^2}y = 0$

Forma estándar: $x^2y'' + \frac{x}{2}y' - \frac{x+1}{2}y = 0$

$p(x) = \frac{1}{2}$, $q(x) = -\frac{x+1}{2}$

**Paso 2:** $p_0 = \frac{1}{2}$, $q_0 = -\frac{1}{2}$

**Paso 3:** $r(r-1) + \frac{1}{2}r - \frac{1}{2} = 0$

$r^2 - \frac{1}{2}r - \frac{1}{2} = 0$

$2r^2 - r - 1 = 0$

**Paso 4:** $(2r+1)(r-1) = 0 \Rightarrow r_1 = 1, r_2 = -\frac{1}{2}$

**Paso 5:** $r_1 - r_2 = \frac{3}{2} \notin \mathbb{Z}$ → **Caso 1**

---

## Método 3: Frobenius - Encontrar Coeficientes

### Pasos

1. **Sustituir** $y = \sum_{n=0}^{\infty} c_n x^{n+r}$ en la EDO

2. **Calcular:**
   - $y' = \sum_{n=0}^{\infty} (n+r) c_n x^{n+r-1}$
   - $y'' = \sum_{n=0}^{\infty} (n+r)(n+r-1) c_n x^{n+r-2}$

3. **Sustituir** y agrupar por potencias de $x$

4. **Coeficiente de $x^{r-2}$ o potencia más baja:** Da ecuación indicial

5. **Coeficientes siguientes:** Dan relación de recurrencia

6. **Resolver** para $c_1, c_2, ...$ en términos de $c_0$

7. **Obtener** $y_1$ con $r = r_1$

8. **Para $y_2$:** Usar fórmulas del caso correspondiente

### Ejemplo Paso a Paso

**Resolver:** $2xy'' + y' + y = 0$

Ecuación indicial: $r(r - \frac{1}{2}) = 0 \Rightarrow r = \frac{1}{2}, 0$

**Para $r = \frac{1}{2}$:**

$y = \sum_{n=0}^{\infty} c_n x^{n+1/2}$

$y' = \sum_{n=0}^{\infty} (n+\frac{1}{2}) c_n x^{n-1/2}$

$y'' = \sum_{n=0}^{\infty} (n+\frac{1}{2})(n-\frac{1}{2}) c_n x^{n-3/2}$

Sustituyendo:
$2x \cdot y'' + y' + y = 0$

$\sum_{n=0}^{\infty} 2(n+\frac{1}{2})(n-\frac{1}{2}) c_n x^{n-1/2} + \sum_{n=0}^{\infty} (n+\frac{1}{2}) c_n x^{n-1/2} + \sum_{n=0}^{\infty} c_n x^{n+1/2} = 0$

Reindexando la última suma (sea $m = n+1$):

$\sum_{n=0}^{\infty} [2(n+\frac{1}{2})(n-\frac{1}{2}) + (n+\frac{1}{2})] c_n x^{n-1/2} + \sum_{m=1}^{\infty} c_{m-1} x^{m-1/2} = 0$

Combinando ($n = 0$ separado):
$(2 \cdot \frac{1}{2} \cdot (-\frac{1}{2}) + \frac{1}{2})c_0 = 0$ ✓ (ecuación indicial satisfecha)

Para $n \geq 1$:
$[2(n+\frac{1}{2})(n-\frac{1}{2}) + (n+\frac{1}{2})]c_n + c_{n-1} = 0$

$(n+\frac{1}{2})[2(n-\frac{1}{2}) + 1]c_n = -c_{n-1}$

$(n+\frac{1}{2})(2n)c_n = -c_{n-1}$

**Recurrencia:** $c_n = -\frac{c_{n-1}}{n(2n+1)}$

$c_1 = -\frac{c_0}{3}$, $c_2 = -\frac{c_1}{10} = \frac{c_0}{30}$, ...

$$y_1 = x^{1/2}\left(1 - \frac{x}{3} + \frac{x^2}{30} - \cdots\right)$$

---

## Método 4: Verificar Convergencia

### Pasos

1. **Encontrar** los puntos singulares de la EDO

2. **Calcular** la distancia del centro de la serie al punto singular más cercano

3. **El radio de convergencia** es al menos esa distancia

### Ejemplo

**Para:** $y'' + \frac{1}{x-1}y' + \frac{1}{x+2}y = 0$

Puntos singulares: $x = 1$ y $x = -2$

Si desarrollamos en $x = 0$:
- Distancia a $x = 1$: 1
- Distancia a $x = -2$: 2

**Radio de convergencia:** $R \geq 1$

---

## Diagrama de Decisión: Series vs Frobenius

```
┌─────────────────────────────────────────────────┐
│    ¿Es x₀ punto ordinario o singular?           │
└─────────────────────────────────────────────────┘
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
   ORDINARIO               SINGULAR
        │                       │
        ▼                       ▼
   Series de              ¿Es regular?
   potencias                   │
   y = Σcₙxⁿ          ┌────────┴────────┐
                      ▼                 ▼
                    SÍ                 NO
                      │                 │
                      ▼                 ▼
                 FROBENIUS          Métodos
                 y = xʳΣcₙxⁿ        avanzados
                      │
                      ▼
              Ecuación indicial
              r(r-1) + p₀r + q₀ = 0
                      │
            ┌─────────┼─────────┐
            ▼         ▼         ▼
        Caso 1    Caso 2    Caso 3
       r₁-r₂∉ℤ   r₁=r₂    r₁-r₂∈ℤ⁺
            │         │         │
            ▼         ▼         ▼
         Dos      y₂ tiene  Puede o no
        series    ln x      tener ln x
```

---

## Método 5: Identificar Ecuaciones Especiales

### Checklist

| Si la EDO tiene forma... | Es ecuación de... |
|--------------------------|-------------------|
| $x^2y'' + xy' + (x^2 - n^2)y = 0$ | Bessel |
| $(1-x^2)y'' - 2xy' + n(n+1)y = 0$ | Legendre |
| $y'' - 2xy' + 2ny = 0$ | Hermite |
| $xy'' + (1-x)y' + ny = 0$ | Laguerre |
| $(1-x^2)y'' - xy' + n^2y = 0$ | Chebyshev |

### Soluciones Conocidas

- **Bessel $n = 0$:** $J_0(x) = 1 - \frac{x^2}{4} + \frac{x^4}{64} - ...$
- **Legendre:** $P_n(\cos\theta)$ para problemas esféricos
- **Hermite:** $H_n(x)e^{-x^2/2}$ para oscilador cuántico
