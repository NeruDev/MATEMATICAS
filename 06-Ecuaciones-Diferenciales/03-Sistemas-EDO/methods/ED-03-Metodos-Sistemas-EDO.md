<!--
::METADATA::
type: method
status: active
-->

# Métodos: Sistemas de EDO

> **Referencia rápida:** Esta guía presenta 10 métodos sistemáticos para resolver sistemas de [ecuaciones diferenciales](../../../glossary.md#ecuaciones-diferenciales) ordinarias lineales.

---

## Índice de Métodos

| # | Método | Aplicación | Complejidad |
|---|--------|------------|-------------|
| 1 | [Eigenvalores Reales Distintos](#método-1-eigenvalores-reales-distintos) | Sistemas $2\times 2$ básicos | ⭐⭐ |
| 2 | [Eigenvalores Complejos](#método-2-eigenvalores-complejos) | Sistemas oscilatorios | ⭐⭐⭐ |
| 3 | [Eigenvalor Repetido](#método-3-eigenvalor-repetido) | Deficiencia algebraica | ⭐⭐⭐ |
| 4 | [Sistema No Homogéneo](#método-4-sistema-no-homogéneo) | $\mathbf{X}' = A\mathbf{X} + \mathbf{F}(t)$ | ⭐⭐⭐ |
| 5 | [Matriz Exponencial](#método-5-[matriz](../../../glossary.md#matriz)-exponencial) | [Solución general](../../../glossary.md#solución-general) elegante | ⭐⭐⭐⭐ |
| 6 | [Desacoplamiento](#método-6-desacoplamiento-por-[diagonalización](../../../glossary.md#diagonalización)) | Sistemas diagonalizables | ⭐⭐⭐ |
| 7 | [Clasificar Retrato de Fase](#método-7-clasificar-retrato-de-fase) | Análisis cualitativo | ⭐⭐ |
| 8 | [PVI de Sistema](#método-8-resolver-pvi-de-sistema) | Con condiciones iniciales | ⭐⭐ |
| 9 | [Sistemas $3\times 3$](#método-9-sistemas-3times-3) | Mayor [dimensión](../../../glossary.md#dimensión) | ⭐⭐⭐⭐ |
| 10 | [Conversión [EDO](../../../glossary.md#edo)-Sistema](#método-10-conversión-edo-a-sistema) | EDO de [orden](../../../glossary.md#orden) superior | ⭐⭐ |

---

## Método 1: Eigenvalores Reales Distintos

### Cuándo Usar

- Sistema $\mathbf{X}' = A\mathbf{X}$ donde $A$ es $n \times n$
- La matriz tiene $n$ eigenvalores reales distintos

### Fórmula

**Solución general:**
$$\mathbf{X}(t) = C_1 e^{\lambda_1 t}\mathbf{v}_1 + C_2 e^{\lambda_2 t}\mathbf{v}_2 + \cdots + C_n e^{\lambda_n t}\mathbf{v}_n$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Ecuación característica** | $\det(A - \lambda I) = 0$ |
| 2 | **Encontrar eigenvalores** | Resolver para $\lambda_1, \lambda_2, \ldots$ |
| 3 | **Para cada** $\lambda_i$ | Resolver $(A - \lambda_i I)\mathbf{v}_i = \mathbf{0}$ |
| 4 | **Formar solución** | $\mathbf{X} = \sum C_i e^{\lambda_i t}\mathbf{v}_i$ |

### Ejemplo Detallado

**Problema:** Resolver $\mathbf{X}' = \begin{pmatrix} 4 & 2 \\ 3 & 3 \end{pmatrix}\mathbf{X}$

---

**Paso 1: Ecuación característica**

$$\det\begin{pmatrix} 4-\lambda & 2 \\ 3 & 3-\lambda \end{pmatrix} = 0$$

$(4-\lambda)(3-\lambda) - 6 = 0$

$\lambda^2 - 7\lambda + 12 - 6 = 0$

$\lambda^2 - 7\lambda + 6 = 0$

---

**Paso 2: Resolver**

$(\lambda - 1)(\lambda - 6) = 0$

$\lambda_1 = 1$, $\lambda_2 = 6$

---

**Paso 3a: Eigenvector para** $\lambda_1 = 1$

$(A - I)\mathbf{v} = \mathbf{0}$

$$\begin{pmatrix} 3 & 2 \\ 3 & 2 \end{pmatrix}\begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$$

$3v_1 + 2v_2 = 0 \implies v_2 = -\frac{3}{2}v_1$

Tomando $v_1 = 2$: $\mathbf{v}_1 = \begin{pmatrix} 2 \\ -3 \end{pmatrix}$

---

**Paso 3b: Eigenvector para** $\lambda_2 = 6$

$(A - 6I)\mathbf{v} = \mathbf{0}$

$$\begin{pmatrix} -2 & 2 \\ 3 & -3 \end{pmatrix}\begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$$

$-2v_1 + 2v_2 = 0 \implies v_1 = v_2$

$\mathbf{v}_2 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$

---

**Paso 4: Solución general**

$$\boxed{\mathbf{X}(t) = C_1 e^{t}\begin{pmatrix} 2 \\ -3 \end{pmatrix} + C_2 e^{6t}\begin{pmatrix} 1 \\ 1 \end{pmatrix}}$$

**Forma explícita:**
$$x(t) = 2C_1 e^t + C_2 e^{6t}$$
$$y(t) = -3C_1 e^t + C_2 e^{6t}$$

---

**Verificación:**

Sea $\mathbf{X}_1 = e^t\begin{pmatrix} 2 \\ -3 \end{pmatrix}$

$\mathbf{X}_1' = e^t\begin{pmatrix} 2 \\ -3 \end{pmatrix}$

$A\mathbf{X}_1 = \begin{pmatrix} 4 & 2 \\ 3 & 3 \end{pmatrix}\begin{pmatrix} 2e^t \\ -3e^t \end{pmatrix} = \begin{pmatrix} 8e^t - 6e^t \\ 6e^t - 9e^t \end{pmatrix} = e^t\begin{pmatrix} 2 \\ -3 \end{pmatrix}$ ✓

---

## Método 2: Eigenvalores Complejos

### Cuándo Usar

- La ecuación característica tiene raíces complejas $\lambda = \alpha \pm \beta i$
- Sistema presenta comportamiento oscilatorio

### Fórmulas

**Del eigenvector complejo** $\mathbf{v} = \mathbf{a} + i\mathbf{b}$, se obtienen dos soluciones reales:

$$\mathbf{X}_1 = e^{\alpha t}(\mathbf{a}\cos\beta t - \mathbf{b}\sin\beta t)$$
$$\mathbf{X}_2 = e^{\alpha t}(\mathbf{a}\sin\beta t + \mathbf{b}\cos\beta t)$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Encontrar eigenvalores** | $\lambda = \alpha + \beta i$ (tomar uno) |
| 2 | **Encontrar eigenvector** | $(A - \lambda I)\mathbf{v} = \mathbf{0}$ |
| 3 | **Separar** | $\mathbf{v} = \mathbf{a} + i\mathbf{b}$ |
| 4 | **Formar soluciones** | $\mathbf{X}_1$ y $\mathbf{X}_2$ usando fórmulas |
| 5 | **Solución general** | $\mathbf{X} = C_1\mathbf{X}_1 + C_2\mathbf{X}_2$ |

### Ejemplo Detallado

**Problema:** Resolver $\mathbf{X}' = \begin{pmatrix} 0 & -4 \\ 1 & 0 \end{pmatrix}\mathbf{X}$

---

**Paso 1: Ecuación característica**

$$\det\begin{pmatrix} -\lambda & -4 \\ 1 & -\lambda \end{pmatrix} = \lambda^2 + 4 = 0$$

$\lambda = \pm 2i$

Tomamos $\lambda = 2i$, entonces $\alpha = 0$, $\beta = 2$

---

**Paso 2: Eigenvector para** $\lambda = 2i$

$(A - 2iI)\mathbf{v} = \mathbf{0}$

$$\begin{pmatrix} -2i & -4 \\ 1 & -2i \end{pmatrix}\begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$$

De la segunda fila: $v_1 - 2iv_2 = 0 \implies v_1 = 2iv_2$

Tomando $v_2 = 1$:

$$\mathbf{v} = \begin{pmatrix} 2i \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ 1 \end{pmatrix} + i\begin{pmatrix} 2 \\ 0 \end{pmatrix}$$

---

**Paso 3: Identificar partes real e imaginaria**

$$\mathbf{a} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}, \quad \mathbf{b} = \begin{pmatrix} 2 \\ 0 \end{pmatrix}$$

---

**Paso 4: Formar soluciones** (con $\alpha = 0$, $\beta = 2$)

$$\mathbf{X}_1 = e^{0 \cdot t}\left[\begin{pmatrix} 0 \\ 1 \end{pmatrix}\cos 2t - \begin{pmatrix} 2 \\ 0 \end{pmatrix}\sin 2t\right] = \begin{pmatrix} -2\sin 2t \\ \cos 2t \end{pmatrix}$$

$$\mathbf{X}_2 = e^{0 \cdot t}\left[\begin{pmatrix} 0 \\ 1 \end{pmatrix}\sin 2t + \begin{pmatrix} 2 \\ 0 \end{pmatrix}\cos 2t\right] = \begin{pmatrix} 2\cos 2t \\ \sin 2t \end{pmatrix}$$

---

**Paso 5: Solución general**

$$\boxed{\mathbf{X}(t) = C_1\begin{pmatrix} -2\sin 2t \\ \cos 2t \end{pmatrix} + C_2\begin{pmatrix} 2\cos 2t \\ \sin 2t \end{pmatrix}}$$

**Forma alternativa:**
$$x(t) = -2C_1\sin 2t + 2C_2\cos 2t$$
$$y(t) = C_1\cos 2t + C_2\sin 2t$$

**Nota:** $\alpha = 0$ significa que las trayectorias son elipses cerradas (centro).

---

## Método 3: Eigenvalor Repetido

### Cuándo Usar

- Eigenvalor $\lambda$ con [multiplicidad algebraica](../../../glossary.md#multiplicidad-algebraica) $> 1$
- Si [multiplicidad geométrica](../../../glossary.md#multiplicidad-geométrica) = algebraica: caso simple
- Si multiplicidad geométrica < algebraica: se necesitan vectores generalizados

### Caso A: Dos Eigenvectores Independientes

**Solución:** $\mathbf{X} = C_1 e^{\lambda t}\mathbf{v}_1 + C_2 e^{\lambda t}\mathbf{v}_2$

### Caso B: Un Solo Eigenvector (Deficiente)

**Solución:**
$$\mathbf{X} = C_1 e^{\lambda t}\mathbf{v} + C_2 e^{\lambda t}(t\mathbf{v} + \mathbf{w})$$

donde $\mathbf{w}$ es el **[vector](../../../glossary.md#vector) generalizado**: $(A - \lambda I)\mathbf{w} = \mathbf{v}$

### Algoritmo de Resolución (Caso Deficiente)

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Encontrar** $\lambda$ | Eigenvalor doble |
| 2 | **Encontrar** $\mathbf{v}$ | Eigenvector: $(A-\lambda I)\mathbf{v} = \mathbf{0}$ |
| 3 | **Verificar** | Si hay solo un eigenvector independiente |
| 4 | **Encontrar** $\mathbf{w}$ | Vector generalizado: $(A-\lambda I)\mathbf{w} = \mathbf{v}$ |
| 5 | **Formar solución** | $\mathbf{X} = C_1 e^{\lambda t}\mathbf{v} + C_2 e^{\lambda t}(t\mathbf{v} + \mathbf{w})$ |

### Ejemplo Detallado

**Problema:** Resolver $\mathbf{X}' = \begin{pmatrix} 3 & 1 \\ -1 & 5 \end{pmatrix}\mathbf{X}$

---

**Paso 1: Ecuación característica**

$$\det\begin{pmatrix} 3-\lambda & 1 \\ -1 & 5-\lambda \end{pmatrix} = (3-\lambda)(5-\lambda) + 1 = 0$$

$\lambda^2 - 8\lambda + 15 + 1 = 0$

$\lambda^2 - 8\lambda + 16 = 0$

$(\lambda - 4)^2 = 0$

$\lambda = 4$ (doble)

---

**Paso 2: Eigenvector**

$(A - 4I)\mathbf{v} = \mathbf{0}$

$$\begin{pmatrix} -1 & 1 \\ -1 & 1 \end{pmatrix}\begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$$

$-v_1 + v_2 = 0 \implies v_1 = v_2$

$$\mathbf{v} = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$$

---

**Paso 3: Verificar**

Solo un eigenvector independiente (espacio propio de dimensión 1).

Se necesita vector generalizado.

---

**Paso 4: Encontrar vector generalizado** $\mathbf{w}$

$(A - 4I)\mathbf{w} = \mathbf{v}$

$$\begin{pmatrix} -1 & 1 \\ -1 & 1 \end{pmatrix}\begin{pmatrix} w_1 \\ w_2 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$$

$-w_1 + w_2 = 1$

Tomando $w_1 = 0$: $w_2 = 1$

$$\mathbf{w} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$$

---

**Paso 5: Formar solución**

Primera solución:
$$\mathbf{X}_1 = e^{4t}\begin{pmatrix} 1 \\ 1 \end{pmatrix}$$

Segunda solución:
$$\mathbf{X}_2 = e^{4t}\left[t\begin{pmatrix} 1 \\ 1 \end{pmatrix} + \begin{pmatrix} 0 \\ 1 \end{pmatrix}\right] = e^{4t}\begin{pmatrix} t \\ t + 1 \end{pmatrix}$$

**Solución general:**

$$\boxed{\mathbf{X}(t) = C_1 e^{4t}\begin{pmatrix} 1 \\ 1 \end{pmatrix} + C_2 e^{4t}\begin{pmatrix} t \\ t+1 \end{pmatrix}}$$

---

**Verificación de** $\mathbf{X}_2$:

$\mathbf{X}_2' = 4e^{4t}\begin{pmatrix} t \\ t+1 \end{pmatrix} + e^{4t}\begin{pmatrix} 1 \\ 1 \end{pmatrix} = e^{4t}\begin{pmatrix} 4t+1 \\ 4t+5 \end{pmatrix}$

$A\mathbf{X}_2 = \begin{pmatrix} 3 & 1 \\ -1 & 5 \end{pmatrix}e^{4t}\begin{pmatrix} t \\ t+1 \end{pmatrix} = e^{4t}\begin{pmatrix} 3t + t + 1 \\ -t + 5t + 5 \end{pmatrix} = e^{4t}\begin{pmatrix} 4t+1 \\ 4t+5 \end{pmatrix}$ ✓

---

## Método 4: Sistema No Homogéneo

### Cuándo Usar

- Sistema $\mathbf{X}' = A\mathbf{X} + \mathbf{F}(t)$
- Se conoce solución de la homogénea

### Fórmula (Variación de Parámetros)

**[Solución particular](../../../glossary.md#solución-particular):**
$$\mathbf{X}_p = \Phi(t)\int \Phi^{-1}(t)\mathbf{F}(t)\,dt$$

donde $\Phi(t)$ es la **matriz fundamental** (columnas son soluciones independientes).

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Resolver homogénea** | Obtener $\mathbf{X}_1, \mathbf{X}_2, \ldots$ |
| 2 | **Formar matriz fundamental** | $\Phi = [\mathbf{X}_1 \mid \mathbf{X}_2 \mid \cdots]$ |
| 3 | **Calcular** $\Phi^{-1}$ | Inversa de la matriz fundamental |
| 4 | **Calcular** $\Phi^{-1}\mathbf{F}$ | Multiplicar por término no homogéneo |
| 5 | **Integrar** | $\int \Phi^{-1}\mathbf{F}\,dt$ |
| 6 | **Multiplicar** | $\mathbf{X}_p = \Phi \cdot (\text{integral})$ |
| 7 | **Solución general** | $\mathbf{X} = \mathbf{X}_h + \mathbf{X}_p$ |

### Ejemplo Detallado

**Problema:** Resolver $\mathbf{X}' = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}\mathbf{X} + \begin{pmatrix} 0 \\ \sec t \end{pmatrix}$

---

**Paso 1: Resolver homogénea**

$\lambda^2 + 1 = 0 \implies \lambda = \pm i$

$$\mathbf{X}_1 = \begin{pmatrix} \cos t \\ -\sin t \end{pmatrix}, \quad \mathbf{X}_2 = \begin{pmatrix} \sin t \\ \cos t \end{pmatrix}$$

---

**Paso 2: Matriz fundamental**

$$\Phi(t) = \begin{pmatrix} \cos t & \sin t \\ -\sin t & \cos t \end{pmatrix}$$

---

**Paso 3: Calcular inversa**

$\det(\Phi) = \cos^2 t + \sin^2 t = 1$

$$\Phi^{-1}(t) = \begin{pmatrix} \cos t & -\sin t \\ \sin t & \cos t \end{pmatrix}$$

---

**Paso 4: Calcular** $\Phi^{-1}\mathbf{F}$

$$\Phi^{-1}\mathbf{F} = \begin{pmatrix} \cos t & -\sin t \\ \sin t & \cos t \end{pmatrix}\begin{pmatrix} 0 \\ \sec t \end{pmatrix} = \begin{pmatrix} -\sin t \cdot \sec t \\ \cos t \cdot \sec t \end{pmatrix} = \begin{pmatrix} -\tan t \\ 1 \end{pmatrix}$$

---

**Paso 5: Integrar**

$$\int \Phi^{-1}\mathbf{F}\,dt = \int \begin{pmatrix} -\tan t \\ 1 \end{pmatrix}dt = \begin{pmatrix} \ln|\cos t| \\ t \end{pmatrix}$$

---

**Paso 6: Multiplicar**

$$\mathbf{X}_p = \Phi \cdot \begin{pmatrix} \ln|\cos t| \\ t \end{pmatrix} = \begin{pmatrix} \cos t & \sin t \\ -\sin t & \cos t \end{pmatrix}\begin{pmatrix} \ln|\cos t| \\ t \end{pmatrix}$$

$$\mathbf{X}_p = \begin{pmatrix} \cos t \ln|\cos t| + t\sin t \\ -\sin t \ln|\cos t| + t\cos t \end{pmatrix}$$

---

**Paso 7: Solución general**

$$\boxed{\mathbf{X} = C_1\begin{pmatrix} \cos t \\ -\sin t \end{pmatrix} + C_2\begin{pmatrix} \sin t \\ \cos t \end{pmatrix} + \begin{pmatrix} \cos t \ln|\cos t| + t\sin t \\ -\sin t \ln|\cos t| + t\cos t \end{pmatrix}}$$

---

## Método 5: Matriz Exponencial

### Cuándo Usar

- Para expresar la solución en forma cerrada
- Especialmente útil para sistemas con condiciones iniciales
- Cuando la matriz $A$ es diagonalizable o tiene forma de Jordan

### Fórmula

**Solución del PVI:** $\mathbf{X}' = A\mathbf{X}$, $\mathbf{X}(0) = \mathbf{X}_0$

$$\mathbf{X}(t) = e^{At}\mathbf{X}_0$$

### Cálculo de $e^{At}$ por Diagonalización

Si $A = PDP^{-1}$ donde $D$ es diagonal:

$$e^{At} = Pe^{Dt}P^{-1}$$

$$e^{Dt} = \begin{pmatrix} e^{\lambda_1 t} & 0 & \cdots \\ 0 & e^{\lambda_2 t} & \cdots \\ \vdots & & \ddots \end{pmatrix}$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Eigenvalores** | $\lambda_1, \lambda_2, \ldots$ |
| 2 | **Eigenvectores** | $\mathbf{v}_1, \mathbf{v}_2, \ldots$ |
| 3 | **Formar** $P$ | $P = [\mathbf{v}_1 \mid \mathbf{v}_2 \mid \cdots]$ |
| 4 | **Calcular** $P^{-1}$ | Inversa de $P$ |
| 5 | **Formar** $e^{Dt}$ | Diagonal con $e^{\lambda_i t}$ |
| 6 | **Calcular** | $e^{At} = Pe^{Dt}P^{-1}$ |

### Ejemplo Detallado

**Problema:** Calcular $e^{At}$ para $A = \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}$

---

**Paso 1: Eigenvalores**

$\det(A - \lambda I) = (1-\lambda)(3-\lambda) = 0$

$\lambda_1 = 1$, $\lambda_2 = 3$

---

**Paso 2: Eigenvectores**

Para $\lambda_1 = 1$:
$$\begin{pmatrix} 0 & 2 \\ 0 & 2 \end{pmatrix}\mathbf{v} = \mathbf{0} \implies \mathbf{v}_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$$

Para $\lambda_2 = 3$:
$$\begin{pmatrix} -2 & 2 \\ 0 & 0 \end{pmatrix}\mathbf{v} = \mathbf{0} \implies \mathbf{v}_2 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$$

---

**Paso 3: Formar P**

$$P = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$$

---

**Paso 4: Calcular** $P^{-1}$

$$P^{-1} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$$

---

**Paso 5: Formar** $e^{Dt}$

$$e^{Dt} = \begin{pmatrix} e^t & 0 \\ 0 & e^{3t} \end{pmatrix}$$

---

**Paso 6: Calcular** $e^{At}$

$$e^{At} = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} e^t & 0 \\ 0 & e^{3t} \end{pmatrix}\begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$$

$$= \begin{pmatrix} e^t & e^{3t} \\ 0 & e^{3t} \end{pmatrix}\begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$$

$$\boxed{e^{At} = \begin{pmatrix} e^t & e^{3t} - e^t \\ 0 & e^{3t} \end{pmatrix}}$$

---

**Verificación:** $e^{A \cdot 0} = I$ ✓

$\frac{d}{dt}e^{At} = \begin{pmatrix} e^t & 3e^{3t} - e^t \\ 0 & 3e^{3t} \end{pmatrix}$

$Ae^{At} = \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}\begin{pmatrix} e^t & e^{3t} - e^t \\ 0 & e^{3t} \end{pmatrix} = \begin{pmatrix} e^t & e^{3t} - e^t + 2e^{3t} \\ 0 & 3e^{3t} \end{pmatrix} = \begin{pmatrix} e^t & 3e^{3t} - e^t \\ 0 & 3e^{3t} \end{pmatrix}$ ✓

---

## Método 6: Desacoplamiento por Diagonalización

### Cuándo Usar

- Para transformar el sistema en ecuaciones independientes
- Cuando $A$ es diagonalizable

### Fórmula

**Cambio de variable:** $\mathbf{X} = P\mathbf{Y}$

**Sistema desacoplado:** $\mathbf{Y}' = D\mathbf{Y}$

donde cada ecuación es $y_i' = \lambda_i y_i$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Diagonalizar** $A$ | $A = PDP^{-1}$ |
| 2 | **Cambio de variable** | $\mathbf{Y} = P^{-1}\mathbf{X}$ |
| 3 | **Resolver** | $y_i' = \lambda_i y_i \implies y_i = c_i e^{\lambda_i t}$ |
| 4 | **Regresar** | $\mathbf{X} = P\mathbf{Y}$ |

### Ejemplo Detallado

**Problema:** Resolver $\begin{cases} x' = 2x + y \\ y' = x + 2y \end{cases}$

---

**Paso 1: Escribir como sistema**

$$\mathbf{X}' = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}\mathbf{X}$$

---

**Paso 2: Diagonalizar**

Eigenvalores: $(2-\lambda)^2 - 1 = 0 \implies \lambda_1 = 1, \lambda_2 = 3$

Eigenvectores:
- $\lambda_1 = 1$: $\mathbf{v}_1 = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$
- $\lambda_2 = 3$: $\mathbf{v}_2 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$

$$P = \begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix}, \quad D = \begin{pmatrix} 1 & 0 \\ 0 & 3 \end{pmatrix}$$

---

**Paso 3: Sistema desacoplado**

$$\mathbf{Y}' = D\mathbf{Y} \implies \begin{cases} u' = u \\ v' = 3v \end{cases}$$

$$u = c_1 e^t, \quad v = c_2 e^{3t}$$

---

**Paso 4: Regresar a** $\mathbf{X}$

$$\mathbf{X} = P\mathbf{Y} = \begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix}\begin{pmatrix} c_1 e^t \\ c_2 e^{3t} \end{pmatrix}$$

$$\boxed{\begin{cases} x = c_1 e^t + c_2 e^{3t} \\ y = -c_1 e^t + c_2 e^{3t} \end{cases}}$$

---

## Método 7: Clasificar Retrato de Fase

### Cuándo Usar

- Análisis cualitativo de sistemas $2 \times 2$
- Determinar estabilidad del punto de equilibrio

### Fórmulas

**[Traza](../../../glossary.md#traza):** $\tau = \text{tr}(A) = a_{11} + a_{22}$

**[Determinante](../../../glossary.md#determinante):** $\Delta = \det(A)$

**Discriminante:** $D = \tau^2 - 4\Delta$

### Tabla de Clasificación

| $\Delta$ | $\tau$ | $D$ | Tipo | Estabilidad |
|----------|--------|-----|------|-------------|
| $< 0$ | — | — | **Punto silla** | Inestable |
| $> 0$ | $< 0$ | $> 0$ | **Nodo** | Estable |
| $> 0$ | $> 0$ | $> 0$ | **Nodo** | Inestable |
| $> 0$ | $< 0$ | $< 0$ | **Espiral** | Estable |
| $> 0$ | $> 0$ | $< 0$ | **Espiral** | Inestable |
| $> 0$ | $= 0$ | $< 0$ | **Centro** | Neutralmente estable |
| $= 0$ | — | — | **Degenerado** | Caso especial |

### Diagrama de Clasificación

```
                         τ (traza)
                          ↑
                          │
         Espirales        │        Nodos
         inestables       │        inestables
                          │
    ──────────────────────┼──────────────────── Δ = τ²/4
                          │
         Espirales        │        Nodos
         estables         │        estables
                          │
    ══════════════════════╪════════════════════ → Δ
                          │
              Punto silla (Δ < 0)
```

### Ejemplo Detallado

**Problema:** Clasificar el punto de equilibrio de $\mathbf{X}' = \begin{pmatrix} 1 & -5 \\ 1 & -3 \end{pmatrix}\mathbf{X}$

---

**Paso 1: Calcular traza y determinante**

$\tau = 1 + (-3) = -2$

$\Delta = (1)(-3) - (-5)(1) = -3 + 5 = 2$

---

**Paso 2: Calcular discriminante**

$D = \tau^2 - 4\Delta = 4 - 8 = -4 < 0$

---

**Paso 3: Clasificar**

- $\Delta = 2 > 0$ ✓
- $\tau = -2 < 0$ ✓
- $D = -4 < 0$ ✓

**Clasificación:** $\boxed{\text{Espiral estable}}$

---

**Paso 4: Verificar con eigenvalores**

$\lambda^2 - (-2)\lambda + 2 = 0$

$\lambda^2 + 2\lambda + 2 = 0$

$\lambda = \frac{-2 \pm \sqrt{-4}}{2} = -1 \pm i$

Parte real negativa → estable ✓
Parte imaginaria no nula → espiral ✓

---

## Método 8: Resolver PVI de Sistema

### Cuándo Usar

- Sistema con condición inicial $\mathbf{X}(t_0) = \mathbf{X}_0$
- Se busca solución única

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Solución general** | $\mathbf{X} = C_1\mathbf{X}_1 + C_2\mathbf{X}_2 + \cdots$ |
| 2 | **Evaluar en** $t_0$ | $\mathbf{X}(t_0) = C_1\mathbf{X}_1(t_0) + C_2\mathbf{X}_2(t_0)$ |
| 3 | **Formar sistema** | Ecuaciones lineales en $C_i$ |
| 4 | **Resolver** | Encontrar $C_1, C_2, \ldots$ |
| 5 | **Sustituir** | Escribir solución particular |

### Ejemplo Detallado

**Problema:** Resolver $\mathbf{X}' = \begin{pmatrix} 1 & 1 \\ 4 & 1 \end{pmatrix}\mathbf{X}$, $\mathbf{X}(0) = \begin{pmatrix} 2 \\ 6 \end{pmatrix}$

---

**Paso 1: Resolver sistema**

$\lambda^2 - 2\lambda - 3 = 0 \implies \lambda_1 = -1, \lambda_2 = 3$

Eigenvectores:
- $\lambda_1 = -1$: $\mathbf{v}_1 = \begin{pmatrix} 1 \\ -2 \end{pmatrix}$
- $\lambda_2 = 3$: $\mathbf{v}_2 = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$

Solución general:
$$\mathbf{X} = C_1 e^{-t}\begin{pmatrix} 1 \\ -2 \end{pmatrix} + C_2 e^{3t}\begin{pmatrix} 1 \\ 2 \end{pmatrix}$$

---

**Paso 2: Evaluar en** $t = 0$

$$\begin{pmatrix} 2 \\ 6 \end{pmatrix} = C_1\begin{pmatrix} 1 \\ -2 \end{pmatrix} + C_2\begin{pmatrix} 1 \\ 2 \end{pmatrix}$$

---

**Paso 3: Sistema de ecuaciones**

$$\begin{cases} C_1 + C_2 = 2 \\ -2C_1 + 2C_2 = 6 \end{cases}$$

---

**Paso 4: Resolver**

De la segunda: $C_2 - C_1 = 3$

Sumando con la primera: $2C_2 = 5 \implies C_2 = \frac{5}{2}$

$C_1 = 2 - \frac{5}{2} = -\frac{1}{2}$

---

**Paso 5: Solución particular**

$$\boxed{\mathbf{X}(t) = -\frac{1}{2}e^{-t}\begin{pmatrix} 1 \\ -2 \end{pmatrix} + \frac{5}{2}e^{3t}\begin{pmatrix} 1 \\ 2 \end{pmatrix}}$$

**Forma explícita:**
$$x(t) = -\frac{1}{2}e^{-t} + \frac{5}{2}e^{3t}$$
$$y(t) = e^{-t} + 5e^{3t}$$

---

## Método 9: Sistemas $3\times 3$

### Cuándo Usar

- Sistemas de 3 ecuaciones lineales
- Proceso similar pero con más cálculo

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Ecuación característica** | Polinomio cúbico $\det(A-\lambda I) = 0$ |
| 2 | **Encontrar raíces** | Buscar raíz racional, luego factorizar |
| 3 | **Eigenvectores** | Para cada $\lambda_i$ |
| 4 | **Formar solución** | $\mathbf{X} = \sum C_i e^{\lambda_i t}\mathbf{v}_i$ |

### Ejemplo Detallado

**Problema:** Resolver $\mathbf{X}' = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ -6 & 11 & -6 \end{pmatrix}\mathbf{X}$

---

**Paso 1: Ecuación característica**

$$\det\begin{pmatrix} -\lambda & 1 & 0 \\ 0 & -\lambda & 1 \\ -6 & 11 & -6-\lambda \end{pmatrix} = 0$$

Expandiendo por primera columna:
$-\lambda[\lambda(6+\lambda) - 11] - 6(-1) = 0$

$-\lambda^3 - 6\lambda^2 + 11\lambda + 6 = 0$

$\lambda^3 + 6\lambda^2 - 11\lambda - 6 = 0$

---

**Paso 2: Encontrar raíces**

Probando $\lambda = 1$: $1 + 6 - 11 - 6 = -10 \neq 0$

Probando $\lambda = -1$: $-1 + 6 + 11 - 6 = 10 \neq 0$

Factorizando (usando fórmulas): $(\lambda - 1)(\lambda - 2)(\lambda - 3) = 0$

$\lambda_1 = 1$, $\lambda_2 = 2$, $\lambda_3 = 3$

---

**Paso 3: Eigenvectores**

Para $\lambda_1 = 1$: Resolver $(A - I)\mathbf{v} = \mathbf{0}$

Después de reducción: $\mathbf{v}_1 = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}$

Para $\lambda_2 = 2$: $\mathbf{v}_2 = \begin{pmatrix} 1 \\ 2 \\ 4 \end{pmatrix}$

Para $\lambda_3 = 3$: $\mathbf{v}_3 = \begin{pmatrix} 1 \\ 3 \\ 9 \end{pmatrix}$

---

**Paso 4: Solución general**

$$\boxed{\mathbf{X}(t) = C_1 e^t\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} + C_2 e^{2t}\begin{pmatrix} 1 \\ 2 \\ 4 \end{pmatrix} + C_3 e^{3t}\begin{pmatrix} 1 \\ 3 \\ 9 \end{pmatrix}}$$

---

## Método 10: Conversión EDO a Sistema

### Cuándo Usar

- Convertir una EDO de orden $n$ a sistema de primer orden
- Útil para aplicar métodos de sistemas

### Fórmula

Para $y^{(n)} + a_{n-1}y^{(n-1)} + \cdots + a_1y' + a_0y = f(t)$

**[Sustitución](../../../glossary.md#sustitución):**
$$x_1 = y, \quad x_2 = y', \quad \ldots, \quad x_n = y^{(n-1)}$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Definir variables** | $x_1 = y$, $x_2 = y'$, ... |
| 2 | **Primera ecuación** | $x_1' = x_2$ |
| 3 | **Ecuaciones intermedias** | $x_k' = x_{k+1}$ |
| 4 | **Última ecuación** | Despejar $y^{(n)}$ de la EDO |
| 5 | **Escribir sistema** | En forma matricial |

### Ejemplo Detallado

**Problema:** Convertir $y''' - 6y'' + 11y' - 6y = 0$ a sistema

---

**Paso 1: Definir variables**

$$x_1 = y, \quad x_2 = y', \quad x_3 = y''$$

---

**Paso 2-3: Ecuaciones**

$$x_1' = y' = x_2$$
$$x_2' = y'' = x_3$$

---

**Paso 4: Última ecuación** (de la EDO)

$y''' = 6y'' - 11y' + 6y = 6x_3 - 11x_2 + 6x_1$

$$x_3' = 6x_1 - 11x_2 + 6x_3$$

---

**Paso 5: Sistema matricial**

$$\boxed{\mathbf{X}' = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 6 & -11 & 6 \end{pmatrix}\mathbf{X}}$$

Esta es la **matriz compañera** de la EDO.

---

## Tabla Resumen de Fórmulas

| Situación | Solución |
|-----------|----------|
| $\lambda_1 \neq \lambda_2$ reales | $\mathbf{X} = C_1 e^{\lambda_1 t}\mathbf{v}_1 + C_2 e^{\lambda_2 t}\mathbf{v}_2$ |
| $\lambda = \alpha \pm \beta i$ | $\mathbf{X} = e^{\alpha t}[C_1(\mathbf{a}\cos\beta t - \mathbf{b}\sin\beta t) + C_2(\mathbf{a}\sin\beta t + \mathbf{b}\cos\beta t)]$ |
| $\lambda$ doble, deficiente | $\mathbf{X} = C_1 e^{\lambda t}\mathbf{v} + C_2 e^{\lambda t}(t\mathbf{v} + \mathbf{w})$ |
| No homogéneo | $\mathbf{X}_p = \Phi \int \Phi^{-1}\mathbf{F}\,dt$ |
| Matriz exponencial | $e^{At} = Pe^{Dt}P^{-1}$ |

---

## Errores Comunes a Evitar

| Error | Consecuencia | Prevención |
|-------|--------------|------------|
| Eigenvector con error de signo | Solución incorrecta | Verificar $(A-\lambda I)\mathbf{v} = \mathbf{0}$ |
| Confundir $\mathbf{a}$ y $\mathbf{b}$ | Solución real incorrecta | $\mathbf{v} = \mathbf{a} + i\mathbf{b}$ claramente |
| Olvidar vector generalizado | Sistema incompleto | Si eigenvalor repetido, buscar $\mathbf{w}$ |
| [Wronskiano](../../../glossary.md#wronskiano) mal calculado | Integral particular errónea | Verificar $\det(\Phi) \neq 0$ |
| Error en clasificación | Análisis cualitativo erróneo | Calcular $\tau$, $\Delta$, $D$ cuidadosamente |

---

## Problemas de Práctica Sugeridos

1. **Reales distintos:** $\mathbf{X}' = \begin{pmatrix} 5 & 3 \\ -6 & -4 \end{pmatrix}\mathbf{X}$

2. **Complejos:** $\mathbf{X}' = \begin{pmatrix} 2 & -5 \\ 1 & -2 \end{pmatrix}\mathbf{X}$

3. **Repetido:** $\mathbf{X}' = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}\mathbf{X}$

4. **PVI:** $\mathbf{X}' = \begin{pmatrix} 1 & 2 \\ 3 & 2 \end{pmatrix}\mathbf{X}$, $\mathbf{X}(0) = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$

5. **No homogéneo:** $\mathbf{X}' = \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}\mathbf{X} + \begin{pmatrix} e^t \\ 0 \end{pmatrix}$

6. **Clasificar:** Determinar tipo y estabilidad para varios sistemas dados

---

*Documento actualizado con formato expandido para estudio detallado.*
