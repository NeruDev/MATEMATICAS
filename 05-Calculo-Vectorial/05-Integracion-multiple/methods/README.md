# Métodos — Integración múltiple

---

## Método 1: Evaluar integrales dobles en coordenadas rectangulares

### Contexto
Las integrales dobles se evalúan iteradamente: primero una variable, luego la otra.

### Pasos
1. Identifica la región $R$ y decide el orden de integración (Tipo I o II).
2. Determina los límites de integración.
3. Integra la variable interior primero, tratando la otra como constante.
4. Integra el resultado respecto a la variable exterior.

### Ejemplo práctico
**Problema**: Calcula $\iint_R xy\,dA$ donde $R$ es el rectángulo $[0, 2] \times [1, 3]$.

**Solución**:
$$\int_0^2 \int_1^3 xy\,dy\,dx = \int_0^2 \left[ \frac{xy^2}{2} \right]_1^3 dx = \int_0^2 x \cdot \frac{9-1}{2}\,dx = \int_0^2 4x\,dx$$
$$= \left[ 2x^2 \right]_0^2 = 8$$

### Verificación
Para rectángulos con $f(x,y) = g(x)h(y)$: $\iint f\,dA = \int g\,dx \cdot \int h\,dy$.

---

## Método 2: Cambiar el orden de integración

### Contexto
A veces un orden de integración produce una integral difícil; invertir el orden puede simplificarla.

### Pasos
1. Dibuja la región de integración.
2. Identifica los límites en el nuevo orden.
3. Reescribe la integral con los nuevos límites.

### Ejemplo práctico
**Problema**: Evalúa $\int_0^1 \int_y^1 e^{x^2}\,dx\,dy$.

**Solución**:
La región es: $0 \leq y \leq 1$, $y \leq x \leq 1$ → triángulo debajo de $y = x$.

Invirtiendo: $0 \leq x \leq 1$, $0 \leq y \leq x$

$$\int_0^1 \int_0^x e^{x^2}\,dy\,dx = \int_0^1 e^{x^2} \cdot x\,dx = \frac{1}{2}\left[ e^{x^2} \right]_0^1 = \frac{e-1}{2}$$

### Verificación
$\int e^{x^2} dx$ no tiene antiderivada elemental, pero $\int x e^{x^2} dx = \frac{1}{2}e^{x^2}$ sí.

---

## Método 3: Integral doble en coordenadas polares

### Contexto
Usar polares cuando la región o el integrando tienen simetría circular.

### Pasos
1. Sustituye $x = r\cos\theta$, $y = r\sin\theta$.
2. Sustituye $dA = r\,dr\,d\theta$ (¡no olvidar el factor $r$!).
3. Determina los límites de $r$ y $\theta$.
4. Evalúa la integral iterada.

### Ejemplo práctico
**Problema**: Calcula $\iint_D e^{-(x^2+y^2)}\,dA$ donde $D$ es el disco $x^2 + y^2 \leq 4$.

**Solución**:
- En polares: $x^2 + y^2 = r^2$, $dA = r\,dr\,d\theta$
- Límites: $0 \leq r \leq 2$, $0 \leq \theta \leq 2\pi$

$$\int_0^{2\pi} \int_0^2 e^{-r^2} \cdot r\,dr\,d\theta = \int_0^{2\pi} d\theta \int_0^2 re^{-r^2}\,dr$$

$$= 2\pi \cdot \left[ -\frac{1}{2}e^{-r^2} \right]_0^2 = 2\pi \cdot \frac{1}{2}(1 - e^{-4}) = \pi(1 - e^{-4})$$

### Verificación
El integrando $re^{-r^2}$ es integrable, mientras que $e^{-(x^2+y^2)}$ en rectangulares no lo es directamente.

---

## Método 4: Integral triple en coordenadas rectangulares

### Contexto
Las integrales triples calculan volúmenes, masas y otras cantidades en regiones 3D.

### Pasos
1. Identifica el sólido $V$ y elige el orden de integración.
2. Determina los límites para $z$, luego $y$, luego $x$ (o el orden elegido).
3. Integra de adentro hacia afuera.

### Ejemplo práctico
**Problema**: Calcula el volumen del tetraedro con vértices $(0,0,0)$, $(1,0,0)$, $(0,1,0)$, $(0,0,1)$.

**Solución**:
El tetraedro está bajo el plano $x + y + z = 1$ en el primer octante.

$$V = \int_0^1 \int_0^{1-x} \int_0^{1-x-y} dz\,dy\,dx$$

$$= \int_0^1 \int_0^{1-x} (1-x-y)\,dy\,dx = \int_0^1 \left[ (1-x)y - \frac{y^2}{2} \right]_0^{1-x} dx$$

$$= \int_0^1 \left[ (1-x)^2 - \frac{(1-x)^2}{2} \right] dx = \int_0^1 \frac{(1-x)^2}{2}\,dx = \frac{1}{6}$$

### Verificación
Volumen del tetraedro = $\frac{1}{6}|(\mathbf{a} \times \mathbf{b}) \cdot \mathbf{c}| = \frac{1}{6}$.

---

## Método 5: Integral triple en coordenadas cilíndricas

### Contexto
Usar cilíndricas cuando el sólido tiene simetría respecto al eje $z$ (cilindros, conos, paraboloides).

### Pasos
1. Sustituye $x = r\cos\theta$, $y = r\sin\theta$, $z = z$.
2. Usa $dV = r\,dr\,d\theta\,dz$.
3. Expresa los límites en términos de $r$, $\theta$, $z$.
4. Evalúa la integral.

### Ejemplo práctico
**Problema**: Calcula el volumen del sólido limitado por $z = 0$, $z = 4 - x^2 - y^2$.

**Solución**:
Es un paraboloide sobre el disco $x^2 + y^2 \leq 4$.

$$V = \int_0^{2\pi} \int_0^2 \int_0^{4-r^2} r\,dz\,dr\,d\theta$$

$$= \int_0^{2\pi} \int_0^2 r(4-r^2)\,dr\,d\theta = \int_0^{2\pi} \left[ 2r^2 - \frac{r^4}{4} \right]_0^2 d\theta$$

$$= \int_0^{2\pi} (8 - 4)\,d\theta = 4 \cdot 2\pi = 8\pi$$

### Verificación
El volumen de un paraboloide es la mitad del cilindro circunscrito: $\frac{1}{2}\pi(2)^2(4) = 8\pi$ ✓

---

## Método 6: Integral triple en coordenadas esféricas

### Contexto
Usar esféricas cuando el sólido tiene simetría respecto al origen (esferas, conos desde el origen).

### Pasos
1. Sustituye $x = \rho\sin\phi\cos\theta$, $y = \rho\sin\phi\sin\theta$, $z = \rho\cos\phi$.
2. Usa $dV = \rho^2\sin\phi\,d\rho\,d\phi\,d\theta$.
3. Determina los límites de $\rho$, $\phi$, $\theta$.
4. Evalúa la integral.

### Ejemplo práctico
**Problema**: Encuentra el volumen de la esfera $x^2 + y^2 + z^2 = a^2$.

**Solución**:
- Límites: $0 \leq \rho \leq a$, $0 \leq \phi \leq \pi$, $0 \leq \theta \leq 2\pi$

$$V = \int_0^{2\pi} \int_0^{\pi} \int_0^a \rho^2\sin\phi\,d\rho\,d\phi\,d\theta$$

$$= \int_0^{2\pi} d\theta \int_0^{\pi} \sin\phi\,d\phi \int_0^a \rho^2\,d\rho$$

$$= 2\pi \cdot [-\cos\phi]_0^{\pi} \cdot \left[ \frac{\rho^3}{3} \right]_0^a = 2\pi \cdot 2 \cdot \frac{a^3}{3} = \frac{4\pi a^3}{3}$$

### Verificación
Es la fórmula conocida del volumen de una esfera.

---

## Método 7: Calcular integral de línea

### Contexto
Las integrales de línea calculan trabajo o flujo a lo largo de una curva.

### Pasos
1. Parametriza la curva: $\mathbf{r}(t) = \langle x(t), y(t), z(t) \rangle$, $t \in [a, b]$.
2. Calcula $\mathbf{r}'(t) = \langle x'(t), y'(t), z'(t) \rangle$.
3. Sustituye en el integrando: $\mathbf{F}(\mathbf{r}(t))$.
4. Calcula $\int_a^b \mathbf{F}(\mathbf{r}(t)) \cdot \mathbf{r}'(t)\,dt$.

### Ejemplo práctico
**Problema**: Calcula $\int_C \mathbf{F} \cdot d\mathbf{r}$ donde $\mathbf{F} = \langle y, x \rangle$ y $C$ va de $(0, 0)$ a $(1, 1)$ por $y = x^2$.

**Solución**:
- Parametrización: $\mathbf{r}(t) = \langle t, t^2 \rangle$, $t \in [0, 1]$
- $\mathbf{r}'(t) = \langle 1, 2t \rangle$
- $\mathbf{F}(\mathbf{r}(t)) = \langle t^2, t \rangle$
- $\mathbf{F} \cdot \mathbf{r}' = t^2 \cdot 1 + t \cdot 2t = t^2 + 2t^2 = 3t^2$

$$\int_0^1 3t^2\,dt = \left[ t^3 \right]_0^1 = 1$$

### Verificación
Si $\mathbf{F}$ fuera conservativo, la integral solo dependería de los extremos.

---

## Método 8: Aplicar el Teorema de Green

### Contexto
Green convierte una integral de línea sobre una curva cerrada en una integral doble.

### Pasos
1. Verifica que $C$ es una curva cerrada simple orientada positivamente (CCW).
2. Identifica $P$ y $Q$ en $\oint_C P\,dx + Q\,dy$.
3. Calcula $\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}$.
4. Evalúa $\iint_R \left( Q_x - P_y \right) dA$.

### Ejemplo práctico
**Problema**: Calcula $\oint_C (x^2 - y)\,dx + (y^2 + x)\,dy$ donde $C$ es el círculo $x^2 + y^2 = 1$ orientado CCW.

**Solución**:
- $P = x^2 - y$, $Q = y^2 + x$
- $Q_x = 1$, $P_y = -1$
- $Q_x - P_y = 1 - (-1) = 2$

$$\oint_C = \iint_R 2\,dA = 2 \cdot \text{Área}(R) = 2\pi$$

### Verificación
Por Green, la circulación es el doble del área encerrada.

---

## Método 9: Aplicar el Teorema de Gauss (Divergencia)

### Contexto
Gauss convierte un flujo de superficie en una integral de volumen.

### Pasos
1. Verifica que $S$ es una superficie cerrada con normal exterior.
2. Calcula $\nabla \cdot \mathbf{F} = P_x + Q_y + R_z$.
3. Evalúa $\iiint_V (\nabla \cdot \mathbf{F})\,dV$.

### Ejemplo práctico
**Problema**: Calcula el flujo de $\mathbf{F} = \langle x, y, z \rangle$ a través de la esfera $x^2 + y^2 + z^2 = 4$.

**Solución**:
- $\nabla \cdot \mathbf{F} = 1 + 1 + 1 = 3$
- Volumen de la esfera de radio 2: $V = \frac{4}{3}\pi(8) = \frac{32\pi}{3}$

$$\oiint_S \mathbf{F} \cdot d\mathbf{S} = \iiint_V 3\,dV = 3 \cdot \frac{32\pi}{3} = 32\pi$$

### Verificación
Sin Gauss, habría que parametrizar la esfera y calcular $\mathbf{F} \cdot \mathbf{n}\,dS$.

---

## Método 10: Aplicar el Teorema de Stokes

### Contexto
Stokes relaciona la circulación en el borde con el flujo del rotacional a través de la superficie.

### Pasos
1. Identifica la superficie $S$ y su borde $C$.
2. Calcula $\nabla \times \mathbf{F}$.
3. Elige si es más fácil calcular la integral de línea o la de superficie.
4. Evalúa la integral elegida.

### Ejemplo práctico
**Problema**: Calcula $\oint_C \mathbf{F} \cdot d\mathbf{r}$ donde $\mathbf{F} = \langle -y, x, z \rangle$ y $C$ es el círculo $x^2 + y^2 = 4$ en $z = 0$, orientado CCW.

**Solución**:
$$\nabla \times \mathbf{F} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ \partial_x & \partial_y & \partial_z \\ -y & x & z \end{vmatrix} = \langle 0 - 0, 0 - 0, 1 - (-1) \rangle = \langle 0, 0, 2 \rangle$$

La superficie es el disco en $z = 0$ con $\mathbf{n} = \langle 0, 0, 1 \rangle$.

$$\iint_S (\nabla \times \mathbf{F}) \cdot d\mathbf{S} = \iint_S 2\,dA = 2 \cdot \pi(4) = 8\pi$$

### Verificación
Es consistente con Green: circulación = $2 \times$ área del disco.
