<!--
content_type: methods
topic: EDO de Segundo Orden
---
-->

# Métodos: EDO de Segundo Orden

---

## Método 1: Resolver Ecuación Homogénea con Coeficientes Constantes

**Ecuación:** $ay'' + by' + cy = 0$

### Pasos

1. **Escribir la ecuación característica:**
   $$ar^2 + br + c = 0$$

2. **Resolver usando la fórmula cuadrática:**
   $$r = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

3. **Determinar la solución según el discriminante:**

| $\Delta = b^2 - 4ac$ | Tipo de raíces | Solución general |
|----------------------|----------------|------------------|
| $\Delta > 0$ | $r_1, r_2$ reales distintas | $y = C_1 e^{r_1 x} + C_2 e^{r_2 x}$ |
| $\Delta = 0$ | $r$ real doble | $y = (C_1 + C_2 x)e^{rx}$ |
| $\Delta < 0$ | $\alpha \pm \beta i$ complejas | $y = e^{\alpha x}(C_1 \cos\beta x + C_2 \sin\beta x)$ |

### Ejemplo Paso a Paso

**Resolver:** $y'' + 6y' + 25y = 0$

**Paso 1:** $r^2 + 6r + 25 = 0$

**Paso 2:** $r = \frac{-6 \pm \sqrt{36 - 100}}{2} = \frac{-6 \pm \sqrt{-64}}{2} = \frac{-6 \pm 8i}{2} = -3 \pm 4i$

**Paso 3:** $\alpha = -3$, $\beta = 4$ (raíces complejas)

**Solución:** $y = e^{-3x}(C_1\cos 4x + C_2\sin 4x)$

---

## Método 2: Coeficientes Indeterminados

**Ecuación:** $ay'' + by' + cy = f(x)$

### Pasos

1. **Resolver la ecuación homogénea** para obtener $y_h$

2. **Proponer la forma de $y_p$** según $f(x)$:

| $f(x)$ | $y_p$ propuesta |
|--------|-----------------|
| $P_n(x)$ (polinomio grado $n$) | $A_n x^n + A_{n-1}x^{n-1} + \cdots + A_0$ |
| $e^{ax}$ | $Ae^{ax}$ |
| $\cos bx$ o $\sin bx$ | $A\cos bx + B\sin bx$ |
| $e^{ax}\cos bx$ | $e^{ax}(A\cos bx + B\sin bx)$ |
| $x^n e^{ax}$ | $(A_n x^n + \cdots + A_0)e^{ax}$ |

3. **Verificar duplicación:** Si $y_p$ contiene términos de $y_h$:
   - Multiplicar por $x$ (primera duplicación)
   - Multiplicar por $x^2$ (segunda duplicación)

4. **Calcular derivadas** de $y_p$

5. **Sustituir** en la ecuación original

6. **Igualar coeficientes** y resolver el sistema

7. **Escribir solución general:** $y = y_h + y_p$

### Ejemplo Paso a Paso

**Resolver:** $y'' - 4y = 8e^{2x}$

**Paso 1:** Homogénea: $r^2 - 4 = 0 \Rightarrow r = \pm 2$
$$y_h = C_1 e^{2x} + C_2 e^{-2x}$$

**Paso 2:** $f(x) = 8e^{2x}$ → proponer $y_p = Ae^{2x}$

**Paso 3:** ¡$e^{2x}$ está en $y_h$! → Modificar: $y_p = Axe^{2x}$

**Paso 4:** 
- $y_p' = Ae^{2x} + 2Axe^{2x} = Ae^{2x}(1 + 2x)$
- $y_p'' = 2Ae^{2x}(1 + 2x) + 2Ae^{2x} = Ae^{2x}(4 + 4x)$

**Paso 5:** $Ae^{2x}(4 + 4x) - 4Axe^{2x} = 8e^{2x}$

$Ae^{2x}(4 + 4x - 4x) = 8e^{2x}$

$4A = 8 \Rightarrow A = 2$

**Paso 6:** $y_p = 2xe^{2x}$

**Solución:** $y = C_1 e^{2x} + C_2 e^{-2x} + 2xe^{2x}$

---

## Método 3: Variación de Parámetros

**Ecuación:** $y'' + P(x)y' + Q(x)y = f(x)$

### Pasos

1. **Resolver la homogénea:** $y_h = C_1 y_1 + C_2 y_2$

2. **Calcular el Wronskiano:**
   $$W = \begin{vmatrix} y_1 & y_2 \\ y_1' & y_2' \end{vmatrix} = y_1 y_2' - y_2 y_1'$$

3. **Calcular $u_1'$ y $u_2'$:**
   $$u_1' = -\frac{y_2 f(x)}{W}, \quad u_2' = \frac{y_1 f(x)}{W}$$

4. **Integrar** para obtener $u_1$ y $u_2$

5. **Formar la solución particular:**
   $$y_p = u_1 y_1 + u_2 y_2$$

6. **Solución general:** $y = y_h + y_p$

### Ejemplo Paso a Paso

**Resolver:** $y'' + y = \tan x$

**Paso 1:** $r^2 + 1 = 0 \Rightarrow r = \pm i$
$$y_h = C_1\cos x + C_2\sin x$$
$y_1 = \cos x$, $y_2 = \sin x$

**Paso 2:** 
$$W = \cos x \cdot \cos x - \sin x \cdot (-\sin x) = \cos^2 x + \sin^2 x = 1$$

**Paso 3:**
$$u_1' = -\frac{\sin x \cdot \tan x}{1} = -\frac{\sin^2 x}{\cos x}$$
$$u_2' = \frac{\cos x \cdot \tan x}{1} = \sin x$$

**Paso 4:**
$$u_1 = -\int \frac{\sin^2 x}{\cos x}dx = -\int \frac{1-\cos^2 x}{\cos x}dx = -\int(\sec x - \cos x)dx$$
$$u_1 = -\ln|\sec x + \tan x| + \sin x$$

$$u_2 = \int \sin x\,dx = -\cos x$$

**Paso 5:**
$$y_p = \cos x(-\ln|\sec x + \tan x| + \sin x) + \sin x(-\cos x)$$
$$y_p = -\cos x \ln|\sec x + \tan x|$$

**Solución:** $y = C_1\cos x + C_2\sin x - \cos x\ln|\sec x + \tan x|$

---

## Método 4: Ecuación de Cauchy-Euler

**Ecuación:** $ax^2y'' + bxy' + cy = 0$

### Pasos

1. **Escribir ecuación auxiliar:** Sustituir $y = x^m$
   $$am(m-1) + bm + c = 0$$
   
   Simplificar: $am^2 + (b-a)m + c = 0$

2. **Resolver para $m$**

3. **Escribir solución según el tipo de raíces:**

| Raíces | Solución ($x > 0$) |
|--------|-------------------|
| $m_1 \neq m_2$ reales | $y = C_1 x^{m_1} + C_2 x^{m_2}$ |
| $m$ doble | $y = (C_1 + C_2\ln x)x^m$ |
| $\alpha \pm \beta i$ | $y = x^\alpha[C_1\cos(\beta\ln x) + C_2\sin(\beta\ln x)]$ |

### Ejemplo Paso a Paso

**Resolver:** $x^2y'' + 3xy' + y = 0$

**Paso 1:** $m(m-1) + 3m + 1 = 0$

$m^2 - m + 3m + 1 = 0$

$m^2 + 2m + 1 = 0$

**Paso 2:** $(m+1)^2 = 0 \Rightarrow m = -1$ (doble)

**Paso 3:** Raíz doble

**Solución:** $y = (C_1 + C_2\ln x)x^{-1} = \frac{C_1 + C_2\ln x}{x}$

---

## Método 5: Resolver PVI de Segundo Orden

### Pasos

1. **Encontrar solución general** $y = C_1 y_1 + C_2 y_2 + y_p$

2. **Aplicar condición inicial** $y(x_0) = y_0$

3. **Derivar** la solución general

4. **Aplicar segunda condición** $y'(x_0) = y_0'$

5. **Resolver sistema** de ecuaciones para $C_1$ y $C_2$

6. **Sustituir** valores en la solución general

### Ejemplo Paso a Paso

**Resolver:** $y'' - y = 0$, $y(0) = 2$, $y'(0) = -1$

**Paso 1:** $r^2 - 1 = 0 \Rightarrow r = \pm 1$
$$y = C_1 e^x + C_2 e^{-x}$$

**Paso 2:** $y(0) = C_1 + C_2 = 2$

**Paso 3:** $y' = C_1 e^x - C_2 e^{-x}$

**Paso 4:** $y'(0) = C_1 - C_2 = -1$

**Paso 5:** 
- $C_1 + C_2 = 2$
- $C_1 - C_2 = -1$

Sumando: $2C_1 = 1 \Rightarrow C_1 = \frac{1}{2}$

$C_2 = 2 - \frac{1}{2} = \frac{3}{2}$

**Solución:** $y = \frac{1}{2}e^x + \frac{3}{2}e^{-x}$

---

## Método 6: Identificar Tipo de Ecuación de Segundo Orden

```
┌─────────────────────────────────────────────────┐
│    ay'' + by' + cy = f(x)                       │
└─────────────────────────────────────────────────┘
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
   ¿f(x) = 0?              f(x) ≠ 0
        │                       │
        ▼                       ▼
   HOMOGÉNEA              NO HOMOGÉNEA
        │                       │
        │           ┌───────────┴───────────┐
        │           ▼                       ▼
        │    ¿f(x) es poli,         f(x) arbitraria
        │    exp, sin/cos?                  │
        │           │                       ▼
        │           ▼                  VARIACIÓN DE
        │     COEFICIENTES              PARÁMETROS
        │    INDETERMINADOS
        │
┌───────┴───────┐
▼               ▼
¿Coef.      ¿Forma ax²y'' + 
constantes?  bxy' + cy = 0?
    │               │
    ▼               ▼
ECUACIÓN      CAUCHY-EULER
CARACTERÍSTICA
```

---

## Método 7: Análisis de Oscilador Mecánico

**Ecuación:** $m\ddot{x} + c\dot{x} + kx = F_0\cos\omega t$

### Pasos

1. **Calcular parámetros:**
   - Frecuencia natural: $\omega_0 = \sqrt{k/m}$
   - Factor de amortiguamiento: $\zeta = \frac{c}{2\sqrt{mk}}$
   - Coeficiente: $\gamma = \frac{c}{2m}$

2. **Clasificar el sistema:**
   - $\zeta < 1$ (subamortiguado): oscila
   - $\zeta = 1$ (crítico): no oscila, más rápido
   - $\zeta > 1$ (sobreamortiguado): no oscila, lento

3. **Para subamortiguado, calcular:**
   - Frecuencia amortiguada: $\omega_d = \omega_0\sqrt{1-\zeta^2}$
   - Período: $T = \frac{2\pi}{\omega_d}$

4. **Solución homogénea:**
   - Sub: $x_h = e^{-\gamma t}(A\cos\omega_d t + B\sin\omega_d t)$
   - Crítico: $x_h = (A + Bt)e^{-\gamma t}$
   - Sobre: $x_h = Ae^{r_1 t} + Be^{r_2 t}$

5. **Solución particular** (respuesta forzada):
   $$x_p = \frac{F_0/m}{\sqrt{(\omega_0^2-\omega^2)^2 + (2\gamma\omega)^2}}\cos(\omega t - \phi)$$

### Ejemplo: Sistema Masa-Resorte

**Datos:** $m = 2$ kg, $c = 4$ N·s/m, $k = 10$ N/m

**Paso 1:**
- $\omega_0 = \sqrt{10/2} = \sqrt{5} \approx 2.24$ rad/s
- $\zeta = \frac{4}{2\sqrt{2 \cdot 10}} = \frac{4}{2\sqrt{20}} = \frac{4}{8.94} \approx 0.45$
- $\gamma = \frac{4}{4} = 1$ s⁻¹

**Paso 2:** $\zeta = 0.45 < 1$ → **Subamortiguado**

**Paso 3:**
- $\omega_d = \sqrt{5}\sqrt{1-0.2} = \sqrt{5 \cdot 0.8} = 2$ rad/s
- $T = \frac{2\pi}{2} = \pi \approx 3.14$ s

**Solución:** $x(t) = e^{-t}(A\cos 2t + B\sin 2t)$
