<!--
::METADATA::
type: method
status: active
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../WIKI_INDEX.md) | [📚 Glosario](../../../glossary.md)

---

# Métodos: Series de Potencias para EDO

> **Referencia rápida:** Esta guía presenta 10 métodos sistemáticos para resolver [ecuaciones diferenciales](../../..](../../../glossary.md)#ecuaciones-diferenciales) usando series de potencias y el método de Frobenius.

---

## Índice de Métodos

| # | Método | Aplicación | Complejidad |
|---|--------|------------|-------------|
| 1 | [Punto Ordinario](#método-1-solución-en-punto-ordinario) | [EDO](../../../glossary.md#edo) en punto ordinario | ⭐⭐ |
| 2 | [Clasificar Puntos Singulares](#método-2-clasificar-puntos-singulares) | Identificar tipo de singularidad | ⭐⭐ |
| 3 | [Ecuación Indicial](#método-3-ecuación-indicial) | Frobenius - encontrar exponentes | ⭐⭐ |
| 4 | [Frobenius Caso 1](#método-4-frobenius-raíces-distintas-diferencia-no-entera) | $r_1 - r_2 \notin \mathbb{Z}$ | ⭐⭐⭐ |
| 5 | [Frobenius Caso 2](#método-5-frobenius-raíces-iguales) | $r_1 = r_2$ | ⭐⭐⭐⭐ |
| 6 | [Frobenius Caso 3](#método-6-frobenius-diferencia-entera) | $r_1 - r_2 \in \mathbb{Z}^+$ | ⭐⭐⭐⭐ |
| 7 | [Radio de Convergencia](#método-7-determinar-radio-de-[convergencia](../../../glossary.md#convergencia)) | Analizar convergencia | ⭐⭐ |
| 8 | [Ecuaciones Especiales](#método-8-identificar-ecuaciones-especiales) | Bessel, Legendre, etc. | ⭐⭐⭐ |
| 9 | [Ecuación de Bessel](#método-9-resolver-ecuación-de-bessel) | Problemas cilíndricos | ⭐⭐⭐⭐ |
| 10 | [Ecuación de Legendre](#método-10-resolver-ecuación-de-legendre) | Problemas esféricos | ⭐⭐⭐⭐ |

---

## Conceptos Fundamentales

### Definiciones Clave

| Concepto | Definición |
|----------|------------|
| **Punto Ordinario** | $x_0$ donde $P(x)$ y $Q(x)$ son analíticas en $y'' + P(x)y' + Q(x)y = 0$ |
| **Punto Singular** | $x_0$ donde $P$ o $Q$ no son analíticas |
| **Singular Regular** | $x_0$ donde $(x-x_0)P$ y $(x-x_0)^2Q$ son analíticas |
| **Singular Irregular** | Punto singular que no es regular |

### Serie de Potencias en $x_0$

$$y = \sum_{n=0}^{\infty} c_n (x - x_0)^n$$

### Serie de Frobenius en $x_0$

$$y = (x-x_0)^r \sum_{n=0}^{\infty} c_n (x-x_0)^n = \sum_{n=0}^{\infty} c_n (x-x_0)^{n+r}$$

---

## Método 1: Solución en Punto Ordinario

### Cuándo Usar

- La [EDO](../../..](../../../glossary.md)#edo) es $y'' + P(x)y' + Q(x)y = 0$
- El punto $x_0$ es ordinario (P y Q analíticas en $x_0$)
- Para mayor simplicidad, usualmente $x_0 = 0$

### Fórmulas de Derivadas

$$y = \sum_{n=0}^{\infty} c_n x^n$$

$$y' = \sum_{n=1}^{\infty} n c_n x^{n-1} = \sum_{n=0}^{\infty} (n+1) c_{n+1} x^n$$

$$y'' = \sum_{n=2}^{\infty} n(n-1) c_n x^{n-2} = \sum_{n=0}^{\infty} (n+2)(n+1) c_{n+2} x^n$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Verificar** | Que $x_0$ es punto ordinario |
| 2 | **Suponer** | $y = \sum c_n x^n$ |
| 3 | **Calcular** | $y'$ y $y''$ |
| 4 | **Sustituir** | En la EDO |
| 5 | **Reindexar** | Unificar potencias de $x$ |
| 6 | **Igualar coeficientes** | Cada potencia = 0 |
| 7 | **Obtener recurrencia** | Fórmula para $c_{n+2}$ |
| 8 | **Calcular coeficientes** | $c_0$ y $c_1$ libres |
| 9 | **Escribir solución** | Dos series independientes |

### Ejemplo Detallado

**Problema:** Resolver $y'' - xy' - y = 0$ en $x = 0$

---

**Paso 1: Verificar punto ordinario**

EDO: $y'' - xy' - y = 0$

$P(x) = -x$, $Q(x) = -1$

Ambas analíticas en $x = 0$ ✓ Punto ordinario

---

**Paso 2-3: Suponer serie y [derivadas](../../..](../../../glossary.md)#derivadas)**

$$y = \sum_{n=0}^{\infty} c_n x^n$$

$$y' = \sum_{n=1}^{\infty} n c_n x^{n-1}$$

$$y'' = \sum_{n=2}^{\infty} n(n-1) c_n x^{n-2}$$

---

**Paso 4: Sustituir en la EDO**

$$\sum_{n=2}^{\infty} n(n-1) c_n x^{n-2} - x\sum_{n=1}^{\infty} n c_n x^{n-1} - \sum_{n=0}^{\infty} c_n x^n = 0$$

$$\sum_{n=2}^{\infty} n(n-1) c_n x^{n-2} - \sum_{n=1}^{\infty} n c_n x^{n} - \sum_{n=0}^{\infty} c_n x^n = 0$$

---

**Paso 5: Reindexar**

Para $y''$: sea $k = n-2$, entonces $n = k+2$:

$$\sum_{k=0}^{\infty} (k+2)(k+1) c_{k+2} x^{k}$$

Renombrando $k \to n$:

$$\sum_{n=0}^{\infty} (n+2)(n+1) c_{n+2} x^{n} - \sum_{n=1}^{\infty} n c_n x^{n} - \sum_{n=0}^{\infty} c_n x^n = 0$$

---

**Paso 6: Separar término $n=0$ y combinar**

Término $n=0$: $(2)(1)c_2 - c_0 = 0 \Rightarrow c_2 = \frac{c_0}{2}$

Para $n \geq 1$:

$$(n+2)(n+1)c_{n+2} - nc_n - c_n = 0$$

$$(n+2)(n+1)c_{n+2} - (n+1)c_n = 0$$

---

**Paso 7: Obtener recurrencia**

$$c_{n+2} = \frac{(n+1)c_n}{(n+2)(n+1)} = \frac{c_n}{n+2}$$

---

**Paso 8: Calcular coeficientes**

**Términos pares** (de $c_0$):
- $c_2 = \frac{c_0}{2}$
- $c_4 = \frac{c_2}{4} = \frac{c_0}{2 \cdot 4} = \frac{c_0}{8}$
- $c_6 = \frac{c_4}{6} = \frac{c_0}{8 \cdot 6} = \frac{c_0}{48}$

**Términos impares** (de $c_1$):
- $c_3 = \frac{c_1}{3}$
- $c_5 = \frac{c_3}{5} = \frac{c_1}{15}$
- $c_7 = \frac{c_5}{7} = \frac{c_1}{105}$

---

**Paso 9: Escribir solución**

$$y_1 = c_0\left(1 + \frac{x^2}{2} + \frac{x^4}{8} + \frac{x^6}{48} + \cdots\right)$$

$$y_2 = c_1\left(x + \frac{x^3}{3} + \frac{x^5}{15} + \frac{x^7}{105} + \cdots\right)$$

$$\boxed{y = c_0 y_1(x) + c_1 y_2(x)}$$

---

## Método 2: Clasificar Puntos Singulares

### Cuándo Usar

- Para determinar si usar series de potencias o Frobenius
- Para identificar puntos singulares de la EDO

### Criterio de Clasificación

Para $y'' + P(x)y' + Q(x)y = 0$ en el punto $x = x_0$:

| Prueba | Resultado |
|--------|-----------|
| $P$ y $Q$ analíticas en $x_0$ | **Punto Ordinario** |
| $(x-x_0)P$ y $(x-x_0)^2Q$ analíticas | **Singular Regular** |
| De otro modo | **Singular Irregular** |

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Escribir** | EDO en forma estándar $y'' + Py' + Qy = 0$ |
| 2 | **Identificar** | $P(x)$ y $Q(x)$ |
| 3 | **Buscar singularidades** | Puntos donde $P$ o $Q$ no están definidas |
| 4 | **Para cada punto singular** | Verificar si $(x-x_0)P$ y $(x-x_0)^2Q$ son analíticas |
| 5 | **Clasificar** | Regular o irregular |

### Ejemplo Detallado

**Problema:** Clasificar los puntos singulares de $x^2(x-1)y'' + 2xy' + (x-1)y = 0$

---

**Paso 1: Forma estándar**

$$y'' + \frac{2x}{x^2(x-1)}y' + \frac{x-1}{x^2(x-1)}y = 0$$

$$y'' + \frac{2}{x(x-1)}y' + \frac{1}{x^2}y = 0$$

---

**Paso 2: Identificar**

$$P(x) = \frac{2}{x(x-1)}, \quad Q(x) = \frac{1}{x^2}$$

---

**Paso 3: Puntos singulares**

$P$ singular en $x = 0$ y $x = 1$

$Q$ singular en $x = 0$

**Puntos singulares:** $x = 0$ y $x = 1$

---

**Paso 4: Clasificar $x = 0$**

$(x-0)P(x) = xP(x) = \frac{2}{x-1}$ ✓ Analítica en $x = 0$

$(x-0)^2Q(x) = x^2 Q(x) = 1$ ✓ Analítica en $x = 0$

**$x = 0$: Singular Regular** ✓

---

**Paso 5: Clasificar $x = 1$**

$(x-1)P(x) = \frac{2(x-1)}{x(x-1)} = \frac{2}{x}$ ✓ Analítica en $x = 1$

$(x-1)^2Q(x) = \frac{(x-1)^2}{x^2}$ ✓ Analítica en $x = 1$

**$x = 1$: Singular Regular** ✓

$$\boxed{\text{Ambos puntos singulares son regulares}}$$

---

## Método 3: Ecuación Indicial

### Cuándo Usar

- En punto singular regular
- Para encontrar los exponentes $r$ de la serie de Frobenius

### Forma Estándar

Para $x^2y'' + xp(x)y' + q(x)y = 0$ con $p(x)$ y $q(x)$ analíticas en $x = 0$:

$$p(x) = p_0 + p_1 x + p_2 x^2 + \cdots$$
$$q(x) = q_0 + q_1 x + q_2 x^2 + \cdots$$

### Ecuación Indicial

$$r(r-1) + p_0 r + q_0 = 0$$

O equivalentemente:

$$r^2 + (p_0 - 1)r + q_0 = 0$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Multiplicar** | Por $x^2$ para obtener forma $x^2y'' + xp(x)y' + q(x)y = 0$ |
| 2 | **Identificar** | $p(x)$ y $q(x)$ |
| 3 | **Evaluar** | $p_0 = p(0)$, $q_0 = q(0)$ |
| 4 | **Formar ecuación** | $r(r-1) + p_0 r + q_0 = 0$ |
| 5 | **Resolver** | Para $r_1$ y $r_2$ ($r_1 \geq r_2$) |
| 6 | **Clasificar caso** | Según $r_1 - r_2$ |

### Ejemplo Detallado

**Problema:** Encontrar la ecuación indicial de $2x^2y'' + xy' - (x+1)y = 0$

---

**Paso 1: Ya está en forma correcta**

$2x^2y'' + xy' - (x+1)y = 0$

Dividir por 2:

$x^2y'' + \frac{x}{2}y' - \frac{(x+1)}{2}y = 0$

---

**Paso 2: Identificar**

$xp(x) = \frac{x}{2} \Rightarrow p(x) = \frac{1}{2}$

$q(x) = -\frac{x+1}{2}$

---

**Paso 3: Evaluar en $x = 0$**

$p_0 = \frac{1}{2}$

$q_0 = -\frac{0+1}{2} = -\frac{1}{2}$

---

**Paso 4: Ecuación indicial**

$$r(r-1) + \frac{1}{2}r - \frac{1}{2} = 0$$

$$r^2 - r + \frac{1}{2}r - \frac{1}{2} = 0$$

$$r^2 - \frac{1}{2}r - \frac{1}{2} = 0$$

Multiplicar por 2:

$$2r^2 - r - 1 = 0$$

---

**Paso 5: Resolver**

$(2r+1)(r-1) = 0$

$$r_1 = 1, \quad r_2 = -\frac{1}{2}$$

---

**Paso 6: Clasificar**

$$r_1 - r_2 = 1 - (-\frac{1}{2}) = \frac{3}{2} \notin \mathbb{Z}$$

$$\boxed{\text{Caso 1: Dos soluciones de Frobenius independientes}}$$

---

## Método 4: Frobenius - Raíces Distintas (Diferencia No Entera)

### Cuándo Usar

- Punto singular regular
- $r_1 - r_2 \notin \mathbb{Z}$ (diferencia no es entero)

### Forma de las Soluciones

$$y_1 = x^{r_1} \sum_{n=0}^{\infty} a_n x^n = x^{r_1}(a_0 + a_1 x + a_2 x^2 + \cdots)$$

$$y_2 = x^{r_2} \sum_{n=0}^{\infty} b_n x^n = x^{r_2}(b_0 + b_1 x + b_2 x^2 + \cdots)$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Sustituir** | $y = x^r \sum c_n x^n$ en la EDO |
| 2 | **Calcular derivadas** | $y'$, $y''$ |
| 3 | **Agrupar** | Por potencias de $x$ |
| 4 | **Extraer potencia menor** | Da ecuación indicial |
| 5 | **Para $r = r_1$** | Encontrar recurrencia y coeficientes |
| 6 | **Repetir con $r = r_2$** | Segunda solución |

### Ejemplo Detallado

**Problema:** Resolver $2xy'' + y' + y = 0$ cerca de $x = 0$

---

**Paso 1: Ecuación indicial**

Multiplicar por $x$: $2x^2y'' + xy' + xy = 0$

$p(x) = 1$, $q(x) = x$

$p_0 = 1$, $q_0 = 0$

Ecuación indicial: $r(r-1) + r = 0 \Rightarrow r^2 = 0$

¡Espera! Esto da $r_1 = r_2 = 0$. 

Verifiquemos la forma original: $2xy'' + y' + y = 0$

Forma estándar: $y'' + \frac{1}{2x}y' + \frac{1}{2x}y = 0$

$P = \frac{1}{2x}$, $Q = \frac{1}{2x}$

$xP = \frac{1}{2}$ → $p_0 = \frac{1}{2}$

$x^2Q = \frac{x}{2}$ → $q_0 = 0$

Ecuación indicial: $r(r-1) + \frac{1}{2}r + 0 = 0$

$r^2 - r + \frac{r}{2} = r^2 - \frac{r}{2} = r(r - \frac{1}{2}) = 0$

$$r_1 = \frac{1}{2}, \quad r_2 = 0$$

$r_1 - r_2 = \frac{1}{2} \notin \mathbb{Z}$ → **Caso 1** ✓

---

**Paso 2: Para $r = \frac{1}{2}$**

$y = \sum_{n=0}^{\infty} c_n x^{n+1/2}$

$y' = \sum_{n=0}^{\infty} (n+\frac{1}{2}) c_n x^{n-1/2}$

$y'' = \sum_{n=0}^{\infty} (n+\frac{1}{2})(n-\frac{1}{2}) c_n x^{n-3/2}$

---

**Paso 3: Sustituir**

$2xy'' + y' + y = 0$

$2\sum(n+\frac{1}{2})(n-\frac{1}{2}) c_n x^{n-1/2} + \sum(n+\frac{1}{2}) c_n x^{n-1/2} + \sum c_n x^{n+1/2} = 0$

---

**Paso 4: Combinar términos con misma potencia**

Para $x^{n-1/2}$: $2(n+\frac{1}{2})(n-\frac{1}{2})c_n + (n+\frac{1}{2})c_n$

Para $x^{n+1/2}$: $c_n$ (que corresponde a $x^{m-1/2}$ con $m = n+1$, es decir $c_{n-1}$)

$n = 0$: $[2(\frac{1}{2})(-\frac{1}{2}) + \frac{1}{2}]c_0 = [-\frac{1}{2} + \frac{1}{2}]c_0 = 0$ ✓

$n \geq 1$: $(n+\frac{1}{2})[2n-1+1]c_n + c_{n-1} = 0$

$(n+\frac{1}{2})(2n)c_n = -c_{n-1}$

**Recurrencia:** $c_n = \frac{-c_{n-1}}{n(2n+1)}$

---

**Paso 5: Calcular coeficientes**

$c_1 = \frac{-c_0}{1 \cdot 3} = \frac{-c_0}{3}$

$c_2 = \frac{-c_1}{2 \cdot 5} = \frac{c_0}{30}$

$c_3 = \frac{-c_2}{3 \cdot 7} = \frac{-c_0}{630}$

$$y_1 = x^{1/2}\left(1 - \frac{x}{3} + \frac{x^2}{30} - \frac{x^3}{630} + \cdots\right)$$

---

**Paso 6: Para $r = 0$** (procedimiento análogo)

Recurrencia: $c_n = \frac{-c_{n-1}}{n(2n-1)}$

$c_1 = \frac{-c_0}{1 \cdot 1} = -c_0$

$c_2 = \frac{-c_1}{2 \cdot 3} = \frac{c_0}{6}$

$c_3 = \frac{-c_2}{3 \cdot 5} = \frac{-c_0}{90}$

$$y_2 = 1 - x + \frac{x^2}{6} - \frac{x^3}{90} + \cdots$$

---

$$\boxed{y = C_1 x^{1/2}\left(1 - \frac{x}{3} + \frac{x^2}{30} - \cdots\right) + C_2\left(1 - x + \frac{x^2}{6} - \cdots\right)}$$

---

## Método 5: Frobenius - Raíces Iguales

### Cuándo Usar

- Punto singular regular
- $r_1 = r_2 = r$

### Forma de las Soluciones

$$y_1 = x^r \sum_{n=0}^{\infty} a_n x^n$$

$$y_2 = y_1 \ln x + x^r \sum_{n=1}^{\infty} b_n x^n$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Encontrar** $y_1$ | Con $r = r_1$ |
| 2 | **Para** $y_2$ | Usar reducción de orden |
| 3 | **Suponer** | $y_2 = v(x) y_1$ |
| 4 | **Sustituir** | En la EDO original |
| 5 | **Resolver** | Para $v'$ |
| 6 | **Integrar** | Obtener $v$ |
| 7 | **Formar** | $y_2 = v \cdot y_1$ |

### Fórmula de Reducción de Orden

Para $y'' + P(x)y' + Q(x)y = 0$:

$$v = \int \frac{e^{-\int P\,dx}}{y_1^2}\,dx$$

$$y_2 = y_1 \int \frac{e^{-\int P\,dx}}{y_1^2}\,dx$$

### Ejemplo Detallado

**Problema:** Resolver $x^2y'' + 3xy' + y = 0$ cerca de $x = 0$

---

**Paso 1: Ecuación indicial**

$p(x) = 3$, $q(x) = 1$

$p_0 = 3$, $q_0 = 1$

$$r(r-1) + 3r + 1 = 0$$
$$r^2 + 2r + 1 = (r+1)^2 = 0$$

$r_1 = r_2 = -1$ → **Caso 2**

---

**Paso 2: Encontrar** $y_1$

$y = x^{-1}\sum c_n x^n = \sum c_n x^{n-1}$

$y' = \sum (n-1)c_n x^{n-2}$

$y'' = \sum (n-1)(n-2)c_n x^{n-3}$

Sustituyendo en $x^2y'' + 3xy' + y = 0$:

$\sum (n-1)(n-2)c_n x^{n-1} + 3\sum (n-1)c_n x^{n-1} + \sum c_n x^{n-1} = 0$

$\sum [(n-1)(n-2) + 3(n-1) + 1]c_n x^{n-1} = 0$

$(n-1)(n-2) + 3(n-1) + 1 = (n-1)[(n-2)+3] + 1 = (n-1)(n+1) + 1 = n^2 - 1 + 1 = n^2$

$\sum n^2 c_n x^{n-1} = 0$

Para $n \geq 1$: $n^2 c_n = 0 \Rightarrow c_n = 0$ para $n \geq 1$

$c_0$ libre

$$y_1 = \frac{c_0}{x} = \frac{1}{x}$$

---

**Paso 3: Encontrar** $y_2$ **por reducción de [orden](../../..](../../../glossary.md)#orden)**

$y'' + \frac{3}{x}y' + \frac{1}{x^2}y = 0$

$P(x) = \frac{3}{x}$

$$v = \int \frac{e^{-\int \frac{3}{x}dx}}{y_1^2}dx = \int \frac{e^{-3\ln x}}{1/x^2}dx = \int \frac{x^{-3}}{x^{-2}}dx = \int x^{-1}dx = \ln x$$

$$y_2 = y_1 \cdot v = \frac{\ln x}{x}$$

---

$$\boxed{y = \frac{C_1}{x} + \frac{C_2 \ln x}{x} = \frac{C_1 + C_2 \ln x}{x}}$$

---

## Método 6: Frobenius - Diferencia Entera

### Cuándo Usar

- Punto singular regular
- $r_1 - r_2 = N$ donde $N \in \mathbb{Z}^+$ (entero positivo)

### Dos Subcasos

**Subcaso 3a:** La segunda serie con $r_2$ funciona normalmente

$$y_2 = x^{r_2}\sum b_n x^n$$

**Subcaso 3b:** La serie con $r_2$ falla (coeficiente infinito)

$$y_2 = Cy_1 \ln x + x^{r_2}\sum b_n x^n$$

donde $C$ puede ser cero o no cero.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Encontrar** $y_1$ | Con $r = r_1$ (raíz mayor) |
| 2 | **Intentar** $r = r_2$ | Buscar recurrencia |
| 3 | **Verificar** | Si aparece división por cero |
| 4 | **Si no hay problema** | $y_2$ es serie ordinaria (subcaso 3a) |
| 5 | **Si hay problema** | Usar forma con $\ln x$ (subcaso 3b) |

### Ejemplo Detallado (Subcaso 3a)

**Problema:** Resolver $xy'' + y = 0$

---

**Paso 1: Ecuación indicial**

Forma: $x^2y'' + xy \cdot 0 + xy = 0$ → No es forma estándar

Forma estándar: $y'' + 0 \cdot y' + \frac{1}{x}y = 0$

$xP = 0$ → $p_0 = 0$

$x^2 Q = x$ → $q_0 = 0$

$r(r-1) + 0 + 0 = 0 \Rightarrow r(r-1) = 0$

$r_1 = 1$, $r_2 = 0$

$r_1 - r_2 = 1 \in \mathbb{Z}^+$ → **Caso 3**

---

**Paso 2: Encontrar** $y_1$ **con** $r = 1$

$y = x\sum c_n x^n = \sum c_n x^{n+1}$

$y'' = \sum (n+1)n \cdot c_n x^{n-1}$

$xy'' + y = \sum (n+1)n c_n x^n + \sum c_n x^{n+1} = 0$

Reindexando la segunda suma ($m = n+1$):

$\sum (n+1)n c_n x^n + \sum c_{n-1} x^n = 0$ (para $n \geq 1$)

$n = 0$: $(1)(0)c_0 = 0$ ✓ ($c_0$ libre)

$n \geq 1$: $(n+1)n c_n + c_{n-1} = 0$

$c_n = \frac{-c_{n-1}}{n(n+1)}$

$c_1 = \frac{-c_0}{2}$, $c_2 = \frac{c_0}{12}$, $c_3 = \frac{-c_0}{144}$

$$y_1 = x\left(1 - \frac{x}{2} + \frac{x^2}{12} - \frac{x^3}{144} + \cdots\right)$$

---

**Paso 3: Intentar** $r = 0$

$y = \sum c_n x^n$

$y'' = \sum (n)(n-1)c_n x^{n-2}$

$xy'' + y = \sum n(n-1)c_n x^{n-1} + \sum c_n x^n = 0$

Reindexando ($k = n-1$ en primera suma):

$\sum (k+1)k c_{k+1} x^k + \sum c_n x^n = 0$

$k = 0$: $(1)(0)c_1 + c_0 = c_0 = 0$

¡$c_0 = 0$ forzado! Pero $c_1$ es libre.

$k = 1$: $2 \cdot 1 \cdot c_2 + c_1 = 0 \Rightarrow c_2 = -\frac{c_1}{2}$

$k \geq 1$: $(k+1)k c_{k+1} + c_k = 0$

$c_{k+1} = \frac{-c_k}{k(k+1)}$ para $k \geq 1$

La serie con $r = 0$ y $c_0 = 0$, $c_1$ libre es:

$$y_2 = c_1\left(x - \frac{x^2}{2} + \frac{x^3}{12} - \cdots\right)$$

¡Esto es $y_1$! No obtenemos solución nueva.

---

**Paso 4: Usar reducción de [orden](../../..](../../../glossary.md)#orden)**

$P(x) = 0$ en $y'' + 0 \cdot y' + \frac{1}{x}y = 0$

$$v = \int \frac{e^0}{y_1^2}dx = \int \frac{1}{y_1^2}dx$$

Con $y_1 \approx x$ para $x$ pequeño:

$$y_2 = y_1 \int \frac{dx}{y_1^2}$$

Esto genera logaritmos en la solución.

$$\boxed{y = C_1 y_1(x) + C_2 y_2(x) \text{ (donde } y_2 \text{ contiene } \ln x \text{)}}$$

---

## Método 7: Determinar Radio de Convergencia

### Cuándo Usar

- Para conocer el intervalo donde converge la serie
- Antes de usar la solución numéricamente

### Teorema Principal

El radio de [convergencia](../../..](../../../glossary.md)#convergencia) de la serie de potencias centrada en $x_0$ es **al menos** igual a la distancia de $x_0$ al punto singular más cercano.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Identificar** | Todos los puntos singulares |
| 2 | **Calcular distancias** | Desde el centro $x_0$ |
| 3 | **Tomar mínimo** | $R \geq$ distancia mínima |

### Ejemplo Detallado

**Problema:** Determinar el radio de convergencia para $y'' + \frac{1}{x^2-4}y = 0$ centrada en $x_0 = 0$

---

**Paso 1: Puntos singulares**

$Q(x) = \frac{1}{x^2-4} = \frac{1}{(x-2)(x+2)}$

Singularidades: $x = 2$ y $x = -2$

---

**Paso 2: Distancias desde** $x_0 = 0$

$|0 - 2| = 2$

$|0 - (-2)| = 2$

---

**Paso 3: Radio de convergencia**

$$\boxed{R \geq 2}$$

---

### Ejemplo con Singularidades Complejas

**Para:** $(1+x^2)y'' + 2xy' + y = 0$

$P = \frac{2x}{1+x^2}$, $Q = \frac{1}{1+x^2}$

Singularidades: $1 + x^2 = 0 \Rightarrow x = \pm i$

Distancia desde $x = 0$: $|i| = 1$

$$\boxed{R \geq 1}$$

---

## Método 8: Identificar Ecuaciones Especiales

### Cuándo Usar

- La EDO tiene una forma reconocible
- Para usar soluciones tabuladas

### Tabla de Ecuaciones Especiales

| Ecuación | Forma Estándar | Soluciones |
|----------|---------------|------------|
| **Bessel** | $x^2y'' + xy' + (x^2 - \nu^2)y = 0$ | $J_\nu(x)$, $Y_\nu(x)$ |
| **Legendre** | $(1-x^2)y'' - 2xy' + n(n+1)y = 0$ | $P_n(x)$, $Q_n(x)$ |
| **Hermite** | $y'' - 2xy' + 2ny = 0$ | $H_n(x)$ |
| **Laguerre** | $xy'' + (1-x)y' + ny = 0$ | $L_n(x)$ |
| **Chebyshev** | $(1-x^2)y'' - xy' + n^2y = 0$ | $T_n(x)$, $U_n(x)$ |
| **Airy** | $y'' - xy = 0$ | $\text{Ai}(x)$, $\text{Bi}(x)$ |

### Algoritmo de Reconocimiento

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Comparar** | Coeficientes con formas estándar |
| 2 | **Identificar parámetro** | $\nu$, $n$, etc. |
| 3 | **Consultar** | Propiedades de las funciones especiales |

### Ejemplo

**Problema:** Identificar $x^2y'' + xy' + (x^2 - 9)y = 0$

Comparando con Bessel: $x^2y'' + xy' + (x^2 - \nu^2)y = 0$

$\nu^2 = 9 \Rightarrow \nu = 3$

$$\boxed{\text{Ecuación de Bessel con } \nu = 3}$$

**[Solución general](../../..](../../../glossary.md)#solucion-general):** $y = C_1 J_3(x) + C_2 Y_3(x)$

---

## Método 9: Resolver Ecuación de Bessel

### Cuándo Usar

- Problemas con simetría cilíndrica
- Vibraciones de membranas circulares
- Conducción de calor en cilindros

### Ecuación de Bessel de Orden $\nu$

$$x^2y'' + xy' + (x^2 - \nu^2)y = 0$$

### Soluciones

**[Función](../../..](../../../glossary.md)#funcion) de Bessel de primera clase:**

$$J_\nu(x) = \sum_{m=0}^{\infty} \frac{(-1)^m}{m!\,\Gamma(m+\nu+1)}\left(\frac{x}{2}\right)^{2m+\nu}$$

**Para $\nu = 0$:**

$$J_0(x) = 1 - \frac{x^2}{4} + \frac{x^4}{64} - \frac{x^6}{2304} + \cdots = \sum_{m=0}^{\infty} \frac{(-1)^m x^{2m}}{2^{2m}(m!)^2}$$

**Para $\nu = 1$:**

$$J_1(x) = \frac{x}{2} - \frac{x^3}{16} + \frac{x^5}{384} - \cdots$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Identificar** $\nu$ | De la ecuación |
| 2 | **Si** $\nu \notin \mathbb{Z}$ | $y = C_1 J_\nu + C_2 J_{-\nu}$ |
| 3 | **Si** $\nu \in \mathbb{Z}$ | $y = C_1 J_\nu + C_2 Y_\nu$ |
| 4 | **Aplicar CI** | Para encontrar constantes |

### Ejemplo Detallado

**Problema:** Resolver $x^2y'' + xy' + (x^2 - 4)y = 0$

---

**Paso 1: Identificar orden**

$\nu^2 = 4 \Rightarrow \nu = 2$ (entero)

---

**Paso 2: [Solución general](../../..](../../../glossary.md)#solucion-general)**

$$\boxed{y = C_1 J_2(x) + C_2 Y_2(x)}$$

donde:

$$J_2(x) = \sum_{m=0}^{\infty} \frac{(-1)^m}{m!(m+2)!}\left(\frac{x}{2}\right)^{2m+2}$$

$$= \frac{x^2}{8} - \frac{x^4}{96} + \frac{x^6}{3072} - \cdots$$

---

### Propiedades Útiles

| Propiedad | Fórmula |
|-----------|---------|
| Recurrencia | $J_{\nu-1}(x) + J_{\nu+1}(x) = \frac{2\nu}{x}J_\nu(x)$ |
| [Derivada](../../../glossary.md#derivada) | $J'_\nu(x) = \frac{1}{2}[J_{\nu-1}(x) - J_{\nu+1}(x)]$ |
| Ceros | $J_0$ tiene ceros en $x \approx 2.405, 5.520, 8.654, \ldots$ |

---

## Método 10: Resolver Ecuación de Legendre

### Cuándo Usar

- Problemas con simetría esférica
- Potencial en coordenadas esféricas
- Armónicos esféricos

### Ecuación de Legendre

$$(1-x^2)y'' - 2xy' + n(n+1)y = 0$$

### Soluciones

**Polinomios de Legendre** $P_n(x)$ (primera clase):

| $n$ | $P_n(x)$ |
|-----|----------|
| 0 | $1$ |
| 1 | $x$ |
| 2 | $\frac{1}{2}(3x^2 - 1)$ |
| 3 | $\frac{1}{2}(5x^3 - 3x)$ |
| 4 | $\frac{1}{8}(35x^4 - 30x^2 + 3)$ |

**Fórmula de Rodrigues:**

$$P_n(x) = \frac{1}{2^n n!}\frac{d^n}{dx^n}(x^2-1)^n$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Identificar** $n$ | De $n(n+1)$ |
| 2 | **Si** $n \in \mathbb{Z}_{\geq 0}$ | Una solución es $P_n(x)$ |
| 3 | **Segunda solución** | $Q_n(x)$ (diverge en $x = \pm 1$) |
| 4 | **Si necesita acotada** | Usar solo $P_n$ |

### Ejemplo Detallado

**Problema:** Resolver $(1-x^2)y'' - 2xy' + 6y = 0$

---

**Paso 1: Identificar** $n$

$n(n+1) = 6$

$n^2 + n - 6 = 0$

$(n+3)(n-2) = 0$

$n = 2$ (tomamos positivo)

---

**Paso 2: Primera solución**

$$P_2(x) = \frac{1}{2}(3x^2 - 1)$$

---

**Paso 3: Solución general**

$$\boxed{y = C_1 P_2(x) + C_2 Q_2(x) = C_1 \cdot \frac{3x^2-1}{2} + C_2 Q_2(x)}$$

Para problemas físicos en $[-1, 1]$, usualmente $C_2 = 0$.

---

### Propiedades Útiles

| Propiedad | Fórmula |
|-----------|---------|
| Ortogonalidad | $\int_{-1}^{1} P_m(x)P_n(x)\,dx = \frac{2}{2n+1}\delta_{mn}$ |
| Recurrencia | $(n+1)P_{n+1} = (2n+1)xP_n - nP_{n-1}$ |
| Valores especiales | $P_n(1) = 1$, $P_n(-1) = (-1)^n$ |

---

## Diagrama de Decisión: Método de Series

```
┌──────────────────────────────────────────────────────┐
│     EDO lineal de segundo orden                      │
│     y'' + P(x)y' + Q(x)y = 0                         │
└──────────────────────────────────────────────────────┘
                       │
                       ▼
            ┌─────────────────────┐
            │  Clasificar x₀      │
            └─────────────────────┘
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
    ORDINARIO    SING. REGULAR   SING. IRREGULAR
        │              │              │
        ▼              ▼              ▼
    Series de      Frobenius      Métodos
    potencias      y = xʳΣcₙxⁿ    especiales
    y = Σcₙxⁿ          │
        │              ▼
        │      Ecuación indicial
        │      r² + (p₀-1)r + q₀ = 0
        │              │
        │    ┌─────────┼─────────┐
        │    ▼         ▼         ▼
        │  CASO 1   CASO 2    CASO 3
        │  r₁-r₂    r₁=r₂     r₁-r₂
        │  ∉ ℤ                 ∈ ℤ⁺
        │    │         │         │
        ▼    ▼         ▼         ▼
     2 series  2 series   y₂ con   Verificar
     indep.    indep.     ln x     si y₂ falla
```

---

## Tabla Resumen de Casos Frobenius

| Caso | Condición | Forma de $y_1$ | Forma de $y_2$ |
|------|-----------|----------------|----------------|
| 1 | $r_1 - r_2 \notin \mathbb{Z}$ | $x^{r_1}\sum a_n x^n$ | $x^{r_2}\sum b_n x^n$ |
| 2 | $r_1 = r_2 = r$ | $x^r\sum a_n x^n$ | $y_1\ln x + x^r\sum b_n x^n$ |
| 3a | $r_1 - r_2 \in \mathbb{Z}^+$ (sin problema) | $x^{r_1}\sum a_n x^n$ | $x^{r_2}\sum b_n x^n$ |
| 3b | $r_1 - r_2 \in \mathbb{Z}^+$ (con problema) | $x^{r_1}\sum a_n x^n$ | $Cy_1\ln x + x^{r_2}\sum b_n x^n$ |

---

## Errores Comunes a Evitar

| Error | Consecuencia | Prevención |
|-------|--------------|------------|
| Usar serie en punto singular | Serie no converge | Clasificar punto primero |
| Olvidar reindexar | Sumas incompatibles | Unificar potencias |
| Error en recurrencia | Coeficientes incorrectos | Verificar con [sustitución](../../../glossary.md#sustitucion) |
| Confundir $p_0$ con $P(0)$ | Ecuación indicial mal | $xP(x)$ evaluado en 0 |
| No considerar todos los casos | Segunda solución faltante | Analizar $r_1 - r_2$ |

---

## Problemas de Práctica Sugeridos

1. **Serie ordinaria:** $y'' + xy' + y = 0$ en $x = 0$

2. **Clasificar:** Puntos singulares de $x(x-1)^2y'' + 2y' + y = 0$

3. **Frobenius:** $xy'' + y' - y = 0$ en $x = 0$

4. **Bessel:** $x^2y'' + xy' + (x^2 - 1)y = 0$

5. **Legendre:** $(1-x^2)y'' - 2xy' + 12y = 0$

6. **Caso 2:** $x^2y'' - xy' + y = 0$

---

*Documento actualizado con formato expandido para estudio detallado.*
