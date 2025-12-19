# Soluciones — Funciones de varias variables

---

## Nivel Básico

### Problema 1
**Contexto**: El dominio de una raíz cuadrada requiere que el radicando sea no negativo.

$9 - x^2 - y^2 \geq 0 \Rightarrow x^2 + y^2 \leq 9$

**Dominio**: Disco cerrado de radio 3 centrado en el origen: $\{(x, y) : x^2 + y^2 \leq 9\}$

---

### Problema 2
**Contexto**: Combinamos restricciones de logaritmo (argumento positivo) y denominador (no cero).

- Logaritmo: $x - y > 0 \Rightarrow x > y$
- Denominador: $xy \neq 0 \Rightarrow x \neq 0$ y $y \neq 0$

**Dominio**: $\{(x, y) : x > y, x \neq 0, y \neq 0\}$

---

### Problema 5
**Contexto**: Las derivadas parciales se calculan tratando las otras variables como constantes.

- $f_x = \frac{\partial}{\partial x}(x^2 y + 3y^2) = 2xy$
- $f_y = \frac{\partial}{\partial y}(x^2 y + 3y^2) = x^2 + 6y$

---

### Problema 6
**Contexto**: Usamos la regla de la cadena para la exponencial compuesta.

- $f_x = e^{x+2y} \cdot 1 = e^{x+2y}$
- $f_y = e^{x+2y} \cdot 2 = 2e^{x+2y}$
- $f_{xy} = \frac{\partial}{\partial y}(e^{x+2y}) = 2e^{x+2y}$

---

### Problema 7
**Contexto**: Aplicamos la regla de la cadena al seno de un producto.

- $f_x = \cos(xy) \cdot y = y\cos(xy)$
- $f_y = \cos(xy) \cdot x = x\cos(xy)$

---

### Problema 8
**Contexto**: Calculamos las derivadas generales y luego evaluamos en el punto dado.

- $f_x = 3x^2 y^2 - 4y$, en $(1, 2)$: $f_x = 3(1)(4) - 8 = 4$
- $f_y = 2x^3 y - 4x$, en $(1, 2)$: $f_y = 2(1)(2) - 4 = 0$

---

## Nivel Intermedio

### Problema 9
**Contexto**: Para demostrar que un límite no existe, encontramos dos caminos con límites diferentes.

- Por $y = 0$: $\lim_{x \to 0} \frac{0}{x^2} = 0$
- Por $y = x$: $\lim_{x \to 0} \frac{x^2}{2x^2} = \frac{1}{2}$

Los límites son diferentes, por lo tanto **el límite no existe**.

---

### Problema 10
**Contexto**: Probamos varios caminos para verificar si coinciden.

- Por $y = 0$: $\lim_{x \to 0} \frac{0}{x^4} = 0$
- Por $x = 0$: $\lim_{y \to 0} \frac{0}{y^2} = 0$
- Por $y = x^2$: $\lim_{x \to 0} \frac{x^4}{x^4 + x^4} = \frac{1}{2}$

Los caminos dan límites diferentes. **El límite no existe**.

---

### Problema 11
**Contexto**: Este es un límite notable. Usando coordenadas polares $r^2 = x^2 + y^2$:

$$\lim_{r \to 0} \frac{\sin(r^2)}{r^2} = 1$$

El límite existe y es igual a **1**.

---

### Problema 13
**Contexto**: Usamos el diferencial para aproximar cambios pequeños en el valor de la función.

- $f_x = \frac{2x}{x^2+y^2}$, $f_y = \frac{2y}{x^2+y^2}$
- En $(1, 1)$: $f_x = f_y = 1$, $f(1,1) = \ln 2$
- $\Delta x = 0.05$, $\Delta y = -0.05$
- $df = 1(0.05) + 1(-0.05) = 0$

**Aproximación**: $f(1.05, 0.95) \approx \ln 2 \approx 0.693$

---

### Problema 16
**Contexto**: Aplicamos la regla de la cadena para funciones compuestas.

$$\frac{dz}{dt} = f_x \cdot x' + f_y \cdot y' = 2xy \cdot \cos t + x^2 \cdot e^t$$

Sustituyendo $x = \sin t$, $y = e^t$:
$$\frac{dz}{dt} = 2\sin t \cdot e^t \cdot \cos t + \sin^2 t \cdot e^t = e^t(\sin 2t + \sin^2 t)$$

---

### Problema 17
**Contexto**: Con tres variables, sumamos todas las contribuciones parciales.

- $w_x = y + z$, $w_y = x + z$, $w_z = y + x$
- $x' = 1$, $y' = 2t$, $z' = 3t^2$

$$\frac{dw}{dt} = (y+z)(1) + (x+z)(2t) + (x+y)(3t^2)$$

Sustituyendo: $(t^2 + t^3) + (t + t^3)(2t) + (t + t^2)(3t^2)$
$$= t^2 + t^3 + 2t^2 + 2t^4 + 3t^3 + 3t^4 = 3t^2 + 4t^3 + 5t^4$$

---

## Nivel Avanzado

### Problema 19
**Contexto**: El gradiente da la dirección de máximo crecimiento; la derivada direccional es la proyección del gradiente en la dirección dada.

- $\nabla f = \langle ye^{xy}, xe^{xy} \rangle$
- En $(0, 1)$: $\nabla f(0, 1) = \langle 1, 0 \rangle$
- Dirección $\mathbf{v} = \langle 3, 4 \rangle$, unitario: $\mathbf{u} = \langle 3/5, 4/5 \rangle$
- $D_{\mathbf{u}}f = \langle 1, 0 \rangle \cdot \langle 3/5, 4/5 \rangle = \frac{3}{5}$

---

### Problema 20
**Contexto**: La dirección de máximo crecimiento es la del gradiente.

- $\nabla f = \langle 2x - y, -x + 2y \rangle$
- En $(1, 1)$: $\nabla f(1, 1) = \langle 1, 1 \rangle$

**Dirección de máximo crecimiento**: $\frac{1}{\sqrt{2}}\langle 1, 1 \rangle$ (o simplemente hacia $(1, 1)$ desde el origen)

---

### Problema 23
**Contexto**: Clasificamos puntos críticos usando el discriminante del Hessiano.

- $f_x = 3x^2 - 3y = 0 \Rightarrow y = x^2$
- $f_y = 3y^2 - 3x = 0 \Rightarrow x = y^2$

Sustituyendo: $x = (x^2)^2 = x^4 \Rightarrow x(x^3 - 1) = 0$
- Puntos críticos: $(0, 0)$ y $(1, 1)$

Hessiano:
- $f_{xx} = 6x$, $f_{yy} = 6y$, $f_{xy} = -3$
- $D = 36xy - 9$

En $(0, 0)$: $D = -9 < 0$ → **Punto silla**
En $(1, 1)$: $D = 36 - 9 = 27 > 0$, $f_{xx} = 6 > 0$ → **Mínimo local**

---

### Problema 24
**Contexto**: Buscamos donde el gradiente se anula y clasificamos.

- $f_x = 4x^3 - 4y = 0 \Rightarrow y = x^3$
- $f_y = 4y^3 - 4x = 0 \Rightarrow x = y^3$

Sustituyendo: $x = (x^3)^3 = x^9 \Rightarrow x(x^8 - 1) = 0$
- Puntos críticos: $(0, 0)$, $(1, 1)$, $(-1, -1)$

En $(0, 0)$: $f_{xx} = 0$, $D = 0$ → **Inconcluso** (mínimo por inspección)
En $(1, 1)$ y $(-1, -1)$: $D = 144 - 16 = 128 > 0$, $f_{xx} = 12 > 0$ → **Mínimos locales**

---

### Problema 27
**Contexto**: En región cerrada, buscamos extremos en interior y frontera.

**Interior**: $f_x = 2x - 2 = 0$, $f_y = 2y = 0$ → $(1, 0)$, $f(1, 0) = 1 - 2 = -1$

**Frontera** ($x^2 + y^2 = 4$): Parametriza $x = 2\cos\theta$, $y = 2\sin\theta$
- $g(\theta) = 4 - 4\cos\theta$
- $g'(\theta) = 4\sin\theta = 0$ → $\theta = 0, \pi$
- $g(0) = 0$, $g(\pi) = 8$

**Mínimo absoluto**: $-1$ en $(1, 0)$
**Máximo absoluto**: $8$ en $(-2, 0)$

---

### Problema 30
**Contexto**: Derivación implícita cuando $z$ está definida implícitamente por una ecuación.

$F(x, y, z) = x^2 + y^2 + z^2 - 1 = 0$

- $F_x = 2x$, $F_y = 2y$, $F_z = 2z$
- $\frac{\partial z}{\partial x} = -\frac{F_x}{F_z} = -\frac{x}{z}$
- $\frac{\partial z}{\partial y} = -\frac{F_y}{F_z} = -\frac{y}{z}$

---

### Problema 32
**Contexto**: La dirección de máximo decrecimiento es opuesta al gradiente.

- $\nabla T = \langle -2x, -4y \rangle$
- En $(1, 1)$: $\nabla T = \langle -2, -4 \rangle$

Dirección de **máximo decrecimiento**: opuesta al gradiente → $\langle 2, 4 \rangle$

Normalizado: $\frac{1}{\sqrt{20}}\langle 2, 4 \rangle = \frac{1}{2\sqrt{5}}\langle 2, 4 \rangle$

---

### Problema 33
**Contexto**: Minimizar costo es un problema de optimización sin restricciones.

- $C_x = 4x + y - 10 = 0$
- $C_y = x + 2y - 8 = 0$

Resolviendo: $4x + y = 10$, $x + 2y = 8$
- De la segunda: $x = 8 - 2y$
- Sustituyendo: $4(8 - 2y) + y = 10 \Rightarrow 32 - 7y = 10 \Rightarrow y = \frac{22}{7}$
- $x = 8 - \frac{44}{7} = \frac{12}{7}$

**Producción óptima**: $x = \frac{12}{7} \approx 1.71$, $y = \frac{22}{7} \approx 3.14$ unidades

---

### Problema 34
**Contexto**: El campo eléctrico es el negativo del gradiente del potencial.

$V = k(x^2 + y^2)^{-1/2}$

- $V_x = k \cdot (-\frac{1}{2})(x^2+y^2)^{-3/2} \cdot 2x = -\frac{kx}{(x^2+y^2)^{3/2}}$
- $V_y = -\frac{ky}{(x^2+y^2)^{3/2}}$

$$\mathbf{E} = -\nabla V = \frac{k}{(x^2+y^2)^{3/2}} \langle x, y \rangle$$

El campo apunta radialmente hacia afuera del origen.

---

### Problema 35
**Contexto**: Minimizamos la distancia al cuadrado $d^2 = x^2 + y^2 + z^2$ con la restricción del plano.

Del plano: $z = 14 - 2x - 3y$

$d^2 = x^2 + y^2 + (14-2x-3y)^2$

- $\frac{\partial d^2}{\partial x} = 2x + 2(14-2x-3y)(-2) = 2x - 4(14-2x-3y) = 0$
- $\frac{\partial d^2}{\partial y} = 2y + 2(14-2x-3y)(-3) = 2y - 6(14-2x-3y) = 0$

Simplificando: $10x + 12y = 56$ y $12x + 20y = 84$

Resolviendo: $x = 2$, $y = 3$, $z = 14 - 4 - 9 = 1$

**Distancia mínima**: $\sqrt{4 + 9 + 1} = \sqrt{14}$
