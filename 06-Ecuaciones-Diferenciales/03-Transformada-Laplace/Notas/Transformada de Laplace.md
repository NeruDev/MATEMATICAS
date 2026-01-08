# 3. Transformada de Laplace

Basado en las fuentes proporcionadas, aquí presento la información más relevante sobre la **Transformada de Laplace**, estructurada según los subtemas solicitados.

### 3.1 Teoría preliminar

La transformada de Laplace es un tipo de **transformada integral**. Al igual que la diferenciación y la integración transforman una función en otra, una transformada integral cambia una función $f(t)$ en una función $F(s)$ mediante una integral definida. En este caso, el intervalo de integración es no acotado $[0, \infty)$,.

#### 3.1.1 Definición de la transformada de Laplace y Propiedades

*   **Definición:** Sea $f$ una función definida para $t \geq 0$. La integral
    $$ \mathcal{L}\{f(t)\} = \int_{0}^{\infty} e^{-st} f(t) \, dt $$
    se conoce como la **transformada de Laplace** de $f$, siempre y cuando la integral converja.
    *   La función $K(s, t) = e^{-st}$ se denomina el **núcleo** (o kernel) de la transformada.
    *   El resultado es una función de $s$. Generalmente se usa una letra minúscula para la función original y la correspondiente mayúscula para la transformada: $\mathcal{L}\{f(t)\} = F(s)$.

*   **Linealidad:** La transformada de Laplace es una **transformada lineal**. Esto significa que la transformada de una combinación lineal de funciones es la combinación lineal de las transformadas. Para constantes $\alpha$ y $\beta$:
    $$ \mathcal{L}\{\alpha f(t) + \beta g(t)\} = \alpha \mathcal{L}\{f(t)\} + \beta \mathcal{L}\{g(t)\} $$
    siempre que ambas integrales converjan,,.

*   **Transformadas Básicas (Teorema 4.1):** Se proporcionan transformadas para funciones elementales comunes:
    *   $\mathcal{L}\{1\} = \frac{1}{s}$
    *   $\mathcal{L}\{t^n\} = \frac{n!}{s^{n+1}}$, donde $n$ es un entero positivo.
    *   $\mathcal{L}\{e^{at}\} = \frac{1}{s-a}$
    *   $\mathcal{L}\{\text{sen } kt\} = \frac{k}{s^2 + k^2}$
    *   $\mathcal{L}\{\cos kt\} = \frac{s}{s^2 + k^2}$
    *   $\mathcal{L}\{\text{senh } kt\} = \frac{k}{s^2 - k^2}$
    *   $\mathcal{L}\{\cosh kt\} = \frac{s}{s^2 - k^2}$

#### 3.1.2 Condiciones suficientes de existencia para la transformada de una función

No todas las funciones poseen una transformada de Laplace (la integral definitoria podría diverger, como en el caso de $f(t) = e^{t^2}$),. Existen condiciones suficientes que garantizan su existencia:

1.  **Continuidad por tramos:** La función $f$ debe ser continua por tramos en el intervalo $[0, \infty)$. Esto significa que en cualquier intervalo finito $0 \leq a \leq t \leq b$, hay a lo sumo un número finito de puntos donde $f$ tiene discontinuidades finitas (no infinitas) y es continua en los intervalos abiertos entre ellos.

2.  **Orden Exponencial:** La función $f$ debe ser de **orden exponencial $c$**. Esto significa que existen constantes $c$, $M > 0$ y $T > 0$ tales que:
    $$ |f(t)| \leq Me^{ct} \quad \text{para todo } t > T $$
    En términos simples, esto indica que la gráfica de $f(t)$ no crece más rápido que la gráfica de una función exponencial $Me^{ct}$ cuando $t$ es muy grande.
    *   Ejemplos de funciones de orden exponencial incluyen $t^n$, $e^{-t}$ y $\cos t$,.
    *   La función $f(t) = e^{t^2}$ **no** es de orden exponencial, ya que crece más rápido que $e^{ct}$ para cualquier $c$.

*   **Teorema de Existencia (Teorema 4.2):** Si $f(t)$ es continua por tramos en $[0, \infty)$ y de orden exponencial $c$, entonces $\mathcal{L}\{f(t)\}$ existe para $s > c$.

*   **Comportamiento en el infinito (Teorema 4.5):** Una consecuencia importante de estas condiciones es el comportamiento de la transformada cuando $s$ tiende a infinito. Si $f$ cumple las condiciones de existencia, entonces:
    $$ \lim_{s \to \infty} F(s) = 0 $$
    Esto implica que funciones como $F(s) = 1$ o $F(s) = \frac{s}{s+1}$ no pueden ser transformadas de Laplace de funciones continuas por tramos de orden exponencial, ya que no tienden a cero cuando $s \to \infty$.

    Basado en las fuentes proporcionadas, aquí está la información relevante sobre la **Transformada Directa de Laplace**. Aunque el texto no utiliza el encabezado exacto "3.2 Transformada directa", este concepto se refiere al proceso de calcular la transformada $\mathcal{L}\{f(t)\}$ utilizando la definición integral y las propiedades básicas derivadas de ella.

### 3.2 Transformada Directa

La transformada directa consiste en convertir una función $f(t)$ (definida para $t \ge 0$) en una función $F(s)$ mediante el uso de una integral impropia o mediante el uso de tablas y propiedades de linealidad derivadas de dicha integral.

#### 3.2.1 Cálculo mediante la Definición Integral
La herramienta fundamental para calcular la transformada directa es la definición:
$$ \mathcal{L}\{f(t)\} = \int_{0}^{\infty} e^{-st} f(t) \, dt $$
Siempre que la integral converja, el resultado es una función de $s$, denotada generalmente como $F(s)$, $G(s)$, etc..
*   **El Núcleo:** La función $K(s, t) = e^{-st}$ se conoce como el núcleo o kernel de la transformada.
*   **Convergencia:** La integral existe (converge) si el límite $\lim_{b \to \infty} \int_{0}^{b} e^{-st} f(t) \, dt$ existe. Esto generalmente impone una restricción sobre la variable $s$ (por ejemplo, $s > 0$ o $s > a$),.

**Ejemplos de cálculo directo:**
1.  **Función constante $f(t) = 1$:**
    Al integrar $\int_{0}^{\infty} e^{-st}(1) dt$, se obtiene que $\mathcal{L}\{1\} = \frac{1}{s}$, siempre que $s > 0$,.
2.  **Función exponencial $f(t) = e^{3t}$:**
    Al integrar $\int_{0}^{\infty} e^{-st} e^{3t} dt = \int_{0}^{\infty} e^{-(s-3)t} dt$, el resultado es $\frac{1}{s-3}$, válido para $s > 3$.
3.  **Funciones trigonométricas:**
    Para $f(t) = \text{sen}(2t)$, se utiliza integración por partes dos veces sobre la definición integral, resultando en $\frac{2}{s^2 + 4}$,.

#### 3.2.2 Propiedad de Linealidad
La transformada de Laplace es una **transformación lineal**. Esto permite calcular la transformada directa de una suma de funciones sin necesidad de integrar todo el conjunto, sino transformando cada término individualmente y sumando los resultados.
*   **Propiedad:** $\mathcal{L}\{\alpha f(t) + \beta g(t)\} = \alpha \mathcal{L}\{f(t)\} + \beta \mathcal{L}\{g(t)\}$.
*   **Ejemplo:** Para calcular $\mathcal{L}\{1 + 5t\}$, se calcula $\mathcal{L}\{1\} + 5\mathcal{L}\{t\}$, resultando en $\frac{1}{s} + \frac{5}{s^2}$.

#### 3.2.3 Transformadas de Funciones Básicas (Teorema)
Como resultado de aplicar la transformada directa a funciones elementales, se obtiene una lista de transformadas estándar que suelen utilizarse para cálculos rápidos sin recurrir a la integración repetitiva:
*   $\mathcal{L}\{1\} = \frac{1}{s}$
*   $\mathcal{L}\{t^n\} = \frac{n!}{s^{n+1}}$, para $n = 1, 2, 3, \dots$
*   $\mathcal{L}\{e^{at}\} = \frac{1}{s-a}$
*   $\mathcal{L}\{\text{sen } kt\} = \frac{k}{s^2 + k^2}$
*   $\mathcal{L}\{\cos kt\} = \frac{s}{s^2 + k^2}$
*   $\mathcal{L}\{\text{senh } kt\} = \frac{k}{s^2 - k^2}$
*   $\mathcal{L}\{\cosh kt\} = \frac{s}{s^2 - k^2}$

#### 3.2.4 Transformada de funciones definidas por tramos
La definición integral permite calcular la transformada directa de funciones que cambian de fórmula en diferentes intervalos (funciones continuas por tramos).
*   **Método:** La integral $\int_{0}^{\infty}$ se divide en sumas de integrales sobre los intervalos donde la función está definida por diferentes fórmulas.
*   **Ejemplo:** Si $f(t) = 0$ para $0 \le t < 3$ y $f(t) = 2$ para $t \ge 3$, la transformada se calcula como:
    $\int_{0}^{3} e^{-st}(0) dt + \int_{3}^{\infty} e^{-st}(2) dt$, lo que resulta en $\frac{2e^{-3s}}{s}$.

Basado en las fuentes proporcionadas (específicamente la sección 4.2 del texto de Zill), aquí está la información relevante sobre la **Transformada Inversa de Laplace**.

### 3.3 Transformada inversa

El problema de la transformada inversa consiste en encontrar la función $f(t)$ cuando se conoce su transformada $F(s)$.

#### 3.3.1 Definición y Concepto
*   **El Problema Inverso:** Si $F(s)$ representa la transformada de Laplace de una función $f(t)$, es decir, $\mathcal{L}\{f(t)\} = F(s)$, entonces se dice que $f(t)$ es la **transformada de Laplace inversa** de $F(s)$.
*   **Notación:** Se escribe como $f(t) = \mathcal{L}^{-1}\{F(s)\}$.
*   **Unicidad:** Aunque la transformada inversa podría no ser única (funciones que difieren solo en puntos aislados tienen la misma transformada), para fines de aplicaciones en ecuaciones diferenciales, si $f_1$ y $f_2$ son continuas en $[0, \infty)$ y tienen la misma transformada, entonces $f_1 = f_2$ en el intervalo, por lo que tratamos la inversa como esencialmente única,.

#### 3.3.2 Propiedad de Linealidad
Al igual que la transformada directa, la transformada inversa de Laplace es una **transformación lineal**.
*   **Propiedad:** Para constantes $\alpha$ y $\beta$:
    $$ \mathcal{L}^{-1}\{\alpha F(s) + \beta G(s)\} = \alpha \mathcal{L}^{-1}\{F(s)\} + \beta \mathcal{L}^{-1}\{G(s)\} $$
    donde $F$ y $G$ son las transformadas de las funciones $f$ y $g$.
*   **Aplicación:** Esto permite descomponer una expresión compleja en una suma de expresiones más simples, calcular la inversa de cada término por separado y luego sumar los resultados.

#### 3.3.3 Transformadas Inversas Básicas (Teorema 4.3)
Se proporciona una lista de transformadas inversas fundamentales derivadas directamente de las transformadas básicas:
*   $\mathcal{L}^{-1}\{\frac{1}{s}\} = 1$
*   $\mathcal{L}^{-1}\{\frac{n!}{s^{n+1}}\} = t^n$, para $n = 1, 2, 3, \dots$
*   $\mathcal{L}^{-1}\{\frac{1}{s-a}\} = e^{at}$
*   $\mathcal{L}^{-1}\{\frac{k}{s^2 + k^2}\} = \sen kt$
*   $\mathcal{L}^{-1}\{\frac{s}{s^2 + k^2}\} = \cos kt$
*   $\mathcal{L}^{-1}\{\frac{k}{s^2 - k^2}\} = \senh kt$
*   $\mathcal{L}^{-1}\{\frac{s}{s^2 - k^2}\} = \cosh kt$

**Ajuste de constantes:** A menudo, la función de $s$ no coincide exactamente con la forma de la tabla. Puede ser necesario multiplicar y dividir por una constante apropiada para ajustar la expresión a las formas estándar (por ejemplo, completar un $k$ faltante en el numerador para un seno),.

#### 3.3.4 Uso de Fracciones Parciales
Las fracciones parciales juegan un papel crucial cuando $F(s)$ es una función racional (cociente de polinomios) que no aparece directamente en las tablas básicas.
*   **Objetivo:** Descomponer una expresión racional compleja en una suma de fracciones más simples cuyos denominadores son factores lineales o cuadráticos, las cuales sí se pueden transformar inversamente usando la linealidad y la tabla básica.
*   **Casos comunes:**
    1.  **Factores lineales distintos:** Si el denominador se descompone en factores distintos $(s-a)(s-b)\dots$, se separa en sumas de la forma $A/(s-a) + B/(s-b)$,.
    2.  **Factores lineales repetidos:** Si aparece $(s-a)^n$, la descomposición incluye términos con potencias desde 1 hasta $n$: $\frac{A}{s-a} + \frac{B}{(s-a)^2} + \dots$.
    3.  **Factores cuadráticos (Completar el cuadrado):** Si el denominador contiene un polinomio cuadrático $s^2 + bs + c$ que no tiene raíces reales, se debe completar el cuadrado para llevarlo a la forma $(s+a)^2 + k^2$. Esto permite usar los teoremas de traslación (que se verán más adelante) o ajustar a formas de seno y coseno desplazadas,.

    Basado en las fuentes proporcionadas (específicamente la sección 4.3.2 del texto de Zill), aquí está la información relevante sobre la **Función Escalón Unitario** en el contexto de la Transformada de Laplace.

### 3.4 Función escalón unitario (Función de Heaviside)

#### 3.4.1 Definición y Propiedades Básicas
*   **Definición:** La función escalón unitario, denotada como $\mathcal{U}(t - a)$, se define como:
    $$ \mathcal{U}(t - a) = \begin{cases} 0, & 0 \le t < a \\ 1, & t \ge a \end{cases} $$
    Donde $a \ge 0$. En un sentido más amplio, es cero para $t < a$,.
*   **Propósito:** Esta función es útil en ingeniería para modelar situaciones donde una función está en estado "inactivo" y luego pasa a estado "activo" (como un interruptor de voltaje o una fuerza externa que se aplica repentinamente).
*   **Efecto de "desactivación":** Cuando una función $f(t)$ se multiplica por $\mathcal{U}(t - a)$, la función se "desactiva" (es cero) para el intervalo $0 \le t < a$ y se "activa" (toma el valor de la función) para $t \ge a$.

#### 3.4.2 Representación de funciones definidas por tramos
La función escalón unitario permite escribir funciones definidas por tramos en una forma compacta:
*   Una función general definida por tramos del tipo:
    $$ f(t) = \begin{cases} g(t), & 0 \le t < a \\ h(t), & t \ge a \end{cases} $$
    se puede escribir como $f(t) = g(t) - g(t)\mathcal{U}(t - a) + h(t)\mathcal{U}(t - a)$.
*   De manera similar, una función que es cero en todas partes excepto en un intervalo $(a, b)$ se puede escribir como $f(t) = g(t)[\mathcal{U}(t - a) - \mathcal{U}(t - b)]$.

#### 3.4.3 Segundo Teorema de Traslación (Traslación en el eje t)
Este teorema conecta la función escalón unitario en el dominio del tiempo con la función exponencial en el dominio de la frecuencia ($s$).

*   **Teorema Directo:** Si $F(s) = \mathcal{L}\{f(t)\}$ y $a > 0$, entonces:
    $$ \mathcal{L}\{f(t - a)\mathcal{U}(t - a)\} = e^{-as}F(s) $$
    Esto significa que multiplicar la transformada $F(s)$ por $e^{-as}$ corresponde a desplazar la función $f(t)$ una distancia $a$ a lo largo del eje $t$.

*   **Transformada de la función escalón unitario:** Como caso especial (donde $f(t)=1$), la transformada de la función escalón por sí misma es:
    $$ \mathcal{L}\{\mathcal{U}(t - a)\} = \frac{e^{-as}}{s} $$
   .

*   **Forma Inversa:** Para calcular la transformada inversa de una función que contiene un factor exponencial $e^{-as}$:
    $$ \mathcal{L}^{-1}\{e^{-as}F(s)\} = f(t - a)\mathcal{U}(t - a) $$
    donde $f(t) = \mathcal{L}^{-1}\{F(s)\}$.

*   **Forma Alternativa del Teorema:** A menudo se necesita transformar el producto de una función $g(t)$ y una función escalón $\mathcal{U}(t - a)$ donde $g(t)$ no está desplazada (no tiene la forma $f(t-a)$). En este caso, se utiliza la fórmula:
    $$ \mathcal{L}\{g(t)\mathcal{U}(t - a)\} = e^{-as}\mathcal{L}\{g(t + a)\} $$
    Esto evita tener que manipular algebraicamente la función para forzar la forma desplazada,.

### 3.5 Teoremas de Traslación

Basado en las fuentes proporcionadas (específicamente la sección 4.3 del texto de Zill), aquí está la información relevante sobre los **Teoremas de Traslación** dentro de la Transformada de Laplace.

Estos teoremas permiten calcular transformadas y transformadas inversas de funciones más complejas sin tener que recurrir siempre a la definición integral básica.

### 3.5.1 Primer Teorema de Traslación (Traslación en el eje s)

Este teorema es útil para evaluar la transformada de una función $f(t)$ multiplicada por una función exponencial $e^{at}$.

*   **El Teorema:** Si se conoce que $\mathcal{L}\{f(t)\} = F(s)$, entonces la transformada de Laplace de $e^{at}f(t)$ es simplemente la transformada $F(s)$ desplazada o trasladada a $F(s - a)$.
    *   **Fórmula:** $\mathcal{L}\{e^{at}f(t)\} = F(s - a)$.
    *   **Interpretación:** Si $s$ se considera una variable real, la gráfica de $F(s - a)$ es la gráfica de $F(s)$ desplazada sobre el eje $s$ por la cantidad $|a|$.

*   **Forma Inversa:** Para calcular la transformada inversa de una función $F(s - a)$, se debe reconocer $F(s)$, encontrar su inversa $f(t)$ y luego multiplicarla por $e^{at}$.
    *   **Fórmula:** $\mathcal{L}^{-1}\{F(s - a)\} = e^{at}f(t)$, donde $f(t) = \mathcal{L}^{-1}\{F(s)\}$.
    *   **Aplicación práctica:** A menudo se utiliza completando el cuadrado en el denominador si este es un polinomio cuadrático que no tiene factores reales, para llevarlo a una forma $F(s-a)$ reconocible (por ejemplo, frecuencias desplazadas de seno o coseno).

### 3.5.2 Segundo Teorema de Traslación (Traslación en el eje t)

Este teorema trata con funciones que se "activan" o "desactivan" en un tiempo determinado, generalmente involucrando la **función escalón unitario** $\mathcal{U}(t - a)$.

*   **El Teorema:** Si $F(s) = \mathcal{L}\{f(t)\}$ y $a > 0$, entonces la transformada de la función desplazada $f(t - a)$ multiplicada por el escalón unitario es igual a la transformada original multiplicada por una exponencial en $s$.
    *   **Fórmula:** $\mathcal{L}\{f(t - a)\mathcal{U}(t - a)\} = e^{-as}F(s)$.
    *   **Interpretación:** La presencia del factor $e^{-as}$ en el dominio de $s$ corresponde a un desplazamiento de la función a lo largo del eje $t$ una distancia $a$ hacia la derecha.

*   **Forma Inversa:** Si se tiene una transformada que contiene un factor $e^{-as}$, su inversa será una función desplazada en el tiempo multiplicada por la función escalón.
    *   **Fórmula:** $\mathcal{L}^{-1}\{e^{-as}F(s)\} = f(t - a)\mathcal{U}(t - a)$.

*   **Forma Alternativa:** Frecuentemente se necesita transformar un producto $g(t)\mathcal{U}(t - a)$ donde $g(t)$ no está escrita como $f(t-a)$. Para evitar manipulaciones algebraicas complicadas, se puede usar la forma alternativa:
    *   **Fórmula:** $\mathcal{L}\{g(t)\mathcal{U}(t - a)\} = e^{-as}\mathcal{L}\{g(t + a)\}$.

Basado en las fuentes proporcionadas (Capítulo 4.4 y Apéndice III del texto de Zill), aquí está la información relevante respecto a la transformada de funciones multiplicadas por $t^n$ y divididas entre $t$.

### 3.6 Transformada de funciones multiplicadas por $t^n$

Esta propiedad se conoce como **Derivadas de una Transformada**. La transformada de Laplace del producto de una función $f(t)$ con $t^n$ se puede encontrar diferenciando la transformada de Laplace de $f(t)$.

*   **Fundamento:** Si $F(s) = \mathcal{L}\{f(t)\}$, entonces la derivación de la transformada con respecto a $s$ corresponde a la multiplicación por $-t$ en el dominio del tiempo:
    $$ \frac{d}{ds}F(s) = -\mathcal{L}\{t f(t)\} $$
    o equivalentemente $\mathcal{L}\{t f(t)\} = -\frac{d}{ds}F(s)$,.

*   **Teorema General (Teorema 4.8 / 7.4.1):** Si $F(s) = \mathcal{L}\{f(t)\}$ y $n = 1, 2, 3, \dots$, entonces:
    $$ \mathcal{L}\{t^n f(t)\} = (-1)^n \frac{d^n}{ds^n} F(s) $$
    Esto indica que multiplicar una función por $t^n$ resulta en la $n$-ésima derivada de su transformada, multiplicada por $(-1)^n$,.

*   **Ejemplos de aplicación:**
    *   $\mathcal{L}\{t \text{ sen } kt\} = -\frac{d}{ds} \left[ \frac{k}{s^2 + k^2} \right] = \frac{2ks}{(s^2 + k^2)^2}$,.
    *   $\mathcal{L}\{t e^{3t}\} = -\frac{d}{ds} \left[ \frac{1}{s-3} \right] = \frac{1}{(s-3)^2}$.

### Transformada de funciones divididas entre $t$

Aunque el texto principal de las secciones provistas se enfoca en las derivadas de transformadas (multiplicación por $t$) y transformadas de integrales (convolución), la **Tabla de Transformadas de Laplace (Apéndice III)** proporciona fórmulas explícitas para funciones divididas entre $t$. Estas transformadas generalmente resultan en funciones logarítmicas o trigonométricas inversas en el dominio $s$.

Ejemplos específicos extraídos de la tabla incluyen:

*   **Exponenciales divididas por $t$:**
    $$ \mathcal{L}\left\{ \frac{e^{bt} - e^{at}}{t} \right\} = \ln \frac{s-a}{s-b} $$
   ,.

*   **Funciones trigonométricas divididas por $t$:**
    *   $\mathcal{L}\left\{ \frac{1 - \cos kt}{t} \right\} = \ln \sqrt{\frac{s^2 + k^2}{s^2}}$.
    *   $\mathcal{L}\left\{ \frac{\text{sen } at}{t} \right\} = \arctan \left(\frac{a}{s}\right)$,.
    *   $\mathcal{L}\left\{ \frac{\text{sen } at \cos bt}{t} \right\} = \frac{1}{2} \arctan \frac{a+b}{s} + \frac{1}{2} \arctan \frac{a-b}{s}$.

*   **Funciones hiperbólicas divididas por $t$:**
    *   $\mathcal{L}\left\{ \frac{1 - \cosh at}{t} \right\} = \ln \sqrt{\frac{s^2 - a^2}{s^2}}$.
    *   $\mathcal{L}\left\{ \frac{\text{senh } at}{t} \right\} = \frac{1}{2} \ln \frac{s+a}{s-a}$.

**Nota sobre la relación inversa:** El texto sugiere en los ejercicios que para encontrar la transformada inversa de funciones que involucran logaritmos (como $\ln s$), se puede utilizar el teorema de la derivada de la transformada a la inversa. Es decir, derivar $F(s)$ para eliminar el logaritmo, encontrar la inversa de la derivada y luego relacionarla con $-t f(t)$,.

### 3.7 Transformada de una derivada y derivada de una transformada. 

Basado en el texto de "Ecuaciones diferenciales con aplicaciones de modelado" de Zill (Secciones 4.2.2 y 4.4.1), aquí está la información relevante sobre la **Transformada de una derivada** y la **Derivada de una transformada**.

Es fundamental distinguir entre ambas operaciones: la primera se utiliza para transformar las derivadas de una función en el dominio $t$ (útil para resolver ecuaciones diferenciales), mientras que la segunda se utiliza para encontrar la transformada de una función multiplicada por potencias de $t$.

### 3.7.1 Transformada de una derivada

Esta propiedad es la herramienta principal que permite utilizar la transformada de Laplace para resolver ecuaciones diferenciales lineales con coeficientes constantes, ya que convierte la diferenciación con respecto a $t$ en una multiplicación algebraica por $s$.

*   **Propósito:** Evaluar cantidades como $\mathcal{L}\{dy/dt\}$ y $\mathcal{L}\{d^2y/dt^2\}$ en términos de $Y(s)$ y las condiciones iniciales.
*   **Fórmulas Específicas:**
    *   Para la **primera derivada**:
        $$ \mathcal{L}\{f'(t)\} = sF(s) - f(0) $$
        donde $F(s) = \mathcal{L}\{f(t)\}$.
    *   Para la **segunda derivada**:
        $$ \mathcal{L}\{f''(t)\} = s^2F(s) - sf(0) - f'(0) $$.
*   **Teorema General (Transformada de la n-ésima derivada):**
    Si $f, f', \dots, f^{(n-1)}$ son continuas y de orden exponencial, y $f^{(n)}(t)$ es continua por tramos:
    $$ \mathcal{L}\{f^{(n)}(t)\} = s^n F(s) - s^{n-1}f(0) - s^{n-2}f'(0) - \dots - f^{(n-1)}(0) $$
    Esta fórmula muestra que la transformada de la derivada $n$-ésima depende de $F(s)$ y de las $n-1$ derivadas de $f(t)$ evaluadas en $t=0$.

*   **Aplicación en Ecuaciones Diferenciales:**
    Esta propiedad permite transformar una ecuación diferencial lineal de coeficientes constantes en una **ecuación algebraica** en términos de $Y(s)$. El método incorpora automáticamente las condiciones iniciales prescritas (como $y(0), y'(0)$, etc.) directamente en la solución, evitando la necesidad de encontrar una solución general y luego aplicar las constantes,,.

### 3.7.2 Derivada de una transformada

Esta propiedad opera a la inversa: relaciona la diferenciación en el dominio de la frecuencia ($s$) con la multiplicación por $t$ en el dominio del tiempo ($t$).

*   **Propósito:** Encontrar la transformada de Laplace de una función $f(t)$ que está multiplicada por un monomio $t^n$.
*   **Teorema (Derivadas de transformadas):**
    Si $F(s) = \mathcal{L}\{f(t)\}$ y $n = 1, 2, 3, \dots$, entonces:
    $$ \mathcal{L}\{t^n f(t)\} = (-1)^n \frac{d^n}{ds^n} F(s) $$
    Esto indica que multiplicar una función $f(t)$ por $t^n$ es equivalente a derivar su transformada $F(s)$, $n$ veces con respecto a $s$, y multiplicar por $(-1)^n$.

*   **Ejemplos de Aplicación:**
    *   Para evaluar $\mathcal{L}\{t \text{ sen } kt\}$, se toma la derivada negativa de la transformada del seno:
        $$ \mathcal{L}\{t \text{ sen } kt\} = -\frac{d}{ds} \left[ \frac{k}{s^2 + k^2} \right] = \frac{2ks}{(s^2 + k^2)^2} $$.
    *   Para $\mathcal{L}\{t^2 f(t)\}$, se calcula la segunda derivada de la transformada de $f(t)$.

### 3.8 Teorema de convolución. 

Basado en las fuentes proporcionadas (sección 4.4.2 del texto de Zill), aquí está la información relevante sobre el **Teorema de Convolución** dentro de la Transformada de Laplace.

### 3.8 Teorema de Convolución

Este teorema proporciona una herramienta poderosa para encontrar la transformada de Laplace de un tipo especial de integral conocida como **convolución**, y es especialmente útil para calcular transformadas inversas de productos de funciones en el dominio $s$.

#### 3.8.1 Definición de Convolución
Si las funciones $f$ y $g$ son continuas por tramos en el intervalo $[0, \infty)$, la convolución de $f$ y $g$, denotada por $f * g$, se define mediante la integral:
$$ f * g = \int_{0}^{t} f(\tau)g(t - \tau) \, d\tau $$
El resultado de esta operación es una función de $t$.

*   **Propiedad Conmutativa:** La convolución es conmutativa, lo que significa que $f * g = g * f$. Esto implica que no importa el orden en que se coloquen las funciones dentro de la integral: $\int_{0}^{t} f(\tau)g(t - \tau) \, d\tau = \int_{0}^{t} f(t - \tau)g(\tau) \, d\tau$.

#### 3.8.2 El Teorema de Convolución (Teorema 4.9)
Aunque la integral del producto de dos funciones no es el producto de las integrales, la transformada de Laplace de la convolución sí corresponde al producto de las transformadas individuales.

*   **Teorema:** Si $f(t)$ y $g(t)$ son continuas por tramos en $[0, \infty)$ y de orden exponencial, entonces:
    $$ \mathcal{L}\{f * g\} = \mathcal{L}\{f(t)\} \mathcal{L}\{g(t)\} = F(s)G(s) $$
    Esto permite encontrar la transformada de la integral de convolución sin necesidad de evaluar la integral primero.

#### 3.8.3 Forma Inversa del Teorema
El teorema es particularmente útil para encontrar la **transformada inversa de Laplace** cuando $F(s)$ es un producto de dos transformadas conocidas $F(s)$ y $G(s)$.

*   **Fórmula Inversa:**
    $$ \mathcal{L}^{-1}\{F(s)G(s)\} = f * g $$
    Esto significa que para encontrar la inversa de un producto, se identifican $f(t)$ y $g(t)$ y se calcula su convolución.

#### 3.8.4 Aplicaciones Derivadas del Teorema
1.  **Transformada de una Integral:** Como caso especial, si se elige $g(t) = 1$ (cuya transformada es $G(s) = 1/s$), el teorema de convolución implica que la transformada de la integral de una función es la transformada de la función dividida por $s$:
    $$ \mathcal{L}\left\{ \int_{0}^{t} f(\tau) \, d\tau \right\} = \frac{F(s)}{s} $$
    Inversamente, $\mathcal{L}^{-1}\{F(s)/s\} = \int_{0}^{t} f(\tau) \, d\tau$,.

2.  **Ecuación Integral de Volterra:** El teorema permite resolver ecuaciones integrales donde la función desconocida aparece dentro de una integral de convolución, de la forma:
    $$ f(t) = g(t) + \int_{0}^{t} f(\tau)h(t - \tau) \, d\tau $$
    Al aplicar la transformada de Laplace, la integral se convierte en un producto $F(s)H(s)$, permitiendo despejar $F(s)$ algebraicamente y luego encontrar $f(t)$ mediante la inversa.

    Basado en las fuentes proporcionadas (específicamente la sección 4.4.2 del texto de Zill), aquí está la información relevante sobre la **Transformada de una integral**.

### 3.9 Transformada de una integral

Esta propiedad operacional es una consecuencia directa del teorema de convolución y establece una relación fundamental: la integración en el dominio del tiempo corresponde a la división por $s$ en el dominio de la frecuencia,.

#### Teorema y Fórmula
Si $f(t)$ es una función continua por tramos para $t \ge 0$ y de orden exponencial, y su transformada es $F(s)$, entonces la transformada de Laplace de la integral de $f$ es:
$$ \mathcal{L}\left\{ \int_{0}^{t} f(\tau) \, d\tau \right\} = \frac{F(s)}{s} $$
Esto demuestra que la operación de integración se convierte en una operación algebraica simple (división) en el dominio $s$.

#### Deducción mediante Convolución
Este resultado es un caso especial del **teorema de convolución**. Si se considera la función $g(t) = 1$, cuya transformada es $G(s) = 1/s$, la convolución de $f(t)$ con $1$ es precisamente la integral de $f$:
$$ f * 1 = \int_{0}^{t} f(\tau) \cdot 1 \, d\tau = \int_{0}^{t} f(\tau) \, d\tau $$
Por lo tanto, la transformada del producto de convolución es el producto de las transformadas: $F(s) \cdot \frac{1}{s}$.

#### Forma Inversa y Utilidad
La forma inversa de este teorema es extremadamente útil para calcular transformadas inversas cuando la función $F(s)$ tiene un factor $s$ en el denominador. Permite eliminar la $s$, encontrar la inversa del resto de la expresión y luego integrar el resultado:
$$ \mathcal{L}^{-1}\left\{ \frac{F(s)}{s} \right\} = \int_{0}^{t} f(\tau) \, d\tau = \int_{0}^{t} \mathcal{L}^{-1}\{F(s)\} \, d\tau $$
Por ejemplo, para hallar $\mathcal{L}^{-1}\{ \frac{1}{s(s^2 + 1)} \}$, se puede identificar $F(s) = \frac{1}{s^2 + 1}$ (cuya inversa es $\text{sen } t$) y simplemente integrar $\int_{0}^{t} \text{sen } \tau \, d\tau$ para obtener $1 - \cos t$,.

#### Aplicación: Ecuaciones Integrodiferenciales
Esta propiedad permite utilizar la transformada de Laplace para resolver **ecuaciones integrodiferenciales**, que son ecuaciones que contienen tanto derivadas como integrales de la función incógnita.
*   **Ejemplo Físico:** En un circuito eléctrico en serie con un inductor, un resistor y un capacitor, la ecuación que gobierna la corriente $i(t)$ puede escribirse como:
    $$ L \frac{di}{dt} + Ri(t) + \frac{1}{C} \int_{0}^{t} i(\tau) \, d\tau = E(t) $$
    Al aplicar la transformada, el término integral se convierte en $\frac{I(s)}{s \cdot C}$, lo que convierte toda la ecuación diferencial e integral en una ecuación algebraica que se puede despejar para $I(s)$,.

Basado en las fuentes proporcionadas (sección 4.4.3 del texto de Zill), aquí está la información relevante sobre la **Transformada de una función periódica**.

### 3.10 Transformada de una función periódica

Este teorema permite calcular la transformada de Laplace de una función que se repite a intervalos regulares sin necesidad de integrar hasta el infinito, reduciendo el problema a una integración sobre un solo periodo.

#### 3.10.1 Definición y Teorema
*   **Función Periódica:** Si una función $f(t)$ satisface $f(t + T) = f(t)$ para todo $t \ge 0$, donde $T > 0$, se dice que es periódica con periodo $T$,.
*   **Teorema (Transformada de una función periódica):** Si $f(t)$ es continua por tramos en $[0, \infty)$, de orden exponencial y periódica con periodo $T$, entonces su transformada de Laplace es:
    $$ \mathcal{L}\{f(t)\} = \frac{1}{1 - e^{-sT}} \int_{0}^{T} e^{-st} f(t) \, dt $$
    Esta fórmula demuestra que la transformada se obtiene integrando la función sobre el primer periodo ($0$ a $T$) y dividiendo el resultado por $1 - e^{-sT}$,.

#### 3.10.2 Fundamento del Teorema
La demostración se basa en dividir la integral impropia de definición $\int_{0}^{\infty}$ en dos partes: una de $0$ a $T$ y otra de $T$ a $\infty$. Mediante un cambio de variable ($t = u + T$) y usando la propiedad de periodicidad $f(u + T) = f(u)$, la segunda integral se convierte en $e^{-sT}\mathcal{L}\{f(t)\}$. Al despejar $\mathcal{L}\{f(t)\}$ de la ecuación resultante, se obtiene la fórmula del teorema,.

#### 3.10.3 Ejemplos de Aplicación
Esta propiedad es fundamental para analizar fenómenos con entradas repetitivas, como ondas cuadradas, dientes de sierra u ondas rectificadas en circuitos eléctricos.

*   **Onda Cuadrada:** Para una función $E(t)$ con periodo $T=2$, definida como $1$ en $[0, 1)$ y $0$ en $[1, 2)$, la transformada se calcula integrando solo de 0 a 2.
    $$ \mathcal{L}\{E(t)\} = \frac{1}{1 - e^{-2s}} \left[ \int_{0}^{1} e^{-st}(1) \, dt + \int_{1}^{2} e^{-st}(0) \, dt \right] $$
    El resultado simplificado es $\frac{1}{s(1 + e^{-s})}$,.

*   **Circuitos Eléctricos:** Esta transformada permite resolver ecuaciones diferenciales de circuitos (como un circuito LR) sometidos a voltajes periódicos de entrada (como la onda cuadrada mencionada), permitiendo encontrar la corriente $i(t)$ mediante la transformada inversa,.

Basado en las fuentes proporcionadas (sección 4.5 del texto de Zill), aquí está la información relevante sobre la **Transformada de la función delta de Dirac**.

### 3.11 Transformada de la función delta de Dirac

Este tema aborda el modelado matemático de fuerzas externas de gran magnitud que actúan durante un intervalo de tiempo muy corto (impulso unitario), como un golpe de martillo en un sistema mecánico o un relámpago en un circuito eléctrico.

#### 3.11.1 Definición y Concepto
*   **Impulso Unitario:** Se comienza definiendo una función $\delta_a(t - t_0)$ que vale $1/2a$ en un intervalo pequeño alrededor de $t_0$ y 0 fuera de él. El área bajo esta curva es siempre 1.
*   **Función Delta de Dirac:** Se define mediante el límite cuando el intervalo de tiempo se hace infinitamente pequeño ($a \to 0$). Se denota como $\delta(t - t_0)$.
*   **Propiedades:** Esta "función" (que matemáticamente es una distribución o función generalizada) se caracteriza por dos propiedades fundamentales:
    1.  $\delta(t - t_0) = \begin{cases} \infty, & t = t_0 \\ 0, & t \neq t_0 \end{cases}$
    2.  $\int_{0}^{\infty} \delta(t - t_0) \, dt = 1$

#### 3.11.2 La Transformada de Laplace (Teorema 4.11)
La transformada de Laplace de la función delta de Dirac se obtiene formalmente tomando el límite de la transformada del impulso unitario.
*   **Fórmula General:** Para $t_0 > 0$:
    $$ \mathcal{L}\{\delta(t - t_0)\} = e^{-st_0} $$
    Esto se demuestra utilizando la función escalón unitario y la regla de L'Hôpital.
*   **Caso Especial:** Cuando $t_0 = 0$, la transformada es simplemente:
    $$ \mathcal{L}\{\delta(t)\} = 1 $$
    Este resultado es notable porque $\delta(t)$ no es una función de orden exponencial usual (cuya transformada tendería a 0 cuando $s \to \infty$).

#### 3.11.3 Propiedad de Tamizado (Sifting Property)
La función delta de Dirac tiene la capacidad de "filtrar" o seleccionar el valor de una función en un punto específico. Si $f(t)$ es una función continua, entonces:
$$ \int_{0}^{\infty} f(t)\delta(t - t_0) \, dt = f(t_0) $$
Esta propiedad es fundamental para entender cómo actúa la función delta sobre otras funciones dentro de una integral.

#### 3.11.4 Aplicación en Ecuaciones Diferenciales
La función delta se utiliza para resolver problemas de valor inicial donde el sistema recibe un "golpe" o impulso repentino.
*   **Ejemplo:** En un sistema masa-resorte modelado por $y'' + y = 4\delta(t - 2\pi)$, el término $\delta$ indica que el sistema recibe un impacto fuerte en el tiempo $t = 2\pi$. La solución muestra que el sistema puede cambiar de comportamiento (por ejemplo, aumentar la amplitud de vibración) instantáneamente en el momento del impacto.
*   **Función de Peso:** En sistemas lineales, la transformada inversa de la función de transferencia, $w(t) = \mathcal{L}^{-1}\{1/P(s)\}$, se conoce como la **respuesta al impulso** del sistema, ya que corresponde a la respuesta del sistema cuando la entrada es un impulso unitario $\delta(t)$.

Basado en el texto "Ecuaciones diferenciales con aplicaciones de modelado" de Zill, la sección de aplicaciones de la Transformada de Laplace (que corresponde a partes de los capítulos 4, 7 y 13 en el texto fuente) destaca por su utilidad para resolver problemas de valor inicial lineales, especialmente aquellos con entradas discontinuas o impulsivas.

Aquí está la información relevante sobre las aplicaciones:

### 3.12 Aplicaciones de la Transformada de Laplace

La transformada de Laplace se utiliza principalmente para transformar ecuaciones diferenciales (ordinarias y parciales) en ecuaciones algebraicas, lo que facilita su resolución, especialmente en sistemas físicos.

#### 3.12.1 Circuitos Eléctricos (Redes)
La transformada es una herramienta estándar para analizar circuitos en serie y redes complejas, particularmente cuando los voltajes de entrada son funciones complejas (como ondas cuadradas o dientes de sierra).
*   **Circuitos LRC en serie:** La ecuación que modela la carga $q(t)$ o la corriente $i(t)$ en un circuito con inductor, resistor y capacitor es una ecuación integrodiferencial:
    $$ L \frac{di}{dt} + Ri(t) + \frac{1}{C} \int_{0}^{t} i(\tau) \, d\tau = E(t) $$
    Al aplicar la transformada, la integral se convierte en una división por $s$, permitiendo despejar la corriente transformada $I(s)$ algebraicamente.
*   **Redes Acopladas:** Se utiliza para resolver sistemas de ecuaciones diferenciales lineales que surgen de aplicar las leyes de Kirchhoff a redes con múltiples mallas. El proceso convierte el sistema de ecuaciones diferenciales en un sistema de ecuaciones lineales algebraicas en el dominio $s$, que luego se resuelven para aplicar la transformada inversa,.

#### 3.12.2 Sistemas Mecánicos (Resorte-Masa)
Se utiliza para modelar vibraciones mecánicas, tanto en sistemas simples como acoplados.
*   **Resortes Acoplados:** El movimiento de dos masas unidas por resortes (sistema acoplado) se modela mediante un sistema de ecuaciones diferenciales de segundo orden:
    $$ m_1 x''_1 = -k_1 x_1 + k_2(x_2 - x_1) $$
    $$ m_2 x''_2 = -k_2(x_2 - x_1) $$
    La transformada de Laplace permite resolver estas ecuaciones simultáneamente para encontrar las posiciones $x_1(t)$ y $x_2(t)$.
*   **Fuerzas Impulsivas:** La función **delta de Dirac** se aplica para modelar fuerzas externas de gran magnitud que actúan en un intervalo de tiempo muy corto, como un golpe de martillo sobre una masa en un resorte. Esto permite analizar la respuesta del sistema ante impactos repentinos,.
*   **Péndulo Doble:** Para desplazamientos pequeños, el sistema no lineal de un péndulo doble se linealiza y se resuelve utilizando la transformada de Laplace,.

#### 3.12.3 Deflexión de Vigas
La transformada de Laplace es útil para determinar la deflexión estática $y(x)$ de una viga uniforme bajo cargas transversales.
*   La ecuación gobernante es de cuarto orden: $EI \frac{d^4y}{dx^4} = w(x)$.
*   La ventaja principal de usar Laplace aquí es cuando la carga $w(x)$ es **discontinua** o está definida por tramos. El uso de la función escalón unitario en la transformada permite manejar cargas que se "activan" o "desactivan" a lo largo de la viga sin tener que resolver la ecuación por secciones separadas y empalmar las constantes de integración,.

#### 3.12.4 Ecuaciones Diferenciales Parciales (Problemas de Valor en la Frontera)
La transformada de Laplace es una técnica poderosa para resolver problemas de valores en la frontera que involucran ecuaciones diferenciales parciales lineales con coeficientes constantes, particularmente cuando una de las variables representa el tiempo y el dominio es no acotado (semi-infinito).
*   **Ecuación de Calor:** Se aplica para encontrar la temperatura $u(x, t)$ en varillas infinitas o semi-infinitas. La transformada reduce la EDP a una ecuación diferencial ordinaria en la variable espacial $x$, tratando a $s$ como un parámetro,.
*   **Ecuación de Onda:** Similarmente, se utiliza para resolver problemas de vibraciones en cuerdas muy largas o infinitas, transformando la dependencia temporal.