<!--
::METADATA::
type: method
status: active
-->

# Métodos: Transformada de Laplace

> **Referencia rápida:** Esta guía presenta 12 métodos sistemáticos para aplicar la [Transformada de Laplace](../../../glossary.md#transformada-de-laplace) en la resolución de [ecuaciones diferenciales](../../../glossary.md#ecuaciones-diferenciales).

---

## Índice de Métodos

| # | Método | Aplicación | Complejidad |
|---|--------|------------|-------------|
| 1 | [Transformada Directa](#método-1-calcular-transformada-directamente) | Funciones básicas | ⭐ |
| 2 | [Primera Traslación](#método-2-primera-traslación-en-s) | Funciones con $e^{at}$ | ⭐⭐ |
| 3 | [Segunda Traslación](#método-3-segunda-traslación-en-t) | Funciones escalón | ⭐⭐⭐ |
| 4 | [Fracciones Parciales](#método-4-inversa-por-fracciones-parciales) | Inversas racionales | ⭐⭐⭐ |
| 5 | [Completar Cuadrado](#método-5-completar-el-cuadrado) | Denominadores cuadráticos | ⭐⭐⭐ |
| 6 | [Resolver PVI](#método-6-resolver-pvi-con-laplace) | Ecuaciones diferenciales | ⭐⭐⭐ |
| 7 | [Funciones Escalón](#método-7-manejar-funciones-escalón) | Entradas discontinuas | ⭐⭐⭐ |
| 8 | [Función Delta](#método-8-[función](../../../glossary.md#función)-delta-de-dirac) | Impulsos | ⭐⭐⭐ |
| 9 | [Convolución](#método-9-teorema-de-convolución) | Productos de transformadas | ⭐⭐⭐⭐ |
| 10 | [Sistemas con Laplace](#método-10-sistemas-de-[edo](../../../glossary.md#edo)-con-laplace) | Sistemas acoplados | ⭐⭐⭐⭐ |
| 11 | [Derivada de F(s)](#método-11-[derivada](../../../glossary.md#derivada)-de-la-transformada) | Transformadas con $t^n$ | ⭐⭐ |
| 12 | [Funciones Periódicas](#método-12-funciones-periódicas) | Entradas repetitivas | ⭐⭐⭐⭐ |

---

## Tabla de Transformadas Fundamentales

| $f(t)$ | $F(s) = \mathcal{L}\{f(t)\}$ | Condición |
|--------|------------------------------|-----------|
| $1$ | $\frac{1}{s}$ | $s > 0$ |
| $t^n$ | $\frac{n!}{s^{n+1}}$ | $s > 0$ |
| $e^{at}$ | $\frac{1}{s-a}$ | $s > a$ |
| $\sin bt$ | $\frac{b}{s^2+b^2}$ | $s > 0$ |
| $\cos bt$ | $\frac{s}{s^2+b^2}$ | $s > 0$ |
| $\sinh bt$ | $\frac{b}{s^2-b^2}$ | $s > \lvert b \rvert$ |
| $\cosh bt$ | $\frac{s}{s^2-b^2}$ | $s > \lvert b \rvert$ |
| $t^n e^{at}$ | $\frac{n!}{(s-a)^{n+1}}$ | $s > a$ |
| $e^{at}\sin bt$ | $\frac{b}{(s-a)^2+b^2}$ | $s > a$ |
| $e^{at}\cos bt$ | $\frac{s-a}{(s-a)^2+b^2}$ | $s > a$ |
| $u(t-a)$ | $\frac{e^{-as}}{s}$ | $s > 0$ |
| $\delta(t-a)$ | $e^{-as}$ | — |

---

## Método 1: Calcular Transformada Directamente

### Cuándo Usar

- La función es [combinación lineal](../../../glossary.md#combinación-lineal) de funciones de la tabla
- Aplicar [linealidad](../../../glossary.md#linealidad): $\mathcal{L}\{af + bg\} = aF + bG$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Identificar** | Descomponer $f(t)$ en términos simples |
| 2 | **Consultar tabla** | Encontrar transformada de cada término |
| 3 | **Aplicar linealidad** | Combinar con constantes |
| 4 | **Simplificar** | Reducir expresión si es posible |

### Ejemplo Detallado

**Problema:** Encontrar $\mathcal{L}\{3t^2 - 5e^{-2t} + 4\sin 3t + 2\}$

---

**Paso 1: Identificar componentes**

- $3t^2$: potencia
- $-5e^{-2t}$: exponencial
- $4\sin 3t$: [seno](../../../glossary.md#seno)
- $2$: constante

---

**Paso 2: Transformadas individuales**

$$\mathcal{L}\{t^2\} = \frac{2!}{s^3} = \frac{2}{s^3}$$

$$\mathcal{L}\{e^{-2t}\} = \frac{1}{s+2}$$

$$\mathcal{L}\{\sin 3t\} = \frac{3}{s^2+9}$$

$$\mathcal{L}\{1\} = \frac{1}{s}$$

---

**Paso 3: Aplicar linealidad**

$$\mathcal{L}\{f(t)\} = 3 \cdot \frac{2}{s^3} - 5 \cdot \frac{1}{s+2} + 4 \cdot \frac{3}{s^2+9} + 2 \cdot \frac{1}{s}$$

---

**Paso 4: Simplificar**

$$\boxed{F(s) = \frac{6}{s^3} - \frac{5}{s+2} + \frac{12}{s^2+9} + \frac{2}{s}}$$

---

## Método 2: Primera Traslación (en s)

### Cuándo Usar

- La función tiene factor exponencial: $f(t) = e^{at}g(t)$
- Para exponenciales multiplicando senos/cosenos

### Fórmula

$$\mathcal{L}\{e^{at}g(t)\} = G(s-a)$$

donde $G(s) = \mathcal{L}\{g(t)\}$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Identificar** | Factor $e^{at}$ y función $g(t)$ |
| 2 | **Transformar** $g(t)$ | Encontrar $G(s)$ |
| 3 | **Trasladar** | Reemplazar $s$ por $s-a$ en $G(s)$ |

### Ejemplo Detallado

**Problema:** Encontrar $\mathcal{L}\{e^{-3t}t^2\cos 4t\}$

---

**Paso 1: Identificar**

$a = -3$, $g(t) = t^2\cos 4t$

---

**Paso 2: Transformar** $g(t) = t^2\cos 4t$

Usando $\mathcal{L}\{t^n f(t)\} = (-1)^n \frac{d^n}{ds^n}F(s)$:

$\mathcal{L}\{\cos 4t\} = \frac{s}{s^2+16}$

$\mathcal{L}\{t\cos 4t\} = -\frac{d}{ds}\left(\frac{s}{s^2+16}\right) = -\frac{(s^2+16) - s(2s)}{(s^2+16)^2} = \frac{s^2-16}{(s^2+16)^2}$

$\mathcal{L}\{t^2\cos 4t\} = -\frac{d}{ds}\left(\frac{s^2-16}{(s^2+16)^2}\right)$

Derivando (usando regla del cociente):

$$G(s) = \frac{2s(s^2+48)}{(s^2+16)^3}$$

---

**Paso 3: Trasladar** ($s \to s+3$)

$$\boxed{\mathcal{L}\{e^{-3t}t^2\cos 4t\} = \frac{2(s+3)[(s+3)^2+48]}{[(s+3)^2+16]^3}}$$

---

### Ejemplo Más Simple

**Problema:** Encontrar $\mathcal{L}\{e^{2t}\sin 5t\}$

**Paso 1:** $a = 2$, $g(t) = \sin 5t$

**Paso 2:** $G(s) = \frac{5}{s^2+25}$

**Paso 3:** $s \to s-2$

$$\boxed{\mathcal{L}\{e^{2t}\sin 5t\} = \frac{5}{(s-2)^2+25}}$$

---

## Método 3: Segunda Traslación (en t)

### Cuándo Usar

- Funciones con retardo temporal
- Funciones definidas por partes usando escalón unitario

### Fórmulas

$$\mathcal{L}\{f(t-a)u(t-a)\} = e^{-as}F(s)$$

$$\mathcal{L}^{-1}\{e^{-as}F(s)\} = f(t-a)u(t-a)$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Identificar retardo** | El valor de $a$ en $u(t-a)$ |
| 2 | **Reescribir función** | En términos de $(t-a)$ |
| 3 | **Aplicar fórmula** | Multiplicar por $e^{-as}$ |

### Ejemplo Detallado

**Problema:** Encontrar $\mathcal{L}\{(t-2)^3 u(t-2)\}$

---

**Paso 1: Identificar**

Retardo $a = 2$, función $f(t) = t^3$

---

**Paso 2: Verificar forma**

Ya está en forma $(t-a)^3 u(t-a)$ ✓

$f(t-2) = (t-2)^3$ con $f(t) = t^3$

---

**Paso 3: Aplicar fórmula**

$\mathcal{L}\{t^3\} = \frac{6}{s^4}$

$$\boxed{\mathcal{L}\{(t-2)^3 u(t-2)\} = e^{-2s} \cdot \frac{6}{s^4} = \frac{6e^{-2s}}{s^4}}$$

---

### Ejemplo con Reescritura

**Problema:** Encontrar $\mathcal{L}\{t^2 u(t-3)\}$

---

**Paso 1:** Necesitamos reescribir $t^2$ en términos de $(t-3)$

$t = (t-3) + 3$

$t^2 = [(t-3) + 3]^2 = (t-3)^2 + 6(t-3) + 9$

---

**Paso 2:** Aplicar linealidad

$$\mathcal{L}\{t^2 u(t-3)\} = \mathcal{L}\{[(t-3)^2 + 6(t-3) + 9]u(t-3)\}$$

---

**Paso 3:** Transformar cada término

$$= e^{-3s}\mathcal{L}\{t^2 + 6t + 9\}$$

$$= e^{-3s}\left(\frac{2}{s^3} + \frac{6}{s^2} + \frac{9}{s}\right)$$

$$\boxed{= \frac{e^{-3s}(2 + 6s + 9s^2)}{s^3}}$$

---

## Método 4: Inversa por Fracciones Parciales

### Cuándo Usar

- $F(s)$ es función racional propia
- Denominador factorizable

### Tipos de Factores

| Factor en Denominador | Forma de Fracción Parcial |
|-----------------------|---------------------------|
| $(s-a)$ | $\frac{A}{s-a}$ |
| $(s-a)^n$ | $\frac{A_1}{s-a} + \frac{A_2}{(s-a)^2} + \cdots + \frac{A_n}{(s-a)^n}$ |
| $(s^2+bs+c)$ irreducible | $\frac{As+B}{s^2+bs+c}$ |
| $(s^2+bs+c)^n$ | Suma de $\frac{A_ks+B_k}{(s^2+bs+c)^k}$ |

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Verificar** | Grado(num) < Grado(den) |
| 2 | **Factorizar** | Denominador completamente |
| 3 | **Escribir** | Descomposición en fracciones parciales |
| 4 | **Encontrar coeficientes** | Por cover-up o sistema de ecuaciones |
| 5 | **Invertir** | Cada fracción usando tabla |

### Ejemplo Detallado

**Problema:** Encontrar $\mathcal{L}^{-1}\left\{\frac{3s+7}{(s-1)(s+2)^2}\right\}$

---

**Paso 1: Verificar**

Grado(num) = 1 < Grado(den) = 3 ✓

---

**Paso 2: Ya factorizado**

$(s-1)$ factor simple, $(s+2)^2$ factor repetido

---

**Paso 3: Escribir descomposición**

$$\frac{3s+7}{(s-1)(s+2)^2} = \frac{A}{s-1} + \frac{B}{s+2} + \frac{C}{(s+2)^2}$$

---

**Paso 4: Encontrar coeficientes**

Multiplicando ambos lados por $(s-1)(s+2)^2$:

$3s+7 = A(s+2)^2 + B(s-1)(s+2) + C(s-1)$

**Método cover-up:**

$s = 1$: $3(1)+7 = A(3)^2 \implies 10 = 9A \implies A = \frac{10}{9}$

$s = -2$: $3(-2)+7 = C(-3) \implies 1 = -3C \implies C = -\frac{1}{3}$

**Para $B$:** usar $s = 0$:

$7 = \frac{10}{9}(4) + B(-1)(2) + (-\frac{1}{3})(-1)$

$7 = \frac{40}{9} - 2B + \frac{1}{3}$

$7 = \frac{40}{9} + \frac{3}{9} - 2B = \frac{43}{9} - 2B$

$2B = \frac{43}{9} - 7 = \frac{43-63}{9} = -\frac{20}{9}$

$B = -\frac{10}{9}$

---

**Paso 5: Invertir**

$$F(s) = \frac{10/9}{s-1} - \frac{10/9}{s+2} - \frac{1/3}{(s+2)^2}$$

$$f(t) = \frac{10}{9}e^t - \frac{10}{9}e^{-2t} - \frac{1}{3}te^{-2t}$$

$$\boxed{f(t) = \frac{10}{9}(e^t - e^{-2t}) - \frac{1}{3}te^{-2t}}$$

---

## Método 5: Completar el Cuadrado

### Cuándo Usar

- Denominador cuadrático que no factoriza fácilmente
- Para obtener formas de seno/[coseno](../../../glossary.md#coseno) amortiguado

### Fórmula

$$s^2 + bs + c = \left(s + \frac{b}{2}\right)^2 + \left(c - \frac{b^2}{4}\right)$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Completar cuadrado** | En denominador |
| 2 | **Identificar** | $\alpha = \frac{b}{2}$, $\omega^2 = c - \frac{b^2}{4}$ |
| 3 | **Ajustar numerador** | Escribir como $A(s+\alpha) + B$ |
| 4 | **Separar** | En dos fracciones |
| 5 | **Identificar formas** | Coseno y seno amortiguados |

### Ejemplo Detallado

**Problema:** Encontrar $\mathcal{L}^{-1}\left\{\frac{2s+5}{s^2+4s+13}\right\}$

---

**Paso 1: Completar el cuadrado**

$s^2 + 4s + 13 = (s^2 + 4s + 4) + 9 = (s+2)^2 + 9$

---

**Paso 2: Identificar**

$\alpha = 2$, $\omega^2 = 9$, $\omega = 3$

---

**Paso 3: Ajustar numerador**

$2s + 5 = 2(s+2) + (5-4) = 2(s+2) + 1$

---

**Paso 4: Separar**

$$\frac{2s+5}{(s+2)^2+9} = \frac{2(s+2)}{(s+2)^2+9} + \frac{1}{(s+2)^2+9}$$

---

**Paso 5: Identificar formas**

$$\frac{s+2}{(s+2)^2+9} \xleftarrow{\mathcal{L}^{-1}} e^{-2t}\cos 3t$$

$$\frac{3}{(s+2)^2+9} \xleftarrow{\mathcal{L}^{-1}} e^{-2t}\sin 3t$$

Entonces:

$$\frac{1}{(s+2)^2+9} = \frac{1}{3} \cdot \frac{3}{(s+2)^2+9} \xleftarrow{\mathcal{L}^{-1}} \frac{1}{3}e^{-2t}\sin 3t$$

---

**Paso 6: Combinar**

$$\boxed{f(t) = 2e^{-2t}\cos 3t + \frac{1}{3}e^{-2t}\sin 3t = e^{-2t}\left(2\cos 3t + \frac{1}{3}\sin 3t\right)}$$

---

## Método 6: Resolver PVI con Laplace

### Cuándo Usar

- EDO lineal con coeficientes constantes
- Condiciones iniciales dadas
- Especialmente útil para entradas discontinuas

### Fórmulas de Derivadas

$$\mathcal{L}\{y'\} = sY(s) - y(0)$$
$$\mathcal{L}\{y''\} = s^2Y(s) - sy(0) - y'(0)$$
$$\mathcal{L}\{y'''\} = s^3Y(s) - s^2y(0) - sy'(0) - y''(0)$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Aplicar** $\mathcal{L}$ | A toda la ecuación |
| 2 | **Sustituir** | Fórmulas de derivadas con CI |
| 3 | **Despejar** | $Y(s)$ |
| 4 | **Simplificar** | Algebra de fracciones |
| 5 | **Aplicar** $\mathcal{L}^{-1}$ | Obtener $y(t)$ |

### Ejemplo Detallado

**Problema:** Resolver $y'' + 4y' + 3y = e^{-t}$, $y(0) = 0$, $y'(0) = 2$

---

**Paso 1: Aplicar transformada**

$$\mathcal{L}\{y''\} + 4\mathcal{L}\{y'\} + 3\mathcal{L}\{y\} = \mathcal{L}\{e^{-t}\}$$

---

**Paso 2: Sustituir usando CI**

$[s^2Y - s(0) - 2] + 4[sY - 0] + 3Y = \frac{1}{s+1}$

$s^2Y - 2 + 4sY + 3Y = \frac{1}{s+1}$

---

**Paso 3: Despejar** $Y(s)$

$Y(s^2 + 4s + 3) = \frac{1}{s+1} + 2$

$Y(s+1)(s+3) = \frac{1 + 2(s+1)}{s+1} = \frac{2s+3}{s+1}$

$$Y(s) = \frac{2s+3}{(s+1)^2(s+3)}$$

---

**Paso 4: [Fracciones parciales](../../../glossary.md#fracciones-parciales)**

$$\frac{2s+3}{(s+1)^2(s+3)} = \frac{A}{s+1} + \frac{B}{(s+1)^2} + \frac{C}{s+3}$$

$2s+3 = A(s+1)(s+3) + B(s+3) + C(s+1)^2$

$s = -1$: $1 = 2B \implies B = \frac{1}{2}$

$s = -3$: $-3 = 4C \implies C = -\frac{3}{4}$

$s = 0$: $3 = 3A + 3B + C = 3A + \frac{3}{2} - \frac{3}{4}$

$3 = 3A + \frac{3}{4} \implies A = \frac{3}{4}$

$$Y(s) = \frac{3/4}{s+1} + \frac{1/2}{(s+1)^2} - \frac{3/4}{s+3}$$

---

**Paso 5: Inversa**

$$y(t) = \frac{3}{4}e^{-t} + \frac{1}{2}te^{-t} - \frac{3}{4}e^{-3t}$$

$$\boxed{y(t) = \frac{3}{4}(e^{-t} - e^{-3t}) + \frac{1}{2}te^{-t}}$$

---

**Verificación de CI:**

$y(0) = \frac{3}{4}(1-1) + 0 = 0$ ✓

$y'(t) = \frac{3}{4}(-e^{-t} + 3e^{-3t}) + \frac{1}{2}(e^{-t} - te^{-t})$

$y'(0) = \frac{3}{4}(-1+3) + \frac{1}{2}(1-0) = \frac{3}{2} + \frac{1}{2} = 2$ ✓

---

## Método 7: Manejar Funciones Escalón

### Cuándo Usar

- Funciones definidas por partes
- Entradas que se activan/desactivan

### Convertir Función por Partes a Escalones

$$f(t) = \begin{cases} f_1(t) & 0 \leq t < a \\ f_2(t) & a \leq t < b \\ f_3(t) & t \geq b \end{cases}$$

$$= f_1(t) + [f_2(t) - f_1(t)]u(t-a) + [f_3(t) - f_2(t)]u(t-b)$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Escribir** | En términos de funciones escalón |
| 2 | **Para cada término** | Reescribir como $g(t-a)u(t-a)$ |
| 3 | **Transformar** | Usar segunda traslación |
| 4 | **Combinar** | Sumar todas las transformadas |

### Ejemplo Detallado

**Problema:** Resolver $y' + y = f(t)$, $y(0) = 0$, donde

$$f(t) = \begin{cases} 1 & 0 \leq t < 2 \\ 0 & t \geq 2 \end{cases}$$

---

**Paso 1: Escribir $f(t)$ con escalones**

$f(t) = 1 - u(t-2) = u(t) - u(t-2)$

(asumiendo $t \geq 0$, entonces $f(t) = 1 - u(t-2)$)

---

**Paso 2: Transformar $f(t)$**

$$\mathcal{L}\{f\} = \frac{1}{s} - \frac{e^{-2s}}{s} = \frac{1 - e^{-2s}}{s}$$

---

**Paso 3: Aplicar Laplace a la EDO**

$sY - 0 + Y = \frac{1 - e^{-2s}}{s}$

$Y(s+1) = \frac{1 - e^{-2s}}{s}$

$$Y(s) = \frac{1 - e^{-2s}}{s(s+1)}$$

---

**Paso 4: Fracciones parciales**

$$\frac{1}{s(s+1)} = \frac{1}{s} - \frac{1}{s+1}$$

$$Y(s) = \left(\frac{1}{s} - \frac{1}{s+1}\right) - e^{-2s}\left(\frac{1}{s} - \frac{1}{s+1}\right)$$

---

**Paso 5: Inversa**

$$\mathcal{L}^{-1}\left\{\frac{1}{s} - \frac{1}{s+1}\right\} = 1 - e^{-t}$$

$$\mathcal{L}^{-1}\left\{e^{-2s}\left(\frac{1}{s} - \frac{1}{s+1}\right)\right\} = [1 - e^{-(t-2)}]u(t-2)$$

---

**Paso 6: Solución**

$$\boxed{y(t) = (1 - e^{-t}) - (1 - e^{-(t-2)})u(t-2)}$$

**Forma explícita:**
$$y(t) = \begin{cases} 1 - e^{-t} & 0 \leq t < 2 \\ e^{-(t-2)} - e^{-t} & t \geq 2 \end{cases}$$

---

## Método 8: Función Delta de Dirac

### Cuándo Usar

- Impulsos instantáneos
- Fuerzas aplicadas en un instante

### Propiedades

$$\mathcal{L}\{\delta(t-a)\} = e^{-as}$$

$$\mathcal{L}\{\delta(t)\} = 1$$

$$\int_0^\infty f(t)\delta(t-a)\,dt = f(a) \quad (a > 0)$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Aplicar** $\mathcal{L}$ | $\delta(t-a) \to e^{-as}$ |
| 2 | **Resolver** | Para $Y(s)$ |
| 3 | **Inversa** | Usando segunda traslación |

### Ejemplo Detallado

**Problema:** Resolver $y'' + y = 2\delta(t-\pi)$, $y(0) = 0$, $y'(0) = 0$

---

**Paso 1: Aplicar transformada**

$s^2Y - 0 - 0 + Y = 2e^{-\pi s}$

$Y(s^2 + 1) = 2e^{-\pi s}$

$$Y(s) = \frac{2e^{-\pi s}}{s^2 + 1}$$

---

**Paso 2: Identificar forma**

$$\mathcal{L}^{-1}\left\{\frac{1}{s^2+1}\right\} = \sin t$$

---

**Paso 3: Aplicar segunda traslación**

$$\mathcal{L}^{-1}\left\{e^{-\pi s} \cdot \frac{2}{s^2+1}\right\} = 2\sin(t-\pi)u(t-\pi)$$

---

**Paso 4: Simplificar**

$\sin(t - \pi) = -\sin t$

$$\boxed{y(t) = -2\sin(t)u(t-\pi) = \begin{cases} 0 & 0 \leq t < \pi \\ -2\sin t & t \geq \pi \end{cases}}$$

---

**Interpretación física:** El sistema está en reposo hasta $t = \pi$, cuando recibe un impulso que lo pone en movimiento.

---

## Método 9: Teorema de Convolución

### Cuándo Usar

- $F(s) = G(s) \cdot H(s)$ y es difícil [factorizar](../../../glossary.md#factorizar)
- Para resolver ecuaciones integro-diferenciales

### Fórmulas

**[Convolución](../../../glossary.md#convolución):**
$$(f * g)(t) = \int_0^t f(\tau)g(t-\tau)\,d\tau$$

**Teorema:**
$$\mathcal{L}\{f * g\} = F(s) \cdot G(s)$$

$$\mathcal{L}^{-1}\{F(s)G(s)\} = f * g$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Factorizar** | $F(s) = G(s) \cdot H(s)$ |
| 2 | **Invertir** | $g = \mathcal{L}^{-1}\{G\}$, $h = \mathcal{L}^{-1}\{H\}$ |
| 3 | **Calcular** | $(g * h)(t) = \int_0^t g(\tau)h(t-\tau)\,d\tau$ |

### Ejemplo Detallado

**Problema:** Encontrar $\mathcal{L}^{-1}\left\{\frac{1}{(s^2+1)^2}\right\}$

---

**Paso 1: Factorizar**

$$\frac{1}{(s^2+1)^2} = \frac{1}{s^2+1} \cdot \frac{1}{s^2+1}$$

$G(s) = H(s) = \frac{1}{s^2+1}$

---

**Paso 2: Invertir**

$g(t) = h(t) = \sin t$

---

**Paso 3: Calcular convolución**

$$f(t) = \int_0^t \sin\tau \sin(t-\tau)\,d\tau$$

Usando identidad: $\sin A \sin B = \frac{1}{2}[\cos(A-B) - \cos(A+B)]$

$$\sin\tau\sin(t-\tau) = \frac{1}{2}[\cos(2\tau - t) - \cos t]$$

$$f(t) = \frac{1}{2}\int_0^t [\cos(2\tau - t) - \cos t]\,d\tau$$

$$= \frac{1}{2}\left[\frac{\sin(2\tau - t)}{2} - \tau\cos t\right]_0^t$$

$$= \frac{1}{2}\left[\frac{\sin t}{2} - t\cos t - \frac{\sin(-t)}{2}\right]$$

$$= \frac{1}{2}\left[\frac{\sin t + \sin t}{2} - t\cos t\right]$$

$$= \frac{1}{2}[\sin t - t\cos t]$$

$$\boxed{f(t) = \frac{1}{2}(\sin t - t\cos t)}$$

---

## Método 10: Sistemas de EDO con Laplace

### Cuándo Usar

- Sistema de EDOs lineales acopladas
- Condiciones iniciales dadas

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Aplicar** $\mathcal{L}$ | A cada ecuación |
| 2 | **Formar sistema** | Algebraico en $X(s)$, $Y(s)$ |
| 3 | **Resolver** | Sistema lineal |
| 4 | **Invertir** | Cada transformada |

### Ejemplo Detallado

**Problema:** Resolver el sistema

$$\begin{cases} x' = 2x - 3y \\ y' = -2x + y \end{cases}, \quad x(0) = 8, \quad y(0) = 3$$

---

**Paso 1: Aplicar transformada**

$sX - 8 = 2X - 3Y$

$sY - 3 = -2X + Y$

---

**Paso 2: Reorganizar**

$(s-2)X + 3Y = 8$

$2X + (s-1)Y = 3$

---

**Paso 3: Resolver sistema** (Cramer)

$$\Delta = (s-2)(s-1) - 6 = s^2 - 3s + 2 - 6 = s^2 - 3s - 4 = (s-4)(s+1)$$

$$X = \frac{\begin{vmatrix} 8 & 3 \\ 3 & s-1 \end{vmatrix}}{(s-4)(s+1)} = \frac{8(s-1) - 9}{(s-4)(s+1)} = \frac{8s - 17}{(s-4)(s+1)}$$

$$Y = \frac{\begin{vmatrix} s-2 & 8 \\ 2 & 3 \end{vmatrix}}{(s-4)(s+1)} = \frac{3(s-2) - 16}{(s-4)(s+1)} = \frac{3s - 22}{(s-4)(s+1)}$$

---

**Paso 4: Fracciones parciales para** $X(s)$

$$\frac{8s-17}{(s-4)(s+1)} = \frac{A}{s-4} + \frac{B}{s+1}$$

$s = 4$: $15 = 5A \implies A = 3$

$s = -1$: $-25 = -5B \implies B = 5$

$$X(s) = \frac{3}{s-4} + \frac{5}{s+1}$$

$$x(t) = 3e^{4t} + 5e^{-t}$$

---

**Fracciones parciales para** $Y(s)$

$$\frac{3s-22}{(s-4)(s+1)} = \frac{C}{s-4} + \frac{D}{s+1}$$

$s = 4$: $-10 = 5C \implies C = -2$

$s = -1$: $-25 = -5D \implies D = 5$

$$Y(s) = \frac{-2}{s-4} + \frac{5}{s+1}$$

$$y(t) = -2e^{4t} + 5e^{-t}$$

---

**Solución:**

$$\boxed{\begin{cases} x(t) = 3e^{4t} + 5e^{-t} \\ y(t) = -2e^{4t} + 5e^{-t} \end{cases}}$$

---

**Verificación:** $x(0) = 3 + 5 = 8$ ✓, $y(0) = -2 + 5 = 3$ ✓

---

## Método 11: Derivada de la Transformada

### Cuándo Usar

- Transformadas de $t^n f(t)$
- Cuando aparece $t$ multiplicando una función conocida

### Fórmula

$$\mathcal{L}\{t^n f(t)\} = (-1)^n \frac{d^n F(s)}{ds^n}$$

**Caso $n=1$:**
$$\mathcal{L}\{tf(t)\} = -\frac{dF(s)}{ds}$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Identificar** | $f(t)$ sin el factor $t^n$ |
| 2 | **Transformar** | Encontrar $F(s)$ |
| 3 | **Derivar** | $n$ veces respecto a $s$ |
| 4 | **Multiplicar** | Por $(-1)^n$ |

### Ejemplo Detallado

**Problema:** Encontrar $\mathcal{L}\{t^2 e^{3t}\}$

---

**Método 1: Usando derivada**

**Paso 1:** $f(t) = e^{3t}$, $n = 2$

**Paso 2:** $F(s) = \frac{1}{s-3}$

**Paso 3:** 

$\frac{dF}{ds} = -\frac{1}{(s-3)^2}$

$\frac{d^2F}{ds^2} = \frac{2}{(s-3)^3}$

**Paso 4:**

$$\mathcal{L}\{t^2 e^{3t}\} = (-1)^2 \cdot \frac{2}{(s-3)^3} = \frac{2}{(s-3)^3}$$

---

**Método 2: Usando tabla directamente**

$$\mathcal{L}\{t^n e^{at}\} = \frac{n!}{(s-a)^{n+1}}$$

$$\mathcal{L}\{t^2 e^{3t}\} = \frac{2!}{(s-3)^3} = \frac{2}{(s-3)^3}$$

$$\boxed{\mathcal{L}\{t^2 e^{3t}\} = \frac{2}{(s-3)^3}}$$

---

## Método 12: Funciones Periódicas

### Cuándo Usar

- Funciones con período $T$: $f(t+T) = f(t)$
- Entradas oscilantes, ondas cuadradas, diente de sierra

### Fórmula

$$\mathcal{L}\{f(t)\} = \frac{1}{1 - e^{-sT}} \int_0^T e^{-st}f(t)\,dt$$

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|:----:|--------|---------|
| 1 | **Identificar período** | $T$ |
| 2 | **Definir** $f(t)$ | En un período $[0,T)$ |
| 3 | **Calcular integral** | $\int_0^T e^{-st}f(t)\,dt$ |
| 4 | **Aplicar fórmula** | Dividir por $(1 - e^{-sT})$ |

### Ejemplo Detallado

**Problema:** Encontrar la transformada de la onda cuadrada

$$f(t) = \begin{cases} 1 & 0 \leq t < 1 \\ 0 & 1 \leq t < 2 \end{cases}, \quad f(t+2) = f(t)$$

---

**Paso 1: Período**

$T = 2$

---

**Paso 2: Calcular integral**

$$\int_0^2 e^{-st}f(t)\,dt = \int_0^1 e^{-st}(1)\,dt + \int_1^2 e^{-st}(0)\,dt$$

$$= \left[-\frac{e^{-st}}{s}\right]_0^1 = -\frac{e^{-s}}{s} + \frac{1}{s} = \frac{1 - e^{-s}}{s}$$

---

**Paso 3: Aplicar fórmula**

$$\mathcal{L}\{f\} = \frac{1}{1-e^{-2s}} \cdot \frac{1-e^{-s}}{s}$$

$$= \frac{(1-e^{-s})}{s(1-e^{-s})(1+e^{-s})}$$

$$\boxed{= \frac{1}{s(1+e^{-s})}}$$

---

## Diagrama de Decisión

```
┌─────────────────────────────────────────────┐
│        ¿Qué tipo de problema?               │
└─────────────────────────────────────────────┘
                    │
    ┌───────────────┼───────────────┐
    ▼               ▼               ▼
Calcular 𝓛      Calcular 𝓛⁻¹    Resolver PVI
    │               │               │
    ▼               ▼               ▼
¿e^(at)·f?      ¿Racional?      Aplicar 𝓛
    │               │               │
    ▼               ▼               ▼
SÍ → 1ª trasl   SÍ → Fracc.     Sustituir
NO → ¿u(t-a)?   parciales       derivadas
    │               │               │
    ▼               ▼               ▼
SÍ → 2ª trasl   ¿Cuadrático     Despejar Y(s)
NO → Tabla      irreducible?         │
                    │               ▼
                    ▼           Fracciones
              SÍ → Completar    parciales
              cuadrado              │
                    │               ▼
                    ▼           Aplicar 𝓛⁻¹
              Identificar
              cos/sin amort.
```

---

## Tabla Resumen de Propiedades

| Propiedad | En $t$ | En $s$ |
|-----------|--------|--------|
| Linealidad | $af + bg$ | $aF + bG$ |
| 1ª Traslación | $e^{at}f(t)$ | $F(s-a)$ |
| 2ª Traslación | $f(t-a)u(t-a)$ | $e^{-as}F(s)$ |
| Derivada temporal | $f'(t)$ | $sF - f(0)$ |
| Derivada en $s$ | $tf(t)$ | $-F'(s)$ |
| Convolución | $(f*g)(t)$ | $F(s)G(s)$ |
| Integral | $\int_0^t f$ | $\frac{F(s)}{s}$ |

---

## Errores Comunes a Evitar

| Error | Consecuencia | Prevención |
|-------|--------------|------------|
| Olvidar condiciones iniciales | Término faltante | Siempre incluir $y(0)$, $y'(0)$ |
| Error en traslación | Signo incorrecto | $e^{at}$ → $s-a$; retardo → $e^{-as}$ |
| Fracciones parciales mal | Inversa incorrecta | Verificar expandiendo |
| No completar cuadrado | Forma no reconocible | Siempre intentar para denominador cuadrático |
| Convolución con [límites](../../../glossary.md#límites) | Integral mal planteada | Límites son $0$ a $t$ |

---

## Problemas de Práctica Sugeridos

1. **Transformada:** $\mathcal{L}\{e^{-2t}\sin 3t \cdot u(t-\pi)\}$

2. **Inversa:** $\mathcal{L}^{-1}\left\{\frac{s+1}{(s^2+2s+5)(s-1)}\right\}$

3. **PVI:** $y'' + 4y = \delta(t-2\pi)$, $y(0) = 1$, $y'(0) = 0$

4. **Sistema:** $x' = x + y$, $y' = 4x - 2y$, $x(0) = 1$, $y(0) = 0$

5. **Escalón:** $y' + 2y = f(t)$ donde $f(t) = t$ si $0 \leq t < 1$, $f(t) = 1$ si $t \geq 1$

6. **Convolución:** $\mathcal{L}^{-1}\left\{\frac{1}{s(s^2+4)}\right\}$

---

*Documento actualizado con formato expandido para estudio detallado.*
