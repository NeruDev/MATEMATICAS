<!--
HUMANO:
Métodos para integrales impropias.

IA:
Procedimientos para evaluar y determinar convergencia.

---
content_type: methods
format: step_by_step
---
-->

# Métodos para Integrales Impropias

---

## Método 1: Evaluación Directa (Tipo I)

**Aplicación:** Integrales con límite infinito evaluables explícitamente.

**Pasos:**
1. Reemplazar $\infty$ por $t$.
2. Calcular la integral definida en términos de $t$.
3. Tomar el límite cuando $t \to \infty$.

**Ejemplo:** $\displaystyle\int_1^{\infty} e^{-x}\,dx$

1. $\int_1^t e^{-x}\,dx = [-e^{-x}]_1^t = -e^{-t} + e^{-1}$
2. $\lim_{t \to \infty} (-e^{-t} + e^{-1}) = 0 + e^{-1} = \frac{1}{e}$

---

## Método 2: Evaluación Directa (Tipo II)

**Aplicación:** Integrales con discontinuidad evaluables explícitamente.

**Pasos:**
1. Identificar el punto de discontinuidad $c$.
2. Reemplazar $c$ por $t$ con límite apropiado.
3. Evaluar y tomar el límite.

**Ejemplo:** $\displaystyle\int_0^4 \frac{1}{\sqrt{x}}\,dx$

Discontinuidad en $x = 0$:
1. $\int_t^4 x^{-1/2}\,dx = [2\sqrt{x}]_t^4 = 4 - 2\sqrt{t}$
2. $\lim_{t \to 0^+} (4 - 2\sqrt{t}) = 4$

---

## Método 3: Test de la Integral p (Infinito)

**Aplicación:** Determinar convergencia rápidamente.

**Regla:** Para $\int_1^{\infty} \frac{1}{x^p}\,dx$:
- **Converge** si $p > 1$
- **Diverge** si $p \leq 1$

**Ejemplo:** $\int_1^{\infty} \frac{1}{x^{3/2}}\,dx$

Como $p = 3/2 > 1$, **converge** a $\frac{1}{3/2 - 1} = 2$.

---

## Método 4: Test de la Integral p (Cero)

**Aplicación:** Discontinuidades en $x = 0$.

**Regla:** Para $\int_0^{1} \frac{1}{x^p}\,dx$:
- **Converge** si $p < 1$
- **Diverge** si $p \geq 1$

**Ejemplo:** $\int_0^1 \frac{1}{x^{2/3}}\,dx$

Como $p = 2/3 < 1$, **converge** a $\frac{1}{1 - 2/3} = 3$.

---

## Método 5: Comparación Directa

**Aplicación:** Cuando no se puede integrar explícitamente.

**Pasos:**
1. Encontrar $g(x)$ tal que $0 \leq f(x) \leq g(x)$ (para convergencia) o $f(x) \geq g(x) \geq 0$ (para divergencia).
2. Verificar que $\int g$ converge/diverge.
3. Concluir sobre $\int f$.

**Ejemplo:** $\int_1^{\infty} \frac{1}{x^2 + 1}\,dx$

Como $\frac{1}{x^2+1} < \frac{1}{x^2}$ y $\int_1^{\infty} \frac{1}{x^2}\,dx$ converge, la integral **converge**.

---

## Método 6: Comparación por Límite

**Aplicación:** Cuando la comparación directa es difícil.

**Pasos:**
1. Identificar el comportamiento dominante de $f(x)$ cuando $x \to \infty$.
2. Elegir $g(x)$ con ese comportamiento.
3. Calcular $L = \lim_{x \to \infty} \frac{f(x)}{g(x)}$.
4. Si $0 < L < \infty$, ambas tienen el mismo comportamiento.

**Ejemplo:** $\int_1^{\infty} \frac{x^2 + 3}{x^4 - x + 2}\,dx$

Comportamiento: $\frac{x^2}{x^4} = \frac{1}{x^2}$

$$\lim_{x \to \infty} \frac{(x^2+3)/(x^4-x+2)}{1/x^2} = \lim_{x \to \infty} \frac{x^4 + 3x^2}{x^4 - x + 2} = 1$$

Como $\int_1^{\infty} \frac{1}{x^2}\,dx$ converge, la integral **converge**.

---

## Método 7: División en Subintervalos

**Aplicación:** Discontinuidad interior o ambos límites infinitos.

**Pasos:**
1. Dividir en el punto problemático.
2. Evaluar cada parte por separado.
3. Sumar si ambas convergen.

**Ejemplo:** $\int_{-\infty}^{\infty} \frac{1}{1+x^2}\,dx$

$$= \int_{-\infty}^{0} \frac{1}{1+x^2}\,dx + \int_0^{\infty} \frac{1}{1+x^2}\,dx$$

$$= \lim_{t \to -\infty} [\arctan x]_t^0 + \lim_{s \to \infty} [\arctan x]_0^s$$

$$= (0 - (-\frac{\pi}{2})) + (\frac{\pi}{2} - 0) = \pi$$

---

## Método 8: Sustitución en Impropias

**Aplicación:** Simplificar la integral antes de evaluar.

**Pasos:**
1. Aplicar sustitución usual.
2. **Cambiar límites** (importante: $\infty$ puede convertirse en otro valor).
3. Evaluar la nueva integral impropia.

**Ejemplo:** $\int_1^{\infty} \frac{1}{x\sqrt{x^2-1}}\,dx$

Sea $x = \sec\theta$, $dx = \sec\theta\tan\theta\,d\theta$

- $x = 1 \Rightarrow \theta = 0$
- $x \to \infty \Rightarrow \theta \to \frac{\pi}{2}$

$$= \int_0^{\pi/2} \frac{\sec\theta\tan\theta}{\sec\theta \cdot \tan\theta}\,d\theta = \int_0^{\pi/2} d\theta = \frac{\pi}{2}$$

---

## Método 9: Identificar Forma Conocida

**Aplicación:** Reconocer integrales clásicas.

**Formas útiles:**
- $\int_0^{\infty} e^{-ax}\,dx = \frac{1}{a}$ (para $a > 0$)
- $\int_0^{\infty} x^{n}e^{-x}\,dx = n!$
- $\int_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt{\pi}$

---

## Método 10: Análisis de Comportamiento Asintótico

**Aplicación:** Determinar convergencia sin calcular.

**Pasos:**
1. Analizar $f(x)$ cuando $x \to \infty$ (o hacia la discontinuidad).
2. Simplificar a la forma $\frac{c}{x^p}$ o similar.
3. Aplicar el test p.

**Ejemplo:** $\int_2^{\infty} \frac{\ln x}{x^2}\,dx$

Para $x$ grande: $\ln x$ crece más lento que cualquier potencia positiva.

$$\frac{\ln x}{x^2} < \frac{x^{1/2}}{x^2} = \frac{1}{x^{3/2}}$$

Como $\int \frac{1}{x^{3/2}}\,dx$ converge (p = 3/2 > 1), la integral **converge**.
