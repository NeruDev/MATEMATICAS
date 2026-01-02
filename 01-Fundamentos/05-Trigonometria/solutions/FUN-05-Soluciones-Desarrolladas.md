<!--
HUMANO:
Soluciones detalladas y contextualizadas para problemas de [trigonometría](../../../glossary.md#trigonometria).

IA:
Antes de cada solución, incluye contexto teórico.
Usa el círculo unitario y valores exactos cuando sea posible.

---
content_type: solutions_comprehensive
expected_output:
  default: markdown
solution_format: context + development + verification
---
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../glossary.md)

---

# Soluciones de Trigonometría

> **Formato:** Contexto teórico → Desarrollo paso a paso → Verificación

---

## 5.1 Ángulos y Medidas

### Solución 5.1.1
**Contexto:** Para convertir de grados a radianes, multiplicamos por $\frac{\pi}{180°}$.

**Desarrollo:**
a) $45° \times \frac{\pi}{180°} = \frac{\pi}{4}$

b) $120° \times \frac{\pi}{180°} = \frac{2\pi}{3}$

c) $225° \times \frac{\pi}{180°} = \frac{5\pi}{4}$

d) $330° \times \frac{\pi}{180°} = \frac{11\pi}{6}$

e) $270° \times \frac{\pi}{180°} = \frac{3\pi}{2}$

---

### Solución 5.1.2
**Contexto:** Para convertir de radianes a grados, multiplicamos por $\frac{180°}{\pi}$.

**Desarrollo:**
a) $\frac{\pi}{6} \times \frac{180°}{\pi} = 30°$

b) $\frac{2\pi}{3} \times \frac{180°}{\pi} = 120°$

c) $\frac{5\pi}{4} \times \frac{180°}{\pi} = 225°$

d) $\frac{11\pi}{6} \times \frac{180°}{\pi} = 330°$

e) $\frac{7\pi}{2} \times \frac{180°}{\pi} = 630°$

---

### Solución 5.1.5
**Contexto:** La longitud de arco es $s = r\theta$, donde $\theta$ debe estar en radianes.

**Desarrollo:**
a) Primero convertimos: $60° = \frac{\pi}{3}$ rad
$$s = 8 \times \frac{\pi}{3} = \frac{8\pi}{3} \approx 8.38 \text{ cm}$$

b) Ya está en radianes:
$$s = 8 \times \frac{2\pi}{3} = \frac{16\pi}{3} \approx 16.76 \text{ cm}$$

---

### Solución 5.1.6
**Contexto:** Una revolución completa equivale a una circunferencia completa: $C = 2\pi r$.

**Desarrollo:**
$$\text{Distancia} = 4 \times 2\pi(35) = 280\pi \approx 879.6 \text{ cm} = 8.796 \text{ m}$$

---

### Solución 5.1.7
**Contexto:** El área de un sector circular es $A = \frac{1}{2}r^2\theta$ (con $\theta$ en radianes).

**Desarrollo:**
Convertimos: $150° = \frac{5\pi}{6}$ rad

$$A = \frac{1}{2}(12)^2 \times \frac{5\pi}{6} = \frac{1}{2} \times 144 \times \frac{5\pi}{6} = 60\pi \approx 188.5 \text{ cm}^2$$

---

### Solución 5.1.9
**Contexto:** Para encontrar el cuadrante, reducimos el ángulo al rango $[0°, 360°)$ usando coterminales.

**Desarrollo:**
$$1000° = 1000° - 2(360°) = 1000° - 720° = 280°$$

Como $270° < 280° < 360°$, el ángulo está en el **Cuadrante IV**.

---

## 5.2 Razones Trigonométricas en el Triángulo Rectángulo

### Solución 5.2.1
**Contexto:** En un triángulo rectángulo con $CO = 3$ y $H = 5$, usamos Pitágoras para encontrar $CA$.

**Desarrollo:**
$$CA = \sqrt{H^2 - CO^2} = \sqrt{25 - 9} = \sqrt{16} = 4$$

Las seis razones:
$$\sin\theta = \frac{3}{5} \qquad \cos\theta = \frac{4}{5} \qquad \tan\theta = \frac{3}{4}$$
$$\csc\theta = \frac{5}{3} \qquad \sec\theta = \frac{5}{4} \qquad \cot\theta = \frac{4}{3}$$

**Verificación:** $\sin^2\theta + \cos^2\theta = \frac{9}{25} + \frac{16}{25} = 1$ ✓

---

### Solución 5.2.2
**Contexto:** Con $\cos\theta = \frac{12}{13}$, usamos la identidad pitagórica.

**Desarrollo:**
$$\sin^2\theta = 1 - \cos^2\theta = 1 - \frac{144}{169} = \frac{25}{169}$$
$$\sin\theta = \frac{5}{13} \quad \text{(positivo porque } \theta \text{ es agudo)}$$
$$\tan\theta = \frac{\sin\theta}{\cos\theta} = \frac{5/13}{12/13} = \frac{5}{12}$$

---

### Solución 5.2.6
**Contexto:** En un triángulo rectángulo, la altura es el cateto opuesto al ángulo de elevación.

**Desarrollo:**
$$\sin 65° = \frac{h}{10}$$
$$h = 10 \sin 65° = 10 \times 0.9063 \approx 9.06 \text{ m}$$

---

### Solución 5.2.7
**Contexto:** El ángulo de elevación se mide desde la horizontal hacia arriba.

**Desarrollo:**
$$\tan 62° = \frac{h}{50}$$
$$h = 50 \tan 62° = 50 \times 1.8807 \approx 94.0 \text{ m}$$

---

### Solución 5.2.10
**Contexto:** Si $90° < \theta < 180°$ (segundo cuadrante), el [coseno](../../../glossary.md#coseno) es negativo.

**Desarrollo:**
$$\cos^2\theta = 1 - \sin^2\theta = 1 - \frac{4}{9} = \frac{5}{9}$$
$$\cos\theta = -\frac{\sqrt{5}}{3} \quad \text{(negativo en cuadrante II)}$$
$$\tan\theta = \frac{\sin\theta}{\cos\theta} = \frac{2/3}{-\sqrt{5}/3} = -\frac{2}{\sqrt{5}} = -\frac{2\sqrt{5}}{5}$$

---

## 5.3 Círculo Unitario

### Solución 5.3.1
**Contexto:** Valores memorables del círculo unitario.

a) $\sin\frac{\pi}{4} = \frac{\sqrt{2}}{2}$

b) $\cos\frac{\pi}{3} = \frac{1}{2}$

c) $\tan\frac{\pi}{6} = \frac{\sin(\pi/6)}{\cos(\pi/6)} = \frac{1/2}{\sqrt{3}/2} = \frac{1}{\sqrt{3}} = \frac{\sqrt{3}}{3}$

---

### Solución 5.3.3
**Contexto:** Usamos ángulos de referencia y signos según el cuadrante.

a) $\sin 150°$: Cuadrante II, ángulo ref. = 30°
$$\sin 150° = +\sin 30° = \frac{1}{2}$$

b) $\cos 240°$: Cuadrante III, ángulo ref. = 60°
$$\cos 240° = -\cos 60° = -\frac{1}{2}$$

c) $\tan 300°$: Cuadrante IV, ángulo ref. = 60°
$$\tan 300° = -\tan 60° = -\sqrt{3}$$

---

### Solución 5.3.5
**Contexto:** En el tercer cuadrante, [seno](../../../glossary.md#seno) y [coseno](../../../glossary.md#coseno) son negativos.

**Desarrollo:**
Dado $\cos\theta = -\frac{3}{5}$ en el cuadrante III:
$$\sin^2\theta = 1 - \frac{9}{25} = \frac{16}{25}$$
$$\sin\theta = -\frac{4}{5} \quad \text{(negativo en cuadrante III)}$$
$$\tan\theta = \frac{-4/5}{-3/5} = \frac{4}{3} \quad \text{(positivo en cuadrante III)}$$

---

### Solución 5.3.7
**Contexto:** $\sin\theta = -\frac{\sqrt{2}}{2}$ ocurre cuando el ángulo de referencia es 45° y el [seno](../../../glossary.md#seno) es negativo (cuadrantes III y IV).

**Desarrollo:**
- Cuadrante III: $\theta = 180° + 45° = 225° = \frac{5\pi}{4}$
- Cuadrante IV: $\theta = 360° - 45° = 315° = \frac{7\pi}{4}$

**Respuesta:** $\theta = \frac{5\pi}{4}, \frac{7\pi}{4}$

---

## 5.4 Gráficas de Funciones Trigonométricas

### Solución 5.4.4
**Contexto:** Buscamos $y = A\sin(Bx)$ con amplitud 4 y período $\pi$.

**Desarrollo:**
- Amplitud = 4 → $A = 4$
- Período = $\frac{2\pi}{B} = \pi$ → $B = 2$

**Respuesta:** $y = 4\sin(2x)$

---

### Solución 5.4.6
**Contexto:** Para $y = A\cos x + D$, el rango es $[D - \lvert A \rvert, D + \lvert A \rvert]$.

**Desarrollo:**
Para $y = -2\cos x + 5$:
- Máximo: cuando $\cos x = -1$ → $y = -2(-1) + 5 = 7$
- Mínimo: cuando $\cos x = 1$ → $y = -2(1) + 5 = 3$
- Rango: $[3, 7]$

---

### Solución 5.4.9
**Contexto:** El voltaje AC sigue $V(t) = V_0\sin(\omega t)$ donde $\omega = 2\pi f$.

**Desarrollo:**
$V(t) = 170\sin(120\pi t)$

- Amplitud = $170$ V (voltaje pico)
- $\omega = 120\pi$ → Frecuencia: $f = \frac{120\pi}{2\pi} = 60$ Hz
- Período: $T = \frac{1}{60} \approx 0.0167$ s

---

## 5.5 Identidades Trigonométricas Fundamentales

### Solución 5.5.1
**Contexto:** Usamos $\cot^2\theta = \frac{\cos^2\theta}{\sin^2\theta}$.

**Desarrollo:**
$$\sin^2\theta + \sin^2\theta\cot^2\theta = \sin^2\theta + \sin^2\theta \cdot \frac{\cos^2\theta}{\sin^2\theta}$$
$$= \sin^2\theta + \cos^2\theta = 1$$

---

### Solución 5.5.3
**Contexto:** Convertimos todo a senos y cosenos.

**Desarrollo:**
$$\tan\theta + \cot\theta = \frac{\sin\theta}{\cos\theta} + \frac{\cos\theta}{\sin\theta}$$
$$= \frac{\sin^2\theta + \cos^2\theta}{\sin\theta\cos\theta} = \frac{1}{\sin\theta\cos\theta} = \sec\theta\csc\theta \quad \checkmark$$

---

### Solución 5.5.8
**Contexto:** Usamos la identidad $(\sin\theta + \cos\theta)^2 = 1 + 2\sin\theta\cos\theta$.

**Desarrollo:**
$$\left(\frac{7}{5}\right)^2 = 1 + 2\sin\theta\cos\theta$$
$$\frac{49}{25} = 1 + 2\sin\theta\cos\theta$$
$$2\sin\theta\cos\theta = \frac{49}{25} - 1 = \frac{24}{25}$$
$$\sin\theta\cos\theta = \frac{12}{25}$$

---

## 5.6 Identidades de Suma, Resta y Múltiplos

### Solución 5.6.1
**Contexto:** $\sin 75° = \sin(45° + 30°)$

**Desarrollo:**
$$\sin 75° = \sin 45°\cos 30° + \cos 45°\sin 30°$$
$$= \frac{\sqrt{2}}{2} \cdot \frac{\sqrt{3}}{2} + \frac{\sqrt{2}}{2} \cdot \frac{1}{2}$$
$$= \frac{\sqrt{6}}{4} + \frac{\sqrt{2}}{4} = \frac{\sqrt{6} + \sqrt{2}}{4}$$

---

### Solución 5.6.3
**Contexto:** Con $\sin\alpha = \frac{3}{5}$, calculamos $\cos\alpha = \frac{4}{5}$. Con $\cos\beta = \frac{12}{13}$, calculamos $\sin\beta = \frac{5}{13}$.

**Desarrollo:**
$$\sin(\alpha + \beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta$$
$$= \frac{3}{5} \cdot \frac{12}{13} + \frac{4}{5} \cdot \frac{5}{13}$$
$$= \frac{36}{65} + \frac{20}{65} = \frac{56}{65}$$

---

### Solución 5.6.5
**Contexto:** Con $\cos\theta = \frac{4}{5}$ en cuadrante IV, $\sin\theta = -\frac{3}{5}$.

**Desarrollo:**
$$\sin(2\theta) = 2\sin\theta\cos\theta = 2 \cdot \left(-\frac{3}{5}\right) \cdot \frac{4}{5} = -\frac{24}{25}$$

$$\cos(2\theta) = \cos^2\theta - \sin^2\theta = \frac{16}{25} - \frac{9}{25} = \frac{7}{25}$$

---

## 5.7 Ecuaciones Trigonométricas

### Solución 5.7.1
**Contexto:** $\sin\theta = \frac{1}{2}$ tiene ángulo de referencia 30° y es positivo en cuadrantes I y II.

**Desarrollo:**
- Cuadrante I: $\theta = \frac{\pi}{6}$
- Cuadrante II: $\theta = \pi - \frac{\pi}{6} = \frac{5\pi}{6}$

**Respuesta:** $\theta = \frac{\pi}{6}, \frac{5\pi}{6}$

---

### Solución 5.7.5
**Contexto:** Factorizamos la ecuación cuadrática en $\sin\theta$.

**Desarrollo:**
$$2\sin^2\theta - \sin\theta = 0$$
$$\sin\theta(2\sin\theta - 1) = 0$$

$\sin\theta = 0$: $\theta = 0°, 180°$

$\sin\theta = \frac{1}{2}$: $\theta = 30°, 150°$

**Respuesta:** $\theta = 0°, 30°, 150°, 180°$

---

### Solución 5.7.7
**Contexto:** Usamos $\sin^2\theta = 1 - \cos^2\theta$ para obtener ecuación en $\cos\theta$.

**Desarrollo:**
$$2(1 - \cos^2\theta) + 3\cos\theta = 3$$
$$2 - 2\cos^2\theta + 3\cos\theta = 3$$
$$2\cos^2\theta - 3\cos\theta + 1 = 0$$
$$(2\cos\theta - 1)(\cos\theta - 1) = 0$$

$\cos\theta = \frac{1}{2}$: $\theta = \frac{\pi}{3}, \frac{5\pi}{3}$

$\cos\theta = 1$: $\theta = 0$

**Respuesta:** $\theta = 0, \frac{\pi}{3}, \frac{5\pi}{3}$

---

## 5.8 Funciones Trigonométricas Inversas

### Solución 5.8.3
**Contexto:** Si $\theta = \arcsin\frac{3}{5}$, entonces $\sin\theta = \frac{3}{5}$ con $\theta$ en $[-\frac{\pi}{2}, \frac{\pi}{2}]$.

**Desarrollo:**
Como $\theta$ está en el rango principal (primer o cuarto cuadrante) y $\sin\theta > 0$, $\theta$ está en el primer cuadrante.
$$\cos\theta = \sqrt{1 - \sin^2\theta} = \sqrt{1 - \frac{9}{25}} = \sqrt{\frac{16}{25}} = \frac{4}{5}$$

---

### Solución 5.8.5
**Contexto:** Sea $\theta = \arctan x$, entonces $\tan\theta = x$ con $\theta \in (-\frac{\pi}{2}, \frac{\pi}{2})$.

**Desarrollo:**
Si $\tan\theta = \frac{x}{1}$, tenemos cateto opuesto = $x$, cateto adyacente = $1$.
Hipotenusa = $\sqrt{x^2 + 1}$

$$\sin(\arctan x) = \sin\theta = \frac{x}{\sqrt{x^2 + 1}} = \frac{x\sqrt{x^2+1}}{x^2+1}$$

---

## 5.9 Ley de Senos y Ley de Cosenos

### Solución 5.9.1
**Contexto:** Aplicamos la ley de senos: $\frac{a}{\sin A} = \frac{b}{\sin B}$

**Desarrollo:**
$$\frac{14}{\sin 45°} = \frac{b}{\sin 60°}$$
$$b = \frac{14 \sin 60°}{\sin 45°} = \frac{14 \cdot \frac{\sqrt{3}}{2}}{\frac{\sqrt{2}}{2}} = \frac{14\sqrt{3}}{\sqrt{2}} = 7\sqrt{6} \approx 17.15$$

---

### Solución 5.9.2
**Contexto:** Aplicamos la ley de cosenos: $c^2 = a^2 + b^2 - 2ab\cos C$

**Desarrollo:**
$$c^2 = 7^2 + 10^2 - 2(7)(10)\cos 38°$$
$$c^2 = 49 + 100 - 140(0.788) = 149 - 110.3 = 38.7$$
$$c \approx 6.22$$

---

### Solución 5.9.3
**Contexto:** El ángulo mayor está opuesto al lado mayor. Usamos la ley de cosenos para hallar ángulos.

**Desarrollo:**
El lado mayor es $c = 11$, así que buscamos $C$:
$$\cos C = \frac{a^2 + b^2 - c^2}{2ab} = \frac{25 + 64 - 121}{2(5)(8)} = \frac{-32}{80} = -0.4$$
$$C = \arccos(-0.4) \approx 113.6°$$

---

### Solución 5.9.5
**Contexto:** El área con dos lados y ángulo incluido es $A = \frac{1}{2}ab\sin C$.

**Desarrollo:**
$$A = \frac{1}{2}(9)(12)\sin 50° = 54 \times 0.766 \approx 41.4 \text{ unidades}^2$$

---

## 5.10 Aplicaciones de la Trigonometría

### Solución 5.10.1
**Contexto:** El ángulo de elevación forma un triángulo rectángulo con el edificio.

**Desarrollo:**
$$\tan 72° = \frac{h}{25}$$
$$h = 25 \tan 72° = 25 \times 3.078 \approx 76.9 \text{ m}$$

---

### Solución 5.10.3
**Contexto:** El ángulo de depresión es igual al ángulo de elevación desde el barco.

**Desarrollo:**
$$\tan 17° = \frac{50}{d}$$
$$d = \frac{50}{\tan 17°} = \frac{50}{0.3057} \approx 163.6 \text{ m}$$

---

### Solución 5.10.7
**Contexto:** Modelamos con [función](../../../glossary.md#funcion) seno/coseno. El pasajero sube y baja con el centro a 35 m.

**Desarrollo:**
- El centro está a 35 m, el radio es 30 m
- Mínimo: 35 - 30 = 5 m
- Máximo: 35 + 30 = 65 m
- A 2 rpm, período = 30 segundos
- Comienza en el punto más bajo (mínimo)

$$h(t) = -30\cos\left(\frac{2\pi}{30}t\right) + 35 = -30\cos\left(\frac{\pi t}{15}\right) + 35$$

(Usamos $-\cos$ porque comienza en el mínimo)

---

### Solución 5.10.8
**Contexto:** Modelamos la marea como [función](../../../glossary.md#funcion) coseno con máximo en $t = 0$ (6:00 AM).

**Desarrollo:**
- Amplitud: $\frac{12 - 4}{2} = 4$ m
- Línea media: $\frac{12 + 4}{2} = 8$ m
- Período: 12 horas (máx a mín es medio período = 6 h)
- $B = \frac{2\pi}{12} = \frac{\pi}{6}$

$$d(t) = 4\cos\left(\frac{\pi t}{6}\right) + 8$$

A las 9:00 AM ($t = 3$):
$$d(3) = 4\cos\left(\frac{3\pi}{6}\right) + 8 = 4\cos\left(\frac{\pi}{2}\right) + 8 = 4(0) + 8 = 8 \text{ m}$$
