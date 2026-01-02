<!--
::METADATA::
type: method
topic_id: cv-05-integracion-multiple
file_id: CV-05-Metodos-Integracion-Multiple
status: stable
audience: student
-->

# Métodos para Integración Múltiple

> **Objetivo:** Dominar las integrales dobles y triples con algoritmos detallados, cambios de coordenadas y ejemplos clásicos paso a paso.

---

## Método 1: Integral Doble sobre Rectángulos

### Cuándo Usar
- Región de integración es un rectángulo $R = [a,b] \times [c,d]$

### Fórmula (Teorema de Fubini)
$$\iint_R f(x,y)\, dA = \int_a^b \int_c^d f(x,y)\, dy\, dx = \int_c^d \int_a^b f(x,y)\, dx\, dy$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Identificar [límites](../../../glossary.md#límites) | $a \leq x \leq b$, $c \leq y \leq d$ |
| 2 | Elegir [orden](../../../glossary.md#orden) de integración | El que simplifique más |
| 3 | Integrar la variable interior | Tratar la otra como constante |
| 4 | Integrar la variable exterior | Con el resultado del paso 3 |

### Ejemplo Detallado

**Problema:** Evaluar $\iint_R (x^2 + y^2)\, dA$ donde $R = [0,1] \times [0,2]$

**Paso 1:** Planteamos la integral iterada:
$$\int_0^1 \int_0^2 (x^2 + y^2)\, dy\, dx$$

**Paso 2:** Integramos respecto a $y$ (tratando $x$ como constante):
$$\int_0^2 (x^2 + y^2)\, dy = \left[x^2y + \frac{y^3}{3}\right]_0^2 = 2x^2 + \frac{8}{3}$$

**Paso 3:** Integramos respecto a $x$:
$$\int_0^1 \left(2x^2 + \frac{8}{3}\right)\, dx = \left[\frac{2x^3}{3} + \frac{8x}{3}\right]_0^1 = \frac{2}{3} + \frac{8}{3} = \frac{10}{3}$$

**Resultado:** $\iint_R (x^2 + y^2)\, dA = \boxed{\frac{10}{3}}$

---

## Método 2: Integral Doble sobre Regiones Generales

### Cuándo Usar
- Región no rectangular
- Límites de una variable dependen de la otra

### Tipos de Región

**Tipo I (verticalmente simple):** $a \leq x \leq b$, $g_1(x) \leq y \leq g_2(x)$
$$\iint_D f\, dA = \int_a^b \int_{g_1(x)}^{g_2(x)} f(x,y)\, dy\, dx$$

**Tipo II (horizontalmente simple):** $c \leq y \leq d$, $h_1(y) \leq x \leq h_2(y)$
$$\iint_D f\, dA = \int_c^d \int_{h_1(y)}^{h_2(y)} f(x,y)\, dx\, dy$$

### Ejemplo Detallado

**Problema:** Evaluar $\iint_D xy\, dA$ donde $D$ es la región acotada por $y = x$ y $y = x^2$

**Paso 1:** Graficamos y encontramos intersecciones:
$x = x^2 \implies x(x-1) = 0 \implies x = 0, 1$

**Paso 2:** Identificamos el tipo de región (Tipo I):
- $0 \leq x \leq 1$
- $x^2 \leq y \leq x$ (la parábola está abajo)

**Paso 3:** Planteamos la integral:
$$\int_0^1 \int_{x^2}^{x} xy\, dy\, dx$$

**Paso 4:** Integramos respecto a $y$:
$$\int_{x^2}^{x} xy\, dy = x\left[\frac{y^2}{2}\right]_{x^2}^{x} = x \cdot \frac{1}{2}(x^2 - x^4) = \frac{x^3 - x^5}{2}$$

**Paso 5:** Integramos respecto a $x$:
$$\int_0^1 \frac{x^3 - x^5}{2}\, dx = \frac{1}{2}\left[\frac{x^4}{4} - \frac{x^6}{6}\right]_0^1 = \frac{1}{2}\left(\frac{1}{4} - \frac{1}{6}\right) = \frac{1}{2} \cdot \frac{1}{12} = \frac{1}{24}$$

**Resultado:** $\iint_D xy\, dA = \boxed{\frac{1}{24}}$

---

## Método 3: Cambio de Orden de Integración

### Cuándo Usar
- La integral en un orden es difícil o imposible
- Optimizar cálculos

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Graficar la región | Identificar curvas [límite](../../../glossary.md#límite) |
| 2 | Expresar como Tipo I | Límites en [función](../../../glossary.md#función) de $x$ |
| 3 | Expresar como Tipo II | Límites en función de $y$ |
| 4 | Elegir el orden más simple | Para el integrando dado |

### Ejemplo Detallado

**Problema:** Evaluar $\int_0^1 \int_x^1 e^{y^2}\, dy\, dx$

**Paso 1:** Analizamos los límites actuales:
- $0 \leq x \leq 1$
- $x \leq y \leq 1$

**Paso 2:** Graficamos: La región está entre $y = x$ e $y = 1$, arriba de la diagonal.

**Paso 3:** Cambiamos a Tipo II:
- $0 \leq y \leq 1$
- $0 \leq x \leq y$

**Paso 4:** Reescribimos la integral:
$$\int_0^1 \int_0^y e^{y^2}\, dx\, dy$$

**Paso 5:** Integramos respecto a $x$ (¡ahora $e^{y^2}$ es constante!):
$$\int_0^y e^{y^2}\, dx = e^{y^2} \cdot y = ye^{y^2}$$

**Paso 6:** Integramos respecto a $y$:
$$\int_0^1 ye^{y^2}\, dy$$

[Sustitución](../../../glossary.md#sustitución): $u = y^2$, $du = 2y\, dy$
$$= \frac{1}{2}\int_0^1 e^u\, du = \frac{1}{2}[e^u]_0^1 = \frac{1}{2}(e - 1)$$

**Resultado:** $\int_0^1 \int_x^1 e^{y^2}\, dy\, dx = \boxed{\frac{e-1}{2}}$

---

## Método 4: Integral Doble en Coordenadas Polares

### Cuándo Usar
- Región circular o sector circular
- Integrando contiene $x^2 + y^2$

### Fórmulas de Transformación
$$x = r\cos\theta, \quad y = r\sin\theta, \quad dA = r\, dr\, d\theta$$

$$x^2 + y^2 = r^2$$

### Tipos de Regiones Polares

| Región | Límites |
|--------|---------|
| Disco completo radio $R$ | $0 \leq r \leq R$, $0 \leq \theta \leq 2\pi$ |
| Semicírculo superior | $0 \leq r \leq R$, $0 \leq \theta \leq \pi$ |
| Sector circular | $\alpha \leq \theta \leq \beta$, $r_1 \leq r \leq r_2$ |

### Ejemplo Detallado

**Problema:** Evaluar $\iint_D e^{-(x^2+y^2)}\, dA$ donde $D$ es el disco $x^2 + y^2 \leq 4$

**Paso 1:** Convertimos a polares:
- Región: $0 \leq r \leq 2$, $0 \leq \theta \leq 2\pi$
- Integrando: $e^{-(x^2+y^2)} = e^{-r^2}$
- Jacobiano: $dA = r\, dr\, d\theta$

**Paso 2:** Planteamos la integral:
$$\int_0^{2\pi} \int_0^2 e^{-r^2} \cdot r\, dr\, d\theta$$

**Paso 3:** Integramos respecto a $r$:
$$\int_0^2 re^{-r^2}\, dr$$

Sustitución: $u = -r^2$, $du = -2r\, dr$
$$= -\frac{1}{2}\int_0^{-4} e^u\, du = -\frac{1}{2}[e^u]_0^{-4} = -\frac{1}{2}(e^{-4} - 1) = \frac{1 - e^{-4}}{2}$$

**Paso 4:** Integramos respecto a $\theta$:
$$\int_0^{2\pi} \frac{1 - e^{-4}}{2}\, d\theta = \frac{1 - e^{-4}}{2} \cdot 2\pi = \pi(1 - e^{-4})$$

**Resultado:** $\iint_D e^{-(x^2+y^2)}\, dA = \boxed{\pi(1 - e^{-4})}$

---

## Método 5: Área y Volumen con Integrales Dobles

### Cuándo Usar
- Área de una región plana: $f(x,y) = 1$
- Volumen bajo una superficie: $f(x,y) \geq 0$

### Fórmulas

**Área:**
$$A = \iint_D 1\, dA$$

**Volumen:**
$$V = \iint_D f(x,y)\, dA$$

### Ejemplo Detallado

**Problema:** Encontrar el volumen del sólido bajo $z = 4 - x^2 - y^2$ y sobre el disco $x^2 + y^2 \leq 4$

**Paso 1:** Usamos coordenadas polares:
- $z = 4 - r^2$
- Región: $0 \leq r \leq 2$, $0 \leq \theta \leq 2\pi$

**Paso 2:** Planteamos la integral:
$$V = \int_0^{2\pi} \int_0^2 (4 - r^2) \cdot r\, dr\, d\theta$$

**Paso 3:** Integramos respecto a $r$:
$$\int_0^2 (4r - r^3)\, dr = \left[2r^2 - \frac{r^4}{4}\right]_0^2 = 8 - 4 = 4$$

**Paso 4:** Integramos respecto a $\theta$:
$$V = \int_0^{2\pi} 4\, d\theta = 4 \cdot 2\pi = 8\pi$$

**Resultado:** El volumen es $\boxed{8\pi}$

---

## Método 6: Integral Triple en Coordenadas Cartesianas

### Cuándo Usar
- Regiones con límites lineales o polinomiales
- Sólidos tipo "caja" o prismas

### Fórmula
$$\iiint_E f(x,y,z)\, dV = \int_a^b \int_{g_1(x)}^{g_2(x)} \int_{h_1(x,y)}^{h_2(x,y)} f(x,y,z)\, dz\, dy\, dx$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Proyectar sobre un plano | Por ejemplo, plano $xy$ |
| 2 | Determinar límites de $z$ | En función de $x$ e $y$ |
| 3 | Determinar límites de $y$ | En función de $x$ |
| 4 | Determinar límites de $x$ | Constantes |
| 5 | Integrar de adentro hacia afuera | Tres integraciones |

### Ejemplo Detallado

**Problema:** Evaluar $\iiint_E z\, dV$ donde $E$ es el tetraedro con vértices $(0,0,0)$, $(1,0,0)$, $(0,2,0)$, $(0,0,3)$

**Paso 1:** Encontramos la ecuación del plano:
El plano pasa por $(1,0,0)$, $(0,2,0)$, $(0,0,3)$.
$$\frac{x}{1} + \frac{y}{2} + \frac{z}{3} = 1 \implies z = 3\left(1 - x - \frac{y}{2}\right)$$

**Paso 2:** Proyectamos sobre el plano $xy$:
La proyección es el triángulo con vértices $(0,0)$, $(1,0)$, $(0,2)$.
Ecuación del borde: $y = 2(1-x)$

**Paso 3:** Establecemos los límites:
- $0 \leq x \leq 1$
- $0 \leq y \leq 2(1-x)$
- $0 \leq z \leq 3(1 - x - y/2)$

**Paso 4:** Planteamos la integral:
$$\int_0^1 \int_0^{2(1-x)} \int_0^{3(1-x-y/2)} z\, dz\, dy\, dx$$

**Paso 5:** Integramos respecto a $z$:
$$\int_0^{3(1-x-y/2)} z\, dz = \frac{z^2}{2}\bigg|_0^{3(1-x-y/2)} = \frac{9}{2}\left(1-x-\frac{y}{2}\right)^2$$

**Paso 6:** Integramos respecto a $y$:
Sea $u = 1 - x - \frac{y}{2}$, entonces $du = -\frac{1}{2}dy$
$$\int_0^{2(1-x)} \frac{9}{2}u^2\, dy = \frac{9}{2} \cdot (-2)\int_{1-x}^0 u^2\, du = 9\int_0^{1-x} u^2\, du = 3(1-x)^3$$

**Paso 7:** Integramos respecto a $x$:
$$\int_0^1 3(1-x)^3\, dx = -3 \cdot \frac{(1-x)^4}{4}\bigg|_0^1 = -3\left(0 - \frac{1}{4}\right) = \frac{3}{4}$$

**Resultado:** $\iiint_E z\, dV = \boxed{\frac{3}{4}}$

---

## Método 7: Integral Triple en Coordenadas Cilíndricas

### Cuándo Usar
- Sólidos con simetría cilíndrica (cilindros, conos)
- Integrando contiene $x^2 + y^2$

### Fórmulas de Transformación
$$x = r\cos\theta, \quad y = r\sin\theta, \quad z = z$$

$$dV = r\, dz\, dr\, d\theta$$

### Ejemplo Detallado

**Problema:** Encontrar el volumen del sólido acotado por $z = \sqrt{x^2 + y^2}$ (cono) y $z = 4$

**Paso 1:** Convertimos a cilíndricas:
- Cono: $z = r$
- Plano: $z = 4$
- Intersección: $r = 4$

**Paso 2:** Establecemos límites:
- $0 \leq \theta \leq 2\pi$
- $0 \leq r \leq 4$
- $r \leq z \leq 4$

**Paso 3:** Planteamos la integral:
$$V = \int_0^{2\pi} \int_0^4 \int_r^4 r\, dz\, dr\, d\theta$$

**Paso 4:** Integramos respecto a $z$:
$$\int_r^4 r\, dz = r(4 - r) = 4r - r^2$$

**Paso 5:** Integramos respecto a $r$:
$$\int_0^4 (4r - r^2)\, dr = \left[2r^2 - \frac{r^3}{3}\right]_0^4 = 32 - \frac{64}{3} = \frac{32}{3}$$

**Paso 6:** Integramos respecto a $\theta$:
$$V = \int_0^{2\pi} \frac{32}{3}\, d\theta = \frac{32}{3} \cdot 2\pi = \frac{64\pi}{3}$$

**Resultado:** El volumen es $\boxed{\frac{64\pi}{3}}$

---

## Método 8: Integral Triple en Coordenadas Esféricas

### Cuándo Usar
- Sólidos con simetría esférica (esferas, conos desde el origen)
- Integrando contiene $x^2 + y^2 + z^2$

### Fórmulas de Transformación
$$x = \rho\sin\phi\cos\theta, \quad y = \rho\sin\phi\sin\theta, \quad z = \rho\cos\phi$$

$$dV = \rho^2\sin\phi\, d\rho\, d\phi\, d\theta$$

### Significado de las Variables

| Variable | Rango típico | Descripción |
|----------|--------------|-------------|
| $\rho$ | $0 \leq \rho \leq R$ | Distancia al origen |
| $\phi$ | $0 \leq \phi \leq \pi$ | Ángulo desde eje $z$ positivo |
| $\theta$ | $0 \leq \theta \leq 2\pi$ | Ángulo azimutal (en plano $xy$) |

### Ejemplo Detallado

**Problema:** Evaluar $\iiint_E (x^2 + y^2 + z^2)\, dV$ donde $E$ es la esfera $x^2 + y^2 + z^2 \leq 1$

**Paso 1:** Convertimos a esféricas:
- $x^2 + y^2 + z^2 = \rho^2$
- Esfera: $\rho \leq 1$

**Paso 2:** Establecemos límites:
- $0 \leq \rho \leq 1$
- $0 \leq \phi \leq \pi$
- $0 \leq \theta \leq 2\pi$

**Paso 3:** Planteamos la integral:
$$\int_0^{2\pi} \int_0^{\pi} \int_0^1 \rho^2 \cdot \rho^2\sin\phi\, d\rho\, d\phi\, d\theta$$

$$= \int_0^{2\pi} \int_0^{\pi} \int_0^1 \rho^4\sin\phi\, d\rho\, d\phi\, d\theta$$

**Paso 4:** Integramos respecto a $\rho$:
$$\int_0^1 \rho^4\, d\rho = \frac{\rho^5}{5}\bigg|_0^1 = \frac{1}{5}$$

**Paso 5:** Integramos respecto a $\phi$:
$$\int_0^{\pi} \sin\phi\, d\phi = [-\cos\phi]_0^{\pi} = -(-1 - 1) = 2$$

**Paso 6:** Integramos respecto a $\theta$:
$$\int_0^{2\pi} d\theta = 2\pi$$

**Paso 7:** Multiplicamos:
$$\frac{1}{5} \cdot 2 \cdot 2\pi = \frac{4\pi}{5}$$

**Resultado:** $\iiint_E (x^2 + y^2 + z^2)\, dV = \boxed{\frac{4\pi}{5}}$

---

## Método 9: Cambio de Variables General (Jacobiano)

### Cuándo Usar
- Transformaciones que no son polares, cilíndricas o esféricas
- Simplificar regiones o integrandos complicados

### Fórmula
Para la transformación $T: (u,v) \mapsto (x,y)$:
$$\iint_R f(x,y)\, dA = \iint_S f(x(u,v), y(u,v)) \left|\frac{\partial(x,y)}{\partial(u,v)}\right|\, du\, dv$$

### Jacobiano (2D)
$$\frac{\partial(x,y)}{\partial(u,v)} = \begin{vmatrix} \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\ \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} \end{vmatrix}$$

### Jacobiano (3D)
$$\frac{\partial(x,y,z)}{\partial(u,v,w)} = \begin{vmatrix} \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} & \frac{\partial x}{\partial w} \\ \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} & \frac{\partial y}{\partial w} \\ \frac{\partial z}{\partial u} & \frac{\partial z}{\partial v} & \frac{\partial z}{\partial w} \end{vmatrix}$$

### Ejemplo Detallado

**Problema:** Evaluar $\iint_R (x-y)\, dA$ donde $R$ es el paralelogramo con vértices $(0,0)$, $(1,1)$, $(2,0)$, $(1,-1)$

**Paso 1:** Identificamos las transformación. Los lados del paralelogramo están en:
- $y = x$ y $y = x - 2$ (pendiente 1)
- $y = -x$ y $y = -x + 2$ (pendiente $-1$)

Sea $u = x + y$, $v = x - y$

**Paso 2:** Determinamos los límites en $uv$:
- De $y = x$: $v = 0$
- De $y = x - 2$: $v = 2$
- De $y = -x$: $u = 0$
- De $y = -x + 2$: $u = 2$

Región en $uv$: $0 \leq u \leq 2$, $0 \leq v \leq 2$

**Paso 3:** Despejamos $x$ e $y$:
$$x = \frac{u + v}{2}, \quad y = \frac{u - v}{2}$$

**Paso 4:** Calculamos el Jacobiano:
$$\frac{\partial(x,y)}{\partial(u,v)} = \begin{vmatrix} \frac{1}{2} & \frac{1}{2} \\ \frac{1}{2} & -\frac{1}{2} \end{vmatrix} = \frac{1}{2} \cdot \left(-\frac{1}{2}\right) - \frac{1}{2} \cdot \frac{1}{2} = -\frac{1}{2}$$

$$\left|\frac{\partial(x,y)}{\partial(u,v)}\right| = \frac{1}{2}$$

**Paso 5:** Transformamos el integrando:
$$x - y = v$$

**Paso 6:** Planteamos la integral:
$$\iint_R (x-y)\, dA = \int_0^2 \int_0^2 v \cdot \frac{1}{2}\, du\, dv$$

**Paso 7:** Evaluamos:
$$= \frac{1}{2}\int_0^2 v\, dv \int_0^2 du = \frac{1}{2} \cdot 2 \cdot 2 = 2$$

**Resultado:** $\iint_R (x-y)\, dA = \boxed{2}$

---

## Método 10: Aplicaciones de Integrales Múltiples

### Centro de Masa

**Lámina plana con densidad $\rho(x,y)$:**
$$\bar{x} = \frac{1}{m}\iint_D x\rho(x,y)\, dA, \quad \bar{y} = \frac{1}{m}\iint_D y\rho(x,y)\, dA$$

donde $m = \iint_D \rho(x,y)\, dA$

**Sólido con densidad $\rho(x,y,z)$:**
$$\bar{x} = \frac{1}{m}\iiint_E x\rho\, dV, \quad \bar{y} = \frac{1}{m}\iiint_E y\rho\, dV, \quad \bar{z} = \frac{1}{m}\iiint_E z\rho\, dV$$

### Ejemplo: Centro de Masa

**Problema:** Encontrar el centro de masa de la lámina semicircular $x^2 + y^2 \leq 4$, $y \geq 0$, con densidad $\rho = 1$.

**Por simetría:** $\bar{x} = 0$

**Calculamos la masa:**
$$m = \iint_D dA = \frac{1}{2}\pi(2)^2 = 2\pi$$

**Calculamos $\bar{y}$** (usando polares):
$$\iint_D y\, dA = \int_0^{\pi} \int_0^2 (r\sin\theta) \cdot r\, dr\, d\theta$$

$$= \int_0^{\pi} \sin\theta\, d\theta \int_0^2 r^2\, dr = [-\cos\theta]_0^{\pi} \cdot \frac{r^3}{3}\bigg|_0^2 = 2 \cdot \frac{8}{3} = \frac{16}{3}$$

$$\bar{y} = \frac{16/3}{2\pi} = \frac{8}{3\pi}$$

**Resultado:** Centro de masa: $\boxed{\left(0, \frac{8}{3\pi}\right)}$

---

### Momentos de Inercia

**Respecto a los ejes:**
$$I_x = \iint_D y^2\rho\, dA, \quad I_y = \iint_D x^2\rho\, dA$$

**Respecto al origen (polar):**
$$I_0 = \iint_D (x^2 + y^2)\rho\, dA = I_x + I_y$$

### Ejemplo: Momento de Inercia

**Problema:** Encontrar $I_x$ para el disco $x^2 + y^2 \leq 1$ con $\rho = 1$.

**Usamos polares:**
$$I_x = \int_0^{2\pi} \int_0^1 (r\sin\theta)^2 \cdot r\, dr\, d\theta$$

$$= \int_0^{2\pi} \sin^2\theta\, d\theta \int_0^1 r^3\, dr$$

$$= \pi \cdot \frac{1}{4} = \frac{\pi}{4}$$

**Resultado:** $I_x = \boxed{\frac{\pi}{4}}$

---

## Método 11: Área de Superficie

### Cuándo Usar
- Calcular el área de una superficie $z = f(x,y)$ sobre una región $D$

### Fórmula
$$S = \iint_D \sqrt{1 + \left(\frac{\partial z}{\partial x}\right)^2 + \left(\frac{\partial z}{\partial y}\right)^2}\, dA$$

### Ejemplo Detallado

**Problema:** Encontrar el área de la porción del paraboloide $z = x^2 + y^2$ que está debajo del plano $z = 4$

**Paso 1:** Calculamos las [derivadas](../../../glossary.md#derivadas) parciales:
$$\frac{\partial z}{\partial x} = 2x, \quad \frac{\partial z}{\partial y} = 2y$$

**Paso 2:** Calculamos el integrando:
$$\sqrt{1 + 4x^2 + 4y^2}$$

**Paso 3:** La región $D$ es el disco $x^2 + y^2 \leq 4$. Usamos polares:
$$S = \int_0^{2\pi} \int_0^2 \sqrt{1 + 4r^2} \cdot r\, dr\, d\theta$$

**Paso 4:** Integramos respecto a $r$:
Sea $u = 1 + 4r^2$, $du = 8r\, dr$
$$\int_0^2 r\sqrt{1+4r^2}\, dr = \frac{1}{8}\int_1^{17} u^{1/2}\, du = \frac{1}{8} \cdot \frac{2}{3}[u^{3/2}]_1^{17}$$

$$= \frac{1}{12}(17^{3/2} - 1) = \frac{17\sqrt{17} - 1}{12}$$

**Paso 5:** Integramos respecto a $\theta$:
$$S = 2\pi \cdot \frac{17\sqrt{17} - 1}{12} = \frac{\pi(17\sqrt{17} - 1)}{6}$$

**Resultado:** El área es $\boxed{\frac{\pi(17\sqrt{17} - 1)}{6}}$

---

## Tabla Resumen de Coordenadas

| Sistema | Variables | Jacobiano |
|---------|-----------|-----------|
| **Polar** | $x = r\cos\theta$, $y = r\sin\theta$ | $r$ |
| **Cilíndrico** | $x = r\cos\theta$, $y = r\sin\theta$, $z = z$ | $r$ |
| **Esférico** | $x = \rho\sin\phi\cos\theta$, $y = \rho\sin\phi\sin\theta$, $z = \rho\cos\phi$ | $\rho^2\sin\phi$ |
