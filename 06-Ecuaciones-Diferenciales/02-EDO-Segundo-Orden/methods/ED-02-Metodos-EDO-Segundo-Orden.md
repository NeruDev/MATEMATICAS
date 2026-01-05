<!--
::METADATA::
type: method
status: active
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../glossary.md)

---

# Métodos: EDO de Segundo Orden

> **Referencia rápida:** Esta guía presenta 10 métodos sistemáticos para resolver [ecuaciones diferenciales](../../../glossary.md#ecuaciones-diferenciales) ordinarias lineales de segundo [orden](../../../glossary.md#orden).

---

## Índice de Métodos

| # | Método | Tipo de Ecuación | Complejidad |
|---|--------|------------------|-------------|
| 1 | [Homogénea Coef. Constantes](#método-2-coeficientes-indeterminados) | $ay'' + by' + cy = f(x)$ especial | ⭐⭐⭐ |
| 3 | [Variación de Parámetros](#método-4-ecuación-de-cauchy-euler) | $ax^2y'' + bxy' + cy = 0$ | ⭐⭐⭐ |
| 5 | [Reducción de Orden](../../../glossary.md#orden)) | Conocida una solución $y_1$ | ⭐⭐⭐ |
| 6 | [Operador Anulador](../../../glossary.md#polinomio), exp, trig | ⭐⭐⭐⭐ |
| 7 | [Superposición](#método-8-resolver-pvi-de-segundo-orden) | Con condiciones iniciales | ⭐⭐ |
| 9 | [Identificar Tipo](#método-10-análisis-de-oscilador-mecánico) | Aplicaciones físicas | ⭐⭐⭐ |

---

## Método 1: Resolver Ecuación Homogénea con Coeficientes Constantes

### Cuándo Usar

- Ecuación de la forma $ay'' + by' + cy = 0$
- Los coeficientes $a$, $b$, $c$ son constantes

### Fórmula

**Ecuación característica:** $ar^2 + br + c = 0$

**Solución según discriminante** $\Delta = b^2 - 4ac$:

| Caso | Raíces | [Solución General](../../../glossary.md#solucion-general) |
|------|--------|------------------|
| $\Delta > 0$ | $r_1, r_2$ reales distintas | $y = C_1 e^{r_1 x} + C_2 e^{r_2 x}$ |
| $\Delta = 0$ | $r$ real doble | $y = (C_1 + C_2 x)e^{rx}$ |
| $\Delta < 0$ | $\alpha \pm \beta i$ complejas | $y = e^{\alpha x}(C_1 \cos\beta x + C_2 \sin\beta x)$ |

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Escribir** | Ecuación característica $ar^2 + br + c = 0$ |
| 2 | **Calcular** | Discriminante $\Delta = b^2 - 4ac$ |
| 3 | **Resolver** | $r = \frac{-b \pm \sqrt{\Delta}}{2a}$ |
| 4 | **Clasificar** | Según signo de $\Delta$ |
| 5 | **Escribir solución** | Usar fórmula correspondiente |

### Ejemplo Detallado

**Problema:** Resolver $y'' + 6y' + 25y = 0$

---

**Paso 1: Ecuación característica**

$$r^2 + 6r + 25 = 0$$

---

**Paso 2: Calcular discriminante**

$$\Delta = 6^2 - 4(1)(25) = 36 - 100 = -64$$

---

**Paso 3: Resolver**

$$r = \frac{-6 \pm \sqrt{-64}}{2} = \frac{-6 \pm 8i}{2} = -3 \pm 4i$$

---

**Paso 4: Clasificar**

$\Delta < 0$ → Raíces complejas conjugadas

$\alpha = -3$, $\beta = 4$

---

**Paso 5: Escribir solución**

$$\boxed{y = e^{-3x}(C_1 \cos 4x + C_2 \sin 4x)}$$

---

**Verificación:** Sea $y = e^{-3x}\cos 4x$

$y' = -3e^{-3x}\cos 4x - 4e^{-3x}\sin 4x = e^{-3x}(-3\cos 4x - 4\sin 4x)$

$y'' = e^{-3x}(9\cos 4x + 12\sin 4x + 12\sin 4x - 16\cos 4x) = e^{-3x}(-7\cos 4x + 24\sin 4x)$

$y'' + 6y' + 25y = e^{-3x}[(-7 - 18 + 25)\cos 4x + (24 - 24)\sin 4x] = 0$ ✓

---

## Método 2: Coeficientes Indeterminados

### Cuándo Usar

- Ecuación $ay'' + by' + cy = f(x)$ donde $f(x)$ es:
  - [Polinomio](../../../glossary.md#polinomio)
  - Exponencial $e^{ax}$
  - [Seno](../../../glossary.md#seno)/[coseno](../../../glossary.md#coseno) $\sin bx$, $\cos bx$
  - Productos de los anteriores

### Tabla de Propuestas para $y_p$

| $f(x)$ | Propuesta para $y_p$ |
|--------|----------------------|
| $P_n(x)$ (polinomio grado $n$) | $A_n x^n + A_{n-1}x^{n-1} + \cdots + A_0$ |
| $e^{ax}$ | $Ae^{ax}$ |
| $\cos bx$ o $\sin bx$ | $A\cos bx + B\sin bx$ |
| $e^{ax}\cos bx$ o $e^{ax}\sin bx$ | $e^{ax}(A\cos bx + B\sin bx)$ |
| $x^n e^{ax}$ | $(A_n x^n + \cdots + A_0)e^{ax}$ |
| $x^n \cos bx$ | $(A_n x^n + \cdots + A_0)\cos bx + (B_n x^n + \cdots + B_0)\sin bx$ |

### Regla de Modificación (Duplicación)

Si la propuesta $y_p$ contiene términos de $y_h$:
- **Primera duplicación:** Multiplicar por $x$
- **Segunda duplicación:** Multiplicar por $x^2$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Resolver homogénea** | Obtener $y_h = C_1 y_1 + C_2 y_2$ |
| 2 | **Proponer** $y_p$ | Según tabla para $f(x)$ |
| 3 | **Verificar duplicación** | Si hay términos comunes con $y_h$, multiplicar por $x$ |
| 4 | **Calcular derivadas** | $y_p'$ y $y_p''$ |
| 5 | **Sustituir** | En la ecuación original |
| 6 | **Igualar coeficientes** | Resolver sistema para constantes |
| 7 | **Escribir solución** | $y = y_h + y_p$ |

### Ejemplo Detallado

**Problema:** Resolver $y'' - 4y = 8e^{2x} + 3x$

---

**Paso 1: Resolver [ecuación homogénea](../../../glossary.md#ecuacion-homogenea)**

$r^2 - 4 = 0 \implies r = \pm 2$

$$y_h = C_1 e^{2x} + C_2 e^{-2x}$$

---

**Paso 2: Proponer $y_p$**

Para $8e^{2x}$: proponer $Ae^{2x}$

Para $3x$: proponer $Bx + D$

Propuesta inicial: $y_p = Ae^{2x} + Bx + D$

---

**Paso 3: Verificar duplicación**

$e^{2x}$ está en $y_h$ → multiplicar por $x$

$$y_p = Axe^{2x} + Bx + D$$

---

**Paso 4: Calcular [derivadas](../../../glossary.md#derivadas)**

$y_p' = Ae^{2x} + 2Axe^{2x} + B = Ae^{2x}(1 + 2x) + B$

$y_p'' = 2Ae^{2x}(1 + 2x) + 2Ae^{2x} = Ae^{2x}(4 + 4x)$

---

**Paso 5: Sustituir en** $y'' - 4y = 8e^{2x} + 3x$

$Ae^{2x}(4 + 4x) - 4[Axe^{2x} + Bx + D] = 8e^{2x} + 3x$

$4Ae^{2x} + 4Axe^{2x} - 4Axe^{2x} - 4Bx - 4D = 8e^{2x} + 3x$

$4Ae^{2x} - 4Bx - 4D = 8e^{2x} + 3x$

---

**Paso 6: Igualar coeficientes**

| Término | Ecuación |
|---------|----------|
| $e^{2x}$ | $4A = 8 \implies A = 2$ |
| $x$ | $-4B = 3 \implies B = -\frac{3}{4}$ |
| Constante | $-4D = 0 \implies D = 0$ |

---

**Paso 7: Escribir [solución general](../../../glossary.md#solucion-general)**

$$y_p = 2xe^{2x} - \frac{3x}{4}$$

$$\boxed{y = C_1 e^{2x} + C_2 e^{-2x} + 2xe^{2x} - \frac{3x}{4}}$$

---

## Método 3: Variación de Parámetros

### Cuándo Usar

- Ecuación $y'' + P(x)y' + Q(x)y = f(x)$
- Funciona para cualquier $f(x)$ (no solo casos especiales)
- Cuando coeficientes indeterminados no aplica

### Fórmulas

**[Wronskiano](../../../glossary.md#wronskiano):**
$$W = \begin{vmatrix} y_1 & y_2 \\ y_1' & y_2' \end{vmatrix} = y_1 y_2' - y_2 y_1'$$

**Funciones auxiliares:**
$$u_1' = -\frac{y_2 f(x)}{W}, \quad u_2' = \frac{y_1 f(x)}{W}$$

**[Solución particular](../../../glossary.md#solucion-particular):**
$$y_p = u_1 y_1 + u_2 y_2$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Forma estándar** | Dividir para que coef. de $y''$ sea 1 |
| 2 | **Resolver homogénea** | Obtener $y_1$ y $y_2$ |
| 3 | **Calcular Wronskiano** | $W = y_1 y_2' - y_2 y_1'$ |
| 4 | **Calcular** $u_1'$ y $u_2'$ | Usar fórmulas |
| 5 | **Integrar** | Obtener $u_1$ y $u_2$ |
| 6 | **Formar** $y_p$ | $y_p = u_1 y_1 + u_2 y_2$ |
| 7 | **Solución general** | $y = y_h + y_p$ |

### Ejemplo Detallado

**Problema:** Resolver $y'' + y = \sec x$

---

**Paso 1: Ya está en forma estándar**

$P(x) = 0$, $Q(x) = 1$, $f(x) = \sec x$

---

**Paso 2: Resolver homogénea**

$r^2 + 1 = 0 \implies r = \pm i$

$$y_h = C_1 \cos x + C_2 \sin x$$

$y_1 = \cos x$, $y_2 = \sin x$

---

**Paso 3: Calcular [Wronskiano](../../../glossary.md#wronskiano)**

$$W = \begin{vmatrix} \cos x & \sin x \\ -\sin x & \cos x \end{vmatrix} = \cos^2 x + \sin^2 x = 1$$

---

**Paso 4: Calcular** $u_1'$ y $u_2'$

$$u_1' = -\frac{y_2 \cdot f(x)}{W} = -\frac{\sin x \cdot \sec x}{1} = -\frac{\sin x}{\cos x} = -\tan x$$

$$u_2' = \frac{y_1 \cdot f(x)}{W} = \frac{\cos x \cdot \sec x}{1} = 1$$

---

**Paso 5: Integrar**

$$u_1 = \int -\tan x\,dx = \ln|\cos x|$$

$$u_2 = \int 1\,dx = x$$

---

**Paso 6: Formar [solución particular](../../../glossary.md#solucion-particular)**

$$y_p = u_1 y_1 + u_2 y_2 = \ln|\cos x| \cdot \cos x + x \cdot \sin x$$

$$y_p = \cos x \ln|\cos x| + x\sin x$$

---

**Paso 7: Solución general**

$$\boxed{y = C_1 \cos x + C_2 \sin x + \cos x \ln|\cos x| + x\sin x}$$

---

**Verificación de** $y_p$:

$y_p' = -\sin x \ln|\cos x| + \cos x \cdot \frac{-\sin x}{\cos x} + \sin x + x\cos x$

$y_p' = -\sin x \ln|\cos x| - \sin x + \sin x + x\cos x = -\sin x \ln|\cos x| + x\cos x$

$y_p'' = -\cos x \ln|\cos x| + \sin x \tan x + \cos x - x\sin x$

$y_p'' + y_p = -\cos x \ln|\cos x| + \frac{\sin^2 x}{\cos x} + \cos x - x\sin x + \cos x \ln|\cos x| + x\sin x$

$= \frac{\sin^2 x}{\cos x} + \cos x = \frac{\sin^2 x + \cos^2 x}{\cos x} = \sec x$ ✓

---

## Método 4: Ecuación de Cauchy-Euler

### Cuándo Usar

- Forma: $ax^2y'' + bxy' + cy = 0$ (o $= f(x)$)
- Los coeficientes son potencias de $x$

### Fórmula

**[Sustitución](../../../glossary.md#sustitucion):** $y = x^m$ transforma en ecuación auxiliar:

$$am(m-1) + bm + c = 0 \implies am^2 + (b-a)m + c = 0$$

**Solución según raíces** (para $x > 0$):

| Caso | Raíces | Solución |
|------|--------|----------|
| Distintas reales | $m_1 \neq m_2$ | $y = C_1 x^{m_1} + C_2 x^{m_2}$ |
| Real doble | $m$ | $y = (C_1 + C_2 \ln x)x^m$ |
| Complejas | $\alpha \pm \beta i$ | $y = x^\alpha[C_1 \cos(\beta \ln x) + C_2 \sin(\beta \ln x)]$ |

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Identificar** | $a$, $b$, $c$ en $ax^2y'' + bxy' + cy = 0$ |
| 2 | **Ecuación auxiliar** | $am^2 + (b-a)m + c = 0$ |
| 3 | **Resolver** | Encontrar raíces $m_1$, $m_2$ |
| 4 | **Clasificar** | Según tipo de raíces |
| 5 | **Escribir solución** | Usar fórmula correspondiente |

### Ejemplo Detallado

**Problema:** Resolver $x^2y'' - xy' + 5y = 0$ para $x > 0$

---

**Paso 1: Identificar coeficientes**

$a = 1$, $b = -1$, $c = 5$

---

**Paso 2: Ecuación auxiliar**

$m(m-1) - m + 5 = 0$

$m^2 - m - m + 5 = 0$

$m^2 - 2m + 5 = 0$

---

**Paso 3: Resolver**

$$m = \frac{2 \pm \sqrt{4 - 20}}{2} = \frac{2 \pm \sqrt{-16}}{2} = \frac{2 \pm 4i}{2} = 1 \pm 2i$$

---

**Paso 4: Clasificar**

Raíces complejas: $\alpha = 1$, $\beta = 2$

---

**Paso 5: Escribir solución**

$$\boxed{y = x^1[C_1 \cos(2\ln x) + C_2 \sin(2\ln x)] = x[C_1 \cos(2\ln x) + C_2 \sin(2\ln x)]}$$

---

**Método alternativo: [Sustitución](../../../glossary.md#sustitucion)** $x = e^t$

$t = \ln x$, $\frac{dt}{dx} = \frac{1}{x}$

$\frac{dy}{dx} = \frac{dy}{dt} \cdot \frac{1}{x}$

$x\frac{dy}{dx} = \frac{dy}{dt}$

$x^2\frac{d^2y}{dx^2} = \frac{d^2y}{dt^2} - \frac{dy}{dt}$

La ecuación se transforma en:

$$\frac{d^2y}{dt^2} - \frac{dy}{dt} - \frac{dy}{dt} + 5y = 0$$

$$\frac{d^2y}{dt^2} - 2\frac{dy}{dt} + 5y = 0$$

Ecuación con coeficientes constantes, misma solución.

---

## Método 5: Reducción de Orden

### Cuándo Usar

- Se conoce una solución $y_1(x)$ de la homogénea
- Se busca la segunda solución independiente $y_2$

### Fórmula

**Segunda solución:**
$$y_2 = y_1 \int \frac{e^{-\int P(x)dx}}{y_1^2}\,dx$$

**O mediante sustitución** $y = y_1 v$:
$$y_1 v'' + (2y_1' + Py_1)v' = 0$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Forma estándar** | $y'' + P(x)y' + Q(x)y = 0$ |
| 2 | **Identificar** $y_1$ | Solución conocida |
| 3 | **Sustituir** | $y = y_1 v$, calcular $y'$, $y''$ |
| 4 | **Simplificar** | Obtener EDO en $v'$ (primer orden) |
| 5 | **Resolver** | Encontrar $v'$, luego $v$ |
| 6 | **Formar** $y_2$ | $y_2 = y_1 \cdot v$ |
| 7 | **Solución general** | $y = C_1 y_1 + C_2 y_2$ |

### Ejemplo Detallado

**Problema:** Resolver $x^2y'' + xy' - y = 0$, sabiendo que $y_1 = x$ es solución

---

**Paso 1: Verificar que** $y_1 = x$ **es solución**

$y_1 = x$, $y_1' = 1$, $y_1'' = 0$

$x^2(0) + x(1) - x = x - x = 0$ ✓

---

**Paso 2: Forma estándar** (dividir por $x^2$)

$$y'' + \frac{1}{x}y' - \frac{1}{x^2}y = 0$$

$P(x) = \frac{1}{x}$

---

**Paso 3: Sustituir** $y = xv$

$y' = v + xv'$

$y'' = v' + v' + xv'' = 2v' + xv''$

---

**Paso 4: Sustituir en la ecuación**

$x^2(2v' + xv'') + x(v + xv') - xv = 0$

$2x^2v' + x^3v'' + xv + x^2v' - xv = 0$

$x^3v'' + 3x^2v' = 0$

Dividir por $x^2$:

$xv'' + 3v' = 0$

---

**Paso 5: Sea** $w = v'$

$xw' + 3w = 0$

$\frac{dw}{w} = -\frac{3dx}{x}$

$\ln|w| = -3\ln|x| + C_1$

$w = \frac{A}{x^3}$

$v' = \frac{1}{x^3}$ (tomando $A = 1$)

$v = \int x^{-3}dx = -\frac{1}{2x^2}$

---

**Paso 6: Formar segunda solución**

$$y_2 = y_1 \cdot v = x \cdot \left(-\frac{1}{2x^2}\right) = -\frac{1}{2x}$$

Simplificando (ignorando constante): $y_2 = \frac{1}{x}$

---

**Paso 7: Solución general**

$$\boxed{y = C_1 x + C_2 \frac{1}{x}}$$

---

**Verificación de** $y_2 = x^{-1}$:

$y_2' = -x^{-2}$, $y_2'' = 2x^{-3}$

$x^2(2x^{-3}) + x(-x^{-2}) - x^{-1} = 2x^{-1} - x^{-1} - x^{-1} = 0$ ✓

---

## Método 6: Método del Operador Anulador

### Cuándo Usar

- Para encontrar la forma de $y_p$ sistemáticamente
- $f(x)$ es anulada por un operador diferencial con coeficientes constantes

### Tabla de Operadores Anuladores

| $f(x)$ | Operador Anulador |
|--------|-------------------|
| $x^n$ | $D^{n+1}$ |
| $e^{ax}$ | $D - a$ |
| $\cos bx$ o $\sin bx$ | $D^2 + b^2$ |
| $e^{ax}\cos bx$ o $e^{ax}\sin bx$ | $(D-a)^2 + b^2$ |
| $x^n e^{ax}$ | $(D-a)^{n+1}$ |

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Escribir** | Ecuación como $L[y] = f(x)$ donde $L = aD^2 + bD + c$ |
| 2 | **Encontrar anulador** | $A$ tal que $A[f(x)] = 0$ |
| 3 | **Aplicar** | $A \cdot L[y] = A[f(x)] = 0$ |
| 4 | **Resolver** | Ecuación homogénea de mayor orden |
| 5 | **Identificar** | Términos de $y_p$ (no en $y_h$ original) |
| 6 | **Determinar coeficientes** | Sustituir en ecuación original |

### Ejemplo Detallado

**Problema:** Resolver $y'' - 3y' + 2y = 4e^{2x}$

---

**Paso 1: Escribir operador**

$L = D^2 - 3D + 2$

$L[y] = 4e^{2x}$

---

**Paso 2: Anulador de** $f(x) = 4e^{2x}$

$A = D - 2$ (ya que $(D-2)[e^{2x}] = 0$)

---

**Paso 3: Aplicar anulador**

$(D-2)(D^2 - 3D + 2)[y] = 0$

$(D-2)(D-1)(D-2)[y] = 0$

$(D-2)^2(D-1)[y] = 0$

---

**Paso 4: Solución de la ecuación auxiliar**

$r = 2$ (doble), $r = 1$

Solución general: $y = C_1 e^x + C_2 e^{2x} + C_3 xe^{2x}$

---

**Paso 5: Identificar** $y_p$

$y_h$ original: $C_1 e^x + C_2 e^{2x}$

Términos nuevos: $xe^{2x}$

Por tanto: $y_p = Axe^{2x}$

---

**Paso 6: Determinar $A$**

$y_p = Axe^{2x}$

$y_p' = Ae^{2x}(1 + 2x)$

$y_p'' = Ae^{2x}(4 + 4x)$

Sustituyendo:

$Ae^{2x}(4 + 4x) - 3Ae^{2x}(1 + 2x) + 2Axe^{2x} = 4e^{2x}$

$Ae^{2x}[4 + 4x - 3 - 6x + 2x] = 4e^{2x}$

$Ae^{2x}[1] = 4e^{2x}$

$A = 4$

---

**Solución:**

$$\boxed{y = C_1 e^x + C_2 e^{2x} + 4xe^{2x}}$$

---

## Método 7: Principio de Superposición

### Cuándo Usar

- Cuando $f(x) = f_1(x) + f_2(x) + \cdots$
- Se resuelve cada parte por separado

### Fórmula

Si $y_{p_1}$ es solución particular de $L[y] = f_1(x)$
y $y_{p_2}$ es solución particular de $L[y] = f_2(x)$

Entonces $y_p = y_{p_1} + y_{p_2}$ es solución de $L[y] = f_1(x) + f_2(x)$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Descomponer** | $f(x) = f_1 + f_2 + \cdots$ |
| 2 | **Resolver cada** | $L[y] = f_i(x)$ por separado |
| 3 | **Sumar** | $y_p = y_{p_1} + y_{p_2} + \cdots$ |
| 4 | **Combinar** | $y = y_h + y_p$ |

### Ejemplo Detallado

**Problema:** Resolver $y'' - y = e^x + \cos x$

---

**Paso 1: Resolver homogénea**

$r^2 - 1 = 0 \implies r = \pm 1$

$y_h = C_1 e^x + C_2 e^{-x}$

---

**Paso 2: Resolver** $y'' - y = e^x$

Propuesta: $y_{p_1} = Axe^x$ (duplicación por $e^x$ en $y_h$)

$y_{p_1}' = Ae^x(1 + x)$

$y_{p_1}'' = Ae^x(2 + x)$

$Ae^x(2 + x) - Axe^x = e^x$

$2Ae^x = e^x \implies A = \frac{1}{2}$

$$y_{p_1} = \frac{1}{2}xe^x$$

---

**Paso 3: Resolver** $y'' - y = \cos x$

Propuesta: $y_{p_2} = B\cos x + C\sin x$

$y_{p_2}'' = -B\cos x - C\sin x$

$-B\cos x - C\sin x - B\cos x - C\sin x = \cos x$

$-2B\cos x - 2C\sin x = \cos x$

$B = -\frac{1}{2}$, $C = 0$

$$y_{p_2} = -\frac{1}{2}\cos x$$

---

**Paso 4: Combinar**

$$y_p = y_{p_1} + y_{p_2} = \frac{1}{2}xe^x - \frac{1}{2}\cos x$$

$$\boxed{y = C_1 e^x + C_2 e^{-x} + \frac{1}{2}xe^x - \frac{1}{2}\cos x}$$

---

## Método 8: Resolver PVI de Segundo Orden

### Cuándo Usar

- Ecuación con condiciones iniciales $y(x_0) = y_0$, $y'(x_0) = y_0'$
- Se busca solución única

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Resolver** | Ecuación general $y = C_1 y_1 + C_2 y_2 + y_p$ |
| 2 | **Derivar** | Obtener $y'$ |
| 3 | **Aplicar** $y(x_0) = y_0$ | Primera ecuación en $C_1$, $C_2$ |
| 4 | **Aplicar** $y'(x_0) = y_0'$ | Segunda ecuación |
| 5 | **Resolver sistema** | Encontrar $C_1$ y $C_2$ |
| 6 | **Escribir solución** | Sustituir valores |

### Ejemplo Detallado

**Problema:** Resolver $y'' + 4y = 0$, $y(0) = 1$, $y'(0) = 4$

---

**Paso 1: Resolver ecuación**

$r^2 + 4 = 0 \implies r = \pm 2i$

$$y = C_1 \cos 2x + C_2 \sin 2x$$

---

**Paso 2: Derivar**

$$y' = -2C_1 \sin 2x + 2C_2 \cos 2x$$

---

**Paso 3: Aplicar** $y(0) = 1$

$C_1 \cos 0 + C_2 \sin 0 = 1$

$C_1 = 1$

---

**Paso 4: Aplicar** $y'(0) = 4$

$-2C_1 \sin 0 + 2C_2 \cos 0 = 4$

$2C_2 = 4 \implies C_2 = 2$

---

**Paso 5: Escribir solución**

$$\boxed{y = \cos 2x + 2\sin 2x}$$

---

**Verificación:**

$y'' = -4\cos 2x - 8\sin 2x$

$y'' + 4y = -4\cos 2x - 8\sin 2x + 4\cos 2x + 8\sin 2x = 0$ ✓

$y(0) = 1 + 0 = 1$ ✓

$y'(0) = 0 + 4 = 4$ ✓

---

## Método 9: Identificar Tipo de Ecuación

### Diagrama de Clasificación

![Diagrama de clasificación de EDO de segundo orden](../media/generated/diagrama_clasificacion_edo_segundo_orden.svg)

*Figura: Clasificación jerárquica de ecuaciones diferenciales de segundo orden según tipo de coeficientes y término no homogéneo.*

### Tabla de Decisión Rápida

| Característica | Método |
|----------------|--------|
| $a, b, c$ constantes, $f(x) = 0$ | Ecuación característica |
| $ax^2, bx, c$ coeficientes, $f(x) = 0$ | Cauchy-Euler |
| $f(x)$ = polinomio, exp, sin/cos | Coeficientes indeterminados |
| $f(x)$ cualquier [función](../../../glossary.md#funcion) | Variación de parámetros |
| Conocida una solución $y_1$ | Reducción de orden |

---

## Método 10: Análisis de Oscilador Mecánico

### Cuándo Usar

- Problemas de vibración mecánica
- Circuitos RLC análogos
- Ecuación: $m\ddot{x} + c\dot{x} + kx = F(t)$

### Parámetros Fundamentales

| Parámetro | Fórmula | Significado |
|-----------|---------|-------------|
| Frecuencia natural | $\omega_0 = \sqrt{\frac{k}{m}}$ | Frecuencia sin amortiguamiento |
| Factor de amortiguamiento | $\zeta = \frac{c}{2\sqrt{km}}$ | Razón de amortiguamiento |
| Frecuencia amortiguada | $\omega_d = \omega_0\sqrt{1-\zeta^2}$ | Frecuencia real de oscilación |

### Clasificación del Sistema

| Condición | Tipo | Comportamiento |
|-----------|------|----------------|
| $\zeta < 1$ | Subamortiguado | Oscila con amplitud decreciente |
| $\zeta = 1$ | Críticamente amortiguado | Retorna sin oscilar (más rápido) |
| $\zeta > 1$ | Sobreamortiguado | Retorna sin oscilar (lento) |

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Identificar** | $m$, $c$, $k$, $F(t)$ |
| 2 | **Calcular** | $\omega_0$, $\zeta$, $\omega_d$ |
| 3 | **Clasificar** | Según valor de $\zeta$ |
| 4 | **Escribir** $x_h$ | Solución homogénea según caso |
| 5 | **Encontrar** $x_p$ | Si hay fuerza externa |
| 6 | **Aplicar CI** | Determinar constantes |

### Ejemplo Detallado

**Problema:** Un sistema masa-resorte tiene $m = 1$ kg, $k = 9$ N/m, $c = 4$ N·s/m. 
Desplazamiento inicial $x(0) = 2$ cm, velocidad inicial $\dot{x}(0) = 0$. Hallar $x(t)$.

---

**Paso 1: Ecuación del sistema**

$$\ddot{x} + 4\dot{x} + 9x = 0$$

---

**Paso 2: Calcular parámetros**

$\omega_0 = \sqrt{\frac{9}{1}} = 3$ rad/s

$\zeta = \frac{4}{2\sqrt{1 \cdot 9}} = \frac{4}{6} = \frac{2}{3} \approx 0.667$

$\omega_d = 3\sqrt{1 - \frac{4}{9}} = 3\sqrt{\frac{5}{9}} = \sqrt{5} \approx 2.236$ rad/s

---

**Paso 3: Clasificar**

$\zeta = 0.667 < 1$ → **Subamortiguado**

---

**Paso 4: Resolver ecuación característica**

$r^2 + 4r + 9 = 0$

$r = \frac{-4 \pm \sqrt{16 - 36}}{2} = \frac{-4 \pm \sqrt{-20}}{2} = -2 \pm \sqrt{5}i$

$$x_h = e^{-2t}(C_1 \cos\sqrt{5}t + C_2 \sin\sqrt{5}t)$$

---

**Paso 5: Aplicar condiciones iniciales**

$x(0) = C_1 = 0.02$ m (= 2 cm)

$\dot{x} = e^{-2t}[-2(C_1 \cos\sqrt{5}t + C_2 \sin\sqrt{5}t) + (-C_1\sqrt{5}\sin\sqrt{5}t + C_2\sqrt{5}\cos\sqrt{5}t)]$

$\dot{x}(0) = -2C_1 + C_2\sqrt{5} = 0$

$C_2 = \frac{2C_1}{\sqrt{5}} = \frac{0.04}{\sqrt{5}} = \frac{0.04\sqrt{5}}{5} \approx 0.0179$ m

---

**Paso 6: Solución final**

$$\boxed{x(t) = e^{-2t}\left(0.02\cos\sqrt{5}t + \frac{0.04}{\sqrt{5}}\sin\sqrt{5}t\right) \text{ m}}$$

**Forma alternativa (amplitud-fase):**

$A = \sqrt{C_1^2 + C_2^2} \approx 0.0268$ m

$\phi = \arctan\left(\frac{C_2}{C_1}\right) \approx 0.7297$ rad

$$x(t) = 0.0268 e^{-2t}\cos(\sqrt{5}t - 0.73) \text{ m}$$

---

## Tabla Resumen de Fórmulas

| Tipo | Ecuación | Solución |
|------|----------|----------|
| **Homogénea coef. const.** | $ar^2 + br + c = 0$ | Según discriminante |
| **Coef. indet.** | Ver tabla de propuestas | Verificar duplicación |
| **Variación parámetros** | $W = y_1y_2' - y_2y_1'$ | $y_p = u_1y_1 + u_2y_2$ |
| **Cauchy-Euler** | $am^2 + (b-a)m + c = 0$ | $y = x^m$ o variantes |
| **Reducción de orden** | Con $y_1$ conocida | $y_2 = y_1\int\frac{e^{-\int P\,dx}}{y_1^2}dx$ |

---

## Errores Comunes a Evitar

| Error | Consecuencia | Prevención |
|-------|--------------|------------|
| Olvidar modificar $y_p$ por duplicación | Coeficientes indeterminables | Siempre comparar $y_p$ con $y_h$ |
| Error de signo en ecuación característica | Raíces incorrectas | Verificar signos cuidadosamente |
| Wronskiano calculado mal | Integrales incorrectas | $W = y_1y_2' - y_2y_1'$ |
| No pasar a forma estándar | [Factor integrante](../../../glossary.md#factor-integrante) erróneo | Dividir por coef. de $y''$ |
| Confundir $\alpha$ y $\beta$ en raíces complejas | Solución mal formada | $r = \alpha \pm \beta i$, $\alpha$ = parte real |

---

## Problemas de Práctica Sugeridos

1. **Homogénea:** $y'' + 2y' + 5y = 0$
2. **Coef. indet.:** $y'' - 4y' + 3y = e^{3x} + x$
3. **Variación parámetros:** $y'' + y = \csc x$
4. **Cauchy-Euler:** $x^2y'' + 5xy' + 4y = 0$
5. **PVI:** $y'' - 2y' + y = 0$, $y(0) = 1$, $y'(0) = 0$
6. **Oscilador:** $\ddot{x} + 2\dot{x} + 5x = 10\cos t$

---

*Documento actualizado con formato expandido para estudio detallado.*
