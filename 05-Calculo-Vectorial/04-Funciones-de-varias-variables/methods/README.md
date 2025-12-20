# Métodos — Funciones de varias variables

---

## Método 1: Determinar el dominio de una función

### Contexto
El dominio determina dónde está definida la función. Es el primer paso antes de cualquier análisis.

### Pasos
1. Identifica operaciones restrictivas: raíces pares, logaritmos, denominadores.
2. Escribe las desigualdades correspondientes.
3. Resuelve el sistema de desigualdades.
4. Expresa el dominio como conjunto o región.

### Ejemplo práctico
**Problema**: Encuentra el dominio de $f(x, y) = \sqrt{4 - x^2 - y^2} + \ln(y - x)$.

**Solución**:
- Raíz: $4 - x^2 - y^2 \geq 0 \Rightarrow x^2 + y^2 \leq 4$ (disco de radio 2)
- Logaritmo: $y - x > 0 \Rightarrow y > x$ (semiplano superior a $y = x$)
- **Dominio**: $\{(x, y) : x^2 + y^2 \leq 4 \text{ y } y > x\}$

### Verificación
Prueba un punto interior como $(0, 1)$: $\sqrt{4-1} + \ln(1) = \sqrt{3} + 0$ ✓

---

## Método 2: Calcular derivadas parciales

### Contexto
Las derivadas parciales miden la tasa de cambio en cada dirección coordinada.

### Pasos
1. Para $f_x$: trata $y$ como constante, deriva respecto a $x$.
2. Para $f_y$: trata $x$ como constante, deriva respecto a $y$.
3. Aplica reglas de derivación (producto, cociente, cadena).
4. Simplifica el resultado.

### Ejemplo práctico
**Problema**: Calcula $f_x$ y $f_y$ para $f(x, y) = x^2 e^{xy} + \sin(x + y)$.

**Solución**:
$$f_x = 2x \cdot e^{xy} + x^2 \cdot y \cdot e^{xy} + \cos(x + y) = e^{xy}(2x + x^2 y) + \cos(x+y)$$
$$f_y = x^2 \cdot x \cdot e^{xy} + \cos(x + y) = x^3 e^{xy} + \cos(x + y)$$

### Verificación
Comprueba que $f_{xy} = f_{yx}$ (teorema de Clairaut).

---

## Método 3: Verificar existencia de un límite

### Contexto
Si el límite por diferentes caminos da resultados distintos, el límite no existe.

### Pasos
1. Prueba el camino $y = 0$ (sustituye $y = 0$).
2. Prueba el camino $x = 0$ (sustituye $x = 0$).
3. Prueba el camino $y = mx$ (sustituye y simplifica).
4. Si algún par de caminos da límites diferentes, el límite no existe.
5. Si todos coinciden, intenta demostrar con $\varepsilon-\delta$ o coordenadas polares.

### Ejemplo práctico
**Problema**: Determina si existe $\lim_{(x,y) \to (0,0)} \frac{xy}{x^2 + y^2}$.

**Solución**:
- Por $y = 0$: $\frac{x \cdot 0}{x^2} = 0$
- Por $x = 0$: $\frac{0 \cdot y}{y^2} = 0$
- Por $y = x$: $\frac{x^2}{2x^2} = \frac{1}{2}$
- Por $y = -x$: $\frac{-x^2}{2x^2} = -\frac{1}{2}$

Los caminos dan límites diferentes. **El límite no existe**.

### Verificación
Siempre prueba al menos 3 caminos diferentes antes de concluir que existe.

---

## Método 4: Aproximación lineal usando diferenciales

### Contexto
El diferencial permite estimar el cambio en $f$ sin calcular el valor exacto.

### Pasos
1. Identifica el punto base $(a, b)$ y los incrementos $\Delta x$, $\Delta y$.
2. Calcula $f(a, b)$.
3. Calcula $f_x(a, b)$ y $f_y(a, b)$.
4. Aplica: $f(a + \Delta x, b + \Delta y) \approx f(a,b) + f_x \Delta x + f_y \Delta y$.

### Ejemplo práctico
**Problema**: Aproxima $\sqrt{(3.02)^2 + (3.97)^2}$ usando $f(x, y) = \sqrt{x^2 + y^2}$.

**Solución**:
- Punto base: $(3, 4)$ donde $f(3,4) = 5$.
- Incrementos: $\Delta x = 0.02$, $\Delta y = -0.03$.
- $f_x = \frac{x}{\sqrt{x^2+y^2}}$, en $(3,4)$: $f_x = \frac{3}{5}$.
- $f_y = \frac{y}{\sqrt{x^2+y^2}}$, en $(3,4)$: $f_y = \frac{4}{5}$.
- Aproximación: $5 + \frac{3}{5}(0.02) + \frac{4}{5}(-0.03) = 5 + 0.012 - 0.024 = 4.988$

**Valor exacto**: $\sqrt{9.1204 + 15.7609} \approx 4.9882$ ✓

---

## Método 5: Aplicar la regla de la cadena

### Contexto
Se usa cuando las variables de $f$ dependen de otras variables intermedias.

### Pasos
1. Identifica la estructura: $z = f(x, y)$ con $x = x(t)$, $y = y(t)$.
2. Calcula las derivadas parciales $f_x$, $f_y$.
3. Calcula las derivadas de las funciones intermedias $x'(t)$, $y'(t)$.
4. Aplica: $\frac{dz}{dt} = f_x \cdot x'(t) + f_y \cdot y'(t)$.

### Ejemplo práctico
**Problema**: Si $z = x^2 \ln y$ con $x = \cos t$, $y = e^{2t}$, halla $\frac{dz}{dt}$.

**Solución**:
- $f_x = 2x \ln y$, $f_y = \frac{x^2}{y}$
- $x' = -\sin t$, $y' = 2e^{2t}$
- $\frac{dz}{dt} = 2x \ln y \cdot (-\sin t) + \frac{x^2}{y} \cdot 2e^{2t}$
- $= -2\cos t \cdot 2t \cdot \sin t + \frac{\cos^2 t}{e^{2t}} \cdot 2e^{2t}$
- $= -4t \sin t \cos t + 2\cos^2 t$

### Verificación
Sustituye primero y deriva: $z = \cos^2 t \cdot 2t$. Deriva y compara.

---

## Método 6: Calcular el gradiente y derivada direccional

### Contexto
El gradiente indica la dirección de máximo crecimiento; la derivada direccional da la tasa en cualquier dirección.

### Pasos
1. Calcula $\nabla f = \langle f_x, f_y \rangle$.
2. Evalúa en el punto dado.
3. Para derivada direccional: normaliza la dirección a $\mathbf{u}$ unitario.
4. Calcula $D_{\mathbf{u}}f = \nabla f \cdot \mathbf{u}$.

### Ejemplo práctico
**Problema**: Para $f(x, y) = x^2 y - y^3$, calcula la derivada direccional en $(2, 1)$ en dirección a $(5, 4)$.

**Solución**:
- $\nabla f = \langle 2xy, x^2 - 3y^2 \rangle$
- En $(2, 1)$: $\nabla f(2, 1) = \langle 4, 1 \rangle$
- Dirección: $\mathbf{v} = \langle 5-2, 4-1 \rangle = \langle 3, 3 \rangle$
- Unitario: $\mathbf{u} = \frac{1}{\sqrt{18}} \langle 3, 3 \rangle = \frac{1}{3\sqrt{2}} \langle 3, 3 \rangle$
- $D_{\mathbf{u}}f = \langle 4, 1 \rangle \cdot \frac{1}{3\sqrt{2}} \langle 3, 3 \rangle = \frac{12 + 3}{3\sqrt{2}} = \frac{15}{3\sqrt{2}} = \frac{5\sqrt{2}}{2}$

### Verificación
La derivada direccional máxima es $\|\nabla f\| = \sqrt{17} \approx 4.12$. Nuestro resultado $\frac{5\sqrt{2}}{2} \approx 3.54$ es menor ✓

---

## Método 7: Encontrar y clasificar puntos críticos

### Contexto
Los puntos críticos son candidatos a extremos locales; el Hessiano los clasifica.

### Pasos
1. Calcula $f_x$ y $f_y$.
2. Resuelve el sistema $f_x = 0$, $f_y = 0$ simultáneamente.
3. Para cada punto crítico $(a, b)$, calcula $f_{xx}$, $f_{yy}$, $f_{xy}$.
4. Evalúa $D = f_{xx} f_{yy} - f_{xy}^2$.
5. Clasifica según el signo de $D$ y $f_{xx}$.

### Ejemplo práctico
**Problema**: Encuentra y clasifica los extremos de $f(x, y) = x^3 - 3x + y^2 - 2y$.

**Solución**:
- $f_x = 3x^2 - 3 = 0 \Rightarrow x^2 = 1 \Rightarrow x = \pm 1$
- $f_y = 2y - 2 = 0 \Rightarrow y = 1$
- Puntos críticos: $(1, 1)$ y $(-1, 1)$

- $f_{xx} = 6x$, $f_{yy} = 2$, $f_{xy} = 0$
- $D = 6x \cdot 2 - 0 = 12x$

En $(1, 1)$: $D = 12 > 0$, $f_{xx} = 6 > 0$ → **Mínimo local**
En $(-1, 1)$: $D = -12 < 0$ → **Punto silla**

### Verificación
Calcula $f(1, 1) = 1 - 3 + 1 - 2 = -3$ (mínimo) y $f(-1, 1) = -1 + 3 + 1 - 2 = 1$.

---

## Método 8: Derivación implícita multivariable

### Contexto
Cuando una ecuación $F(x, y, z) = 0$ define $z$ implícitamente.

### Pasos
1. Escribe la ecuación como $F(x, y, z) = 0$.
2. Calcula $F_x$, $F_y$, $F_z$.
3. Aplica: $\frac{\partial z}{\partial x} = -\frac{F_x}{F_z}$, $\frac{\partial z}{\partial y} = -\frac{F_y}{F_z}$.

### Ejemplo práctico
**Problema**: Si $x^2 + y^2 + z^2 = 25$ (esfera), encuentra $\frac{\partial z}{\partial x}$.

**Solución**:
- $F(x, y, z) = x^2 + y^2 + z^2 - 25$
- $F_x = 2x$, $F_y = 2y$, $F_z = 2z$
- $\frac{\partial z}{\partial x} = -\frac{2x}{2z} = -\frac{x}{z}$

**En el punto $(3, 0, 4)$**: $\frac{\partial z}{\partial x} = -\frac{3}{4}$

### Verificación
Despeja $z = \sqrt{25 - x^2 - y^2}$ y deriva directamente.

---

## Método 9: Ecuación del plano tangente

### Contexto
El plano tangente es la mejor aproximación lineal a una superficie en un punto.

### Pasos
1. Evalúa $f(a, b) = z_0$.
2. Calcula $f_x(a, b)$ y $f_y(a, b)$.
3. Escribe: $z - z_0 = f_x(a,b)(x - a) + f_y(a,b)(y - b)$.

### Ejemplo práctico
**Problema**: Encuentra el plano tangente a $z = x^2 + y^2$ en $(1, 2, 5)$.

**Solución**:
- $f_x = 2x$, en $(1, 2)$: $f_x = 2$
- $f_y = 2y$, en $(1, 2)$: $f_y = 4$
- Plano: $z - 5 = 2(x - 1) + 4(y - 2)$
- **Resultado**: $z = 2x + 4y - 5$ o $2x + 4y - z = 5$

### Verificación
El plano debe pasar por $(1, 2, 5)$: $2(1) + 4(2) - 5 = 5$ ✓

---

## Método 10: Extremos absolutos en región cerrada

### Contexto
En una región cerrada y acotada, una función continua siempre alcanza su máximo y mínimo absolutos.

### Pasos
1. Encuentra puntos críticos interiores (resolver $\nabla f = 0$).
2. Parametriza cada segmento de la frontera.
3. Reduce a función de una variable en cada frontera; encuentra extremos.
4. Evalúa $f$ en todos los candidatos.
5. El mayor valor es el máximo absoluto; el menor, el mínimo absoluto.

### Ejemplo práctico
**Problema**: Halla los extremos de $f(x, y) = x^2 - 2x + y^2$ en el disco $x^2 + y^2 \leq 4$.

**Solución**:
- **Interior**: $f_x = 2x - 2 = 0$, $f_y = 2y = 0$ → $(1, 0)$. $f(1, 0) = 1 - 2 + 0 = -1$
- **Frontera** ($x^2 + y^2 = 4$): Usa $x = 2\cos\theta$, $y = 2\sin\theta$.
  - $g(\theta) = 4\cos^2\theta - 4\cos\theta + 4\sin^2\theta = 4 - 4\cos\theta$
  - $g'(\theta) = 4\sin\theta = 0$ → $\theta = 0, \pi$
  - $g(0) = 4 - 4 = 0$, $g(\pi) = 4 + 4 = 8$

**Conclusión**: Mínimo absoluto $-1$ en $(1, 0)$; máximo absoluto $8$ en $(-2, 0)$.
