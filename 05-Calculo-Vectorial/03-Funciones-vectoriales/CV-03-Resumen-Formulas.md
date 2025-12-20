<!--
::METADATA::
type: cheatsheet
topic_id: cv-03-funciones-vectoriales
file_id: CV-03-Resumen-Formulas
status: stable
audience: exam_review
requires: []
-->

# Resumen rápido — Funciones vectoriales

## Definición y operaciones básicas

| Concepto | Fórmula |
|----------|---------|
| **Función vectorial** | $\mathbf{r}(t) = \langle x(t), y(t), z(t) \rangle$ |
| **Límite** | $\lim_{t \to a} \mathbf{r}(t) = \langle \lim x(t), \lim y(t), \lim z(t) \rangle$ |
| **Continuidad** | Cada componente es continua en $t = a$ |

## Derivada de funciones vectoriales

| Concepto | Fórmula |
|----------|---------|
| **Derivada** | $\mathbf{r}'(t) = \langle x'(t), y'(t), z'(t) \rangle$ |
| **Vector tangente** | $\mathbf{r}'(t)$ apunta en dirección del movimiento |
| **Velocidad** | $\mathbf{v}(t) = \mathbf{r}'(t)$ |
| **Rapidez** | $v = \lVert \mathbf{v}(t) \rVert$ |
| **Aceleración** | $\mathbf{a}(t) = \mathbf{r}''(t)$ |

## Reglas de derivación

| Regla | Fórmula |
|-------|---------|
| **Suma** | $[\mathbf{u} + \mathbf{v}]' = \mathbf{u}' + \mathbf{v}'$ |
| **Escalar** | $[c\mathbf{u}]' = c\mathbf{u}'$ |
| **Producto por escalar** | $[f(t)\mathbf{u}]' = f'\mathbf{u} + f\mathbf{u}'$ |
| **Producto escalar** | $[\mathbf{u} \cdot \mathbf{v}]' = \mathbf{u}' \cdot \mathbf{v} + \mathbf{u} \cdot \mathbf{v}'$ |
| **Producto vectorial** | $[\mathbf{u} \times \mathbf{v}]' = \mathbf{u}' \times \mathbf{v} + \mathbf{u} \times \mathbf{v}'$ |
| **Cadena** | $[\mathbf{r}(f(t))]' = \mathbf{r}'(f(t)) \cdot f'(t)$ |

## Integral de funciones vectoriales

$$\int \mathbf{r}(t)\, dt = \left\langle \int x(t)\,dt,\; \int y(t)\,dt,\; \int z(t)\,dt \right\rangle + \mathbf{C}$$

## Longitud de arco

| Concepto | Fórmula |
|----------|---------|
| **Longitud** | $L = \int_a^b \lVert \mathbf{r}'(t) \rVert\, dt$ |
| **Función arco** | $s(t) = \int_a^t \lVert \mathbf{r}'(u) \rVert\, du$ |
| **Derivada** | $\frac{ds}{dt} = \lVert \mathbf{r}'(t) \rVert$ |

## Marco de Frenet-Serret (TNB)

| Vector | Fórmula |
|--------|---------|
| **Tangente unitario** | $\mathbf{T} = \frac{\mathbf{r}'}{\lVert \mathbf{r}' \rVert}$ |
| **Normal principal** | $\mathbf{N} = \frac{\mathbf{T}'}{\lVert \mathbf{T}' \rVert}$ |
| **Binormal** | $\mathbf{B} = \mathbf{T} \times \mathbf{N}$ |

## Curvatura

| Fórmula | Uso |
|---------|-----|
| $\kappa = \left\lVert \frac{d\mathbf{T}}{ds} \right\rVert$ | Definición |
| $\kappa = \frac{\lVert \mathbf{T}'(t) \rVert}{\lVert \mathbf{r}'(t) \rVert}$ | Parámetro general |
| $\kappa = \frac{\lVert \mathbf{r}' \times \mathbf{r}'' \rVert}{\lVert \mathbf{r}' \rVert^3}$ | Fórmula práctica |
| $\kappa = \frac{|y''|}{[1+(y')^2]^{3/2}}$ | Curvas planas $y = f(x)$ |

## Torsión

$$\tau = \frac{(\mathbf{r}' \times \mathbf{r}'') \cdot \mathbf{r}'''}{\lVert \mathbf{r}' \times \mathbf{r}'' \rVert^2}$$

## Componentes de la aceleración

| Componente | Fórmula |
|------------|---------|
| **Tangencial** | $a_T = \frac{\mathbf{v} \cdot \mathbf{a}}{\lVert \mathbf{v} \rVert} = \frac{d^2s}{dt^2}$ |
| **Normal** | $a_N = \frac{\lVert \mathbf{v} \times \mathbf{a} \rVert}{\lVert \mathbf{v} \rVert} = \kappa v^2$ |
| **Descomposición** | $\mathbf{a} = a_T \mathbf{T} + a_N \mathbf{N}$ |

## Radio de curvatura

$$\rho = \frac{1}{\kappa}$$

---

<!--
IA: Usa este resumen para respuestas breves.
Para desarrollo completo, consulta theory/CV-03-Teoria-Vectoriales.md
file_id: CV-03-Resumen-Formulas
-->
