<!--
::METADATA::
type: method
topic_id: cv-04-funciones-varias-variables
file_id: CV-04-Metodos-Varias-Variables
status: stable
audience: student
-->

# Métodos para Funciones de Varias Variables

> **Objetivo:** Dominar el cálculo diferencial de funciones de varias variables con algoritmos detallados, cálculos intermedios y ejemplos clásicos paso a paso.

---

## Método 1: Dominio de Funciones de Varias Variables

### Cuándo Usar
- Determinar el conjunto de puntos $(x, y)$ o $(x, y, z)$ donde la función está definida

### Restricciones Comunes

| Expresión | Restricción |
|-----------|-------------|
| $\sqrt{g(x,y)}$ | $g(x,y) \geq 0$ |
| $\ln(g(x,y))$ | $g(x,y) > 0$ |
| $\frac{1}{g(x,y)}$ | $g(x,y) \neq 0$ |
| $\arcsin(g)$ | $-1 \leq g \leq 1$ |

### Ejemplo Detallado

**Problema:** Encontrar el dominio de $f(x,y) = \sqrt{9 - x^2 - y^2}$

**Paso 1:** Identificamos la restricción:
$$9 - x^2 - y^2 \geq 0$$

**Paso 2:** Despejamos:
$$x^2 + y^2 \leq 9$$

**Resultado:** El dominio es el **disco cerrado** de radio 3 centrado en el origen:
$$\text{Dom}(f) = \boxed{\{(x,y) : x^2 + y^2 \leq 9\}}$$

---

## Método 2: Curvas y Superficies de Nivel

### Cuándo Usar
- Visualizar funciones de 2 variables: curvas de nivel $f(x,y) = k$
- Visualizar funciones de 3 variables: superficies de nivel $f(x,y,z) = k$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Fijar $k$ constante | Elegir varios valores |
| 2 | Resolver $f(x,y) = k$ | Obtener ecuación 2D |
| 3 | Graficar cada curva | Etiquetar con valor de $k$ |

### Ejemplo Detallado

**Problema:** Trazar curvas de nivel de $f(x,y) = x^2 + y^2$

**Paso 1:** $f(x,y) = k$ implica $x^2 + y^2 = k$

**Paso 2:** Analizamos para diferentes valores de $k$:

| $k$ | Curva | Descripción |
|-----|-------|-------------|
| 0 | $x^2 + y^2 = 0$ | Punto $(0,0)$ |
| 1 | $x^2 + y^2 = 1$ | Círculo radio 1 |
| 4 | $x^2 + y^2 = 4$ | Círculo radio 2 |
| 9 | $x^2 + y^2 = 9$ | Círculo radio 3 |

**Resultado:** Las curvas de nivel son **círculos concéntricos** centrados en el origen.

---

## Método 3: Límites de Funciones de Varias Variables

### Cuándo Usar
- Verificar si existe $\lim_{(x,y) \to (a,b)} f(x,y)$

### Estrategias

| Método | Uso |
|--------|-----|
| **Sustitución directa** | Si no hay indeterminación |
| **Trayectorias** | Para mostrar que NO existe |
| **Coordenadas polares** | $(x,y) \to (0,0)$, usar $x = r\cos\theta$, $y = r\sin\theta$ |
| **Acotación (Squeeze)** | Para demostrar que SÍ existe |

### Algoritmo para Probar que NO Existe

| Paso | Acción |
|------|--------|
| 1 | Evaluar por $y = 0$ (eje $x$) |
| 2 | Evaluar por $x = 0$ (eje $y$) |
| 3 | Evaluar por $y = mx$ (rectas) |
| 4 | Evaluar por $y = x^2$ (parábola) si es necesario |
| 5 | Si dos dan diferente → NO existe |

### Ejemplo Detallado (NO existe)

**Problema:** Evaluar $\lim_{(x,y) \to (0,0)} \frac{xy}{x^2 + y^2}$

**Por el eje $x$** ($y = 0$):
$$\lim_{x \to 0} \frac{x \cdot 0}{x^2 + 0} = \lim_{x \to 0} \frac{0}{x^2} = 0$$

**Por el eje $y$** ($x = 0$):
$$\lim_{y \to 0} \frac{0 \cdot y}{0 + y^2} = \lim_{y \to 0} \frac{0}{y^2} = 0$$

**Por la recta $y = x$**:
$$\lim_{x \to 0} \frac{x \cdot x}{x^2 + x^2} = \lim_{x \to 0} \frac{x^2}{2x^2} = \frac{1}{2}$$

**Resultado:** El límite **no existe** porque por diferentes trayectorias obtenemos valores distintos ($0$ y $\frac{1}{2}$).

### Ejemplo Detallado (SÍ existe)

**Problema:** Evaluar $\lim_{(x,y) \to (0,0)} \frac{x^2 y}{x^2 + y^2}$

**Usamos coordenadas polares:** $x = r\cos\theta$, $y = r\sin\theta$

$$\frac{x^2 y}{x^2 + y^2} = \frac{r^2\cos^2\theta \cdot r\sin\theta}{r^2} = r\cos^2\theta \sin\theta$$

Cuando $(x,y) \to (0,0)$, tenemos $r \to 0$.

$$\lim_{r \to 0} r\cos^2\theta \sin\theta = 0$$

**Verificación:** $|r\cos^2\theta \sin\theta| \leq r \cdot 1 \cdot 1 = r \to 0$

**Resultado:** El límite es $\boxed{0}$

---

## Método 4: Derivadas Parciales

### Cuándo Usar
- Calcular la tasa de cambio respecto a una variable manteniendo las otras constantes

### Fórmulas
$$\frac{\partial f}{\partial x} = \lim_{h \to 0} \frac{f(x+h, y) - f(x, y)}{h}$$

$$\frac{\partial f}{\partial y} = \lim_{h \to 0} \frac{f(x, y+h) - f(x, y)}{h}$$

### Regla Práctica
- Para $\frac{\partial f}{\partial x}$: Tratar $y$ como constante, derivar respecto a $x$
- Para $\frac{\partial f}{\partial y}$: Tratar $x$ como constante, derivar respecto a $y$

### Ejemplo Detallado

**Problema:** Encontrar $\frac{\partial f}{\partial x}$ y $\frac{\partial f}{\partial y}$ para $f(x,y) = x^3y^2 + 3xy^4 - 2y$

**Derivada parcial respecto a $x$** ($y$ constante):
$$\frac{\partial f}{\partial x} = 3x^2y^2 + 3y^4 + 0 = \boxed{3x^2y^2 + 3y^4}$$

**Derivada parcial respecto a $y$** ($x$ constante):
$$\frac{\partial f}{\partial y} = 2x^3y + 12xy^3 - 2 = \boxed{2x^3y + 12xy^3 - 2}$$

---

## Método 5: Derivadas Parciales de Orden Superior

### Cuándo Usar
- Calcular segundas derivadas, derivadas mixtas
- Análisis de extremos (Hessiano)

### Notación

| Segunda derivada | Notación |
|------------------|----------|
| $\frac{\partial}{\partial x}\left(\frac{\partial f}{\partial x}\right)$ | $f_{xx}$ o $\frac{\partial^2 f}{\partial x^2}$ |
| $\frac{\partial}{\partial y}\left(\frac{\partial f}{\partial y}\right)$ | $f_{yy}$ o $\frac{\partial^2 f}{\partial y^2}$ |
| $\frac{\partial}{\partial y}\left(\frac{\partial f}{\partial x}\right)$ | $f_{xy}$ o $\frac{\partial^2 f}{\partial y \partial x}$ |

### Teorema de Clairaut
Si $f_{xy}$ y $f_{yx}$ son continuas: $f_{xy} = f_{yx}$

### Ejemplo Detallado

**Problema:** Encontrar todas las segundas derivadas de $f(x,y) = x^3 + x^2y^3 - 2y^2$

**Paso 1:** Primeras derivadas:
$$f_x = 3x^2 + 2xy^3$$
$$f_y = 3x^2y^2 - 4y$$

**Paso 2:** Segundas derivadas:
$$f_{xx} = \frac{\partial}{\partial x}(3x^2 + 2xy^3) = \boxed{6x + 2y^3}$$

$$f_{yy} = \frac{\partial}{\partial y}(3x^2y^2 - 4y) = \boxed{6x^2y - 4}$$

$$f_{xy} = \frac{\partial}{\partial y}(3x^2 + 2xy^3) = \boxed{6xy^2}$$

$$f_{yx} = \frac{\partial}{\partial x}(3x^2y^2 - 4y) = \boxed{6xy^2}$$

**Verificación:** $f_{xy} = f_{yx} = 6xy^2$ ✓

---

## Método 6: Gradiente

### Cuándo Usar
- Encontrar la dirección de máximo crecimiento
- Calcular derivadas direccionales
- Vector normal a superficies de nivel

### Fórmulas

**2 variables:**
$$\nabla f = \left\langle \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y} \right\rangle$$

**3 variables:**
$$\nabla f = \left\langle \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z} \right\rangle$$

### Propiedades del Gradiente
- Apunta en la dirección de **máximo crecimiento**
- $\|\nabla f\|$ es la **tasa máxima de cambio**
- $\nabla f$ es **perpendicular** a las curvas/superficies de nivel

### Ejemplo Detallado

**Problema:** Encontrar el gradiente de $f(x,y,z) = x^2yz + 4xz^2$ en $(1, -2, -1)$

**Paso 1:** Calculamos las derivadas parciales:
$$\frac{\partial f}{\partial x} = 2xyz + 4z^2$$
$$\frac{\partial f}{\partial y} = x^2z$$
$$\frac{\partial f}{\partial z} = x^2y + 8xz$$

**Paso 2:** Evaluamos en $(1, -2, -1)$:
$$\frac{\partial f}{\partial x}\bigg|_{(1,-2,-1)} = 2(1)(-2)(-1) + 4(-1)^2 = 4 + 4 = 8$$
$$\frac{\partial f}{\partial y}\bigg|_{(1,-2,-1)} = (1)^2(-1) = -1$$
$$\frac{\partial f}{\partial z}\bigg|_{(1,-2,-1)} = (1)^2(-2) + 8(1)(-1) = -2 - 8 = -10$$

**Resultado:**
$$\nabla f(1, -2, -1) = \boxed{\langle 8, -1, -10 \rangle}$$

---

## Método 7: Derivada Direccional

### Cuándo Usar
- Calcular la tasa de cambio en una dirección específica $\mathbf{u}$

### Fórmula
$$D_\mathbf{u}f = \nabla f \cdot \mathbf{u}$$

donde $\mathbf{u}$ es un **vector unitario**.

### Algoritmo de Resolución

| Paso | Acción | Cálculo |
|------|--------|---------|
| 1 | Calcular $\nabla f$ | Derivadas parciales |
| 2 | Normalizar la dirección | $\mathbf{u} = \frac{\mathbf{v}}{\|\mathbf{v}\|}$ |
| 3 | Producto punto | $D_\mathbf{u}f = \nabla f \cdot \mathbf{u}$ |

### Ejemplo Detallado

**Problema:** Encontrar la derivada direccional de $f(x,y) = x^2 - xy + y^2$ en $(1, 2)$ en la dirección de $\mathbf{v} = \langle 3, -4 \rangle$

**Paso 1:** Calculamos el gradiente:
$$\frac{\partial f}{\partial x} = 2x - y$$
$$\frac{\partial f}{\partial y} = -x + 2y$$

$$\nabla f(1, 2) = \langle 2(1) - 2, -(1) + 2(2) \rangle = \langle 0, 3 \rangle$$

**Paso 2:** Normalizamos la dirección:
$$\|\mathbf{v}\| = \sqrt{9 + 16} = 5$$
$$\mathbf{u} = \left\langle \frac{3}{5}, -\frac{4}{5} \right\rangle$$

**Paso 3:** Calculamos la derivada direccional:
$$D_\mathbf{u}f = \nabla f \cdot \mathbf{u} = \langle 0, 3 \rangle \cdot \left\langle \frac{3}{5}, -\frac{4}{5} \right\rangle$$
$$= 0 \cdot \frac{3}{5} + 3 \cdot \left(-\frac{4}{5}\right) = -\frac{12}{5}$$

**Resultado:**
$$D_\mathbf{u}f(1, 2) = \boxed{-\frac{12}{5}}$$

**Interpretación:** La función decrece en la dirección dada (tasa negativa).

---

## Método 8: Plano Tangente a Superficies

### Cuándo Usar
- Aproximación lineal de $z = f(x,y)$ cerca de un punto

### Fórmulas

**Para $z = f(x,y)$:**
$$z - z_0 = f_x(x_0, y_0)(x - x_0) + f_y(x_0, y_0)(y - y_0)$$

**Para superficie de nivel $F(x,y,z) = k$:**
$$F_x(x-x_0) + F_y(y-y_0) + F_z(z-z_0) = 0$$

o usando el gradiente:
$$\nabla F \cdot \langle x-x_0, y-y_0, z-z_0 \rangle = 0$$

### Ejemplo Detallado

**Problema:** Encontrar el plano tangente a $z = x^2 + y^2$ en $(1, 1, 2)$

**Paso 1:** Calculamos las derivadas parciales:
$$f_x = 2x \implies f_x(1, 1) = 2$$
$$f_y = 2y \implies f_y(1, 1) = 2$$

**Paso 2:** Aplicamos la fórmula:
$$z - 2 = 2(x - 1) + 2(y - 1)$$
$$z = 2x + 2y - 2$$

**Resultado:** El plano tangente es $\boxed{2x + 2y - z = 2}$

---

## Método 9: Extremos Locales (Sin Restricciones)

### Cuándo Usar
- Encontrar máximos y mínimos de $f(x,y)$

### Algoritmo de Resolución

| Paso | Acción | Cálculo |
|------|--------|---------|
| 1 | Encontrar puntos críticos | $f_x = 0$ y $f_y = 0$ |
| 2 | Calcular el Hessiano | $D = f_{xx}f_{yy} - (f_{xy})^2$ |
| 3 | Clasificar cada punto | Ver tabla |

### Criterio de la Segunda Derivada

| Condición | Clasificación |
|-----------|---------------|
| $D > 0$ y $f_{xx} > 0$ | **Mínimo local** |
| $D > 0$ y $f_{xx} < 0$ | **Máximo local** |
| $D < 0$ | **Punto silla** |
| $D = 0$ | Prueba no concluyente |

### Ejemplo Detallado

**Problema:** Encontrar y clasificar los extremos de $f(x,y) = x^3 - 3xy + y^3$

**Paso 1:** Derivadas parciales y puntos críticos:
$$f_x = 3x^2 - 3y = 0 \implies y = x^2$$
$$f_y = -3x + 3y^2 = 0 \implies x = y^2$$

Sustituyendo: $x = (x^2)^2 = x^4 \implies x(x^3 - 1) = 0$

$x = 0 \implies y = 0$
$x = 1 \implies y = 1$

Puntos críticos: $(0, 0)$ y $(1, 1)$

**Paso 2:** Calculamos las segundas derivadas:
$$f_{xx} = 6x, \quad f_{yy} = 6y, \quad f_{xy} = -3$$

**Paso 3:** Clasificamos cada punto:

**En $(0, 0)$:**
$$D = (6 \cdot 0)(6 \cdot 0) - (-3)^2 = 0 - 9 = -9 < 0$$
→ **Punto silla**

**En $(1, 1)$:**
$$D = (6)(6) - 9 = 36 - 9 = 27 > 0$$
$$f_{xx}(1,1) = 6 > 0$$
→ **Mínimo local** con $f(1,1) = 1 - 3 + 1 = -1$

**Resultado:**
- $(0, 0)$: Punto silla
- $(1, 1)$: Mínimo local, $f_{\min} = \boxed{-1}$

---

## Método 10: Multiplicadores de Lagrange

### Cuándo Usar
- Optimizar $f(x,y)$ sujeto a restricción $g(x,y) = k$
- Optimizar $f(x,y,z)$ sujeto a $g(x,y,z) = k$

### Fórmula
$$\nabla f = \lambda \nabla g$$

### Algoritmo de Resolución

| Paso | Acción | Sistema |
|------|--------|---------|
| 1 | Plantear ecuaciones | $\nabla f = \lambda \nabla g$ |
| 2 | Incluir restricción | $g(x,y) = k$ |
| 3 | Resolver el sistema | $n+1$ ecuaciones, $n+1$ incógnitas |
| 4 | Evaluar $f$ en cada punto | Comparar valores |

### Ejemplo Detallado

**Problema:** Encontrar los extremos de $f(x,y) = xy$ en el círculo $x^2 + y^2 = 1$

**Paso 1:** Identificamos:
- $f(x,y) = xy$
- $g(x,y) = x^2 + y^2 - 1 = 0$

**Paso 2:** Calculamos gradientes:
$$\nabla f = \langle y, x \rangle$$
$$\nabla g = \langle 2x, 2y \rangle$$

**Paso 3:** Planteamos $\nabla f = \lambda \nabla g$:
$$y = 2\lambda x \quad \text{(1)}$$
$$x = 2\lambda y \quad \text{(2)}$$
$$x^2 + y^2 = 1 \quad \text{(3)}$$

**Paso 4:** De (1) y (2): $y = 2\lambda(2\lambda y) = 4\lambda^2 y$

Si $y \neq 0$: $4\lambda^2 = 1 \implies \lambda = \pm\frac{1}{2}$

**Caso $\lambda = \frac{1}{2}$:**
De (1): $y = x$. Con (3): $2x^2 = 1 \implies x = \pm\frac{1}{\sqrt{2}}$
Puntos: $\left(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right)$ y $\left(-\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}\right)$

**Caso $\lambda = -\frac{1}{2}$:**
De (1): $y = -x$. Con (3): $2x^2 = 1 \implies x = \pm\frac{1}{\sqrt{2}}$
Puntos: $\left(\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}\right)$ y $\left(-\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right)$

**Paso 5:** Evaluamos $f$ en cada punto:

| Punto | $f(x,y) = xy$ |
|-------|---------------|
| $\left(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right)$ | $\frac{1}{2}$ |
| $\left(-\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}\right)$ | $\frac{1}{2}$ |
| $\left(\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}\right)$ | $-\frac{1}{2}$ |
| $\left(-\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right)$ | $-\frac{1}{2}$ |

**Resultado:**
- Máximo: $f_{\max} = \boxed{\frac{1}{2}}$ en $\left(\pm\frac{1}{\sqrt{2}}, \pm\frac{1}{\sqrt{2}}\right)$
- Mínimo: $f_{\min} = \boxed{-\frac{1}{2}}$ en $\left(\pm\frac{1}{\sqrt{2}}, \mp\frac{1}{\sqrt{2}}\right)$

---

## Método 11: Regla de la Cadena (Varias Variables)

### Cuándo Usar
- Derivar composiciones de funciones multivariable

### Fórmulas

**Caso 1:** $z = f(x,y)$ donde $x = g(t)$, $y = h(t)$
$$\frac{dz}{dt} = \frac{\partial f}{\partial x}\frac{dx}{dt} + \frac{\partial f}{\partial y}\frac{dy}{dt}$$

**Caso 2:** $z = f(x,y)$ donde $x = g(s,t)$, $y = h(s,t)$
$$\frac{\partial z}{\partial s} = \frac{\partial f}{\partial x}\frac{\partial x}{\partial s} + \frac{\partial f}{\partial y}\frac{\partial y}{\partial s}$$

### Ejemplo Detallado

**Problema:** Si $z = x^2y + xy^2$, $x = s + t$, $y = st$, encontrar $\frac{\partial z}{\partial s}$

**Paso 1:** Calculamos derivadas parciales de $z$:
$$\frac{\partial z}{\partial x} = 2xy + y^2$$
$$\frac{\partial z}{\partial y} = x^2 + 2xy$$

**Paso 2:** Calculamos derivadas de $x$ e $y$:
$$\frac{\partial x}{\partial s} = 1$$
$$\frac{\partial y}{\partial s} = t$$

**Paso 3:** Aplicamos la regla de la cadena:
$$\frac{\partial z}{\partial s} = (2xy + y^2)(1) + (x^2 + 2xy)(t)$$

**Paso 4:** Sustituimos $x = s+t$, $y = st$:
$$= 2(s+t)(st) + (st)^2 + t[(s+t)^2 + 2(s+t)(st)]$$

**Resultado simplificado:**
$$\frac{\partial z}{\partial s} = \boxed{2st(s+t) + s^2t^2 + t(s+t)^2 + 2st^2(s+t)}$$

---

## Método 12: Diferencial Total

### Cuándo Usar
- Aproximar cambios en $f$ cuando cambian las variables
- Análisis de error en mediciones

### Fórmula
$$df = \frac{\partial f}{\partial x}dx + \frac{\partial f}{\partial y}dy$$

**Aproximación:**
$$\Delta f \approx f_x \Delta x + f_y \Delta y$$

### Ejemplo Detallado

**Problema:** Aproximar el cambio en el volumen de un cilindro $V = \pi r^2 h$ cuando $r$ cambia de 10 a 10.1 cm y $h$ cambia de 15 a 14.9 cm.

**Paso 1:** Calculamos derivadas parciales:
$$\frac{\partial V}{\partial r} = 2\pi rh$$
$$\frac{\partial V}{\partial h} = \pi r^2$$

**Paso 2:** Evaluamos en $(r, h) = (10, 15)$:
$$\frac{\partial V}{\partial r} = 2\pi(10)(15) = 300\pi$$
$$\frac{\partial V}{\partial h} = \pi(10)^2 = 100\pi$$

**Paso 3:** Identificamos los cambios:
$$\Delta r = 10.1 - 10 = 0.1$$
$$\Delta h = 14.9 - 15 = -0.1$$

**Paso 4:** Aplicamos la fórmula:
$$\Delta V \approx 300\pi(0.1) + 100\pi(-0.1) = 30\pi - 10\pi = 20\pi$$

**Resultado:**
$$\Delta V \approx \boxed{20\pi \approx 62.83 \text{ cm}^3}$$

**Verificación exacta:**
- $V_{\text{inicial}} = \pi(10)^2(15) = 1500\pi$
- $V_{\text{final}} = \pi(10.1)^2(14.9) = 1520.0149\pi$
- $\Delta V_{\text{exacto}} = 20.0149\pi$ ✓
