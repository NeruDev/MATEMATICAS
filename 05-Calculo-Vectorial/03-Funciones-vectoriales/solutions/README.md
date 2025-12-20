# Soluciones — Funciones vectoriales

---

## Nivel Básico

### Problema 1
**Contexto**: Los límites de funciones vectoriales se calculan componente a componente, aplicando los límites conocidos de funciones escalares.

$\lim_{t \to 0} \langle t^2, \sin t, e^t \rangle = \langle 0, 0, 1 \rangle$

---

### Problema 2
**Contexto**: Para verificar continuidad, debemos comprobar si el límite existe y coincide con el valor de la función. La componente $\frac{\sin t}{t}$ requiere definir $x(0) = 1$ para que sea continua (límite notable).

Si definimos $x(0) = \lim_{t \to 0} \frac{\sin t}{t} = 1$, entonces $\mathbf{r}(0) = \langle 1, 0, 1 \rangle$ y la función es continua.

---

### Problema 3
**Contexto**: Evaluamos cada componente en $t = 1$ directamente ya que son funciones continuas.

$\lim_{t \to 1} \langle \ln t, t^3 - 1, \sqrt{t} \rangle = \langle \ln 1, 1-1, 1 \rangle = \langle 0, 0, 1 \rangle$

---

### Problema 4
**Contexto**: La derivada de una función vectorial se obtiene derivando cada componente por separado.

$$\mathbf{r}'(t) = \left\langle 3, 2t, \frac{1}{1+t} \right\rangle$$

---

### Problema 5
**Contexto**: La velocidad es la derivada del vector posición. La rapidez es la magnitud de la velocidad.

- $\mathbf{r}'(t) = \langle 2t, 4, 3t^2 \rangle$
- $\mathbf{v}(2) = \langle 4, 4, 12 \rangle$
- Rapidez: $\|\mathbf{v}(2)\| = \sqrt{16 + 16 + 144} = \sqrt{176} = 4\sqrt{11}$

---

### Problema 6
**Contexto**: La segunda derivada representa la aceleración y describe cómo cambia la velocidad.

- $\mathbf{r}'(t) = \langle -2\sin 2t, 2\cos 2t, 3 \rangle$
- $\mathbf{r}''(t) = \langle -4\cos 2t, -4\sin 2t, 0 \rangle$

---

### Problema 7
**Contexto**: La integral indefinida de una función vectorial se calcula integrando cada componente y añadiendo un vector constante.

$$\int \langle 2t, e^t, \cos t \rangle \, dt = \langle t^2, e^t, \sin t \rangle + \mathbf{C}$$

---

### Problema 8
**Contexto**: La integral definida se evalúa componente a componente en los límites dados.

$$\int_0^1 \langle 3t^2, 2t, 1 \rangle \, dt = \left[ \langle t^3, t^2, t \rangle \right]_0^1 = \langle 1, 1, 1 \rangle - \langle 0, 0, 0 \rangle = \langle 1, 1, 1 \rangle$$

---

### Problema 9
**Contexto**: Para encontrar la posición a partir de la velocidad, integramos y usamos la condición inicial.

- $\mathbf{r}(t) = \int \langle 1, 2t, 3t^2 \rangle \, dt = \langle t, t^2, t^3 \rangle + \mathbf{C}$
- Con $\mathbf{r}(0) = \langle 0, 0, 0 \rangle$: $\mathbf{C} = \langle 0, 0, 0 \rangle$
- **Resultado**: $\mathbf{r}(t) = \langle t, t^2, t^3 \rangle$

---

## Nivel Intermedio

### Problema 10
**Contexto**: La longitud de arco se calcula integrando la magnitud de la derivada. Esta es la hélice circular, cuya derivada tiene magnitud constante.

- $\mathbf{r}'(t) = \langle -\sin t, \cos t, 1 \rangle$
- $\|\mathbf{r}'(t)\| = \sqrt{\sin^2 t + \cos^2 t + 1} = \sqrt{2}$
- $L = \int_0^{\pi} \sqrt{2} \, dt = \pi\sqrt{2}$

---

### Problema 11
**Contexto**: Esta curva (cúbica torcida simplificada) tiene derivada con magnitud variable, pero el radicando resulta ser un cuadrado perfecto.

- $\mathbf{r}'(t) = \langle 1, 2t, 2t^2 \rangle$
- $\|\mathbf{r}'(t)\| = \sqrt{1 + 4t^2 + 4t^4} = \sqrt{(1 + 2t^2)^2} = 1 + 2t^2$
- $L = \int_0^1 (1 + 2t^2) \, dt = \left[ t + \frac{2t^3}{3} \right]_0^1 = 1 + \frac{2}{3} = \frac{5}{3}$

---

### Problema 12
**Contexto**: Esta hélice tiene radio 3 y "paso" 4 por cada $2\pi$ de vuelta.

- $\mathbf{r}'(t) = \langle -3\sin t, 3\cos t, 4 \rangle$
- $\|\mathbf{r}'(t)\| = \sqrt{9 + 16} = 5$
- $L = \int_0^{2\pi} 5 \, dt = 10\pi$

---

### Problema 13
**Contexto**: El vector tangente unitario indica la dirección instantánea de movimiento, normalizado.

- $\mathbf{r}'(t) = \langle 1, 2t, 0 \rangle$
- $\|\mathbf{r}'(t)\| = \sqrt{1 + 4t^2}$
- $\mathbf{T}(t) = \frac{1}{\sqrt{1+4t^2}} \langle 1, 2t, 0 \rangle$

---

### Problema 14
**Contexto**: Evaluamos el vector tangente en un punto específico tras normalizar la derivada.

- $\mathbf{r}'(t) = \langle e^t, -e^{-t}, \sqrt{2} \rangle$
- En $t = 0$: $\mathbf{r}'(0) = \langle 1, -1, \sqrt{2} \rangle$
- $\|\mathbf{r}'(0)\| = \sqrt{1 + 1 + 2} = 2$
- $\mathbf{T}(0) = \langle \frac{1}{2}, -\frac{1}{2}, \frac{\sqrt{2}}{2} \rangle$

---

### Problema 15
**Contexto**: Calculamos primero la derivada general y luego evaluamos en el punto dado.

- $\mathbf{r}'(t) = \langle \cos t, -\sin t, 1 \rangle$
- En $t = \pi/2$: $\mathbf{r}'(\pi/2) = \langle 0, -1, 1 \rangle$
- $\|\mathbf{r}'(\pi/2)\| = \sqrt{2}$
- $\mathbf{T}(\pi/2) = \frac{1}{\sqrt{2}} \langle 0, -1, 1 \rangle$

---

### Problema 16
**Contexto**: La curvatura mide qué tan bruscamente gira la curva. Usamos la fórmula del producto cruz.

- $\mathbf{r}'(t) = \langle 1, 2t, 0 \rangle$, $\mathbf{r}''(t) = \langle 0, 2, 0 \rangle$
- $\mathbf{r}' \times \mathbf{r}'' = \langle 0, 0, 2 \rangle$
- $\|\mathbf{r}' \times \mathbf{r}''\| = 2$
- $\|\mathbf{r}'(1)\| = \sqrt{5}$
- $\kappa(1) = \frac{2}{(\sqrt{5})^3} = \frac{2}{5\sqrt{5}} = \frac{2\sqrt{5}}{25}$

---

### Problema 17
**Contexto**: Para una circunferencia, la curvatura es constante e igual al inverso del radio.

- $\mathbf{r}'(t) = \langle -5\sin t, 5\cos t, 0 \rangle$, $\mathbf{r}''(t) = \langle -5\cos t, -5\sin t, 0 \rangle$
- $\mathbf{r}' \times \mathbf{r}'' = \langle 0, 0, 25 \rangle$
- $\|\mathbf{r}'\| = 5$
- $\kappa = \frac{25}{125} = \frac{1}{5}$

**Verificación**: Para círculo de radio $R = 5$, $\kappa = 1/R = 1/5$ ✓

---

### Problema 18
**Contexto**: Esta es la curva tractriz. En $t = 0$, las funciones trigonométricas simplifican el cálculo.

- $y(t) = \ln(\cos t)$, $y'(t) = -\tan t$, $y''(t) = -\sec^2 t$
- $\mathbf{r}'(t) = \langle 1, -\tan t, 0 \rangle$
- En $t = 0$: $\mathbf{r}'(0) = \langle 1, 0, 0 \rangle$, $\mathbf{r}''(0) = \langle 0, -1, 0 \rangle$
- $\mathbf{r}' \times \mathbf{r}'' = \langle 0, 0, -1 \rangle$
- $\kappa(0) = \frac{1}{1} = 1$

---

## Nivel Avanzado

### Problema 19
**Contexto**: Construimos el marco TNB completo, que forma un sistema de referencia ortonormal móvil.

- $\mathbf{r}'(t) = \langle 1, -\sin t, \cos t \rangle$
- En $t = 0$: $\mathbf{r}'(0) = \langle 1, 0, 1 \rangle$, $\|\mathbf{r}'(0)\| = \sqrt{2}$
- $\mathbf{T}(0) = \frac{1}{\sqrt{2}} \langle 1, 0, 1 \rangle$

- $\mathbf{T}(t) = \frac{1}{\sqrt{2}} \langle 1, -\sin t, \cos t \rangle$
- $\mathbf{T}'(t) = \frac{1}{\sqrt{2}} \langle 0, -\cos t, -\sin t \rangle$
- En $t = 0$: $\mathbf{T}'(0) = \frac{1}{\sqrt{2}} \langle 0, -1, 0 \rangle$
- $\mathbf{N}(0) = \langle 0, -1, 0 \rangle$

- $\mathbf{B}(0) = \mathbf{T}(0) \times \mathbf{N}(0) = \frac{1}{\sqrt{2}} \langle 1, 0, -1 \rangle$

---

### Problema 20
**Contexto**: La hélice tiene un marco TNB con comportamiento regular que rota a medida que avanzamos.

- $\mathbf{r}'(t) = \langle -2\sin t, 2\cos t, 1 \rangle$
- En $t = \pi/2$: $\mathbf{r}'(\pi/2) = \langle -2, 0, 1 \rangle$, $\|\mathbf{r}'\| = \sqrt{5}$
- $\mathbf{T}(\pi/2) = \frac{1}{\sqrt{5}} \langle -2, 0, 1 \rangle$

- $\mathbf{r}''(t) = \langle -2\cos t, -2\sin t, 0 \rangle$
- En $t = \pi/2$: $\mathbf{r}''(\pi/2) = \langle 0, -2, 0 \rangle$
- $\mathbf{N}(\pi/2) = \langle 0, -1, 0 \rangle$

- $\mathbf{B}(\pi/2) = \frac{1}{\sqrt{5}} \langle -2, 0, 1 \rangle \times \langle 0, -1, 0 \rangle = \frac{1}{\sqrt{5}} \langle 1, 0, 2 \rangle$

---

### Problema 22
**Contexto**: Esta es la "cúbica torcida". En $t = 0$ los cálculos simplifican considerablemente.

- $\mathbf{r}' = \langle 1, 2t, 3t^2 \rangle$, $\mathbf{r}'' = \langle 0, 2, 6t \rangle$, $\mathbf{r}''' = \langle 0, 0, 6 \rangle$
- En $t = 0$: $\mathbf{r}'(0) = \langle 1, 0, 0 \rangle$, $\mathbf{r}''(0) = \langle 0, 2, 0 \rangle$, $\mathbf{r}'''(0) = \langle 0, 0, 6 \rangle$
- $\mathbf{r}' \times \mathbf{r}'' = \langle 0, 0, 2 \rangle$
- $\|\mathbf{r}' \times \mathbf{r}''\| = 2$, $\|\mathbf{r}'\| = 1$

**Curvatura**: $\kappa(0) = \frac{2}{1} = 2$

**Torsión**: $\tau(0) = \frac{\langle 0, 0, 2 \rangle \cdot \langle 0, 0, 6 \rangle}{4} = \frac{12}{4} = 3$

---

### Problema 23
**Contexto**: La hélice circular tiene torsión constante, lo que significa que "sube" a un ritmo uniforme.

- $\mathbf{r}' = \langle -a\sin t, a\cos t, b \rangle$
- $\mathbf{r}'' = \langle -a\cos t, -a\sin t, 0 \rangle$
- $\mathbf{r}''' = \langle a\sin t, -a\cos t, 0 \rangle$
- $\mathbf{r}' \times \mathbf{r}'' = \langle ab\sin t, -ab\cos t, a^2 \rangle$
- $\|\mathbf{r}' \times \mathbf{r}''\|^2 = a^2b^2 + a^4 = a^2(a^2 + b^2)$
- $(\mathbf{r}' \times \mathbf{r}'') \cdot \mathbf{r}''' = a^2b$

$$\tau = \frac{a^2 b}{a^2(a^2 + b^2)} = \frac{b}{a^2 + b^2}$$

La torsión es constante (no depende de $t$). ∎

---

### Problema 25
**Contexto**: Este problema aplica los conceptos de cinemática vectorial: posición → velocidad → aceleración.

- $\mathbf{r}(t) = \langle t^2, 2t, \ln(t+1) \rangle$
- $\mathbf{v}(t) = \mathbf{r}'(t) = \langle 2t, 2, \frac{1}{t+1} \rangle$
- $\mathbf{a}(t) = \mathbf{r}''(t) = \langle 2, 0, -\frac{1}{(t+1)^2} \rangle$

En $t = 1$:
- **Velocidad**: $\mathbf{v}(1) = \langle 2, 2, \frac{1}{2} \rangle$
- **Rapidez**: $\|\mathbf{v}(1)\| = \sqrt{4 + 4 + \frac{1}{4}} = \sqrt{\frac{33}{4}} = \frac{\sqrt{33}}{2}$
- **Aceleración**: $\mathbf{a}(1) = \langle 2, 0, -\frac{1}{4} \rangle$

---

### Problema 27
**Contexto**: Modelamos el movimiento de un proyectil sin resistencia del aire. La altura máxima ocurre cuando la componente vertical de la velocidad es cero.

- $\mathbf{r}(t) = \langle 10t, 20t - 5t^2, 0 \rangle$
- $\mathbf{v}(t) = \langle 10, 20 - 10t, 0 \rangle$

**Altura máxima**: $v_y = 0 \Rightarrow 20 - 10t = 0 \Rightarrow t = 2$
- $y(2) = 20(2) - 5(4) = 40 - 20 = 20$
- **Altura máxima**: 20 unidades

**Alcance**: $y = 0 \Rightarrow 20t - 5t^2 = 0 \Rightarrow t(20 - 5t) = 0 \Rightarrow t = 4$
- $x(4) = 10(4) = 40$
- **Alcance horizontal**: 40 unidades

---

### Problema 31
**Contexto**: Aplicación a ingeniería - diseño de montaña rusa. La longitud de vía determina el costo del material.

- $\mathbf{r}'(t) = \langle -10\sin t, 10\cos t, 5 \rangle$
- $\|\mathbf{r}'(t)\| = \sqrt{100 + 25} = \sqrt{125} = 5\sqrt{5}$
- $L = \int_0^{4\pi} 5\sqrt{5} \, dt = 20\pi\sqrt{5} \approx 140.5$ unidades

---

### Problema 32
**Contexto**: Aplicación a mecánica orbital. La rapidez determina si el satélite mantiene la órbita.

- $\mathbf{r}'(t) = \langle -7\sin(0.001t), 7\cos(0.001t), \cos(0.002t) \rangle$
- $\|\mathbf{r}'(t)\| \approx \sqrt{49 + 1} = \sqrt{50} \approx 7.07$ km/s

La curvatura varía según la posición en la órbita elíptica perturbada.
