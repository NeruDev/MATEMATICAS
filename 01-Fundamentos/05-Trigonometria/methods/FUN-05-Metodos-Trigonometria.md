<!--
HUMANO:
Procedimientos sistemáticos para resolver problemas de trigonometría.

IA:
Incluye unidades, rangos válidos y verificaciones.
Cada método debe tener ejemplo(s) resuelto(s).

---
content_type: methods_comprehensive
expected_output:
  default: markdown
audience: self-study
---
-->

# Métodos de Trigonometría

---

## Método 1: Conversión entre Grados y Radianes

### Objetivo
Convertir medidas de ángulos entre sistemas de grados y radianes.

### Procedimiento

**De grados a radianes:**
1. Multiplica los grados por $\frac{\pi}{180°}$
2. Simplifica la fracción resultante

**De radianes a grados:**
1. Multiplica los radianes por $\frac{180°}{\pi}$
2. Simplifica

### Ejemplo 1: Convertir 150° a radianes

$$150° \times \frac{\pi}{180°} = \frac{150\pi}{180} = \frac{5\pi}{6} \text{ rad}$$

### Ejemplo 2: Convertir $\frac{7\pi}{4}$ a grados

$$\frac{7\pi}{4} \times \frac{180°}{\pi} = \frac{7 \times 180°}{4} = \frac{1260°}{4} = 315°$$

### Verificación
- $\frac{5\pi}{6} \times \frac{180°}{\pi} = 150°$ ✓
- $315° \times \frac{\pi}{180°} = \frac{7\pi}{4}$ ✓

---

## Método 2: Encontrar Razones Trigonométricas en Triángulos Rectángulos

### Objetivo
Calcular las seis razones trigonométricas dado un triángulo rectángulo o información parcial.

### Procedimiento
1. Identifica el ángulo de interés $\theta$
2. Identifica cateto opuesto (CO), cateto adyacente (CA) e hipotenusa (H) respecto a $\theta$
3. Si falta un lado, usa el teorema de Pitágoras: $H^2 = CO^2 + CA^2$
4. Calcula las razones:
   - $\sin\theta = \frac{CO}{H}$
   - $\cos\theta = \frac{CA}{H}$
   - $\tan\theta = \frac{CO}{CA}$
   - Y sus recíprocas

### Ejemplo
En un triángulo rectángulo, el cateto opuesto a $\theta$ mide 5 y la hipotenusa mide 13. Encuentra las seis razones.

**Paso 1:** Encontrar el cateto adyacente
$$CA = \sqrt{13^2 - 5^2} = \sqrt{169 - 25} = \sqrt{144} = 12$$

**Paso 2:** Calcular razones
$$\sin\theta = \frac{5}{13} \qquad \cos\theta = \frac{12}{13} \qquad \tan\theta = \frac{5}{12}$$
$$\csc\theta = \frac{13}{5} \qquad \sec\theta = \frac{13}{12} \qquad \cot\theta = \frac{12}{5}$$

### Verificación
$$\sin^2\theta + \cos^2\theta = \frac{25}{169} + \frac{144}{169} = \frac{169}{169} = 1 \checkmark$$

---

## Método 3: Evaluar Funciones Trigonométricas usando el Círculo Unitario

### Objetivo
Encontrar el valor exacto de funciones trigonométricas para cualquier ángulo usando ángulos de referencia.

### Procedimiento
1. Convierte el ángulo a posición estándar (0° a 360° o 0 a $2\pi$)
2. Determina el cuadrante
3. Calcula el ángulo de referencia $\theta_R$
4. Evalúa la función para $\theta_R$ (ángulo agudo)
5. Aplica el signo según el cuadrante

### Ejemplo: Calcular $\sin(240°)$

**Paso 1:** El ángulo está en posición estándar.

**Paso 2:** 240° está en el Cuadrante III (180° < 240° < 270°)

**Paso 3:** Ángulo de referencia: $\theta_R = 240° - 180° = 60°$

**Paso 4:** $\sin(60°) = \frac{\sqrt{3}}{2}$

**Paso 5:** En el Cuadrante III, el seno es negativo.

$$\sin(240°) = -\frac{\sqrt{3}}{2}$$

### Verificación
En el círculo unitario, el punto para 240° es $\left(-\frac{1}{2}, -\frac{\sqrt{3}}{2}\right)$
La coordenada $y = -\frac{\sqrt{3}}{2}$ ✓

---

## Método 4: Graficar Funciones Trigonométricas Transformadas

### Objetivo
Graficar $y = A\sin(Bx - C) + D$ o $y = A\cos(Bx - C) + D$

### Procedimiento
1. Identifica los parámetros:
   - Amplitud: $\lvert A \rvert$
   - Período: $\frac{2\pi}{\lvert B \rvert}$
   - Desplazamiento horizontal (fase): $\frac{C}{B}$
   - Desplazamiento vertical: $D$
2. Determina los puntos clave dividiendo el período en 4 partes
3. Desplaza horizontalmente por $\frac{C}{B}$
4. Desplaza verticalmente por $D$
5. Si $A < 0$, refleja respecto al eje $x$

### Ejemplo: Graficar $y = 3\sin(2x - \pi) + 1$

**Parámetros:**
- Amplitud = 3
- Período = $\frac{2\pi}{2} = \pi$
- Desplazamiento horizontal = $\frac{\pi}{2}$ (hacia la derecha)
- Desplazamiento vertical = 1 (hacia arriba)

**Puntos clave de $\sin x$ sobre un período:** $(0,0), (\frac{\pi}{4},1), (\frac{\pi}{2},0), (\frac{3\pi}{4},-1), (\pi,0)$

**Aplicando transformaciones:**
| $x$ original | $x$ transformado | $y$ transformado |
|--------------|------------------|------------------|
| 0 | $\frac{\pi}{2}$ | $3(0)+1 = 1$ |
| $\frac{\pi}{4}$ | $\frac{3\pi}{4}$ | $3(1)+1 = 4$ |
| $\frac{\pi}{2}$ | $\pi$ | $3(0)+1 = 1$ |
| $\frac{3\pi}{4}$ | $\frac{5\pi}{4}$ | $3(-1)+1 = -2$ |
| $\pi$ | $\frac{3\pi}{2}$ | $3(0)+1 = 1$ |

---

## Método 5: Demostrar Identidades Trigonométricas

### Objetivo
Verificar que una ecuación es una identidad trabajando con un lado hasta obtener el otro.

### Procedimiento
1. Identifica el lado más complejo (generalmente trabaja con ese)
2. Convierte todo a senos y cosenos si es necesario
3. Usa identidades fundamentales:
   - $\sin^2\theta + \cos^2\theta = 1$
   - $\tan\theta = \frac{\sin\theta}{\cos\theta}$
4. Factoriza, simplifica o multiplica por conjugados
5. Continúa hasta obtener el otro lado

### Ejemplo: Demostrar $\frac{\tan\theta}{\sec\theta} = \sin\theta$

**Lado izquierdo:**
$$\frac{\tan\theta}{\sec\theta} = \frac{\frac{\sin\theta}{\cos\theta}}{\frac{1}{\cos\theta}}$$

$$= \frac{\sin\theta}{\cos\theta} \cdot \cos\theta = \sin\theta$$

**Conclusión:** LI = LD ∎

### Ejemplo 2: Demostrar $\frac{1}{1-\sin\theta} + \frac{1}{1+\sin\theta} = 2\sec^2\theta$

**Lado izquierdo:**
$$\frac{(1+\sin\theta) + (1-\sin\theta)}{(1-\sin\theta)(1+\sin\theta)} = \frac{2}{1-\sin^2\theta} = \frac{2}{\cos^2\theta} = 2\sec^2\theta$$

**Conclusión:** LI = LD ∎

---

## Método 6: Resolver Ecuaciones Trigonométricas

### Objetivo
Encontrar todas las soluciones de una ecuación trigonométrica.

### Procedimiento
1. Aísla la función trigonométrica
2. Si hay múltiples funciones, usa identidades para reducir a una sola
3. Encuentra las soluciones en el intervalo principal $[0, 2\pi)$
4. Escribe la solución general agregando el período

### Ejemplo 1: Resolver $2\sin\theta - 1 = 0$

**Paso 1:** $\sin\theta = \frac{1}{2}$

**Paso 2:** ¿En qué cuadrantes es $\sin\theta > 0$? Cuadrantes I y II.

**Paso 3:** Ángulo de referencia: $\arcsin\left(\frac{1}{2}\right) = \frac{\pi}{6}$

**Paso 4:** Soluciones en $[0, 2\pi)$:
- Cuadrante I: $\theta = \frac{\pi}{6}$
- Cuadrante II: $\theta = \pi - \frac{\pi}{6} = \frac{5\pi}{6}$

**Solución general:**
$$\theta = \frac{\pi}{6} + 2\pi n \quad \text{o} \quad \theta = \frac{5\pi}{6} + 2\pi n, \quad n \in \mathbb{Z}$$

### Ejemplo 2: Resolver $2\cos^2\theta - \cos\theta - 1 = 0$

**Paso 1:** Factorizamos (es una cuadrática en $\cos\theta$):
$$(2\cos\theta + 1)(\cos\theta - 1) = 0$$

**Paso 2:** 
- $\cos\theta = -\frac{1}{2}$ → $\theta = \frac{2\pi}{3}, \frac{4\pi}{3}$
- $\cos\theta = 1$ → $\theta = 0$

**Solución general:**
$$\theta = \frac{2\pi}{3} + 2\pi n, \quad \theta = \frac{4\pi}{3} + 2\pi n, \quad \theta = 2\pi n$$

---

## Método 7: Usar Fórmulas de Suma y Resta de Ángulos

### Objetivo
Calcular valores exactos de funciones trigonométricas para ángulos no estándar.

### Procedimiento
1. Expresa el ángulo como suma o diferencia de ángulos conocidos
2. Aplica la fórmula correspondiente
3. Sustituye los valores conocidos
4. Simplifica

### Ejemplo: Calcular $\cos(15°)$

**Paso 1:** $15° = 45° - 30°$

**Paso 2:** Aplicamos $\cos(\alpha - \beta) = \cos\alpha\cos\beta + \sin\alpha\sin\beta$

$$\cos(15°) = \cos(45°)\cos(30°) + \sin(45°)\sin(30°)$$

**Paso 3:**
$$= \frac{\sqrt{2}}{2} \cdot \frac{\sqrt{3}}{2} + \frac{\sqrt{2}}{2} \cdot \frac{1}{2}$$

$$= \frac{\sqrt{6}}{4} + \frac{\sqrt{2}}{4} = \frac{\sqrt{6} + \sqrt{2}}{4}$$

### Verificación
$\cos(15°) \approx 0.9659$ y $\frac{\sqrt{6} + \sqrt{2}}{4} \approx \frac{2.449 + 1.414}{4} \approx 0.9659$ ✓

---

## Método 8: Resolver Triángulos con la Ley de Senos

### Objetivo
Encontrar lados y ángulos desconocidos en triángulos oblicuángulos (casos ALA, LAA, LLA).

### Procedimiento
1. Identifica los datos conocidos
2. Aplica la ley de senos: $\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}$
3. Para el caso LLA, verifica si hay 0, 1 o 2 soluciones
4. Usa que la suma de ángulos es 180°

### Ejemplo (Caso LAA): En el triángulo ABC, $A = 40°$, $B = 60°$, $a = 10$. Encuentra $b$ y $c$.

**Paso 1:** $C = 180° - 40° - 60° = 80°$

**Paso 2:** Por ley de senos:
$$\frac{10}{\sin 40°} = \frac{b}{\sin 60°} = \frac{c}{\sin 80°}$$

**Paso 3:**
$$b = \frac{10 \sin 60°}{\sin 40°} = \frac{10 \cdot 0.866}{0.643} \approx 13.47$$

$$c = \frac{10 \sin 80°}{\sin 40°} = \frac{10 \cdot 0.985}{0.643} \approx 15.32$$

### Verificación
$\frac{13.47}{\sin 60°} \approx \frac{13.47}{0.866} \approx 15.56$
$\frac{10}{\sin 40°} \approx \frac{10}{0.643} \approx 15.55$ ✓

---

## Método 9: Resolver Triángulos con la Ley de Cosenos

### Objetivo
Encontrar lados y ángulos en triángulos oblicuángulos (casos LLL, LAL).

### Procedimiento
**Caso LAL (encontrar un lado):**
1. Usa $c^2 = a^2 + b^2 - 2ab\cos C$

**Caso LLL (encontrar un ángulo):**
1. Usa $\cos A = \frac{b^2 + c^2 - a^2}{2bc}$
2. Calcula $A = \arccos(\text{resultado})$

### Ejemplo (Caso LAL): En el triángulo ABC, $a = 7$, $b = 10$, $C = 51°$. Encuentra $c$.

$$c^2 = 7^2 + 10^2 - 2(7)(10)\cos 51°$$
$$c^2 = 49 + 100 - 140(0.629)$$
$$c^2 = 149 - 88.06 = 60.94$$
$$c \approx 7.81$$

### Ejemplo (Caso LLL): En un triángulo con $a = 8$, $b = 6$, $c = 10$. Encuentra el ángulo mayor.

El ángulo mayor está opuesto al lado mayor ($c = 10$), así que buscamos $C$.

$$\cos C = \frac{8^2 + 6^2 - 10^2}{2(8)(6)} = \frac{64 + 36 - 100}{96} = \frac{0}{96} = 0$$

$$C = \arccos(0) = 90°$$

**Conclusión:** Es un triángulo rectángulo (6, 8, 10 es múltiplo de 3, 4, 5).

---

## Método 10: Calcular el Área de un Triángulo con Trigonometría

### Objetivo
Encontrar el área cuando se conocen dos lados y el ángulo incluido.

### Procedimiento
1. Identifica dos lados y el ángulo entre ellos
2. Aplica: $A = \frac{1}{2}ab\sin C$

### Ejemplo
Calcula el área del triángulo con $a = 12$, $b = 15$, $C = 47°$.

$$A = \frac{1}{2}(12)(15)\sin 47°$$
$$A = 90 \cdot 0.7314 \approx 65.8 \text{ unidades}^2$$

### Verificación alternativa
Si conocemos los tres lados después de aplicar la ley de cosenos, podemos usar Herón y comparar.

---

## Método 11: Evaluar Funciones Trigonométricas Inversas

### Objetivo
Calcular $\arcsin(x)$, $\arccos(x)$, $\arctan(x)$ respetando dominios y rangos.

### Procedimiento
1. Verifica que el argumento esté en el dominio
2. Identifica el ángulo de referencia
3. Selecciona el ángulo dentro del rango de la función inversa

### Rangos a recordar:
- $\arcsin(x)$: $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$
- $\arccos(x)$: $[0, \pi]$
- $\arctan(x)$: $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$

### Ejemplo 1: $\arcsin\left(-\frac{\sqrt{3}}{2}\right)$

El valor de referencia es $\arcsin\left(\frac{\sqrt{3}}{2}\right) = \frac{\pi}{3}$

Como el argumento es negativo y el rango de $\arcsin$ incluye valores negativos:
$$\arcsin\left(-\frac{\sqrt{3}}{2}\right) = -\frac{\pi}{3}$$

### Ejemplo 2: $\arccos\left(-\frac{1}{2}\right)$

El valor de referencia es $\arccos\left(\frac{1}{2}\right) = \frac{\pi}{3}$

Como el argumento es negativo y el rango de $\arccos$ es $[0, \pi]$:
$$\arccos\left(-\frac{1}{2}\right) = \pi - \frac{\pi}{3} = \frac{2\pi}{3}$$

---

## Método 12: Resolver Problemas de Aplicación (Altura y Distancia)

### Objetivo
Usar trigonometría para resolver problemas del mundo real.

### Procedimiento
1. Dibuja un diagrama
2. Identifica ángulos de elevación/depresión
3. Forma triángulos rectángulos
4. Aplica razones trigonométricas
5. Resuelve y verifica que la respuesta tenga sentido

### Ejemplo
Desde la cima de un edificio de 50 m, el ángulo de depresión hacia un auto es 35°. ¿A qué distancia horizontal está el auto del edificio?

**Diagrama:**
```
         Edificio
           |\ 35° (depresión)
        50m| \
           |  \
           |___\ Auto
             d
```

**Solución:**
El ángulo de depresión de 35° equivale a un ángulo de 35° en el triángulo rectángulo formado.

$$\tan(35°) = \frac{50}{d}$$

$$d = \frac{50}{\tan(35°)} = \frac{50}{0.7002} \approx 71.4 \text{ m}$$

### Verificación
$\tan(35°) \times 71.4 \approx 50$ ✓
