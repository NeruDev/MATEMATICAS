# Teoría — Integración múltiple

La integración múltiple extiende el concepto de integral a funciones de varias variables, permitiendo calcular volúmenes, masas, centros de masa, flujos y trabajo.

---

## 5.1 Cálculo de áreas e integrales dobles

### Definición de integral doble
La **integral doble** de $f(x, y)$ sobre una región $R$ se define como:

$$\iint_R f(x, y)\,dA = \lim_{n \to \infty} \sum_{i=1}^n f(x_i^*, y_i^*)\,\Delta A_i$$

### Interpretaciones

| Si $f(x,y)$... | La integral calcula... |
|---------------|------------------------|
| $f(x,y) = 1$ | Área de $R$ |
| $f(x,y) \geq 0$ | Volumen bajo la superficie $z = f(x,y)$ |
| $f(x,y) = \rho(x,y)$ (densidad) | Masa de la lámina |

### Propiedades
- **Linealidad**: $\iint_R (af + bg)\,dA = a\iint_R f\,dA + b\iint_R g\,dA$
- **Aditividad**: Si $R = R_1 \cup R_2$ (disjuntas), $\iint_R f\,dA = \iint_{R_1} f\,dA + \iint_{R_2} f\,dA$
- **Comparación**: Si $f \leq g$ en $R$, entonces $\iint_R f\,dA \leq \iint_R g\,dA$

---

## 5.2 Integrales iteradas y Teorema de Fubini

### Teorema de Fubini
Si $f$ es continua en $R = [a, b] \times [c, d]$:

$$\iint_R f(x, y)\,dA = \int_a^b \int_c^d f(x, y)\,dy\,dx = \int_c^d \int_a^b f(x, y)\,dx\,dy$$

**Importancia**: Permite calcular integrales dobles como integrales iteradas (integrar "de adentro hacia afuera").

### Orden de integración
El orden puede elegirse estratégicamente para simplificar el cálculo.

---

## 5.3 Integral doble en coordenadas rectangulares

### Regiones Tipo I (vertical)
$R = \{(x, y) : a \leq x \leq b, \, g_1(x) \leq y \leq g_2(x)\}$

$$\iint_R f(x, y)\,dA = \int_a^b \int_{g_1(x)}^{g_2(x)} f(x, y)\,dy\,dx$$

### Regiones Tipo II (horizontal)
$R = \{(x, y) : c \leq y \leq d, \, h_1(y) \leq x \leq h_2(y)\}$

$$\iint_R f(x, y)\,dA = \int_c^d \int_{h_1(y)}^{h_2(y)} f(x, y)\,dx\,dy$$

### Criterio de elección
- **Tipo I**: Los límites de $y$ son funciones de $x$.
- **Tipo II**: Los límites de $x$ son funciones de $y$.
- Elige el tipo que simplifique los límites y la integración.

---

## 5.4 Integral doble en coordenadas polares

### Transformación
$$x = r\cos\theta, \quad y = r\sin\theta$$

### Jacobiano
$$dA = r\,dr\,d\theta$$

**Nota**: El factor $r$ es esencial; proviene del Jacobiano de la transformación.

### Fórmula
$$\iint_R f(x, y)\,dA = \int_{\alpha}^{\beta} \int_{r_1(\theta)}^{r_2(\theta)} f(r\cos\theta, r\sin\theta) \cdot r\,dr\,d\theta$$

### Regiones comunes

| Región | Límites |
|--------|---------|
| Disco de radio $a$ | $0 \leq r \leq a$, $0 \leq \theta \leq 2\pi$ |
| Anillo | $a \leq r \leq b$, $0 \leq \theta \leq 2\pi$ |
| Sector circular | $0 \leq r \leq a$, $\alpha \leq \theta \leq \beta$ |
| Cardioide | $0 \leq r \leq a(1 + \cos\theta)$ |

### Cuándo usar polares
- Región tiene simetría circular.
- El integrando contiene $x^2 + y^2$, $\sqrt{x^2+y^2}$, etc.

---

## 5.5 Integral triple en coordenadas rectangulares

### Definición
$$\iiint_V f(x, y, z)\,dV = \int_a^b \int_{g_1(x)}^{g_2(x)} \int_{h_1(x,y)}^{h_2(x,y)} f(x, y, z)\,dz\,dy\,dx$$

### Interpretaciones

| Si $f(x,y,z)$... | La integral calcula... |
|-----------------|------------------------|
| $f = 1$ | Volumen de $V$ |
| $f = \rho(x,y,z)$ (densidad) | Masa del sólido |

### Aplicaciones
- **Masa**: $M = \iiint_V \rho\,dV$
- **Centro de masa**: $\bar{x} = \frac{1}{M}\iiint_V x\rho\,dV$
- **Momentos de inercia**: $I_z = \iiint_V (x^2 + y^2)\rho\,dV$

---

## 5.6 Integral triple en coordenadas cilíndricas y esféricas

### Coordenadas cilíndricas $(r, \theta, z)$

$$x = r\cos\theta, \quad y = r\sin\theta, \quad z = z$$

**Jacobiano**: $dV = r\,dr\,d\theta\,dz$

**Usar cuando**: El sólido tiene simetría cilíndrica (cilindros, conos, paraboloides).

### Coordenadas esféricas $(\rho, \phi, \theta)$

$$x = \rho\sin\phi\cos\theta, \quad y = \rho\sin\phi\sin\theta, \quad z = \rho\cos\phi$$

- $\rho$: distancia al origen
- $\phi$: ángulo desde el eje $z$ positivo ($0 \leq \phi \leq \pi$)
- $\theta$: ángulo azimutal ($0 \leq \theta \leq 2\pi$)

**Jacobiano**: $dV = \rho^2 \sin\phi\,d\rho\,d\phi\,d\theta$

**Usar cuando**: El sólido tiene simetría esférica (esferas, conos desde el origen).

### Comparación de sistemas

| Sistema | Jacobiano | Mejor para |
|---------|-----------|------------|
| Rectangular | $dx\,dy\,dz$ | Cajas, prismas |
| Cilíndrico | $r\,dr\,d\theta\,dz$ | Cilindros, paraboloides |
| Esférico | $\rho^2\sin\phi\,d\rho\,d\phi\,d\theta$ | Esferas, conos |

---

## 5.7 Campos vectoriales

### Definición
Un **campo vectorial** en $\mathbb{R}^2$ o $\mathbb{R}^3$ asigna un vector a cada punto:

$$\mathbf{F}(x, y) = \langle P(x,y), Q(x,y) \rangle$$
$$\mathbf{F}(x, y, z) = \langle P, Q, R \rangle$$

### Ejemplos físicos

| Campo | Expresión | Descripción |
|-------|-----------|-------------|
| Gravitacional | $\mathbf{F} = -\frac{GMm}{r^2}\hat{\mathbf{r}}$ | Atracción hacia masa central |
| Velocidad de fluido | $\mathbf{v}(x, y, z)$ | Velocidad en cada punto |
| Eléctrico | $\mathbf{E} = -\nabla V$ | Fuerza por unidad de carga |

### Campo conservativo
Un campo $\mathbf{F}$ es **conservativo** si existe una función escalar $f$ tal que:

$$\mathbf{F} = \nabla f$$

donde $f$ es el **potencial** de $\mathbf{F}$.

**Criterio (2D)**: $\mathbf{F} = \langle P, Q \rangle$ es conservativo si $\frac{\partial P}{\partial y} = \frac{\partial Q}{\partial x}$.

---

## 5.8 Integral de línea

### Integral de línea de un campo escalar
$$\int_C f\,ds = \int_a^b f(\mathbf{r}(t)) \|\mathbf{r}'(t)\|\,dt$$

### Integral de línea de un campo vectorial
$$\int_C \mathbf{F} \cdot d\mathbf{r} = \int_a^b \mathbf{F}(\mathbf{r}(t)) \cdot \mathbf{r}'(t)\,dt$$

### Interpretaciones

| Integral | Significado físico |
|----------|-------------------|
| $\int_C \mathbf{F} \cdot d\mathbf{r}$ | Trabajo de $\mathbf{F}$ sobre $C$ |
| $\int_C \mathbf{F} \cdot \mathbf{n}\,ds$ | Flujo de $\mathbf{F}$ a través de $C$ |

### Propiedades
- **Independencia del camino**: Si $\mathbf{F}$ es conservativo, la integral solo depende de los extremos:
  $$\int_C \nabla f \cdot d\mathbf{r} = f(\text{final}) - f(\text{inicial})$$

---

## 5.9 Divergencia y rotacional

### Divergencia
$$\nabla \cdot \mathbf{F} = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z}$$

**Interpretación**: Mide la "expansión" o "contracción" del campo en un punto.
- $\nabla \cdot \mathbf{F} > 0$: fuente (el flujo sale)
- $\nabla \cdot \mathbf{F} < 0$: sumidero (el flujo entra)

### Rotacional
$$\nabla \times \mathbf{F} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ P & Q & R \end{vmatrix} = \left\langle \frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z}, \frac{\partial P}{\partial z} - \frac{\partial R}{\partial x}, \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right\rangle$$

**Interpretación**: Mide la "rotación" o "circulación local" del campo.
- $\nabla \times \mathbf{F} = \mathbf{0}$: campo irrotacional (sin vórtices)

### Identidades importantes
- $\nabla \times (\nabla f) = \mathbf{0}$ (el gradiente es irrotacional)
- $\nabla \cdot (\nabla \times \mathbf{F}) = 0$ (el rotacional es solenoidal)

---

## 5.10 Teoremas fundamentales de integrales

### Teorema de Green (2D)
Para una curva cerrada simple $C$ orientada positivamente (CCW) que encierra $R$:

$$\oint_C P\,dx + Q\,dy = \iint_R \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA$$

**Aplicaciones**:
- Calcular áreas: $\text{Área} = \frac{1}{2}\oint_C (x\,dy - y\,dx)$
- Simplificar integrales de línea

### Teorema de la divergencia (Gauss)
Para una superficie cerrada $S$ que encierra $V$, con normal exterior:

$$\oiint_S \mathbf{F} \cdot d\mathbf{S} = \iiint_V (\nabla \cdot \mathbf{F})\,dV$$

**Interpretación**: El flujo total a través de una superficie cerrada es igual a la integral de la divergencia en el volumen interior.

### Teorema de Stokes
Para una superficie $S$ con borde $C$ (orientados consistentemente):

$$\oint_C \mathbf{F} \cdot d\mathbf{r} = \iint_S (\nabla \times \mathbf{F}) \cdot d\mathbf{S}$$

**Interpretación**: La circulación de $\mathbf{F}$ alrededor del borde es igual al flujo del rotacional a través de la superficie.

### Relación entre teoremas

| Teorema | Dimensión | Conecta... |
|---------|-----------|------------|
| Fund. del Cálculo | 1D | Integral de línea ↔ Puntos |
| Green | 2D | Integral de línea ↔ Integral doble |
| Stokes | 3D (superficie) | Circulación ↔ Flujo del rotacional |
| Gauss | 3D (volumen) | Flujo ↔ Integral triple de divergencia |

---

## Resumen de fórmulas clave

| Concepto | Fórmula |
|----------|---------|
| Integral doble (polares) | $\iint f\,dA = \int\int f(r\cos\theta, r\sin\theta)\,r\,dr\,d\theta$ |
| Integral triple (cilíndricas) | $\iiint f\,dV = \int\int\int f\,r\,dr\,d\theta\,dz$ |
| Integral triple (esféricas) | $\iiint f\,dV = \int\int\int f\,\rho^2\sin\phi\,d\rho\,d\phi\,d\theta$ |
| Integral de línea | $\int_C \mathbf{F} \cdot d\mathbf{r} = \int_a^b \mathbf{F}(\mathbf{r}(t)) \cdot \mathbf{r}'(t)\,dt$ |
| Divergencia | $\nabla \cdot \mathbf{F} = P_x + Q_y + R_z$ |
| Rotacional | $\nabla \times \mathbf{F} = \langle R_y - Q_z, P_z - R_x, Q_x - P_y \rangle$ |
| Green | $\oint_C P\,dx + Q\,dy = \iint_R (Q_x - P_y)\,dA$ |
| Gauss | $\oiint_S \mathbf{F} \cdot d\mathbf{S} = \iiint_V \nabla \cdot \mathbf{F}\,dV$ |
| Stokes | $\oint_C \mathbf{F} \cdot d\mathbf{r} = \iint_S (\nabla \times \mathbf{F}) \cdot d\mathbf{S}$ |
