# Teoría — Funciones vectoriales

Las funciones vectoriales describen trayectorias en el espacio y son fundamentales en mecánica, animación y física.

---

## 3.1 Definición de función vectorial

Una **función vectorial** es una función cuyo dominio es un subconjunto de $\mathbb{R}$ y cuyo rango está en $\mathbb{R}^2$ o $\mathbb{R}^3$.

$$\mathbf{r}(t) = \langle x(t), y(t), z(t) \rangle = x(t)\,\mathbf{i} + y(t)\,\mathbf{j} + z(t)\,\mathbf{k}$$

- **Parámetro $t$**: Representa tiempo, ángulo o cualquier variable independiente.
- **Vector de posición**: $\mathbf{r}(t)$ indica la posición de una partícula en el instante $t$.
- **Curva en el espacio**: El conjunto de puntos $\{(x(t), y(t), z(t)) : t \in I\}$ forma una curva.

**Ejemplos clásicos**:

| Curva | Parametrización | Descripción |
|-------|-----------------|-------------|
| Hélice circular | $\mathbf{r}(t) = \langle \cos t, \sin t, t \rangle$ | Sube en espiral |
| Parábola en 3D | $\mathbf{r}(t) = \langle t, t^2, 2t \rangle$ | Trayectoria parabólica |
| Circunferencia | $\mathbf{r}(t) = \langle R\cos t, R\sin t, 0 \rangle$ | Radio $R$ en plano $xy$ |

---

## 3.2 Límites y continuidad

### Límite de una función vectorial

El límite se calcula **componente a componente**:

$$\lim_{t \to a} \mathbf{r}(t) = \left\langle \lim_{t \to a} x(t),\, \lim_{t \to a} y(t),\, \lim_{t \to a} z(t) \right\rangle$$

El límite existe si y solo si existen los tres límites escalares.

### Continuidad

$\mathbf{r}(t)$ es **continua en $t = a$** si:
1. $\mathbf{r}(a)$ está definida.
2. $\lim_{t \to a} \mathbf{r}(t)$ existe.
3. $\lim_{t \to a} \mathbf{r}(t) = \mathbf{r}(a)$.

**Criterio práctico**: Una función vectorial es continua si todas sus componentes son continuas (polinomios, exponenciales, senos, cosenos).

---

## 3.3 Derivada de una función vectorial

### Definición

$$\mathbf{r}'(t) = \lim_{h \to 0} \frac{\mathbf{r}(t+h) - \mathbf{r}(t)}{h} = \langle x'(t), y'(t), z'(t) \rangle$$

### Interpretación geométrica y física

| Concepto | Expresión | Significado |
|----------|-----------|-------------|
| **Vector tangente** | $\mathbf{r}'(t)$ | Dirección de movimiento |
| **Velocidad** | $\mathbf{v}(t) = \mathbf{r}'(t)$ | Vector velocidad |
| **Rapidez** | $\|\mathbf{r}'(t)\|$ | Magnitud de la velocidad (escalar) |
| **Aceleración** | $\mathbf{a}(t) = \mathbf{r}''(t)$ | Cambio de velocidad |

### Reglas de derivación

Sean $\mathbf{u}(t)$, $\mathbf{v}(t)$ funciones vectoriales y $f(t)$ escalar:

| Regla | Fórmula |
|-------|---------|
| Suma | $(\mathbf{u} + \mathbf{v})' = \mathbf{u}' + \mathbf{v}'$ |
| Producto por escalar | $(f\,\mathbf{u})' = f'\,\mathbf{u} + f\,\mathbf{u}'$ |
| Producto punto | $(\mathbf{u} \cdot \mathbf{v})' = \mathbf{u}' \cdot \mathbf{v} + \mathbf{u} \cdot \mathbf{v}'$ |
| Producto cruz | $(\mathbf{u} \times \mathbf{v})' = \mathbf{u}' \times \mathbf{v} + \mathbf{u} \times \mathbf{v}'$ |
| Regla de la cadena | $\mathbf{r}(f(t))' = \mathbf{r}'(f(t)) \cdot f'(t)$ |

---

## 3.4 Integración de funciones vectoriales

### Integral indefinida

$$\int \mathbf{r}(t)\,dt = \left\langle \int x(t)\,dt,\, \int y(t)\,dt,\, \int z(t)\,dt \right\rangle + \mathbf{C}$$

donde $\mathbf{C} = \langle C_1, C_2, C_3 \rangle$ es un **vector constante**.

### Integral definida

$$\int_a^b \mathbf{r}(t)\,dt = \left\langle \int_a^b x(t)\,dt,\, \int_a^b y(t)\,dt,\, \int_a^b z(t)\,dt \right\rangle$$

### Aplicación física

Si $\mathbf{v}(t)$ es la velocidad:
- **Desplazamiento**: $\Delta \mathbf{r} = \int_{t_1}^{t_2} \mathbf{v}(t)\,dt$
- **Posición**: $\mathbf{r}(t) = \mathbf{r}_0 + \int_0^t \mathbf{v}(\tau)\,d\tau$

---

## 3.5 Longitud de arco

### Fórmula general

Para una curva $\mathbf{r}(t)$ con $t \in [a, b]$:

$$L = \int_a^b \|\mathbf{r}'(t)\|\,dt = \int_a^b \sqrt{x'(t)^2 + y'(t)^2 + z'(t)^2}\,dt$$

### Función longitud de arco

$$s(t) = \int_{t_0}^t \|\mathbf{r}'(\tau)\|\,d\tau$$

Mide la "distancia recorrida" desde $t_0$ hasta $t$.

### Parametrización por longitud de arco

Una curva está parametrizada por longitud de arco si $\|\mathbf{r}'(s)\| = 1$ para todo $s$. Esto significa que el parámetro mide directamente la distancia sobre la curva.

**Ventaja**: Simplifica las fórmulas de curvatura y torsión.

---

## 3.6 Vectores T, N, B (Marco de Frenet-Serret)

El **triedro móvil** o **marco TNB** describe la geometría local de una curva.

### Vector tangente unitario $\mathbf{T}$

$$\mathbf{T}(t) = \frac{\mathbf{r}'(t)}{\|\mathbf{r}'(t)\|}$$

- Apunta en la dirección del movimiento.
- Tiene magnitud 1.

### Vector normal principal $\mathbf{N}$

$$\mathbf{N}(t) = \frac{\mathbf{T}'(t)}{\|\mathbf{T}'(t)\|}$$

- Perpendicular a $\mathbf{T}$.
- Apunta hacia el centro de curvatura.
- Solo existe si $\mathbf{T}'(t) \neq \mathbf{0}$.

### Vector binormal $\mathbf{B}$

$$\mathbf{B}(t) = \mathbf{T}(t) \times \mathbf{N}(t)$$

- Perpendicular a $\mathbf{T}$ y $\mathbf{N}$.
- Completa el sistema ortonormal dextrógiro.

### Planos fundamentales

| Plano | Vectores que lo generan | Descripción |
|-------|------------------------|-------------|
| **Osculador** | $\mathbf{T}$, $\mathbf{N}$ | "Mejor" plano que aproxima la curva |
| **Normal** | $\mathbf{N}$, $\mathbf{B}$ | Perpendicular a la tangente |
| **Rectificante** | $\mathbf{T}$, $\mathbf{B}$ | Contiene tangente y binormal |

---

## 3.7 Curvatura y torsión

### Curvatura $\kappa$

Mide qué tan rápido cambia la dirección de la curva.

**Fórmulas equivalentes**:

| Caso | Fórmula |
|------|---------|
| General | $\kappa = \dfrac{\|\mathbf{r}'(t) \times \mathbf{r}''(t)\|}{\|\mathbf{r}'(t)\|^3}$ |
| Por longitud de arco | $\kappa = \|\mathbf{T}'(s)\| = \|\mathbf{r}''(s)\|$ |
| Curva plana $y = f(x)$ | $\kappa = \dfrac{|y''|}{(1 + y'^2)^{3/2}}$ |

### Radio de curvatura

$$\rho = \frac{1}{\kappa}$$

Es el radio del **círculo osculador**, el círculo que mejor aproxima la curva en ese punto.

### Torsión $\tau$

Mide qué tan rápido la curva "sale" del plano osculador (giro fuera del plano).

$$\tau = \frac{(\mathbf{r}' \times \mathbf{r}'') \cdot \mathbf{r}'''}{\|\mathbf{r}' \times \mathbf{r}''\|^2}$$

**Interpretación**:
- $\tau > 0$: la curva gira como tornillo derecho.
- $\tau < 0$: la curva gira como tornillo izquierdo.
- $\tau = 0$: la curva es plana.

### Fórmulas de Frenet-Serret

$$\begin{aligned}
\mathbf{T}' &= \kappa\,\mathbf{N} \\
\mathbf{N}' &= -\kappa\,\mathbf{T} + \tau\,\mathbf{B} \\
\mathbf{B}' &= -\tau\,\mathbf{N}
\end{aligned}$$

Estas ecuaciones relacionan las derivadas del marco TNB con la curvatura y torsión.

---

## Resumen de fórmulas clave

| Concepto | Fórmula |
|----------|---------|
| Velocidad | $\mathbf{v}(t) = \mathbf{r}'(t)$ |
| Rapidez | $v = \|\mathbf{r}'(t)\|$ |
| Aceleración | $\mathbf{a}(t) = \mathbf{r}''(t)$ |
| Longitud de arco | $L = \int_a^b \|\mathbf{r}'(t)\|\,dt$ |
| Vector tangente | $\mathbf{T} = \mathbf{r}'/\|\mathbf{r}'\|$ |
| Vector normal | $\mathbf{N} = \mathbf{T}'/\|\mathbf{T}'\|$ |
| Vector binormal | $\mathbf{B} = \mathbf{T} \times \mathbf{N}$ |
| Curvatura | $\kappa = \|\mathbf{r}' \times \mathbf{r}''\|/\|\mathbf{r}'\|^3$ |
| Torsión | $\tau = (\mathbf{r}' \times \mathbf{r}'') \cdot \mathbf{r}'''/\|\mathbf{r}' \times \mathbf{r}''\|^2$ |
