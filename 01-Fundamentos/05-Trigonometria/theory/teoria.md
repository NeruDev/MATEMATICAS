<!--
HUMANO:
Teoría completa de trigonometría plana desde ángulos hasta resolución de triángulos.

IA:
No incluyas métodos de solución ni problemas aquí.
Presenta definiciones formales y propiedades fundamentales.

---
content_type: theory_comprehensive
expected_output:
  default: markdown
audience: self-study
maturity: complete
---
-->

# Teoría de Trigonometría

## 5.1 Ángulos y Medidas

### Definición de Ángulo
Un **ángulo** es la rotación de un rayo alrededor de su punto inicial (vértice) desde una posición inicial hasta una posición final.

### Ángulo en Posición Estándar
Un ángulo está en **posición estándar** cuando:
- Su vértice está en el origen del plano cartesiano
- Su lado inicial coincide con el semieje positivo de las $x$

### Medidas de Ángulos

#### Grados
- Una vuelta completa = 360°
- Un ángulo recto = 90°
- Subdivisiones: 1° = 60' (minutos), 1' = 60'' (segundos)

#### Radianes
El **radián** es la medida del ángulo central que subtiende un arco de longitud igual al radio.
- Una vuelta completa = $2\pi$ radianes
- Un ángulo recto = $\frac{\pi}{2}$ radianes

### Conversión entre Grados y Radianes

$$\text{Radianes} = \text{Grados} \times \frac{\pi}{180°}$$

$$\text{Grados} = \text{Radianes} \times \frac{180°}{\pi}$$

### Ángulos Notables

| Grados | Radianes |
|--------|----------|
| 0° | 0 |
| 30° | $\frac{\pi}{6}$ |
| 45° | $\frac{\pi}{4}$ |
| 60° | $\frac{\pi}{3}$ |
| 90° | $\frac{\pi}{2}$ |
| 180° | $\pi$ |
| 270° | $\frac{3\pi}{2}$ |
| 360° | $2\pi$ |

### Ángulos Coterminales
Dos ángulos son **coterminales** si tienen el mismo lado terminal cuando están en posición estándar.
$$\theta_2 = \theta_1 + 360°k \quad (k \in \mathbb{Z})$$
$$\theta_2 = \theta_1 + 2\pi k \quad \text{(en radianes)}$$

### Longitud de Arco y Área de Sector

Para un ángulo $\theta$ (en radianes) en un círculo de radio $r$:

**Longitud del arco:**
$$s = r\theta$$

**Área del sector circular:**
$$A = \frac{1}{2}r^2\theta$$

---

## 5.2 Razones Trigonométricas en el Triángulo Rectángulo

### Definiciones
En un triángulo rectángulo con un ángulo agudo $\theta$:

| Razón | Definición | Abreviación |
|-------|------------|-------------|
| Seno | $\sin\theta = \frac{\text{cateto opuesto}}{\text{hipotenusa}}$ | $\sin\theta = \frac{CO}{H}$ |
| Coseno | $\cos\theta = \frac{\text{cateto adyacente}}{\text{hipotenusa}}$ | $\cos\theta = \frac{CA}{H}$ |
| Tangente | $\tan\theta = \frac{\text{cateto opuesto}}{\text{cateto adyacente}}$ | $\tan\theta = \frac{CO}{CA}$ |
| Cotangente | $\cot\theta = \frac{\text{cateto adyacente}}{\text{cateto opuesto}}$ | $\cot\theta = \frac{CA}{CO}$ |
| Secante | $\sec\theta = \frac{\text{hipotenusa}}{\text{cateto adyacente}}$ | $\sec\theta = \frac{H}{CA}$ |
| Cosecante | $\csc\theta = \frac{\text{hipotenusa}}{\text{cateto opuesto}}$ | $\csc\theta = \frac{H}{CO}$ |

### Mnemotecnia: SOH-CAH-TOA
- **S**eno = **O**puesto / **H**ipotenusa
- **C**oseno = **A**dyacente / **H**ipotenusa
- **T**angente = **O**puesto / **A**dyacente

### Valores de Ángulos Notables

| $\theta$ | $\sin\theta$ | $\cos\theta$ | $\tan\theta$ |
|----------|--------------|--------------|--------------|
| 0° | 0 | 1 | 0 |
| 30° | $\frac{1}{2}$ | $\frac{\sqrt{3}}{2}$ | $\frac{\sqrt{3}}{3}$ |
| 45° | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{2}}{2}$ | 1 |
| 60° | $\frac{\sqrt{3}}{2}$ | $\frac{1}{2}$ | $\sqrt{3}$ |
| 90° | 1 | 0 | indefinida |

### Relaciones entre Cofunciones
Para ángulos complementarios ($\alpha + \beta = 90°$):
- $\sin\alpha = \cos(90° - \alpha) = \cos\beta$
- $\tan\alpha = \cot(90° - \alpha) = \cot\beta$
- $\sec\alpha = \csc(90° - \alpha) = \csc\beta$

---

## 5.3 El Círculo Unitario

### Definición
El **círculo unitario** es la circunferencia de radio 1 centrada en el origen:
$$x^2 + y^2 = 1$$

### Funciones Trigonométricas en el Círculo Unitario
Para un ángulo $\theta$ en posición estándar, si $(x, y)$ es el punto donde el lado terminal interseca al círculo unitario:

$$\cos\theta = x \qquad \sin\theta = y$$

$$\tan\theta = \frac{y}{x} \quad (x \neq 0) \qquad \cot\theta = \frac{x}{y} \quad (y \neq 0)$$

$$\sec\theta = \frac{1}{x} \quad (x \neq 0) \qquad \csc\theta = \frac{1}{y} \quad (y \neq 0)$$

### Signos en los Cuadrantes

| Cuadrante | $\sin\theta$ | $\cos\theta$ | $\tan\theta$ |
|-----------|--------------|--------------|--------------|
| I (0° - 90°) | + | + | + |
| II (90° - 180°) | + | − | − |
| III (180° - 270°) | − | − | + |
| IV (270° - 360°) | − | + | − |

**Mnemotecnia:** "**A**ll **S**tudents **T**ake **C**alculus"
- Cuadrante I: **A**ll (todas positivas)
- Cuadrante II: **S**in (solo seno positivo)
- Cuadrante III: **T**an (solo tangente positiva)
- Cuadrante IV: **C**os (solo coseno positivo)

### Coordenadas de Ángulos Notables en el Círculo Unitario

| Ángulo | Coordenada $(x, y)$ |
|--------|---------------------|
| 0° | $(1, 0)$ |
| 30° | $\left(\frac{\sqrt{3}}{2}, \frac{1}{2}\right)$ |
| 45° | $\left(\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2}\right)$ |
| 60° | $\left(\frac{1}{2}, \frac{\sqrt{3}}{2}\right)$ |
| 90° | $(0, 1)$ |
| 120° | $\left(-\frac{1}{2}, \frac{\sqrt{3}}{2}\right)$ |
| 135° | $\left(-\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2}\right)$ |
| 150° | $\left(-\frac{\sqrt{3}}{2}, \frac{1}{2}\right)$ |
| 180° | $(-1, 0)$ |
| 210° | $\left(-\frac{\sqrt{3}}{2}, -\frac{1}{2}\right)$ |
| 225° | $\left(-\frac{\sqrt{2}}{2}, -\frac{\sqrt{2}}{2}\right)$ |
| 240° | $\left(-\frac{1}{2}, -\frac{\sqrt{3}}{2}\right)$ |
| 270° | $(0, -1)$ |
| 300° | $\left(\frac{1}{2}, -\frac{\sqrt{3}}{2}\right)$ |
| 315° | $\left(\frac{\sqrt{2}}{2}, -\frac{\sqrt{2}}{2}\right)$ |
| 330° | $\left(\frac{\sqrt{3}}{2}, -\frac{1}{2}\right)$ |

### Ángulos de Referencia
El **ángulo de referencia** $\theta_R$ es el ángulo agudo formado entre el lado terminal y el eje $x$.

| Cuadrante | Ángulo de referencia |
|-----------|----------------------|
| I | $\theta_R = \theta$ |
| II | $\theta_R = 180° - \theta$ |
| III | $\theta_R = \theta - 180°$ |
| IV | $\theta_R = 360° - \theta$ |

---

## 5.4 Gráficas de Funciones Trigonométricas

### Función Seno: $y = \sin x$
- **Dominio:** $\mathbb{R}$
- **Rango:** $[-1, 1]$
- **Período:** $2\pi$
- **Ceros:** $x = n\pi$, $n \in \mathbb{Z}$
- **Máximos:** $x = \frac{\pi}{2} + 2n\pi$
- **Mínimos:** $x = \frac{3\pi}{2} + 2n\pi$

### Función Coseno: $y = \cos x$
- **Dominio:** $\mathbb{R}$
- **Rango:** $[-1, 1]$
- **Período:** $2\pi$
- **Ceros:** $x = \frac{\pi}{2} + n\pi$
- **Máximos:** $x = 2n\pi$
- **Mínimos:** $x = \pi + 2n\pi$

### Función Tangente: $y = \tan x$
- **Dominio:** $x \neq \frac{\pi}{2} + n\pi$
- **Rango:** $\mathbb{R}$
- **Período:** $\pi$
- **Ceros:** $x = n\pi$
- **Asíntotas verticales:** $x = \frac{\pi}{2} + n\pi$

### Transformaciones: $y = A\sin(Bx - C) + D$

| Parámetro | Efecto |
|-----------|--------|
| $\lvert A \rvert$ | **Amplitud** (estiramiento vertical) |
| $\frac{2\pi}{\lvert B \rvert}$ | **Período** |
| $\frac{C}{B}$ | **Desplazamiento horizontal** (fase) |
| $D$ | **Desplazamiento vertical** |

**Frecuencia:** $f = \frac{\lvert B \rvert}{2\pi}$

---

## 5.5 Identidades Trigonométricas Fundamentales

### Identidades Recíprocas
$$\csc\theta = \frac{1}{\sin\theta} \qquad \sec\theta = \frac{1}{\cos\theta} \qquad \cot\theta = \frac{1}{\tan\theta}$$

### Identidades de Cociente
$$\tan\theta = \frac{\sin\theta}{\cos\theta} \qquad \cot\theta = \frac{\cos\theta}{\sin\theta}$$

### Identidades Pitagóricas
$$\sin^2\theta + \cos^2\theta = 1$$
$$1 + \tan^2\theta = \sec^2\theta$$
$$1 + \cot^2\theta = \csc^2\theta$$

### Identidades de Paridad
$$\sin(-\theta) = -\sin\theta \quad \text{(función impar)}$$
$$\cos(-\theta) = \cos\theta \quad \text{(función par)}$$
$$\tan(-\theta) = -\tan\theta \quad \text{(función impar)}$$

### Identidades de Cofunción
$$\sin\left(\frac{\pi}{2} - \theta\right) = \cos\theta$$
$$\cos\left(\frac{\pi}{2} - \theta\right) = \sin\theta$$
$$\tan\left(\frac{\pi}{2} - \theta\right) = \cot\theta$$

---

## 5.6 Identidades de Suma, Resta y Múltiplos de Ángulos

### Fórmulas de Suma y Resta
$$\sin(\alpha \pm \beta) = \sin\alpha\cos\beta \pm \cos\alpha\sin\beta$$
$$\cos(\alpha \pm \beta) = \cos\alpha\cos\beta \mp \sin\alpha\sin\beta$$
$$\tan(\alpha \pm \beta) = \frac{\tan\alpha \pm \tan\beta}{1 \mp \tan\alpha\tan\beta}$$

### Fórmulas del Ángulo Doble
$$\sin(2\theta) = 2\sin\theta\cos\theta$$

$$\cos(2\theta) = \cos^2\theta - \sin^2\theta = 2\cos^2\theta - 1 = 1 - 2\sin^2\theta$$

$$\tan(2\theta) = \frac{2\tan\theta}{1 - \tan^2\theta}$$

### Fórmulas del Ángulo Medio
$$\sin\left(\frac{\theta}{2}\right) = \pm\sqrt{\frac{1 - \cos\theta}{2}}$$

$$\cos\left(\frac{\theta}{2}\right) = \pm\sqrt{\frac{1 + \cos\theta}{2}}$$

$$\tan\left(\frac{\theta}{2}\right) = \pm\sqrt{\frac{1 - \cos\theta}{1 + \cos\theta}} = \frac{\sin\theta}{1 + \cos\theta} = \frac{1 - \cos\theta}{\sin\theta}$$

(El signo depende del cuadrante donde se encuentra $\frac{\theta}{2}$)

### Fórmulas de Reducción de Potencia
$$\sin^2\theta = \frac{1 - \cos(2\theta)}{2}$$
$$\cos^2\theta = \frac{1 + \cos(2\theta)}{2}$$
$$\tan^2\theta = \frac{1 - \cos(2\theta)}{1 + \cos(2\theta)}$$

### Fórmulas de Producto a Suma
$$\sin\alpha\cos\beta = \frac{1}{2}[\sin(\alpha + \beta) + \sin(\alpha - \beta)]$$
$$\cos\alpha\cos\beta = \frac{1}{2}[\cos(\alpha - \beta) + \cos(\alpha + \beta)]$$
$$\sin\alpha\sin\beta = \frac{1}{2}[\cos(\alpha - \beta) - \cos(\alpha + \beta)]$$

### Fórmulas de Suma a Producto
$$\sin\alpha + \sin\beta = 2\sin\left(\frac{\alpha + \beta}{2}\right)\cos\left(\frac{\alpha - \beta}{2}\right)$$
$$\sin\alpha - \sin\beta = 2\cos\left(\frac{\alpha + \beta}{2}\right)\sin\left(\frac{\alpha - \beta}{2}\right)$$
$$\cos\alpha + \cos\beta = 2\cos\left(\frac{\alpha + \beta}{2}\right)\cos\left(\frac{\alpha - \beta}{2}\right)$$
$$\cos\alpha - \cos\beta = -2\sin\left(\frac{\alpha + \beta}{2}\right)\sin\left(\frac{\alpha - \beta}{2}\right)$$

---

## 5.7 Ecuaciones Trigonométricas

### Ecuaciones Básicas

**Para $\sin\theta = k$ donde $\lvert k \rvert \leq 1$:**
$$\theta = \arcsin(k) + 2\pi n \quad \text{o} \quad \theta = \pi - \arcsin(k) + 2\pi n$$

**Para $\cos\theta = k$ donde $\lvert k \rvert \leq 1$:**
$$\theta = \pm\arccos(k) + 2\pi n$$

**Para $\tan\theta = k$:**
$$\theta = \arctan(k) + \pi n$$

### Valores Especiales

| Ecuación | Soluciones generales |
|----------|---------------------|
| $\sin\theta = 0$ | $\theta = n\pi$ |
| $\sin\theta = 1$ | $\theta = \frac{\pi}{2} + 2\pi n$ |
| $\sin\theta = -1$ | $\theta = \frac{3\pi}{2} + 2\pi n$ |
| $\cos\theta = 0$ | $\theta = \frac{\pi}{2} + n\pi$ |
| $\cos\theta = 1$ | $\theta = 2\pi n$ |
| $\cos\theta = -1$ | $\theta = \pi + 2\pi n$ |
| $\tan\theta = 0$ | $\theta = n\pi$ |

---

## 5.8 Funciones Trigonométricas Inversas

### Función Arcoseno
$$y = \arcsin(x) = \sin^{-1}(x)$$
- **Dominio:** $[-1, 1]$
- **Rango:** $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$
- **Interpretación:** "¿Qué ángulo tiene seno igual a $x$?"

### Función Arcocoseno
$$y = \arccos(x) = \cos^{-1}(x)$$
- **Dominio:** $[-1, 1]$
- **Rango:** $[0, \pi]$
- **Interpretación:** "¿Qué ángulo tiene coseno igual a $x$?"

### Función Arcotangente
$$y = \arctan(x) = \tan^{-1}(x)$$
- **Dominio:** $\mathbb{R}$
- **Rango:** $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$
- **Interpretación:** "¿Qué ángulo tiene tangente igual a $x$?"

### Valores Notables de Funciones Inversas

| $x$ | $\arcsin(x)$ | $\arccos(x)$ | $\arctan(x)$ |
|-----|--------------|--------------|--------------|
| 0 | 0 | $\frac{\pi}{2}$ | 0 |
| $\frac{1}{2}$ | $\frac{\pi}{6}$ | $\frac{\pi}{3}$ | — |
| $\frac{\sqrt{2}}{2}$ | $\frac{\pi}{4}$ | $\frac{\pi}{4}$ | — |
| $\frac{\sqrt{3}}{2}$ | $\frac{\pi}{3}$ | $\frac{\pi}{6}$ | — |
| 1 | $\frac{\pi}{2}$ | 0 | $\frac{\pi}{4}$ |
| $\sqrt{3}$ | — | — | $\frac{\pi}{3}$ |

### Identidades de Funciones Inversas
$$\arcsin(x) + \arccos(x) = \frac{\pi}{2}$$
$$\arctan(x) + \text{arccot}(x) = \frac{\pi}{2}$$

---

## 5.9 Ley de Senos y Ley de Cosenos

### Ley de Senos
En cualquier triángulo con lados $a$, $b$, $c$ opuestos a los ángulos $A$, $B$, $C$:

$$\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} = 2R$$

donde $R$ es el radio del círculo circunscrito.

**Aplicaciones:**
- Dado ALA (Ángulo-Lado-Ángulo)
- Dado LAA (Lado-Ángulo-Ángulo)
- Dado LLA (Lado-Lado-Ángulo) - **Caso ambiguo**

### El Caso Ambiguo (LLA)
Dado $a$, $b$ y $\angle A$ (ángulo opuesto a $a$):

| Condición | Número de triángulos |
|-----------|---------------------|
| $a < b\sin A$ | 0 (ninguno) |
| $a = b\sin A$ | 1 (rectángulo) |
| $b\sin A < a < b$ | 2 (ambiguo) |
| $a \geq b$ | 1 |

### Ley de Cosenos
$$a^2 = b^2 + c^2 - 2bc\cos A$$
$$b^2 = a^2 + c^2 - 2ac\cos B$$
$$c^2 = a^2 + b^2 - 2ab\cos C$$

**Forma para hallar ángulos:**
$$\cos A = \frac{b^2 + c^2 - a^2}{2bc}$$

**Aplicaciones:**
- Dado LLL (tres lados)
- Dado LAL (Lado-Ángulo-Lado)

### Área del Triángulo

**Fórmula con dos lados y ángulo incluido:**
$$A = \frac{1}{2}ab\sin C = \frac{1}{2}bc\sin A = \frac{1}{2}ac\sin B$$

**Fórmula de Herón:**
$$A = \sqrt{s(s-a)(s-b)(s-c)}$$
donde $s = \frac{a+b+c}{2}$

---

## 5.10 Aplicaciones de la Trigonometría

### Problemas de Altura y Distancia

**Ángulo de elevación:** Ángulo formado por la horizontal hacia arriba.

**Ángulo de depresión:** Ángulo formado por la horizontal hacia abajo.

**Nota:** El ángulo de elevación desde A hacia B es igual al ángulo de depresión desde B hacia A.

### Vectores y Componentes
Un vector $\vec{v}$ de magnitud $r$ y dirección $\theta$:
- Componente horizontal: $v_x = r\cos\theta$
- Componente vertical: $v_y = r\sin\theta$

### Movimiento Armónico Simple
La posición de un objeto en movimiento armónico simple:
$$x(t) = A\cos(\omega t + \phi)$$
donde:
- $A$ = amplitud
- $\omega$ = frecuencia angular
- $\phi$ = fase inicial
- Período $T = \frac{2\pi}{\omega}$

### Navegación y Rumbos
- Los rumbos se miden desde el Norte, en sentido horario.
- Rumbo N30°E significa 30° al este del norte.
- Rumbo S45°W significa 45° al oeste del sur.

---

## Resumen de Fórmulas Principales

### Identidades Fundamentales
| Tipo | Fórmulas |
|------|----------|
| Pitagóricas | $\sin^2\theta + \cos^2\theta = 1$ |
| Recíprocas | $\csc\theta = \frac{1}{\sin\theta}$, $\sec\theta = \frac{1}{\cos\theta}$, $\cot\theta = \frac{1}{\tan\theta}$ |
| Cociente | $\tan\theta = \frac{\sin\theta}{\cos\theta}$ |

### Ángulo Doble
| Función | Fórmula |
|---------|---------|
| $\sin(2\theta)$ | $2\sin\theta\cos\theta$ |
| $\cos(2\theta)$ | $\cos^2\theta - \sin^2\theta$ |
| $\tan(2\theta)$ | $\frac{2\tan\theta}{1-\tan^2\theta}$ |

### Resolución de Triángulos
| Caso | Usar |
|------|------|
| ALA, LAA | Ley de senos |
| LLL, LAL | Ley de cosenos |
| LLA | Ley de senos (cuidado con ambigüedad) |
