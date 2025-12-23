<!--
content_type: methods
topic: Sistemas de EDO
---
-->

# Métodos: Sistemas de EDO

---

## Método 1: Resolver Sistema con Eigenvalores Reales Distintos

**Sistema:** $\mathbf{X}' = A\mathbf{X}$

### Pasos

1. **Calcular la ecuación característica:**
   $$\det(A - \lambda I) = 0$$

2. **Encontrar los eigenvalores** $\lambda_1, \lambda_2, ..., \lambda_n$

3. **Para cada eigenvalor $\lambda_i$, encontrar su eigenvector:**
   Resolver $(A - \lambda_i I)\mathbf{v}_i = \mathbf{0}$

4. **Escribir la solución general:**
   $$\mathbf{X} = C_1 e^{\lambda_1 t}\mathbf{v}_1 + C_2 e^{\lambda_2 t}\mathbf{v}_2 + \cdots$$

### Ejemplo Paso a Paso

**Resolver:** $\mathbf{X}' = \begin{pmatrix} 2 & 1 \\ 3 & 4 \end{pmatrix}\mathbf{X}$

**Paso 1:** 
$$\det\begin{pmatrix} 2-\lambda & 1 \\ 3 & 4-\lambda \end{pmatrix} = (2-\lambda)(4-\lambda) - 3 = 0$$
$$\lambda^2 - 6\lambda + 5 = 0$$

**Paso 2:** $(\lambda - 1)(\lambda - 5) = 0 \Rightarrow \lambda_1 = 1, \lambda_2 = 5$

**Paso 3a:** Para $\lambda_1 = 1$:
$$\begin{pmatrix} 1 & 1 \\ 3 & 3 \end{pmatrix}\mathbf{v} = \mathbf{0}$$
$v_1 + v_2 = 0 \Rightarrow \mathbf{v}_1 = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$

**Paso 3b:** Para $\lambda_2 = 5$:
$$\begin{pmatrix} -3 & 1 \\ 3 & -1 \end{pmatrix}\mathbf{v} = \mathbf{0}$$
$-3v_1 + v_2 = 0 \Rightarrow \mathbf{v}_2 = \begin{pmatrix} 1 \\ 3 \end{pmatrix}$

**Paso 4:** 
$$\mathbf{X} = C_1 e^{t}\begin{pmatrix} 1 \\ -1 \end{pmatrix} + C_2 e^{5t}\begin{pmatrix} 1 \\ 3 \end{pmatrix}$$

---

## Método 2: Resolver Sistema con Eigenvalores Complejos

**Sistema:** $\mathbf{X}' = A\mathbf{X}$ con eigenvalores $\lambda = \alpha \pm \beta i$

### Pasos

1. **Encontrar eigenvalores complejos:** $\lambda = \alpha + \beta i$

2. **Encontrar eigenvector complejo** para $\lambda = \alpha + \beta i$:
   $(A - \lambda I)\mathbf{v} = \mathbf{0}$

3. **Separar eigenvector en parte real e imaginaria:**
   $\mathbf{v} = \mathbf{a} + i\mathbf{b}$

4. **Construir dos soluciones reales:**
   $$\mathbf{X}_1 = e^{\alpha t}(\mathbf{a}\cos\beta t - \mathbf{b}\sin\beta t)$$
   $$\mathbf{X}_2 = e^{\alpha t}(\mathbf{a}\sin\beta t + \mathbf{b}\cos\beta t)$$

5. **Solución general:** $\mathbf{X} = C_1\mathbf{X}_1 + C_2\mathbf{X}_2$

### Ejemplo Paso a Paso

**Resolver:** $\mathbf{X}' = \begin{pmatrix} 1 & -2 \\ 1 & 3 \end{pmatrix}\mathbf{X}$

**Paso 1:** 
$$\det\begin{pmatrix} 1-\lambda & -2 \\ 1 & 3-\lambda \end{pmatrix} = (1-\lambda)(3-\lambda) + 2 = 0$$
$$\lambda^2 - 4\lambda + 5 = 0$$
$$\lambda = \frac{4 \pm \sqrt{16-20}}{2} = 2 \pm i$$

**Paso 2:** Para $\lambda = 2 + i$:
$$\begin{pmatrix} -1-i & -2 \\ 1 & 1-i \end{pmatrix}\mathbf{v} = \mathbf{0}$$
$(-1-i)v_1 - 2v_2 = 0$
$v_2 = \frac{(-1-i)}{2}v_1$

Tomando $v_1 = 2$: $v_2 = -1 - i$

$\mathbf{v} = \begin{pmatrix} 2 \\ -1-i \end{pmatrix}$

**Paso 3:**
$\mathbf{a} = \begin{pmatrix} 2 \\ -1 \end{pmatrix}$, $\mathbf{b} = \begin{pmatrix} 0 \\ -1 \end{pmatrix}$

$\alpha = 2$, $\beta = 1$

**Paso 4:**
$$\mathbf{X}_1 = e^{2t}\left[\begin{pmatrix} 2 \\ -1 \end{pmatrix}\cos t - \begin{pmatrix} 0 \\ -1 \end{pmatrix}\sin t\right] = e^{2t}\begin{pmatrix} 2\cos t \\ -\cos t + \sin t \end{pmatrix}$$

$$\mathbf{X}_2 = e^{2t}\left[\begin{pmatrix} 2 \\ -1 \end{pmatrix}\sin t + \begin{pmatrix} 0 \\ -1 \end{pmatrix}\cos t\right] = e^{2t}\begin{pmatrix} 2\sin t \\ -\sin t - \cos t \end{pmatrix}$$

**Paso 5:**
$$\mathbf{X} = C_1 e^{2t}\begin{pmatrix} 2\cos t \\ -\cos t + \sin t \end{pmatrix} + C_2 e^{2t}\begin{pmatrix} 2\sin t \\ -\sin t - \cos t \end{pmatrix}$$

---

## Método 3: Resolver Sistema con Eigenvalor Repetido

### Pasos

1. **Encontrar eigenvalor doble** $\lambda$

2. **Buscar eigenvectores:** Resolver $(A - \lambda I)\mathbf{v} = \mathbf{0}$

3. **Si hay dos eigenvectores independientes:**
   $$\mathbf{X} = C_1 e^{\lambda t}\mathbf{v}_1 + C_2 e^{\lambda t}\mathbf{v}_2$$

4. **Si hay solo un eigenvector $\mathbf{v}$:**
   - Encontrar vector generalizado $\mathbf{w}$: $(A - \lambda I)\mathbf{w} = \mathbf{v}$
   - Solución:
   $$\mathbf{X} = C_1 e^{\lambda t}\mathbf{v} + C_2 e^{\lambda t}(t\mathbf{v} + \mathbf{w})$$

### Ejemplo Paso a Paso

**Resolver:** $\mathbf{X}' = \begin{pmatrix} -1 & 1 \\ -1 & -3 \end{pmatrix}\mathbf{X}$

**Paso 1:**
$$\det\begin{pmatrix} -1-\lambda & 1 \\ -1 & -3-\lambda \end{pmatrix} = (-1-\lambda)(-3-\lambda) + 1 = 0$$
$$\lambda^2 + 4\lambda + 4 = 0 \Rightarrow \lambda = -2$$ (doble)

**Paso 2:**
$$\begin{pmatrix} 1 & 1 \\ -1 & -1 \end{pmatrix}\mathbf{v} = \mathbf{0}$$
$v_1 + v_2 = 0 \Rightarrow \mathbf{v} = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$

Solo un eigenvector independiente.

**Paso 4:** Encontrar $\mathbf{w}$:
$$\begin{pmatrix} 1 & 1 \\ -1 & -1 \end{pmatrix}\mathbf{w} = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$$
$w_1 + w_2 = 1$

Tomando $w_2 = 0$: $\mathbf{w} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$

**Solución:**
$$\mathbf{X} = C_1 e^{-2t}\begin{pmatrix} 1 \\ -1 \end{pmatrix} + C_2 e^{-2t}\left[t\begin{pmatrix} 1 \\ -1 \end{pmatrix} + \begin{pmatrix} 1 \\ 0 \end{pmatrix}\right]$$

---

## Método 4: Clasificar Retrato de Fase

**Sistema:** $\mathbf{X}' = A\mathbf{X}$ (2×2)

### Pasos

1. **Calcular traza y determinante:**
   - $\tau = \text{tr}(A) = a_{11} + a_{22}$
   - $\Delta = \det(A)$

2. **Calcular discriminante:** $D = \tau^2 - 4\Delta$

3. **Clasificar usando la tabla:**

```
              Δ
              ↑
              │
    Espirales │  Nodos
    inestables│  inestables
              │
    ──────────┼──────────→ τ
              │
    Espirales │  Nodos
    estables  │  estables
              │
    ────────────────────
         Sillas (Δ < 0)
```

| Condición | Tipo |
|-----------|------|
| $\Delta < 0$ | Punto silla |
| $\Delta > 0$, $D > 0$, $\tau < 0$ | Nodo estable |
| $\Delta > 0$, $D > 0$, $\tau > 0$ | Nodo inestable |
| $\Delta > 0$, $D < 0$, $\tau < 0$ | Espiral estable |
| $\Delta > 0$, $D < 0$, $\tau > 0$ | Espiral inestable |
| $\Delta > 0$, $\tau = 0$ | Centro |
| $\Delta > 0$, $D = 0$, $\tau \neq 0$ | Nodo degenerado |

### Ejemplo

**Clasificar:** $A = \begin{pmatrix} 1 & 4 \\ -1 & -3 \end{pmatrix}$

$\tau = 1 + (-3) = -2$

$\Delta = (1)(-3) - (4)(-1) = -3 + 4 = 1 > 0$

$D = (-2)^2 - 4(1) = 0$

**Clasificación:** Nodo degenerado estable ($\tau < 0$)

---

## Método 5: Calcular Matriz Exponencial por Diagonalización

### Pasos

1. **Encontrar eigenvalores** $\lambda_1, \lambda_2$

2. **Encontrar eigenvectores** y formar matriz $P = [\mathbf{v}_1 | \mathbf{v}_2]$

3. **Calcular $P^{-1}$**

4. **Formar matriz diagonal:**
   $$e^{Dt} = \begin{pmatrix} e^{\lambda_1 t} & 0 \\ 0 & e^{\lambda_2 t} \end{pmatrix}$$

5. **Calcular:** $e^{At} = P e^{Dt} P^{-1}$

### Ejemplo Paso a Paso

**Calcular $e^{At}$ para:** $A = \begin{pmatrix} 0 & 1 \\ -2 & 3 \end{pmatrix}$

**Paso 1:** $\lambda^2 - 3\lambda + 2 = 0 \Rightarrow \lambda_1 = 1, \lambda_2 = 2$

**Paso 2:**
- $\lambda_1 = 1$: $\mathbf{v}_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$
- $\lambda_2 = 2$: $\mathbf{v}_2 = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$

$P = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$

**Paso 3:**
$P^{-1} = \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix}$

**Paso 4:**
$e^{Dt} = \begin{pmatrix} e^t & 0 \\ 0 & e^{2t} \end{pmatrix}$

**Paso 5:**
$$e^{At} = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}\begin{pmatrix} e^t & 0 \\ 0 & e^{2t} \end{pmatrix}\begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix}$$

$$e^{At} = \begin{pmatrix} e^t & e^{2t} \\ e^t & 2e^{2t} \end{pmatrix}\begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix}$$

$$e^{At} = \begin{pmatrix} 2e^t - e^{2t} & -e^t + e^{2t} \\ 2e^t - 2e^{2t} & -e^t + 2e^{2t} \end{pmatrix}$$

---

## Método 6: Resolver PVI de Sistema

### Pasos

1. **Encontrar solución general** $\mathbf{X}(t)$

2. **Aplicar condición inicial** $\mathbf{X}(t_0) = \mathbf{X}_0$

3. **Resolver sistema** para las constantes $C_1, C_2, ...$

4. **Sustituir** en la solución general

### Ejemplo

**Resolver:** $\mathbf{X}' = \begin{pmatrix} 3 & -2 \\ 2 & -2 \end{pmatrix}\mathbf{X}$, $\mathbf{X}(0) = \begin{pmatrix} 1 \\ 3 \end{pmatrix}$

Eigenvalores: $\lambda_1 = 2$, $\lambda_2 = -1$

Eigenvectores: $\mathbf{v}_1 = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$, $\mathbf{v}_2 = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$

Solución general:
$$\mathbf{X} = C_1 e^{2t}\begin{pmatrix} 2 \\ 1 \end{pmatrix} + C_2 e^{-t}\begin{pmatrix} 1 \\ 2 \end{pmatrix}$$

Condición inicial en $t = 0$:
$$\begin{pmatrix} 1 \\ 3 \end{pmatrix} = C_1\begin{pmatrix} 2 \\ 1 \end{pmatrix} + C_2\begin{pmatrix} 1 \\ 2 \end{pmatrix}$$

Sistema:
- $2C_1 + C_2 = 1$
- $C_1 + 2C_2 = 3$

De la primera: $C_2 = 1 - 2C_1$

Sustituyendo: $C_1 + 2(1 - 2C_1) = 3$

$-3C_1 = 1 \Rightarrow C_1 = -\frac{1}{3}$

$C_2 = 1 - 2(-\frac{1}{3}) = \frac{5}{3}$

**Solución:**
$$\mathbf{X} = -\frac{1}{3}e^{2t}\begin{pmatrix} 2 \\ 1 \end{pmatrix} + \frac{5}{3}e^{-t}\begin{pmatrix} 1 \\ 2 \end{pmatrix}$$
