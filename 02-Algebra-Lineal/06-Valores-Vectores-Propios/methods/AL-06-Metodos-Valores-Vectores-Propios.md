<!--
::METADATA::
type: method
status: active
-->

# Métodos: Valores y Vectores Propios

> Guía completa de métodos con algoritmos detallados, tablas de procedimientos y ejemplos paso a paso.

---

## Método 1: Encontrar Eigenvalores (Matriz 2×2)

**Cuándo Usar:** Para hallar los valores propios de matrices pequeñas de manera eficiente.

**Definición:** $\lambda$ es eigenvalor de $A$ si existe $\mathbf{v} \neq \mathbf{0}$ [tal que](../../../glossary.md#tal-que) $A\mathbf{v} = \lambda\mathbf{v}$.

**Fórmula Rápida para 2×2:** Para $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$:

$$\lambda = \frac{\text{tr}(A) \pm \sqrt{\text{tr}(A)^2 - 4\det(A)}}{2}$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Calcular [traza](../../../glossary.md#traza) | $\text{tr}(A) = a + d$ |
| 2 | Calcular [determinante](../../../glossary.md#determinante) | $\det(A) = ad - bc$ |
| 3 | Calcular discriminante | $\Delta = \text{tr}(A)^2 - 4\det(A)$ |
| 4 | Aplicar fórmula | $\lambda_{1,2} = \frac{\text{tr}(A) \pm \sqrt{\Delta}}{2}$ |

### Ejemplo Detallado

**Problema:** Encontrar los eigenvalores de $A = \begin{pmatrix} 5 & -2 \\ 3 & -4 \end{pmatrix}$

---

**Paso 1: Calcular la [traza](../../../glossary.md#traza)**

$$\text{tr}(A) = 5 + (-4) = 1$$

---

**Paso 2: Calcular el [determinante](../../../glossary.md#determinante)**

$$\det(A) = (5)(-4) - (-2)(3) = -20 + 6 = -14$$

---

**Paso 3: Calcular el discriminante**

$$\Delta = \text{tr}(A)^2 - 4\det(A) = 1^2 - 4(-14) = 1 + 56 = 57$$

---

**Paso 4: Aplicar la fórmula**

$$\lambda = \frac{1 \pm \sqrt{57}}{2}$$

$$\lambda_1 = \frac{1 + \sqrt{57}}{2} \approx 4.27$$

$$\lambda_2 = \frac{1 - \sqrt{57}}{2} \approx -3.27$$

---

**Verificación (Suma y Producto de eigenvalores):**

- $\lambda_1 + \lambda_2 = \text{tr}(A) = 1$ ✓
- $\lambda_1 \cdot \lambda_2 = \det(A) = -14$ ✓

$$\boxed{\lambda_1 = \frac{1 + \sqrt{57}}{2}, \quad \lambda_2 = \frac{1 - \sqrt{57}}{2}}$$

---

### Ejemplo: Eigenvalores Complejos

**Problema:** Encontrar los eigenvalores de $A = \begin{pmatrix} 1 & -2 \\ 1 & 3 \end{pmatrix}$

---

**Cálculos:**

$$\text{tr}(A) = 1 + 3 = 4$$
$$\det(A) = 3 - (-2) = 5$$
$$\Delta = 16 - 20 = -4 < 0$$

---

**Eigenvalores complejos:**

$$\lambda = \frac{4 \pm \sqrt{-4}}{2} = \frac{4 \pm 2i}{2} = 2 \pm i$$

$$\boxed{\lambda_1 = 2 + i, \quad \lambda_2 = 2 - i}$$

---

## Método 2: Encontrar Eigenvalores (Matriz 3×3)

**Cuándo Usar:** Para matrices 3×3 o cuando se necesita el [polinomio característico](../../../glossary.md#polinomio-caracteristico) explícito.

**Fórmula:** $p(\lambda) = \det(A - \lambda I) = 0$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Formar $A - \lambda I$ | Restar $\lambda$ de la diagonal |
| 2 | Calcular determinante | Expandir por cofactores o Sarrus |
| 3 | Buscar raíces racionales | Probar divisores del término independiente |
| 4 | [Factorizar](../../../glossary.md#factorizar) | División sintética si se encuentra raíz |
| 5 | Resolver | Aplicar fórmula cuadrática al factor restante |

### Caso Especial: Matrices Triangulares

Para matrices triangulares (superior o inferior):
$$\text{Eigenvalores} = \text{Elementos de la diagonal}$$

### Ejemplo Detallado

**Problema:** Encontrar los eigenvalores de $A = \begin{pmatrix} 2 & 1 & 0 \\ 0 & 3 & 1 \\ 0 & 0 & 2 \end{pmatrix}$

---

**Paso 1: Identificar tipo de [matriz](../../../glossary.md#matriz)**

$A$ es triangular superior, por lo tanto:

$$\boxed{\text{Eigenvalores: } \lambda_1 = 2 \text{ (doble)}, \quad \lambda_2 = 3}$$

---

### Ejemplo: Matriz 3×3 General

**Problema:** Encontrar los eigenvalores de $A = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 3 \end{pmatrix}$

---

**Paso 1: Formar $A - \lambda I$**

$$A - \lambda I = \begin{pmatrix} 1-\lambda & 1 & 0 \\ 0 & 2-\lambda & 1 \\ 0 & 0 & 3-\lambda \end{pmatrix}$$

---

**Paso 2: Calcular determinante** (triangular superior)

$$\det(A - \lambda I) = (1-\lambda)(2-\lambda)(3-\lambda)$$

---

**Paso 3: Resolver $p(\lambda) = 0$**

$$(1-\lambda)(2-\lambda)(3-\lambda) = 0$$

$$\boxed{\lambda_1 = 1, \quad \lambda_2 = 2, \quad \lambda_3 = 3}$$

---

### Ejemplo: Matriz 3×3 No Triangular

**Problema:** Encontrar los eigenvalores de $A = \begin{pmatrix} 4 & 0 & 1 \\ -1 & 3 & 0 \\ 2 & 0 & 1 \end{pmatrix}$

---

**Paso 1: Formar $A - \lambda I$**

$$A - \lambda I = \begin{pmatrix} 4-\lambda & 0 & 1 \\ -1 & 3-\lambda & 0 \\ 2 & 0 & 1-\lambda \end{pmatrix}$$

---

**Paso 2: Calcular determinante** (expandir por columna 2)

$$\det(A - \lambda I) = (3-\lambda) \cdot \det\begin{pmatrix} 4-\lambda & 1 \\ 2 & 1-\lambda \end{pmatrix}$$

$$= (3-\lambda)[(4-\lambda)(1-\lambda) - 2]$$

$$= (3-\lambda)[4 - 4\lambda - \lambda + \lambda^2 - 2]$$

$$= (3-\lambda)[\lambda^2 - 5\lambda + 2]$$

---

**Paso 3: Resolver**

Factor $(3-\lambda) = 0$: $\lambda_1 = 3$

Factor $\lambda^2 - 5\lambda + 2 = 0$:
$$\lambda = \frac{5 \pm \sqrt{25 - 8}}{2} = \frac{5 \pm \sqrt{17}}{2}$$

$$\boxed{\lambda_1 = 3, \quad \lambda_2 = \frac{5 + \sqrt{17}}{2}, \quad \lambda_3 = \frac{5 - \sqrt{17}}{2}}$$

---

## Método 3: Encontrar Eigenvectores

**Cuándo Usar:** Una vez conocido un eigenvalor $\lambda$, para encontrar los vectores propios asociados.

**Definición:** El eigenespacio asociado a $\lambda$ es:
$$E_\lambda = \ker(A - \lambda I) = \{\mathbf{v} : A\mathbf{v} = \lambda\mathbf{v}\}$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Formar $A - \lambda I$ | Sustituir el eigenvalor dado |
| 2 | Reducir a RREF | Gauss-Jordan |
| 3 | Resolver sistema homogéneo | $(A - \lambda I)\mathbf{v} = \mathbf{0}$ |
| 4 | Parametrizar | Variables libres generan la [base](../../../glossary.md#base) |
| 5 | Escribir [base](../../../glossary.md#base) | Vectores propios LI |

### Ejemplo Detallado

**Problema:** Encontrar los eigenvectores de $A = \begin{pmatrix} 4 & 2 \\ 1 & 3 \end{pmatrix}$

---

**Paso 1: Encontrar eigenvalores**

$$p(\lambda) = \lambda^2 - 7\lambda + 10 = (\lambda - 5)(\lambda - 2) = 0$$

$\lambda_1 = 5$, $\lambda_2 = 2$

---

**Paso 2: Eigenvector para $\lambda_1 = 5$**

$$A - 5I = \begin{pmatrix} 4-5 & 2 \\ 1 & 3-5 \end{pmatrix} = \begin{pmatrix} -1 & 2 \\ 1 & -2 \end{pmatrix}$$

Reducir a RREF:
$R_2 \leftarrow R_2 + R_1$:
$$\begin{pmatrix} -1 & 2 \\ 0 & 0 \end{pmatrix} \rightarrow \begin{pmatrix} 1 & -2 \\ 0 & 0 \end{pmatrix}$$

Sistema: $x_1 - 2x_2 = 0 \Rightarrow x_1 = 2x_2$

Sea $x_2 = t$: $\mathbf{v} = t\begin{pmatrix} 2 \\ 1 \end{pmatrix}$

$$\boxed{E_5 = \text{span}\left\{\begin{pmatrix} 2 \\ 1 \end{pmatrix}\right\}}$$

---

**Paso 3: Eigenvector para $\lambda_2 = 2$**

$$A - 2I = \begin{pmatrix} 4-2 & 2 \\ 1 & 3-2 \end{pmatrix} = \begin{pmatrix} 2 & 2 \\ 1 & 1 \end{pmatrix}$$

Reducir a RREF:
$$\begin{pmatrix} 2 & 2 \\ 1 & 1 \end{pmatrix} \rightarrow \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$$

Sistema: $x_1 + x_2 = 0 \Rightarrow x_1 = -x_2$

Sea $x_2 = t$: $\mathbf{v} = t\begin{pmatrix} -1 \\ 1 \end{pmatrix}$

$$\boxed{E_2 = \text{span}\left\{\begin{pmatrix} -1 \\ 1 \end{pmatrix}\right\}}$$

---

**Verificación:**

$$A\mathbf{v}_1 = \begin{pmatrix} 4 & 2 \\ 1 & 3 \end{pmatrix}\begin{pmatrix} 2 \\ 1 \end{pmatrix} = \begin{pmatrix} 10 \\ 5 \end{pmatrix} = 5\begin{pmatrix} 2 \\ 1 \end{pmatrix} \checkmark$$

$$A\mathbf{v}_2 = \begin{pmatrix} 4 & 2 \\ 1 & 3 \end{pmatrix}\begin{pmatrix} -1 \\ 1 \end{pmatrix} = \begin{pmatrix} -2 \\ 2 \end{pmatrix} = 2\begin{pmatrix} -1 \\ 1 \end{pmatrix} \checkmark$$

---

## Método 4: Verificar Diagonalizabilidad

**Cuándo Usar:** Para determinar si una [matriz](../../../glossary.md#matriz) puede escribirse como $A = PDP^{-1}$ con $D$ diagonal.

**Criterio:** $A$ es diagonalizable si y solo si para cada eigenvalor:
$$m_g(\lambda) = m_a(\lambda)$$

donde:
- $m_a(\lambda)$ = [multiplicidad algebraica](../../../glossary.md#multiplicidad-algebraica) (exponente en el [polinomio](../../../glossary.md#polinomio) característico)
- $m_g(\lambda)$ = [multiplicidad geométrica](../../../glossary.md#multiplicidad-geometrica) = $\dim(E_\lambda)$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Calcular eigenvalores | Con multiplicidades algebraicas |
| 2 | Calcular cada $m_g(\lambda)$ | $m_g = n - \text{rango}(A - \lambda I)$ |
| 3 | Comparar | $m_g(\lambda) = m_a(\lambda)$ para todos |
| 4 | Concluir | Si coinciden → diagonalizable |

### Atajos

| Condición | Resultado |
|-----------|-----------|
| $n$ eigenvalores distintos | Siempre diagonalizable |
| [Matriz simétrica](../../../glossary.md#matriz-simetrica) ($A = A^T$) | Siempre diagonalizable |
| Algún $m_g < m_a$ | NO diagonalizable |

### Ejemplo: Matriz Diagonalizable

**Problema:** ¿Es $A = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 3 \end{pmatrix}$ diagonalizable?

---

**Paso 1: Encontrar eigenvalores**

$A$ es triangular: eigenvalores = $\{1, 3, 3\}$

- $\lambda_1 = 1$ con $m_a(1) = 1$
- $\lambda_2 = 3$ con $m_a(3) = 2$

---

**Paso 2: Calcular [multiplicidad geométrica](../../../glossary.md#multiplicidad-geometrica) de $\lambda = 3$**

$$A - 3I = \begin{pmatrix} -2 & 2 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$$

$\text{rango}(A - 3I) = 1$

$m_g(3) = 3 - 1 = 2$

---

**Paso 3: Comparar**

- $m_g(1) = 1 = m_a(1)$ ✓
- $m_g(3) = 2 = m_a(3)$ ✓

$$\boxed{A \text{ es diagonalizable}}$$

---

### Ejemplo: Matriz NO Diagonalizable

**Problema:** ¿Es $A = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$ diagonalizable?

---

**Paso 1: Encontrar eigenvalores**

$\lambda = 2$ con $m_a(2) = 2$

---

**Paso 2: Calcular multiplicidad geométrica**

$$A - 2I = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$$

$\text{rango}(A - 2I) = 1$

$m_g(2) = 2 - 1 = 1$

---

**Paso 3: Comparar**

$m_g(2) = 1 < 2 = m_a(2)$ ✗

$$\boxed{A \text{ NO es diagonalizable}}$$

---

## Método 5: Diagonalizar una Matriz

**Cuándo Usar:** Para descomponer $A$ en la forma $A = PDP^{-1}$.

**Estructura:**
- $P$ = matriz de eigenvectores (como columnas)
- $D$ = matriz diagonal con eigenvalores
- El [orden](../../../glossary.md#orden) de eigenvalores en $D$ debe corresponder al orden de eigenvectores en $P$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Verificar diagonalizabilidad | $m_g = m_a$ para todos |
| 2 | Encontrar base de cada $E_\lambda$ | Eigenvectores LI |
| 3 | Formar $P$ | Eigenvectores como columnas |
| 4 | Formar $D$ | Eigenvalores en diagonal correspondiente |
| 5 | Verificar | $AP = PD$ |

### Ejemplo Detallado

**Problema:** Diagonalizar $A = \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$

---

**Paso 1: Encontrar eigenvalores**

$$p(\lambda) = \lambda^2 - 2\lambda - 3 = (\lambda - 3)(\lambda + 1) = 0$$

$\lambda_1 = 3$, $\lambda_2 = -1$

---

**Paso 2: Encontrar eigenvectores**

**Para $\lambda_1 = 3$:**
$$A - 3I = \begin{pmatrix} -2 & 2 \\ 2 & -2 \end{pmatrix} \rightarrow \begin{pmatrix} 1 & -1 \\ 0 & 0 \end{pmatrix}$$

$x_1 = x_2$, sea $x_2 = 1$: $\mathbf{v}_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$

**Para $\lambda_2 = -1$:**
$$A - (-1)I = A + I = \begin{pmatrix} 2 & 2 \\ 2 & 2 \end{pmatrix} \rightarrow \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$$

$x_1 = -x_2$, sea $x_2 = 1$: $\mathbf{v}_2 = \begin{pmatrix} -1 \\ 1 \end{pmatrix}$

---

**Paso 3: Formar $P$ y $D$**

$$P = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}, \quad D = \begin{pmatrix} 3 & 0 \\ 0 & -1 \end{pmatrix}$$

---

**Paso 4: Calcular $P^{-1}$**

$$\det(P) = 1 - (-1) = 2$$

$$P^{-1} = \frac{1}{2}\begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix}$$

---

**Paso 5: Verificación**

$$PDP^{-1} = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} 3 & 0 \\ 0 & -1 \end{pmatrix}\frac{1}{2}\begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix}$$

$$= \begin{pmatrix} 3 & 1 \\ 3 & -1 \end{pmatrix}\frac{1}{2}\begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix}$$

$$= \frac{1}{2}\begin{pmatrix} 3-1 & 3+1 \\ 3+1 & 3-1 \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix} = A \checkmark$$

$$\boxed{A = PDP^{-1} = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} 3 & 0 \\ 0 & -1 \end{pmatrix}\begin{pmatrix} 1/2 & 1/2 \\ -1/2 & 1/2 \end{pmatrix}}$$

---

## Método 6: Calcular Potencias de Matrices

**Cuándo Usar:** Para calcular $A^k$ eficientemente cuando $A$ es diagonalizable.

**Fórmula:** Si $A = PDP^{-1}$, entonces:
$$A^k = PD^kP^{-1}$$

donde $D^k$ se calcula elevando cada elemento diagonal a la potencia $k$.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Diagonalizar | $A = PDP^{-1}$ |
| 2 | Calcular $D^k$ | $D^k = \text{diag}(\lambda_1^k, \ldots, \lambda_n^k)$ |
| 3 | Multiplicar | $A^k = PD^kP^{-1}$ |

### Ejemplo Detallado

**Problema:** Calcular $A^{10}$ para $A = \begin{pmatrix} 3 & 2 \\ 0 & 1 \end{pmatrix}$

---

**Paso 1: Encontrar eigenvalores y eigenvectores**

$A$ es triangular: $\lambda_1 = 3$, $\lambda_2 = 1$

**Para $\lambda_1 = 3$:**
$$A - 3I = \begin{pmatrix} 0 & 2 \\ 0 & -2 \end{pmatrix}$$
$x_2 = 0$, $\mathbf{v}_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$

**Para $\lambda_2 = 1$:**
$$A - I = \begin{pmatrix} 2 & 2 \\ 0 & 0 \end{pmatrix}$$
$x_1 = -x_2$, $\mathbf{v}_2 = \begin{pmatrix} -1 \\ 1 \end{pmatrix}$

---

**Paso 2: Formar $P$, $D$, $P^{-1}$**

$$P = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}, \quad D = \begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix}$$

$$P^{-1} = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$$

---

**Paso 3: Calcular $D^{10}$**

$$D^{10} = \begin{pmatrix} 3^{10} & 0 \\ 0 & 1^{10} \end{pmatrix} = \begin{pmatrix} 59049 & 0 \\ 0 & 1 \end{pmatrix}$$

---

**Paso 4: Calcular $A^{10} = PD^{10}P^{-1}$**

$$PD^{10} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 59049 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 59049 & -1 \\ 0 & 1 \end{pmatrix}$$

$$A^{10} = \begin{pmatrix} 59049 & -1 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 59049 & 59048 \\ 0 & 1 \end{pmatrix}$$

$$\boxed{A^{10} = \begin{pmatrix} 59049 & 59048 \\ 0 & 1 \end{pmatrix}}$$

---

**Fórmula general para este tipo de matriz:**

$$A^k = \begin{pmatrix} 3^k & 3^k - 1 \\ 0 & 1 \end{pmatrix}$$

---

## Método 7: Diagonalización Ortogonal (Matrices Simétricas)

**Cuándo Usar:** Para matrices simétricas ($A = A^T$), que siempre son diagonalizables ortogonalmente.

**Teorema Espectral:** Si $A = A^T$, entonces:
1. Todos los eigenvalores son reales
2. Eigenvectores de distintos eigenvalores son ortogonales
3. Existe $Q$ ortogonal ($Q^TQ = I$) [tal que](../../../glossary.md#tal-que) $Q^TAQ = D$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Verificar simetría | $A = A^T$ |
| 2 | Encontrar eigenvalores | Serán reales |
| 3 | Encontrar eigenvectores | Para cada eigenvalor |
| 4 | Ortonormalizar | Gram-Schmidt si $m_a > 1$ |
| 5 | Formar $Q$ | Columnas = eigenvectores ortonormales |
| 6 | Verificar | $Q^TQ = I$ y $Q^TAQ = D$ |

### Ejemplo Detallado

**Problema:** Diagonalizar ortogonalmente $A = \begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix}$

---

**Paso 1: Verificar simetría**

$A^T = \begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix} = A$ ✓

---

**Paso 2: Encontrar eigenvalores**

$$p(\lambda) = (3-\lambda)^2 - 1 = \lambda^2 - 6\lambda + 8 = (\lambda - 4)(\lambda - 2)$$

$\lambda_1 = 4$, $\lambda_2 = 2$

---

**Paso 3: Encontrar eigenvectores**

**Para $\lambda_1 = 4$:**
$$A - 4I = \begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix}$$

$x_1 = x_2$: $\mathbf{v}_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$

**Para $\lambda_2 = 2$:**
$$A - 2I = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$$

$x_1 = -x_2$: $\mathbf{v}_2 = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$

---

**Paso 4: Verificar ortogonalidad**

$$\mathbf{v}_1 \cdot \mathbf{v}_2 = (1)(1) + (1)(-1) = 0 \checkmark$$

---

**Paso 5: Normalizar**

$$\|\mathbf{v}_1\| = \sqrt{1 + 1} = \sqrt{2}$$

$$\mathbf{q}_1 = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix}$$

$$\|\mathbf{v}_2\| = \sqrt{1 + 1} = \sqrt{2}$$

$$\mathbf{q}_2 = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -1 \end{pmatrix}$$

---

**Paso 6: Formar $Q$ y $D$**

$$Q = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}, \quad D = \begin{pmatrix} 4 & 0 \\ 0 & 2 \end{pmatrix}$$

---

**Verificación:**

$$Q^TQ = \frac{1}{2}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} = \frac{1}{2}\begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} = I \checkmark$$

$$\boxed{A = QDQ^T = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}\begin{pmatrix} 4 & 0 \\ 0 & 2 \end{pmatrix}\frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}}$$

---

## Método 8: Estado Estacionario (Cadenas de Markov)

**Cuándo Usar:** Para encontrar la distribución [límite](../../../glossary.md#limite) de una cadena de Markov.

**Definición:** Una matriz de Markov $P$ satisface:
- Todos los elementos son $\geq 0$
- Las columnas suman 1

**Estado estacionario:** [Vector](../../../glossary.md#vector) $\mathbf{\pi}$ tal que $P\mathbf{\pi} = \mathbf{\pi}$ con $\sum \pi_i = 1$.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Verificar matriz de Markov | Elementos $\geq 0$, columnas suman 1 |
| 2 | Formar $(P - I)\mathbf{x} = \mathbf{0}$ | Buscar eigenvector de $\lambda = 1$ |
| 3 | Resolver sistema | Encontrar espacio nulo |
| 4 | Normalizar | Hacer que componentes sumen 1 |

### Ejemplo Detallado

**Problema:** Una ciudad tiene dos estados de clima: Soleado (S) y Lluvioso (L). La matriz de transición es:

$$P = \begin{pmatrix} 0.8 & 0.4 \\ 0.2 & 0.6 \end{pmatrix}$$

Encontrar la distribución de clima a largo plazo.

---

**Paso 1: Verificar matriz de Markov**

- Elementos $\geq 0$ ✓
- Columna 1: $0.8 + 0.2 = 1$ ✓
- Columna 2: $0.4 + 0.6 = 1$ ✓

---

**Paso 2: Resolver $(P - I)\mathbf{x} = \mathbf{0}$**

$$P - I = \begin{pmatrix} 0.8 - 1 & 0.4 \\ 0.2 & 0.6 - 1 \end{pmatrix} = \begin{pmatrix} -0.2 & 0.4 \\ 0.2 & -0.4 \end{pmatrix}$$

---

**Paso 3: Reducir**

$$\begin{pmatrix} -0.2 & 0.4 \\ 0.2 & -0.4 \end{pmatrix} \rightarrow \begin{pmatrix} 1 & -2 \\ 0 & 0 \end{pmatrix}$$

Sistema: $x_1 - 2x_2 = 0 \Rightarrow x_1 = 2x_2$

Eigenvector: $\mathbf{v} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$

---

**Paso 4: Normalizar para que sume 1**

$2 + 1 = 3$

$$\mathbf{\pi} = \frac{1}{3}\begin{pmatrix} 2 \\ 1 \end{pmatrix} = \begin{pmatrix} 2/3 \\ 1/3 \end{pmatrix}$$

---

**Interpretación:**

$$\boxed{\text{A largo plazo: } 66.7\% \text{ Soleado}, \quad 33.3\% \text{ Lluvioso}}$$

---

**Verificación:**

$$P\mathbf{\pi} = \begin{pmatrix} 0.8 & 0.4 \\ 0.2 & 0.6 \end{pmatrix}\begin{pmatrix} 2/3 \\ 1/3 \end{pmatrix} = \begin{pmatrix} 1.6/3 + 0.4/3 \\ 0.4/3 + 0.6/3 \end{pmatrix} = \begin{pmatrix} 2/3 \\ 1/3 \end{pmatrix} = \mathbf{\pi} \checkmark$$

---

## Método 9: Forma de Jordan (Matrices NO Diagonalizables)

**Cuándo Usar:** Cuando $A$ no es diagonalizable pero necesitamos una forma "casi diagonal".

**Definición:** Para cada eigenvalor $\lambda$ con $m_a > m_g$, usamos bloques de Jordan:
$$J_k(\lambda) = \begin{pmatrix} \lambda & 1 & 0 & \cdots \\ 0 & \lambda & 1 & \cdots \\ \vdots & & \ddots & 1 \\ 0 & \cdots & 0 & \lambda \end{pmatrix}_{k \times k}$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Encontrar eigenvalores | Con multiplicidades |
| 2 | Calcular $m_g$ para cada $\lambda$ | Número de bloques de Jordan |
| 3 | Determinar tamaño de bloques | $m_a = \sum$ tamaños |
| 4 | Encontrar cadenas de Jordan | Vectores propios generalizados |
| 5 | Formar $P$ y $J$ | $A = PJP^{-1}$ |

### Ejemplo Detallado

**Problema:** Encontrar la forma de Jordan de $A = \begin{pmatrix} 5 & 4 & 2 \\ 0 & 5 & 3 \\ 0 & 0 & 5 \end{pmatrix}$

---

**Paso 1: Encontrar eigenvalores**

$A$ es triangular: $\lambda = 5$ con $m_a(5) = 3$

---

**Paso 2: Calcular multiplicidad geométrica**

$$A - 5I = \begin{pmatrix} 0 & 4 & 2 \\ 0 & 0 & 3 \\ 0 & 0 & 0 \end{pmatrix}$$

$\text{rango}(A - 5I) = 2$

$m_g(5) = 3 - 2 = 1$

Como $m_g(5) = 1 < 3 = m_a(5)$, hay UN bloque de Jordan de tamaño 3.

---

**Paso 3: Forma de Jordan**

$$\boxed{J = \begin{pmatrix} 5 & 1 & 0 \\ 0 & 5 & 1 \\ 0 & 0 & 5 \end{pmatrix}}$$

---

**Paso 4: Encontrar vectores generalizados**

Eigenvector: $(A - 5I)\mathbf{v}_1 = \mathbf{0}$

Del sistema: $4x_2 + 2x_3 = 0$, $3x_3 = 0$

$x_3 = 0$, $x_2 = 0$, $x_1$ libre: $\mathbf{v}_1 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$

[Vector](../../../glossary.md#vector) generalizado de rango 2: $(A - 5I)\mathbf{v}_2 = \mathbf{v}_1$

$$\begin{pmatrix} 0 & 4 & 2 \\ 0 & 0 & 3 \\ 0 & 0 & 0 \end{pmatrix}\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$$

$3z = 0 \Rightarrow z = 0$, $4y = 1 \Rightarrow y = 1/4$

$\mathbf{v}_2 = \begin{pmatrix} 0 \\ 1/4 \\ 0 \end{pmatrix}$

Vector generalizado de rango 3: $(A - 5I)\mathbf{v}_3 = \mathbf{v}_2$

$$\begin{pmatrix} 0 & 4 & 2 \\ 0 & 0 & 3 \\ 0 & 0 & 0 \end{pmatrix}\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 0 \\ 1/4 \\ 0 \end{pmatrix}$$

$3z = 1/4 \Rightarrow z = 1/12$, $4y + 2(1/12) = 0 \Rightarrow y = -1/24$

$\mathbf{v}_3 = \begin{pmatrix} 0 \\ -1/24 \\ 1/12 \end{pmatrix}$

---

**Matriz de paso:**

$$P = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1/4 & -1/24 \\ 0 & 0 & 1/12 \end{pmatrix}$$

$$\boxed{A = PJP^{-1}}$$

---

## Método 10: Exponencial de Matrices

**Cuándo Usar:** Para resolver sistemas de EDOs lineales $\mathbf{x}' = A\mathbf{x}$.

**Definición:**
$$e^{At} = \sum_{k=0}^{\infty} \frac{(At)^k}{k!} = I + At + \frac{(At)^2}{2!} + \cdots$$

### Caso Diagonalizable

Si $A = PDP^{-1}$:
$$e^{At} = Pe^{Dt}P^{-1}$$

donde $e^{Dt} = \text{diag}(e^{\lambda_1 t}, \ldots, e^{\lambda_n t})$

### Ejemplo Detallado

**Problema:** Calcular $e^{At}$ para $A = \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}$

---

**Paso 1: Diagonalizar**

Eigenvalores: $\lambda_1 = 1$, $\lambda_2 = 3$

Eigenvectores: $\mathbf{v}_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$, $\mathbf{v}_2 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$

$$P = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}, \quad P^{-1} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$$

---

**Paso 2: Calcular $e^{Dt}$**

$$D = \begin{pmatrix} 1 & 0 \\ 0 & 3 \end{pmatrix}, \quad e^{Dt} = \begin{pmatrix} e^t & 0 \\ 0 & e^{3t} \end{pmatrix}$$

---

**Paso 3: Calcular $e^{At} = Pe^{Dt}P^{-1}$**

$$Pe^{Dt} = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} e^t & 0 \\ 0 & e^{3t} \end{pmatrix} = \begin{pmatrix} e^t & e^{3t} \\ 0 & e^{3t} \end{pmatrix}$$

$$e^{At} = \begin{pmatrix} e^t & e^{3t} \\ 0 & e^{3t} \end{pmatrix}\begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} e^t & e^{3t} - e^t \\ 0 & e^{3t} \end{pmatrix}$$

$$\boxed{e^{At} = \begin{pmatrix} e^t & e^{3t} - e^t \\ 0 & e^{3t} \end{pmatrix}}$$

---

**Aplicación:** Solución de $\mathbf{x}' = A\mathbf{x}$ con $\mathbf{x}(0) = \mathbf{x}_0$:

$$\mathbf{x}(t) = e^{At}\mathbf{x}_0$$

---

## Método 11: Teorema de Cayley-Hamilton

**Cuándo Usar:** Para expresar potencias altas de $A$ o calcular $A^{-1}$ usando el [polinomio característico](../../../glossary.md#polinomio-caracteristico).

**Teorema:** Toda matriz satisface su propio [polinomio](../../../glossary.md#polinomio) característico:
$$p(A) = 0$$

### Aplicación: Calcular $A^{-1}$

Para $A$ de 2×2 con $p(\lambda) = \lambda^2 - \text{tr}(A)\lambda + \det(A)$:

$$A^2 - \text{tr}(A) \cdot A + \det(A) \cdot I = 0$$

Despejando:
$$A^{-1} = \frac{1}{\det(A)}(\text{tr}(A) \cdot I - A)$$

### Ejemplo Detallado

**Problema:** Usar Cayley-Hamilton para calcular $A^{-1}$ donde $A = \begin{pmatrix} 3 & 1 \\ 2 & 4 \end{pmatrix}$

---

**Paso 1: Calcular traza y determinante**

$$\text{tr}(A) = 3 + 4 = 7$$
$$\det(A) = 12 - 2 = 10$$

---

**Paso 2: Aplicar Cayley-Hamilton**

$$A^2 - 7A + 10I = 0$$

Despejando:
$$A^{-1} = \frac{1}{10}(7I - A) = \frac{1}{10}\left(\begin{pmatrix} 7 & 0 \\ 0 & 7 \end{pmatrix} - \begin{pmatrix} 3 & 1 \\ 2 & 4 \end{pmatrix}\right)$$

$$= \frac{1}{10}\begin{pmatrix} 4 & -1 \\ -2 & 3 \end{pmatrix}$$

$$\boxed{A^{-1} = \begin{pmatrix} 0.4 & -0.1 \\ -0.2 & 0.3 \end{pmatrix}}$$

---

**Verificación:**

$$AA^{-1} = \begin{pmatrix} 3 & 1 \\ 2 & 4 \end{pmatrix}\frac{1}{10}\begin{pmatrix} 4 & -1 \\ -2 & 3 \end{pmatrix} = \frac{1}{10}\begin{pmatrix} 10 & 0 \\ 0 & 10 \end{pmatrix} = I \checkmark$$

---

## Resumen de Fórmulas

| Concepto | Fórmula |
|----------|---------|
| Polinomio característico | $p(\lambda) = \det(A - \lambda I)$ |
| Eigenvalores 2×2 | $\lambda = \frac{\text{tr}(A) \pm \sqrt{\text{tr}(A)^2 - 4\det(A)}}{2}$ |
| Eigenvector | Resolver $(A - \lambda I)\mathbf{v} = \mathbf{0}$ |
| [Diagonalización](../../../glossary.md#diagonalizacion) | $A = PDP^{-1}$ |
| Potencias | $A^k = PD^kP^{-1}$ |
| Diag. ortogonal | $A = QDQ^T$ para $A$ simétrica |
| Estado estacionario | $(P - I)\mathbf{\pi} = \mathbf{0}$, $\sum \pi_i = 1$ |
| Exponencial | $e^{At} = Pe^{Dt}P^{-1}$ |
| Cayley-Hamilton | $p(A) = 0$ |
| Multiplicidad | $1 \leq m_g(\lambda) \leq m_a(\lambda)$ |

---

## Errores Comunes

| Error | Corrección |
|-------|------------|
| Confundir $m_a$ con $m_g$ | $m_a$ = algebraica (polinomio), $m_g$ = geométrica (eigenespacio) |
| Ordenar mal $P$ y $D$ | El [orden](../../../glossary.md#orden) de columnas en $P$ debe corresponder a diagonal de $D$ |
| Olvidar normalizar en Markov | El vector de estado debe sumar 1 |
| Usar RREF para eigenvalores | Solo REF; los eigenvalores ya están en el polinomio |
| Asumir diagonalizable | Verificar siempre que $m_g = m_a$ |
| Confundir $Q^{-1}$ con $Q^T$ | Solo para matrices ortogonales: $Q^{-1} = Q^T$ |
| Calcular mal $e^{Dt}$ | Cada elemento diagonal se eleva: $e^{\lambda_i t}$ |
