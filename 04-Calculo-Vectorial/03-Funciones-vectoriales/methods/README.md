# Métodos — Funciones vectoriales

---

## Método 1: Evaluar límites de funciones vectoriales

### Contexto
Se usa para determinar el comportamiento de una curva cuando el parámetro tiende a un valor específico.

### Pasos
1. Identifica las componentes $x(t)$, $y(t)$, $z(t)$.
2. Calcula el límite de cada componente por separado.
3. Si algún límite no existe, el límite vectorial no existe.
4. Forma el vector resultado con los límites obtenidos.

### Ejemplo práctico
**Problema**: Halla $\lim_{t \to 0} \mathbf{r}(t)$ donde $\mathbf{r}(t) = \left\langle \frac{\sin t}{t}, e^{2t}, \frac{1-\cos t}{t^2} \right\rangle$.

**Solución**:
- $\lim_{t \to 0} \frac{\sin t}{t} = 1$ (límite notable)
- $\lim_{t \to 0} e^{2t} = e^0 = 1$
- $\lim_{t \to 0} \frac{1-\cos t}{t^2} = \frac{1}{2}$ (límite notable)

**Resultado**: $\langle 1, 1, \frac{1}{2} \rangle$

### Verificación
Sustituir valores cercanos a 0 y comprobar tendencia.

---

## Método 2: Derivar funciones vectoriales

### Contexto
La derivada representa el vector velocidad y tangente a la curva.

### Pasos
1. Deriva cada componente respecto a $t$.
2. Escribe $\mathbf{r}'(t) = \langle x'(t), y'(t), z'(t) \rangle$.
3. Para velocidad instantánea, evalúa en el punto deseado.
4. Para rapidez, calcula $\|\mathbf{r}'(t)\|$.

### Ejemplo práctico
**Problema**: Encuentra la velocidad y rapidez en $t = 1$ para $\mathbf{r}(t) = \langle t^3, e^{-t}, \ln(t+1) \rangle$.

**Solución**:
- $x'(t) = 3t^2$, $y'(t) = -e^{-t}$, $z'(t) = \frac{1}{t+1}$
- $\mathbf{r}'(t) = \langle 3t^2, -e^{-t}, \frac{1}{t+1} \rangle$
- $\mathbf{v}(1) = \mathbf{r}'(1) = \langle 3, -e^{-1}, \frac{1}{2} \rangle$
- Rapidez: $\|\mathbf{v}(1)\| = \sqrt{9 + e^{-2} + \frac{1}{4}} = \sqrt{9.25 + e^{-2}} \approx 3.09$

### Verificación
Comprueba que el vector velocidad sea tangente a la curva graficando.

---

## Método 3: Integrar funciones vectoriales

### Contexto
Se usa para encontrar posición a partir de velocidad, o desplazamiento acumulado.

### Pasos
1. Integra cada componente por separado.
2. Para integral indefinida, añade constante vectorial $\mathbf{C} = \langle C_1, C_2, C_3 \rangle$.
3. Usa condiciones iniciales para determinar $\mathbf{C}$.
4. Para integral definida, evalúa en los límites.

### Ejemplo práctico
**Problema**: Si $\mathbf{v}(t) = \langle 2t, \cos t, 3 \rangle$ y $\mathbf{r}(0) = \langle 1, 0, -1 \rangle$, encuentra $\mathbf{r}(t)$.

**Solución**:
$$\mathbf{r}(t) = \int \mathbf{v}(t)\,dt = \langle t^2 + C_1, \sin t + C_2, 3t + C_3 \rangle$$

Aplicando $\mathbf{r}(0) = \langle 1, 0, -1 \rangle$:
- $0 + C_1 = 1 \Rightarrow C_1 = 1$
- $0 + C_2 = 0 \Rightarrow C_2 = 0$
- $0 + C_3 = -1 \Rightarrow C_3 = -1$

**Resultado**: $\mathbf{r}(t) = \langle t^2 + 1, \sin t, 3t - 1 \rangle$

### Verificación
Deriva el resultado y comprueba que $\mathbf{r}'(t) = \mathbf{v}(t)$.

---

## Método 4: Calcular longitud de arco

### Contexto
Mide la distancia real recorrida sobre la curva, no la distancia en línea recta.

### Pasos
1. Calcula $\mathbf{r}'(t)$.
2. Encuentra $\|\mathbf{r}'(t)\| = \sqrt{x'^2 + y'^2 + z'^2}$.
3. Simplifica si es posible.
4. Integra: $L = \int_a^b \|\mathbf{r}'(t)\|\,dt$.

### Ejemplo práctico
**Problema**: Halla la longitud de la hélice $\mathbf{r}(t) = \langle 2\cos t, 2\sin t, 3t \rangle$ para $t \in [0, 2\pi]$.

**Solución**:
- $\mathbf{r}'(t) = \langle -2\sin t, 2\cos t, 3 \rangle$
- $\|\mathbf{r}'(t)\| = \sqrt{4\sin^2 t + 4\cos^2 t + 9} = \sqrt{4 + 9} = \sqrt{13}$
- $L = \int_0^{2\pi} \sqrt{13}\,dt = \sqrt{13} \cdot 2\pi = 2\pi\sqrt{13}$

**Resultado**: $L = 2\pi\sqrt{13} \approx 22.65$

### Verificación
Para hélice, la longitud debe ser mayor que la circunferencia base ($4\pi \approx 12.57$).

---

## Método 5: Encontrar el vector tangente unitario $\mathbf{T}$

### Contexto
El vector tangente unitario indica la dirección de movimiento normalizada.

### Pasos
1. Calcula $\mathbf{r}'(t)$.
2. Encuentra su magnitud $\|\mathbf{r}'(t)\|$.
3. Normaliza: $\mathbf{T}(t) = \frac{\mathbf{r}'(t)}{\|\mathbf{r}'(t)\|}$.
4. Evalúa en el punto solicitado.

### Ejemplo práctico
**Problema**: Encuentra $\mathbf{T}$ en $t = 0$ para $\mathbf{r}(t) = \langle e^t, e^{-t}, \sqrt{2}t \rangle$.

**Solución**:
- $\mathbf{r}'(t) = \langle e^t, -e^{-t}, \sqrt{2} \rangle$
- En $t = 0$: $\mathbf{r}'(0) = \langle 1, -1, \sqrt{2} \rangle$
- $\|\mathbf{r}'(0)\| = \sqrt{1 + 1 + 2} = 2$
- $\mathbf{T}(0) = \frac{1}{2}\langle 1, -1, \sqrt{2} \rangle = \langle \frac{1}{2}, -\frac{1}{2}, \frac{\sqrt{2}}{2} \rangle$

### Verificación
Comprueba que $\|\mathbf{T}\| = 1$.

---

## Método 6: Encontrar el vector normal $\mathbf{N}$

### Contexto
El vector normal apunta hacia el centro de curvatura, indicando hacia dónde "gira" la curva.

### Pasos
1. Calcula $\mathbf{T}(t)$ (método anterior).
2. Deriva $\mathbf{T}$ para obtener $\mathbf{T}'(t)$.
3. Normaliza: $\mathbf{N}(t) = \frac{\mathbf{T}'(t)}{\|\mathbf{T}'(t)\|}$.

### Ejemplo práctico
**Problema**: Encuentra $\mathbf{N}$ para la circunferencia $\mathbf{r}(t) = \langle \cos t, \sin t, 0 \rangle$.

**Solución**:
- $\mathbf{r}'(t) = \langle -\sin t, \cos t, 0 \rangle$
- $\|\mathbf{r}'(t)\| = 1$
- $\mathbf{T}(t) = \langle -\sin t, \cos t, 0 \rangle$
- $\mathbf{T}'(t) = \langle -\cos t, -\sin t, 0 \rangle$
- $\|\mathbf{T}'(t)\| = 1$
- $\mathbf{N}(t) = \langle -\cos t, -\sin t, 0 \rangle$

**Interpretación**: $\mathbf{N}$ apunta hacia el origen (centro del círculo).

### Verificación
Comprueba que $\mathbf{T} \cdot \mathbf{N} = 0$ (perpendiculares).

---

## Método 7: Calcular curvatura

### Contexto
La curvatura mide qué tan bruscamente gira la curva; mayor curvatura = giro más cerrado.

### Pasos
1. Calcula $\mathbf{r}'(t)$ y $\mathbf{r}''(t)$.
2. Encuentra el producto cruz $\mathbf{r}'(t) \times \mathbf{r}''(t)$.
3. Calcula $\|\mathbf{r}'(t) \times \mathbf{r}''(t)\|$ y $\|\mathbf{r}'(t)\|^3$.
4. Aplica: $\kappa = \frac{\|\mathbf{r}' \times \mathbf{r}''\|}{\|\mathbf{r}'\|^3}$.

### Ejemplo práctico
**Problema**: Calcula la curvatura de $\mathbf{r}(t) = \langle t, t^2, t^3 \rangle$ en $t = 0$.

**Solución**:
- $\mathbf{r}'(t) = \langle 1, 2t, 3t^2 \rangle$
- $\mathbf{r}''(t) = \langle 0, 2, 6t \rangle$
- $\mathbf{r}'(0) = \langle 1, 0, 0 \rangle$, $\mathbf{r}''(0) = \langle 0, 2, 0 \rangle$
- $\mathbf{r}'(0) \times \mathbf{r}''(0) = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 0 & 0 \\ 0 & 2 & 0 \end{vmatrix} = \langle 0, 0, 2 \rangle$
- $\|\mathbf{r}'(0) \times \mathbf{r}''(0)\| = 2$
- $\|\mathbf{r}'(0)\| = 1$
- $\kappa(0) = \frac{2}{1^3} = 2$

**Resultado**: $\kappa(0) = 2$, radio de curvatura $\rho = \frac{1}{2}$

### Verificación
Para recta, $\kappa = 0$. Para círculo de radio $R$, $\kappa = 1/R$.

---

## Método 8: Calcular torsión

### Contexto
La torsión mide cómo la curva "se retuerce" fuera de su plano osculador.

### Pasos
1. Calcula $\mathbf{r}'$, $\mathbf{r}''$, $\mathbf{r}'''$.
2. Encuentra $\mathbf{r}' \times \mathbf{r}''$.
3. Calcula el producto mixto $(\mathbf{r}' \times \mathbf{r}'') \cdot \mathbf{r}'''$.
4. Aplica: $\tau = \frac{(\mathbf{r}' \times \mathbf{r}'') \cdot \mathbf{r}'''}{\|\mathbf{r}' \times \mathbf{r}''\|^2}$.

### Ejemplo práctico
**Problema**: Encuentra la torsión de la hélice $\mathbf{r}(t) = \langle a\cos t, a\sin t, bt \rangle$.

**Solución**:
- $\mathbf{r}' = \langle -a\sin t, a\cos t, b \rangle$
- $\mathbf{r}'' = \langle -a\cos t, -a\sin t, 0 \rangle$
- $\mathbf{r}''' = \langle a\sin t, -a\cos t, 0 \rangle$
- $\mathbf{r}' \times \mathbf{r}'' = \langle ab\sin t, -ab\cos t, a^2 \rangle$
- $\|\mathbf{r}' \times \mathbf{r}''\|^2 = a^2b^2 + a^4 = a^2(a^2 + b^2)$
- $(\mathbf{r}' \times \mathbf{r}'') \cdot \mathbf{r}''' = ab\sin t \cdot a\sin t + (-ab\cos t)(-a\cos t) + 0 = a^2b$
- $\tau = \frac{a^2b}{a^2(a^2 + b^2)} = \frac{b}{a^2 + b^2}$

**Resultado**: La torsión es constante: $\tau = \frac{b}{a^2 + b^2}$

### Verificación
Para curva plana ($b = 0$), $\tau = 0$ ✓

---

## Método 9: Marco TNB completo

### Contexto
El triedro móvil describe completamente la geometría local de una curva espacial.

### Pasos
1. Calcula $\mathbf{T} = \mathbf{r}'/\|\mathbf{r}'\|$.
2. Calcula $\mathbf{N} = \mathbf{T}'/\|\mathbf{T}'\|$.
3. Calcula $\mathbf{B} = \mathbf{T} \times \mathbf{N}$.
4. Verifica: los tres vectores deben ser ortonormales.

### Ejemplo práctico
**Problema**: Encuentra el marco TNB de $\mathbf{r}(t) = \langle \cos t, \sin t, t \rangle$ en $t = 0$.

**Solución**:
- $\mathbf{r}'(t) = \langle -\sin t, \cos t, 1 \rangle$
- En $t=0$: $\mathbf{r}'(0) = \langle 0, 1, 1 \rangle$, $\|\mathbf{r}'(0)\| = \sqrt{2}$
- $\mathbf{T}(0) = \frac{1}{\sqrt{2}}\langle 0, 1, 1 \rangle$

Para $\mathbf{N}$:
- $\mathbf{T}(t) = \frac{1}{\sqrt{2}}\langle -\sin t, \cos t, 1 \rangle$
- $\mathbf{T}'(t) = \frac{1}{\sqrt{2}}\langle -\cos t, -\sin t, 0 \rangle$
- En $t=0$: $\mathbf{T}'(0) = \frac{1}{\sqrt{2}}\langle -1, 0, 0 \rangle$
- $\|\mathbf{T}'(0)\| = \frac{1}{\sqrt{2}}$
- $\mathbf{N}(0) = \langle -1, 0, 0 \rangle$

Para $\mathbf{B}$:
$$\mathbf{B}(0) = \mathbf{T}(0) \times \mathbf{N}(0) = \frac{1}{\sqrt{2}}\langle 0, 1, 1 \rangle \times \langle -1, 0, 0 \rangle = \frac{1}{\sqrt{2}}\langle -1, 1, -1 \rangle$$

### Verificación
- $\mathbf{T} \cdot \mathbf{N} = 0$ ✓
- $\mathbf{T} \cdot \mathbf{B} = 0$ ✓
- $\mathbf{N} \cdot \mathbf{B} = 0$ ✓
- $\|\mathbf{T}\| = \|\mathbf{N}\| = 1$ ✓
