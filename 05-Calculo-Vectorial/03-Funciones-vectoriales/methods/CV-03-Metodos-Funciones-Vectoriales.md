<!--
::METADATA::
type: method
topic_id: cv-03-funciones-vectoriales
file_id: CV-03-Metodos-Funciones-Vectoriales
status: stable
audience: student
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../glossary.md)

---

# Métodos para Funciones Vectoriales

> **Objetivo:** Dominar el análisis de funciones vectoriales con algoritmos detallados, cálculos intermedios y ejemplos clásicos paso a paso.

---

## Método 1: Dominio de una Función Vectorial

### Cuándo Usar
- Determinar los valores de $t$ para los cuales $\mathbf{r}(t)$ está definida

### Fórmula
Para $\mathbf{r}(t) = \langle f(t), g(t), h(t) \rangle$:
$$\text{Dom}(\mathbf{r}) = \text{Dom}(f) \cap \text{Dom}(g) \cap \text{Dom}(h)$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|  
| 1 | Identificar cada componente | $f(t)$, $g(t)$, $h(t)$ |
| 2 | Encontrar [dominio](../../../glossary.md#dominio) de cada una | Restricciones individuales |
| 3 | Intersecar dominios | Dom($\mathbf{r}$) = $\cap$ dominios |

### Ejemplo Detallado

**Problema:** Encontrar el [dominio](../../../glossary.md#dominio) de $\mathbf{r}(t) = \langle \sqrt{t}, \ln(4-t), e^t \rangle$

**Paso 1:** Identificamos restricciones:
- $\sqrt{t}$ requiere $t \geq 0$
- $\ln(4-t)$ requiere $4 - t > 0$, es decir $t < 4$
- $e^t$ está definida para todo $t \in \mathbb{R}$

**Paso 2:** Intersectamos:
$$[0, \infty) \cap (-\infty, 4) \cap \mathbb{R} = [0, 4)$$

**Resultado:** El dominio es $\boxed{[0, 4)}$

---

## Método 2: Límite de una Función Vectorial

### Cuándo Usar
- Calcular $\lim_{t \to a} \mathbf{r}(t)$

### Fórmula
$$\lim_{t \to a} \mathbf{r}(t) = \left\langle \lim_{t \to a} f(t), \lim_{t \to a} g(t), \lim_{t \to a} h(t) \right\rangle$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|  
| 1 | Calcular [límite](../../../glossary.md#limite) de cada componente | Por separado |
| 2 | Si todos existen | El límite vectorial existe |
| 3 | Si alguno no existe | El límite vectorial no existe |

### Ejemplo Detallado

**Problema:** Calcular $\lim_{t \to 0} \left\langle \frac{\sin t}{t}, e^t, \frac{1-\cos t}{t^2} \right\rangle$

**Paso 1:** Límite de la primera componente:
$$\lim_{t \to 0} \frac{\sin t}{t} = 1$$

**Paso 2:** Límite de la segunda componente:
$$\lim_{t \to 0} e^t = 1$$

**Paso 3:** Límite de la tercera componente (L'Hôpital o identidad):
$$\lim_{t \to 0} \frac{1-\cos t}{t^2} = \lim_{t \to 0} \frac{\sin t}{2t} = \frac{1}{2}$$

**Resultado:** 
$$\lim_{t \to 0} \mathbf{r}(t) = \boxed{\left\langle 1, 1, \frac{1}{2} \right\rangle}$$

---

## Método 3: Derivada de una Función Vectorial

### Cuándo Usar
- Encontrar el [vector](../../../glossary.md#vector) [tangente](../../../glossary.md#tangente) $\mathbf{r}'(t)$
- Calcular velocidad en curvas del espacio

### Fórmula
$$\mathbf{r}'(t) = \langle f'(t), g'(t), h'(t) \rangle$$

### Reglas de Derivación

| Operación | Fórmula |
|-----------|---------|
| Suma | $(\mathbf{u} + \mathbf{v})' = \mathbf{u}' + \mathbf{v}'$ |
| Escalar por [vector](../../../glossary.md#funcion) por vector | $(f \cdot \mathbf{u})' = f'\mathbf{u} + f\mathbf{u}'$ |
| Producto punto | $(\mathbf{u} \cdot \mathbf{v})' = \mathbf{u}' \cdot \mathbf{v} + \mathbf{u} \cdot \mathbf{v}'$ |
| Producto cruz | $(\mathbf{u} \times \mathbf{v})' = \mathbf{u}' \times \mathbf{v} + \mathbf{u} \times \mathbf{v}'$ |
| [Composición](../../../glossary.md#composicion) | $[\mathbf{u}(f(t))]' = \mathbf{u}'(f(t)) \cdot f'(t)$ |

### Ejemplo Detallado

**Problema:** Encontrar $\mathbf{r}'(t)$ para $\mathbf{r}(t) = \langle t^3, \cos(2t), e^{-t} \rangle$

**Paso 1:** Derivamos cada componente:
$$f(t) = t^3 \implies f'(t) = 3t^2$$
$$g(t) = \cos(2t) \implies g'(t) = -2\sin(2t)$$
$$h(t) = e^{-t} \implies h'(t) = -e^{-t}$$

**Resultado:**
$$\mathbf{r}'(t) = \boxed{\langle 3t^2, -2\sin(2t), -e^{-t} \rangle}$$

---

## Método 4: Integral de una Función Vectorial

### Cuándo Usar
- Recuperar posición a partir de velocidad
- Calcular integrales definidas de funciones vectoriales

### Fórmulas
**[Integral indefinida](../../../glossary.md#integral-indefinida):**
$$\int \mathbf{r}(t)\, dt = \left\langle \int f(t)\, dt, \int g(t)\, dt, \int h(t)\, dt \right\rangle$$

**[Integral definida](../../../glossary.md#integral-definida):**
$$\int_a^b \mathbf{r}(t)\, dt = \left\langle \int_a^b f(t)\, dt, \int_a^b g(t)\, dt, \int_a^b h(t)\, dt \right\rangle$$

### Ejemplo Detallado

**Problema:** Si $\mathbf{v}(t) = \langle 2t, 3, \cos t \rangle$ y $\mathbf{r}(0) = \langle 1, 0, 0 \rangle$, encontrar $\mathbf{r}(t)$

**Paso 1:** Integramos la velocidad:
$$\mathbf{r}(t) = \int \mathbf{v}(t)\, dt = \left\langle t^2 + C_1, 3t + C_2, \sin t + C_3 \right\rangle$$

**Paso 2:** Aplicamos condición inicial $\mathbf{r}(0) = \langle 1, 0, 0 \rangle$:
$$\langle C_1, C_2, C_3 \rangle = \langle 1, 0, 0 \rangle$$

**Resultado:**
$$\mathbf{r}(t) = \boxed{\langle t^2 + 1, 3t, \sin t \rangle}$$

---

## Método 5: Velocidad, Rapidez y Aceleración

### Cuándo Usar
- Análisis cinemático de partículas en movimiento

### Fórmulas

| Concepto | Fórmula | Descripción |
|----------|---------|-------------|
| **Posición** | $\mathbf{r}(t)$ | Vector de posición |
| **Velocidad** | $\mathbf{v}(t) = \mathbf{r}'(t)$ | Vector tangente |
| **Rapidez** | $\|\mathbf{v}(t)\| = \sqrt{v_x^2 + v_y^2 + v_z^2}$ | Magnitud escalar |
| **Aceleración** | $\mathbf{a}(t) = \mathbf{v}'(t) = \mathbf{r}''(t)$ | Cambio de velocidad |

### Ejemplo Detallado

**Problema:** Una partícula tiene posición $\mathbf{r}(t) = \langle t, t^2, t^3 \rangle$. Encontrar velocidad, rapidez y aceleración en $t = 1$.

**Paso 1:** Calculamos la velocidad:
$$\mathbf{v}(t) = \mathbf{r}'(t) = \langle 1, 2t, 3t^2 \rangle$$
$$\mathbf{v}(1) = \langle 1, 2, 3 \rangle$$

**Paso 2:** Calculamos la rapidez:
$$\|\mathbf{v}(1)\| = \sqrt{1^2 + 2^2 + 3^2} = \sqrt{14}$$

**Paso 3:** Calculamos la aceleración:
$$\mathbf{a}(t) = \mathbf{v}'(t) = \langle 0, 2, 6t \rangle$$
$$\mathbf{a}(1) = \langle 0, 2, 6 \rangle$$

**Resultado:**
- Velocidad: $\mathbf{v}(1) = \boxed{\langle 1, 2, 3 \rangle}$
- Rapidez: $\|\mathbf{v}(1)\| = \boxed{\sqrt{14}}$
- Aceleración: $\mathbf{a}(1) = \boxed{\langle 0, 2, 6 \rangle}$

---

## Método 6: Vector Tangente Unitario (T)

### Cuándo Usar
- Encontrar la dirección del movimiento (normalizado)
- Primer vector del marco de Frenet-Serret

### Fórmula
$$\mathbf{T}(t) = \frac{\mathbf{r}'(t)}{\|\mathbf{r}'(t)\|}$$

### Algoritmo de Resolución

| Paso | Acción | Cálculo |
|------|--------|---------|
| 1 | Calcular $\mathbf{r}'(t)$ | Derivar |
| 2 | Calcular $\|\mathbf{r}'(t)\|$ | Magnitud |
| 3 | Dividir | $\mathbf{T} = \frac{\mathbf{r}'}{\|\mathbf{r}'\|}$ |

### Ejemplo Detallado

**Problema:** Encontrar $\mathbf{T}(t)$ para la hélice $\mathbf{r}(t) = \langle \cos t, \sin t, t \rangle$

**Paso 1:** Calculamos $\mathbf{r}'(t)$:
$$\mathbf{r}'(t) = \langle -\sin t, \cos t, 1 \rangle$$

**Paso 2:** Calculamos la magnitud:
$$\|\mathbf{r}'(t)\| = \sqrt{\sin^2 t + \cos^2 t + 1} = \sqrt{2}$$

**Paso 3:** Dividimos:
$$\mathbf{T}(t) = \frac{1}{\sqrt{2}}\langle -\sin t, \cos t, 1 \rangle$$

**Resultado:**
$$\mathbf{T}(t) = \boxed{\left\langle \frac{-\sin t}{\sqrt{2}}, \frac{\cos t}{\sqrt{2}}, \frac{1}{\sqrt{2}} \right\rangle}$$

**Verificación:** $\|\mathbf{T}\| = \frac{1}{2}(\sin^2 t + \cos^2 t + 1) = 1$ ✓

---

## Método 7: Vector Normal Principal (N)

### Cuándo Usar
- Encontrar la dirección en que "gira" la curva
- Segundo vector del marco de Frenet-Serret

### Fórmula
$$\mathbf{N}(t) = \frac{\mathbf{T}'(t)}{\|\mathbf{T}'(t)\|}$$

### Algoritmo de Resolución

| Paso | Acción | Cálculo |
|------|--------|---------|
| 1 | Calcular $\mathbf{T}(t)$ | Método 6 |
| 2 | Derivar para obtener $\mathbf{T}'(t)$ | [Derivada](../../../glossary.md#derivada) de $\mathbf{T}$ |
| 3 | Normalizar | $\mathbf{N} = \frac{\mathbf{T}'}{\|\mathbf{T}'\|}$ |

### Ejemplo Detallado

**Problema:** Encontrar $\mathbf{N}(t)$ para la hélice $\mathbf{r}(t) = \langle \cos t, \sin t, t \rangle$

**Paso 1:** Ya tenemos $\mathbf{T}(t) = \frac{1}{\sqrt{2}}\langle -\sin t, \cos t, 1 \rangle$

**Paso 2:** Derivamos:
$$\mathbf{T}'(t) = \frac{1}{\sqrt{2}}\langle -\cos t, -\sin t, 0 \rangle$$

**Paso 3:** Calculamos la magnitud:
$$\|\mathbf{T}'(t)\| = \frac{1}{\sqrt{2}}\sqrt{\cos^2 t + \sin^2 t} = \frac{1}{\sqrt{2}}$$

**Paso 4:** Normalizamos:
$$\mathbf{N}(t) = \frac{\frac{1}{\sqrt{2}}\langle -\cos t, -\sin t, 0 \rangle}{\frac{1}{\sqrt{2}}} = \langle -\cos t, -\sin t, 0 \rangle$$

**Resultado:**
$$\mathbf{N}(t) = \boxed{\langle -\cos t, -\sin t, 0 \rangle}$$

> **Observación:** $\mathbf{N}$ apunta hacia el eje $z$ (centro de la hélice).

---

## Método 8: Vector Binormal (B)

### Cuándo Usar
- Completar el marco de Frenet-Serret
- Análisis de torsión de curvas

### Fórmula
$$\mathbf{B}(t) = \mathbf{T}(t) \times \mathbf{N}(t)$$

### Ejemplo Detallado

**Problema:** Encontrar $\mathbf{B}(t)$ para la hélice $\mathbf{r}(t) = \langle \cos t, \sin t, t \rangle$

**Paso 1:** Usamos los resultados anteriores:
$$\mathbf{T} = \frac{1}{\sqrt{2}}\langle -\sin t, \cos t, 1 \rangle$$
$$\mathbf{N} = \langle -\cos t, -\sin t, 0 \rangle$$

**Paso 2:** Calculamos el producto cruz:
$$\mathbf{B} = \mathbf{T} \times \mathbf{N} = \frac{1}{\sqrt{2}}\begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ -\sin t & \cos t & 1 \\ -\cos t & -\sin t & 0 \end{vmatrix}$$

$$= \frac{1}{\sqrt{2}}[\mathbf{i}(0 + \sin t) - \mathbf{j}(0 + \cos t) + \mathbf{k}(\sin^2 t + \cos^2 t)]$$

$$= \frac{1}{\sqrt{2}}\langle \sin t, -\cos t, 1 \rangle$$

**Resultado:**
$$\mathbf{B}(t) = \boxed{\frac{1}{\sqrt{2}}\langle \sin t, -\cos t, 1 \rangle}$$

---

## Método 9: Curvatura (κ)

### Cuándo Usar
- Medir qué tan rápido "gira" la curva
- Radio de curvatura: $\rho = \frac{1}{\kappa}$

### Fórmulas

**Fórmula general:**
$$\kappa = \frac{\|\mathbf{T}'(t)\|}{\|\mathbf{r}'(t)\|}$$

**Fórmula alternativa (más práctica):**
$$\kappa = \frac{\|\mathbf{r}'(t) \times \mathbf{r}''(t)\|}{\|\mathbf{r}'(t)\|^3}$$

**Para curvas planas** $y = f(x)$:
$$\kappa = \frac{|y''|}{(1 + (y')^2)^{3/2}}$$

### Ejemplo Detallado

**Problema:** Calcular la curvatura de $\mathbf{r}(t) = \langle t, t^2, 0 \rangle$ en $t = 1$

**Paso 1:** Calculamos las [derivadas](../../../glossary.md#derivadas):
$$\mathbf{r}'(t) = \langle 1, 2t, 0 \rangle$$
$$\mathbf{r}''(t) = \langle 0, 2, 0 \rangle$$

**Paso 2:** Calculamos el producto cruz:
$$\mathbf{r}' \times \mathbf{r}'' = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 2t & 0 \\ 0 & 2 & 0 \end{vmatrix} = \langle 0, 0, 2 \rangle$$

**Paso 3:** Calculamos las magnitudes:
$$\|\mathbf{r}' \times \mathbf{r}''\| = 2$$
$$\|\mathbf{r}'(1)\| = \sqrt{1 + 4} = \sqrt{5}$$

**Paso 4:** Aplicamos la fórmula:
$$\kappa = \frac{2}{(\sqrt{5})^3} = \frac{2}{5\sqrt{5}} = \frac{2\sqrt{5}}{25}$$

**Resultado:**
$$\kappa(1) = \boxed{\frac{2\sqrt{5}}{25}}$$

**Radio de curvatura:**
$$\rho = \frac{1}{\kappa} = \frac{25}{2\sqrt{5}} = \frac{5\sqrt{5}}{2}$$

---

## Método 10: Torsión (τ)

### Cuándo Usar
- Medir qué tanto la curva "sale" del plano osculador
- Curvas planas tienen $\tau = 0$

### Fórmula
$$\tau = \frac{(\mathbf{r}' \times \mathbf{r}'') \cdot \mathbf{r}'''}{\|\mathbf{r}' \times \mathbf{r}''\|^2}$$

### Algoritmo de Resolución

| Paso | Acción | Cálculo |
|------|--------|---------|
| 1 | Calcular $\mathbf{r}'$, $\mathbf{r}''$, $\mathbf{r}'''$ | Tres [derivadas](../../../glossary.md#derivadas) |
| 2 | Calcular $\mathbf{r}' \times \mathbf{r}''$ | Producto cruz |
| 3 | Calcular triple producto | $(\mathbf{r}' \times \mathbf{r}'') \cdot \mathbf{r}'''$ |
| 4 | Dividir por $\|\mathbf{r}' \times \mathbf{r}''\|^2$ | Aplicar fórmula |

### Ejemplo Detallado

**Problema:** Calcular la torsión de la hélice $\mathbf{r}(t) = \langle a\cos t, a\sin t, bt \rangle$

**Paso 1:** Calculamos las derivadas:
$$\mathbf{r}' = \langle -a\sin t, a\cos t, b \rangle$$
$$\mathbf{r}'' = \langle -a\cos t, -a\sin t, 0 \rangle$$
$$\mathbf{r}''' = \langle a\sin t, -a\cos t, 0 \rangle$$

**Paso 2:** Calculamos el producto cruz:
$$\mathbf{r}' \times \mathbf{r}'' = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ -a\sin t & a\cos t & b \\ -a\cos t & -a\sin t & 0 \end{vmatrix}$$

$$= \langle ab\sin t, -ab\cos t, a^2\sin^2 t + a^2\cos^2 t \rangle = \langle ab\sin t, -ab\cos t, a^2 \rangle$$

**Paso 3:** Calculamos el triple producto escalar:
$$(\mathbf{r}' \times \mathbf{r}'') \cdot \mathbf{r}''' = (ab\sin t)(a\sin t) + (-ab\cos t)(-a\cos t) + (a^2)(0)$$
$$= a^2b\sin^2 t + a^2b\cos^2 t = a^2b$$

**Paso 4:** Calculamos $\|\mathbf{r}' \times \mathbf{r}''\|^2$:
$$= a^2b^2\sin^2 t + a^2b^2\cos^2 t + a^4 = a^2b^2 + a^4 = a^2(a^2 + b^2)$$

**Paso 5:** Aplicamos la fórmula:
$$\tau = \frac{a^2b}{a^2(a^2 + b^2)} = \frac{b}{a^2 + b^2}$$

**Resultado:**
$$\tau = \boxed{\frac{b}{a^2 + b^2}}$$

> **Observación:** La torsión de una hélice es **constante**.

---

## Método 11: Componentes Tangencial y Normal de la Aceleración

### Cuándo Usar
- Descomponer la aceleración en dirección del movimiento ($a_T$) y perpendicular ($a_N$)

### Fórmulas
$$\mathbf{a} = a_T\mathbf{T} + a_N\mathbf{N}$$

donde:
$$a_T = \frac{\mathbf{v} \cdot \mathbf{a}}{\|\mathbf{v}\|} = \frac{d}{dt}\|\mathbf{v}\|$$

$$a_N = \frac{\|\mathbf{v} \times \mathbf{a}\|}{\|\mathbf{v}\|} = \kappa\|\mathbf{v}\|^2$$

### Interpretación

| Componente | Efecto |
|------------|--------|
| $a_T$ | Cambia la **rapidez** (acelera/desacelera) |
| $a_N$ | Cambia la **dirección** (giro) |

### Ejemplo Detallado

**Problema:** Encontrar $a_T$ y $a_N$ para $\mathbf{r}(t) = \langle t, t^2, t^3 \rangle$ en $t = 1$

**Paso 1:** Calculamos velocidad y aceleración:
$$\mathbf{v} = \langle 1, 2t, 3t^2 \rangle \implies \mathbf{v}(1) = \langle 1, 2, 3 \rangle$$
$$\mathbf{a} = \langle 0, 2, 6t \rangle \implies \mathbf{a}(1) = \langle 0, 2, 6 \rangle$$

**Paso 2:** Calculamos $\|\mathbf{v}\|$:
$$\|\mathbf{v}(1)\| = \sqrt{1 + 4 + 9} = \sqrt{14}$$

**Paso 3:** Calculamos $a_T$:
$$\mathbf{v} \cdot \mathbf{a} = (1)(0) + (2)(2) + (3)(6) = 0 + 4 + 18 = 22$$
$$a_T = \frac{22}{\sqrt{14}} = \frac{22\sqrt{14}}{14} = \frac{11\sqrt{14}}{7}$$

**Paso 4:** Calculamos $a_N$ usando $\mathbf{v} \times \mathbf{a}$:
$$\mathbf{v} \times \mathbf{a} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 2 & 3 \\ 0 & 2 & 6 \end{vmatrix} = \langle 12-6, 0-6, 2-0 \rangle = \langle 6, -6, 2 \rangle$$

$$\|\mathbf{v} \times \mathbf{a}\| = \sqrt{36 + 36 + 4} = \sqrt{76} = 2\sqrt{19}$$

$$a_N = \frac{2\sqrt{19}}{\sqrt{14}} = \frac{2\sqrt{266}}{14} = \frac{\sqrt{266}}{7}$$

**Resultado:**
- $a_T = \boxed{\frac{11\sqrt{14}}{7}}$ (componente tangencial)
- $a_N = \boxed{\frac{\sqrt{266}}{7}}$ (componente normal)

---

## Método 12: Longitud de Arco de Curva Espacial

### Cuándo Usar
- Calcular la longitud de una curva en el espacio

### Fórmula
$$L = \int_a^b \|\mathbf{r}'(t)\|\, dt = \int_a^b \sqrt{x'^2 + y'^2 + z'^2}\, dt$$

### Ejemplo Detallado

**Problema:** Calcular la longitud de la hélice $\mathbf{r}(t) = \langle 2\cos t, 2\sin t, 3t \rangle$ para $0 \leq t \leq 2\pi$

**Paso 1:** Calculamos $\mathbf{r}'(t)$:
$$\mathbf{r}'(t) = \langle -2\sin t, 2\cos t, 3 \rangle$$

**Paso 2:** Calculamos $\|\mathbf{r}'(t)\|$:
$$\|\mathbf{r}'(t)\| = \sqrt{4\sin^2 t + 4\cos^2 t + 9} = \sqrt{4 + 9} = \sqrt{13}$$

**Paso 3:** Integramos:
$$L = \int_0^{2\pi} \sqrt{13}\, dt = \sqrt{13} \cdot 2\pi = 2\pi\sqrt{13}$$

**Resultado:**
$$L = \boxed{2\pi\sqrt{13}}$$
