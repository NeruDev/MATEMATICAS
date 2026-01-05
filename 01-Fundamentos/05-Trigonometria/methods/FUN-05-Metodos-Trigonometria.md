<!--
::METADATA::
type: method
status: active
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../glossary.md)

---

# Métodos de Trigonometría

> Guía completa de métodos trigonométricos con algoritmos detallados, tablas de procedimientos y ejemplos paso a paso.

---

## Método 1: Convertir entre Grados y Radianes

**Cuándo Usar:** Para pasar de un sistema de medida angular a otro.

### Fórmulas de Conversión

| De | A | Fórmula |
|----|---|---------|
| Grados a radianes | $\theta_{rad}$ | $\theta_{rad} = \theta_{deg} \times \frac{\pi}{180°}$ |
| Radianes a grados | $\theta_{deg}$ | $\theta_{deg} = \theta_{rad} \times \frac{180°}{\pi}$ |

### Equivalencias Fundamentales

| Grados | Radianes | Grados | Radianes |
|--------|----------|--------|----------|
| $0°$ | $0$ | $180°$ | $\pi$ |
| $30°$ | $\frac{\pi}{6}$ | $210°$ | $\frac{7\pi}{6}$ |
| $45°$ | $\frac{\pi}{4}$ | $225°$ | $\frac{5\pi}{4}$ |
| $60°$ | $\frac{\pi}{3}$ | $240°$ | $\frac{4\pi}{3}$ |
| $90°$ | $\frac{\pi}{2}$ | $270°$ | $\frac{3\pi}{2}$ |
| $120°$ | $\frac{2\pi}{3}$ | $300°$ | $\frac{5\pi}{3}$ |
| $135°$ | $\frac{3\pi}{4}$ | $315°$ | $\frac{7\pi}{4}$ |
| $150°$ | $\frac{5\pi}{6}$ | $330°$ | $\frac{11\pi}{6}$ |
| | | $360°$ | $2\pi$ |

### Ejemplo Detallado

**Problema:** Convertir $225°$ a radianes y $\frac{5\pi}{4}$ a grados.

---

**Grados a radianes:**

$$225° \times \frac{\pi}{180°} = \frac{225\pi}{180} = \frac{5\pi}{4}$$

---

**Radianes a grados:**

$$\frac{5\pi}{4} \times \frac{180°}{\pi} = \frac{5 \times 180°}{4} = \frac{900°}{4} = 225°$$

$$\boxed{225° = \frac{5\pi}{4} \text{ rad}}$$

---

## Método 2: Calcular Razones Trigonométricas en Triángulos Rectángulos

**Cuándo Usar:** Para resolver triángulos rectángulos conociendo un ángulo agudo y un lado.

### Definiciones (SOH-CAH-TOA)

| Razón | Definición | Mnemónico |
|-------|------------|-----------|
| [Seno](../../../glossary.md#seno) | $\sin\theta = \frac{\text{opuesto}}{\text{hipotenusa}}$ | SOH |
| [Coseno](../../../glossary.md#coseno) | $\cos\theta = \frac{\text{adyacente}}{\text{hipotenusa}}$ | CAH |
| [Tangente](../../../glossary.md#tangente) | $\tan\theta = \frac{\text{opuesto}}{\text{adyacente}}$ | TOA |

### Ejemplo Detallado

**Problema:** En un triángulo rectángulo con ángulo $\theta = 30°$ e hipotenusa $c = 10$, encontrar los catetos.

---

**Paso 1: Calcular cateto opuesto usando seno**

$$a = c \cdot \sin(30°) = 10 \times \frac{1}{2} = 5$$

---

**Paso 2: Calcular cateto adyacente usando coseno**

$$b = c \cdot \cos(30°) = 10 \times \frac{\sqrt{3}}{2} = 5\sqrt{3}$$

$$\boxed{a = 5, \quad b = 5\sqrt{3}}$$

---

## Método 3: Evaluar Funciones usando Círculo Unitario

**Cuándo Usar:** Para encontrar valores exactos de funciones trigonométricas en ángulos notables.

### Signos por Cuadrante

| Cuadrante | Seno | Coseno | Tangente |
|-----------|:----:|:------:|:--------:|
| I (0° - 90°) | $+$ | $+$ | $+$ |
| II (90° - 180°) | $+$ | $-$ | $-$ |
| III (180° - 270°) | $-$ | $-$ | $+$ |
| IV (270° - 360°) | $-$ | $+$ | $-$ |

> **Mnemónico ASTC:** "All Students Take Calculus" indica qué funciones son positivas en cada cuadrante.

### Ejemplo Detallado

**Problema:** Evaluar $\sin(240°)$, $\cos(240°)$ y $\tan(240°)$.

---

**Paso 1: Determinar cuadrante y ángulo de referencia**

$240° = 180° + 60°$ → Cuadrante III, ángulo de referencia = $60°$

---

**Paso 2: Determinar signos (Cuadrante III)**

En el cuadrante III, solo tangente y cotangente son positivas.

- $\sin(240°) < 0$
- $\cos(240°) < 0$
- $\tan(240°) > 0$

---

**Paso 3: Aplicar valores de referencia con signos**

$$\sin(240°) = -\sin(60°) = -\frac{\sqrt{3}}{2}$$

$$\cos(240°) = -\cos(60°) = -\frac{1}{2}$$

$$\tan(240°) = +\tan(60°) = \sqrt{3}$$

---

**Verificación:**

$$\tan(240°) = \frac{\sin(240°)}{\cos(240°)} = \frac{-\sqrt{3}/2}{-1/2} = \sqrt{3} \checkmark$$

$$\boxed{\sin(240°) = -\frac{\sqrt{3}}{2}, \quad \cos(240°) = -\frac{1}{2}, \quad \tan(240°) = \sqrt{3}}$$

---

## Método 4: Graficar Funciones Trigonométricas

**Cuándo Usar:** Para trazar o analizar gráficas de sen, cos, tan y sus transformaciones.

### Forma General

$$y = A \sin(B(x - C)) + D$$
$$y = A \cos(B(x - C)) + D$$

### Parámetros

| Parámetro | Efecto | Fórmula |
|-----------|--------|---------|
| $A$ | Amplitud | $\lvert A \rvert$ |
| $B$ | Período | $T = \frac{2\pi}{\lvert B \rvert}$ |
| $C$ | Desplazamiento horizontal | Hacia la derecha si $C > 0$ |
| $D$ | Desplazamiento vertical | Hacia arriba si $D > 0$ |

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Identificar parámetros | $A$, $B$, $C$, $D$ |
| 2 | Calcular amplitud | $\vert A\vert$ |
| 3 | Calcular período | $T = \frac{2\pi}{\vert B\vert}$ |
| 4 | Determinar valores extremos | $D \pm A$ |
| 5 | Graficar puntos clave | Inicio, cuartos de período |

### Ejemplo Detallado

**Problema:** Analizar y graficar $y = 3\sin(2x - \frac{\pi}{2}) + 1$

---

**Paso 1: Reescribir en forma estándar**

$$y = 3\sin\left(2\left(x - \frac{\pi}{4}\right)\right) + 1$$

---

**Paso 2: Identificar parámetros**

| Parámetro | Valor |
|-----------|-------|
| $A$ | $3$ |
| $B$ | $2$ |
| $C$ | $\frac{\pi}{4}$ |
| $D$ | $1$ |

---

**Paso 3: Calcular características**

- **Amplitud:** $|A| = 3$
- **Período:** $T = \frac{2\pi}{2} = \pi$
- **Desplazamiento horizontal:** $\frac{\pi}{4}$ a la derecha
- **Desplazamiento vertical:** 1 unidad hacia arriba
- **Valor máximo:** $D + A = 1 + 3 = 4$
- **Valor mínimo:** $D - A = 1 - 3 = -2$

---

**Paso 4: Puntos clave (un período completo)**

| $x$ | $y$ | Descripción |
|-----|-----|-------------|
| $\frac{\pi}{4}$ | $1$ | Inicio del ciclo |
| $\frac{\pi}{2}$ | $4$ | Máximo |
| $\frac{3\pi}{4}$ | $1$ | Cruza línea media |
| $\pi$ | $-2$ | Mínimo |
| $\frac{5\pi}{4}$ | $1$ | Fin del ciclo |

$$\boxed{\text{Amplitud: } 3, \quad \text{Período: } \pi, \quad \text{Rango: } [-2, 4]}$$

---

## Método 5: Verificar y Demostrar Identidades Trigonométricas

**Cuándo Usar:** Para simplificar expresiones o demostrar igualdades.

### Identidades Fundamentales

| Tipo | Identidad |
|------|-----------|
| Pitagóricas | $\sin^2\theta + \cos^2\theta = 1$ |
| | $1 + \tan^2\theta = \sec^2\theta$ |
| | $1 + \cot^2\theta = \csc^2\theta$ |
| Recíprocas | $\csc\theta = \frac{1}{\sin\theta}$ |
| | $\sec\theta = \frac{1}{\cos\theta}$ |
| | $\cot\theta = \frac{1}{\tan\theta}$ |
| Cociente | $\tan\theta = \frac{\sin\theta}{\cos\theta}$ |
| | $\cot\theta = \frac{\cos\theta}{\sin\theta}$ |

### Estrategias de Demostración

| Estrategia | Descripción |
|------------|-------------|
| Trabajar un lado | Transformar hasta igualar al otro |
| Convertir a sen/cos | Expresar todo en términos de [seno](../../../glossary.md#seno) y [coseno](../../../glossary.md#coseno) |
| [Factorizar](../../../glossary.md#factorizar) | Usar identidades para factorizar expresiones |
| Multiplicar por conjugado | Racionalizar usando $1 + \sin\theta$, $1 - \cos\theta$, etc. |

### Ejemplo Detallado

**Problema:** Demostrar que $\frac{1 - \cos^2\theta}{\sin\theta} = \sin\theta$

---

**Paso 1: Trabajar el lado izquierdo**

$$\frac{1 - \cos^2\theta}{\sin\theta}$$

---

**Paso 2: Usar identidad pitagórica**

$$1 - \cos^2\theta = \sin^2\theta$$

---

**Paso 3: Simplificar**

$$\frac{\sin^2\theta}{\sin\theta} = \sin\theta \checkmark$$

$$\boxed{\frac{1 - \cos^2\theta}{\sin\theta} = \sin\theta}$$

---

## Método 6: Resolver Ecuaciones Trigonométricas

**Cuándo Usar:** Para encontrar todos los ángulos que satisfacen una ecuación trigonométrica.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Aislar función trigonométrica | Simplificar la ecuación |
| 2 | [Factorizar](../../../glossary.md#factorizar) si es necesario | Llevar a forma $\sin x = a$ o similar |
| 3 | Encontrar soluciones en $[0, 2\pi)$ | Usar ángulos de referencia |
| 4 | Escribir solución general | Agregar periodicidad |

### Ejemplo Detallado

**Problema:** Resolver $2\cos^2 x - \cos x - 1 = 0$ en $[0, 2\pi)$.

---

**Paso 1: Hacer sustitución**

Sea $u = \cos x$:
$$2u^2 - u - 1 = 0$$

---

**Paso 2: Factorizar**

$$(2u + 1)(u - 1) = 0$$

$$u = -\frac{1}{2} \quad \text{o} \quad u = 1$$

---

**Paso 3: Resolver para $\cos x = -\frac{1}{2}$**

Ángulo de referencia: $\cos^{-1}\left(\frac{1}{2}\right) = \frac{\pi}{3}$

Coseno es negativo en cuadrantes II y III:
$$x = \pi - \frac{\pi}{3} = \frac{2\pi}{3}$$
$$x = \pi + \frac{\pi}{3} = \frac{4\pi}{3}$$

---

**Paso 4: Resolver para $\cos x = 1$**

$$x = 0$$

---

**Paso 5: Conjunto solución**

$$x \in \left\{0, \frac{2\pi}{3}, \frac{4\pi}{3}\right\}$$

---

**Verificación:**

- $\cos(0) = 1$: $2(1)^2 - 1 - 1 = 0$ ✓
- $\cos\left(\frac{2\pi}{3}\right) = -\frac{1}{2}$: $2\left(\frac{1}{4}\right) + \frac{1}{2} - 1 = 0$ ✓

$$\boxed{x = 0, \frac{2\pi}{3}, \frac{4\pi}{3}}$$

---

## Método 7: Aplicar Fórmulas de Suma y Diferencia de Ángulos

**Cuándo Usar:** Para calcular valores exactos de ángulos no estándar o simplificar expresiones.

### Fórmulas

| Función | Suma | Diferencia |
|---------|------|------------|
| Seno | $\sin(A + B) = \sin A \cos B + \cos A \sin B$ | $\sin(A - B) = \sin A \cos B - \cos A \sin B$ |
| Coseno | $\cos(A + B) = \cos A \cos B - \sin A \sin B$ | $\cos(A - B) = \cos A \cos B + \sin A \sin B$ |
| Tangente | $\tan(A + B) = \frac{\tan A + \tan B}{1 - \tan A \tan B}$ | $\tan(A - B) = \frac{\tan A - \tan B}{1 + \tan A \tan B}$ |

### Ejemplo Detallado

**Problema:** Calcular el valor exacto de $\sin(75°)$

---

**Paso 1: Expresar como suma de ángulos conocidos**

$$75° = 45° + 30°$$

---

**Paso 2: Aplicar fórmula**

$$\sin(75°) = \sin(45° + 30°) = \sin 45° \cos 30° + \cos 45° \sin 30°$$

---

**Paso 3: Sustituir valores conocidos**

$$= \frac{\sqrt{2}}{2} \cdot \frac{\sqrt{3}}{2} + \frac{\sqrt{2}}{2} \cdot \frac{1}{2}$$

$$= \frac{\sqrt{6}}{4} + \frac{\sqrt{2}}{4}$$

$$= \frac{\sqrt{6} + \sqrt{2}}{4}$$

---

**Verificación numérica:**

$$\frac{\sqrt{6} + \sqrt{2}}{4} = \frac{2.449 + 1.414}{4} = \frac{3.863}{4} \approx 0.966$$

$$\sin(75°) \approx 0.9659 \checkmark$$

$$\boxed{\sin(75°) = \frac{\sqrt{6} + \sqrt{2}}{4}}$$

---

## Método 8: Aplicar Fórmulas de Ángulo Doble y Medio

**Cuándo Usar:** Para calcular funciones de $2\theta$ o $\frac{\theta}{2}$ conociendo funciones de $\theta$.

### Fórmulas de Ángulo Doble

| Función | Fórmulas |
|---------|----------|
| $\sin 2\theta$ | $2\sin\theta\cos\theta$ |
| $\cos 2\theta$ | $\cos^2\theta - \sin^2\theta = 2\cos^2\theta - 1 = 1 - 2\sin^2\theta$ |
| $\tan 2\theta$ | $\frac{2\tan\theta}{1 - \tan^2\theta}$ |

### Fórmulas de Ángulo Medio

| Función | Fórmula |
|---------|---------|
| $\sin\frac{\theta}{2}$ | $\pm\sqrt{\frac{1 - \cos\theta}{2}}$ |
| $\cos\frac{\theta}{2}$ | $\pm\sqrt{\frac{1 + \cos\theta}{2}}$ |
| $\tan\frac{\theta}{2}$ | $\frac{\sin\theta}{1 + \cos\theta} = \frac{1 - \cos\theta}{\sin\theta}$ |

### Ejemplo Detallado

**Problema:** Si $\sin\theta = \frac{3}{5}$ y $\theta$ está en el segundo cuadrante, hallar $\sin 2\theta$, $\cos 2\theta$, y $\tan 2\theta$.

---

**Paso 1: Encontrar $\cos\theta$**

$$\sin^2\theta + \cos^2\theta = 1$$
$$\left(\frac{3}{5}\right)^2 + \cos^2\theta = 1$$
$$\cos^2\theta = 1 - \frac{9}{25} = \frac{16}{25}$$
$$\cos\theta = -\frac{4}{5}$$ (negativo en QII)

---

**Paso 2: Calcular $\sin 2\theta$**

$$\sin 2\theta = 2\sin\theta\cos\theta = 2 \cdot \frac{3}{5} \cdot \left(-\frac{4}{5}\right) = -\frac{24}{25}$$

---

**Paso 3: Calcular $\cos 2\theta$**

$$\cos 2\theta = \cos^2\theta - \sin^2\theta = \frac{16}{25} - \frac{9}{25} = \frac{7}{25}$$

---

**Paso 4: Calcular $\tan 2\theta$**

$$\tan 2\theta = \frac{\sin 2\theta}{\cos 2\theta} = \frac{-24/25}{7/25} = -\frac{24}{7}$$

---

**Verificación con fórmula alternativa:**

$$\tan\theta = \frac{\sin\theta}{\cos\theta} = \frac{3/5}{-4/5} = -\frac{3}{4}$$

$$\tan 2\theta = \frac{2\tan\theta}{1 - \tan^2\theta} = \frac{2(-3/4)}{1 - 9/16} = \frac{-3/2}{7/16} = -\frac{24}{7} \checkmark$$

$$\boxed{\sin 2\theta = -\frac{24}{25}, \quad \cos 2\theta = \frac{7}{25}, \quad \tan 2\theta = -\frac{24}{7}}$$

---

## Método 9: Aplicar la Ley de Senos

**Cuándo Usar:** En triángulos oblicuos cuando conoces:
- Dos ángulos y un lado (ALA o AAL)
- Dos lados y un ángulo opuesto a uno de ellos (caso ambiguo)

### Fórmula

$$\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} = 2R$$

Donde $R$ es el radio de la circunferencia circunscrita.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Identificar datos | Qué lados y ángulos conocemos |
| 2 | Plantear proporción | Usar lados con ángulos opuestos |
| 3 | Resolver | Despejar la incógnita |
| 4 | Verificar caso ambiguo | Si hay dos soluciones posibles |

### Ejemplo Detallado

**Problema:** En el triángulo $ABC$, $A = 40°$, $B = 75°$, y $a = 12$. Hallar $b$ y $c$.

---

**Paso 1: Hallar el tercer ángulo**

$$C = 180° - 40° - 75° = 65°$$

---

**Paso 2: Calcular $b$ usando ley de senos**

$$\frac{a}{\sin A} = \frac{b}{\sin B}$$

$$\frac{12}{\sin 40°} = \frac{b}{\sin 75°}$$

$$b = \frac{12 \times \sin 75°}{\sin 40°} = \frac{12 \times 0.9659}{0.6428} = 18.03$$

---

**Paso 3: Calcular $c$**

$$\frac{a}{\sin A} = \frac{c}{\sin C}$$

$$c = \frac{12 \times \sin 65°}{\sin 40°} = \frac{12 \times 0.9063}{0.6428} = 16.92$$

---

**Verificación:** El lado mayor está opuesto al ángulo mayor.

$B = 75°$ es el mayor → $b = 18.03$ es el mayor ✓

$$\boxed{b \approx 18.03, \quad c \approx 16.92}$$

---

### Caso Ambiguo (SSA)

**Problema:** En un triángulo, $a = 8$, $b = 12$, y $A = 30°$. ¿Cuántas soluciones existen?

---

**Paso 1: Calcular $\sin B$**

$$\frac{\sin B}{b} = \frac{\sin A}{a}$$

$$\sin B = \frac{b \sin A}{a} = \frac{12 \times \sin 30°}{8} = \frac{12 \times 0.5}{8} = 0.75$$

---

**Paso 2: Verificar validez**

Como $0 < 0.75 < 1$, existe al menos una solución.

$$B_1 = \arcsin(0.75) = 48.59°$$
$$B_2 = 180° - 48.59° = 131.41°$$

---

**Paso 3: Verificar cada caso**

- Caso 1: $B_1 = 48.59°$ → $C_1 = 180° - 30° - 48.59° = 101.41°$ ✓ (válido)
- Caso 2: $B_2 = 131.41°$ → $C_2 = 180° - 30° - 131.41° = 18.59°$ ✓ (válido)

$$\boxed{\text{Dos soluciones: } B_1 = 48.59°, B_2 = 131.41°}$$

---

## Método 10: Aplicar la Ley de Cosenos

**Cuándo Usar:** En triángulos oblicuos cuando conoces:
- Dos lados y el ángulo incluido (LAL)
- Tres lados (LLL)

### Fórmulas

$$a^2 = b^2 + c^2 - 2bc\cos A$$
$$b^2 = a^2 + c^2 - 2ac\cos B$$
$$c^2 = a^2 + b^2 - 2ab\cos C$$

### Forma Despejada para Ángulos

$$\cos A = \frac{b^2 + c^2 - a^2}{2bc}$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Identificar configuración | LAL o LLL |
| 2 | Aplicar fórmula | Según el caso |
| 3 | Resolver | Calcular lado o ángulo |
| 4 | Completar | Usar ley de senos para el resto |

### Ejemplo Detallado (LAL)

**Problema:** En el triángulo $ABC$, $b = 7$, $c = 10$, y $A = 52°$. Hallar $a$.

---

**Aplicar ley de cosenos:**

$$a^2 = b^2 + c^2 - 2bc\cos A$$

$$a^2 = 7^2 + 10^2 - 2(7)(10)\cos 52°$$

$$a^2 = 49 + 100 - 140(0.6157)$$

$$a^2 = 149 - 86.20 = 62.80$$

$$a = \sqrt{62.80} \approx 7.92$$

$$\boxed{a \approx 7.92}$$

---

### Ejemplo Detallado (LLL)

**Problema:** En el triángulo con lados $a = 5$, $b = 7$, $c = 8$, hallar todos los ángulos.

---

**Paso 1: Hallar ángulo $C$ (opuesto al lado mayor)**

$$\cos C = \frac{a^2 + b^2 - c^2}{2ab} = \frac{25 + 49 - 64}{2(5)(7)} = \frac{10}{70} = \frac{1}{7}$$

$$C = \arccos\left(\frac{1}{7}\right) \approx 81.79°$$

---

**Paso 2: Hallar ángulo $A$**

$$\cos A = \frac{b^2 + c^2 - a^2}{2bc} = \frac{49 + 64 - 25}{2(7)(8)} = \frac{88}{112} = \frac{11}{14}$$

$$A = \arccos\left(\frac{11}{14}\right) \approx 38.21°$$

---

**Paso 3: Hallar ángulo $B$**

$$B = 180° - 81.79° - 38.21° = 60°$$

---

**Verificación:**

$$\cos B = \frac{a^2 + c^2 - b^2}{2ac} = \frac{25 + 64 - 49}{80} = \frac{40}{80} = 0.5$$

$$B = \arccos(0.5) = 60° \checkmark$$

$$\boxed{A \approx 38.21°, \quad B = 60°, \quad C \approx 81.79°}$$

---

## Método 11: Convertir entre Formas Polares y Rectangulares

**Cuándo Usar:** Para cambiar entre coordenadas $(x, y)$ y $(r, \theta)$.

### Fórmulas de Conversión

| De Rectangular a Polar | De Polar a Rectangular |
|------------------------|------------------------|
| $r = \sqrt{x^2 + y^2}$ | $x = r\cos\theta$ |
| $\theta = \arctan\left(\frac{y}{x}\right)$ | $y = r\sin\theta$ |

**Nota:** Ajustar $\theta$ según el cuadrante.

### Ejemplo Detallado

**Problema:** Convertir el punto $(-3, 4)$ a coordenadas polares.

---

**Paso 1: Calcular $r$**

$$r = \sqrt{(-3)^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5$$

---

**Paso 2: Calcular $\theta$**

$$\theta_{ref} = \arctan\left|\frac{4}{-3}\right| = \arctan\left(\frac{4}{3}\right) \approx 53.13°$$

El punto está en el segundo cuadrante (x negativo, y positivo):

$$\theta = 180° - 53.13° = 126.87°$$

En radianes: $\theta = \pi - 0.9273 \approx 2.214$ rad

---

**Verificación:**

$$x = 5\cos(126.87°) = 5(-0.6) = -3 \checkmark$$
$$y = 5\sin(126.87°) = 5(0.8) = 4 \checkmark$$

$$\boxed{(r, \theta) = (5, 126.87°) \text{ o } (5, 2.214 \text{ rad})}$$

---

## Método 12: Calcular Área de Triángulos con Trigonometría

**Cuándo Usar:** Cuando no conoces la altura directamente.

### Fórmulas de Área

| Datos Conocidos | Fórmula |
|-----------------|---------|
| Dos lados y ángulo incluido | $A = \frac{1}{2}ab\sin C$ |
| Dos ángulos y un lado | $A = \frac{a^2\sin B \sin C}{2\sin A}$ |
| Tres lados (Herón) | $A = \sqrt{s(s-a)(s-b)(s-c)}$ |

### Ejemplo Detallado

**Problema:** Hallar el área del triángulo con $b = 8$ cm, $c = 12$ cm, y $A = 65°$.

---

**Aplicar fórmula:**

$$A = \frac{1}{2}bc\sin A$$

$$A = \frac{1}{2}(8)(12)\sin 65°$$

$$A = \frac{1}{2}(96)(0.9063)$$

$$A = 43.50 \text{ cm}^2$$

$$\boxed{A = 43.50 \text{ cm}^2}$$

---

## Resumen de Fórmulas

| Concepto | Fórmula |
|----------|---------|
| Conversión grados-radianes | $\theta_{rad} = \theta_{deg} \times \frac{\pi}{180}$ |
| Identidad pitagórica | $\sin^2\theta + \cos^2\theta = 1$ |
| Ángulo doble (seno) | $\sin 2\theta = 2\sin\theta\cos\theta$ |
| Ángulo doble (coseno) | $\cos 2\theta = \cos^2\theta - \sin^2\theta$ |
| Ley de senos | $\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}$ |
| Ley de cosenos | $a^2 = b^2 + c^2 - 2bc\cos A$ |
| Área (LAL) | $A = \frac{1}{2}ab\sin C$ |
| Período de $\sin(Bx)$ | $T = \frac{2\pi}{|B|}$ |

---

## Errores Comunes

| Error | Corrección |
|-------|------------|
| Olvidar modo de calculadora | Verificar DEG o RAD según el problema |
| $\sin^{-1}(\sin 150°) = 150°$ | El rango de $\arcsin$ es $[-90°, 90°]$, da $30°$ |
| Ignorar el caso ambiguo | En SSA, verificar si hay 0, 1 o 2 soluciones |
| Confundir $\sin^2 x$ con $\sin(x^2)$ | $\sin^2 x = (\sin x)^2$ |
| Ley de senos con ángulo incluido | Usar ley de cosenos para LAL |
| Signo incorrecto por cuadrante | Usar ASTC para determinar signos |
| $\sin(A + B) = \sin A + \sin B$ | Usar fórmula correcta de suma |
