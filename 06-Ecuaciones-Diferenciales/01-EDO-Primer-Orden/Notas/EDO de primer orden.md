# 1. Ecuaciones diferenciales ordinarias de primer orden. 
A continuación presento la información más relevante extraída de las fuentes proporcionadas, organizada según la estructura solicitada sobre la **Teoría preliminar de las Ecuaciones Diferenciales Ordinarias (EDO)**.

### 1.1 Teoría preliminar

#### 1.1.1 Definiciones (Ecuación diferencial, orden, grado, linealidad)

*   **Ecuación Diferencial:** Se define como cualquier ecuación que contiene las derivadas de una o más variables dependientes respecto a una o más variables independientes.
*   **Clasificación por Tipo:**
    *   **Ecuación Diferencial Ordinaria (EDO):** Si la ecuación contiene únicamente derivadas de una o más variables dependientes respecto a una *sola* variable independiente.
    *   **Ecuación Diferencial Parcial (EDP):** Si la ecuación involucra derivadas parciales de una o más variables dependientes de *dos o más* variables independientes.
*   **Clasificación por Orden:** El orden de una ecuación diferencial (ya sea EDO o EDP) es el orden de la mayor derivada presente en la ecuación. Por ejemplo, una ecuación que contiene una segunda derivada ($d^2y/dx^2$) es de segundo orden.
*   **Linealidad (en lugar de Grado):** Las fuentes proporcionadas clasifican las ecuaciones por **linealidad** en lugar de "grado" algebraico. Se dice que una EDO de n-ésimo orden es **lineal** si cumple dos propiedades características:
    1.  La variable dependiente $y$ y todas sus derivadas $y', \dots, y^{(n)}$ son de primer grado (la potencia de cada término que involucra a $y$ es 1).
    2.  Los coeficientes $a_0, a_1, \dots, a_n$ de $y$ y sus derivadas dependen a lo sumo de la variable independiente $x$.
    *   Una ecuación que no cumple con estas características se denomina **no lineal** (por ejemplo, si contiene términos como $\sin(y)$ o $e^{y'}$ o productos de variables dependientes).

#### 1.1.2 Soluciones de las ecuaciones diferenciales

*   **Definición de Solución:** Cualquier función $f$, definida en un intervalo $I$, que posee al menos $n$ derivadas continuas en $I$, y que al sustituirse en una ecuación diferencial ordinaria de n-ésimo orden reduce la ecuación a una identidad, es una solución de la ecuación en el intervalo.
*   **Intervalo de Definición:** Es el intervalo $I$ en el cual la solución está definida y es diferenciable. También se le conoce como intervalo de existencia, intervalo de validez o dominio de la solución.
*   **Tipos de Soluciones:**
    *   **Solución Explícita:** Es aquella en la que la variable dependiente se expresa solo en términos de la variable independiente y constantes.
    *   **Solución Implícita:** Una relación $G(x, y) = 0$ es una solución implícita si define al menos una función $f$ que satisface la ecuación diferencial en un intervalo $I$.
    *   **Familia de Soluciones:** Al resolver una ecuación diferencial de orden $n$, se busca una solución que contiene constantes arbitrarias ($c_1, c_2, \dots$). Una solución con una constante arbitraria representa un conjunto de soluciones llamado familia de soluciones de un parámetro.
    *   **Solución Particular:** Es una solución libre de parámetros arbitrarios (por ejemplo, asignando valores específicos a las constantes de la familia de soluciones).
    *   **Solución Singular:** Es una solución que no puede obtenerse al especializar los parámetros de la familia de soluciones (no pertenece a la familia de soluciones generales).
    *   **Solución Trivial:** Es la solución idéntica a cero en un intervalo $I$ ($y = 0$).

#### 1.1.3 Problema de valor inicial (PVI)

*   **Definición:** Un problema de valor inicial consiste en resolver una ecuación diferencial sujeta a condiciones adicionales impuestas sobre la función incógnita o sus derivadas en un solo punto $x_0$.
*   **PVI de n-ésimo orden:**
    *   Resolver: $\frac{d^ny}{dx^n} = f(x, y, y', \dots, y^{(n-1)})$
    *   Sujeto a: $y(x_0) = y_0, y'(x_0) = y_1, \dots, y^{(n-1)}(x_0) = y_{n-1}$.
*   **Interpretación Geométrica (Primer Orden):** Para un PVI de primer orden ($y' = f(x,y)$, $y(x_0)=y_0$), se busca una curva solución que pase por el punto $(x_0, y_0)$.
*   **Interpretación Geométrica (Segundo Orden):** Para un PVI de segundo orden, se busca una solución cuya gráfica pase por $(x_0, y_0)$ y cuya pendiente en ese punto sea igual a $y_1$.

#### 1.1.4 Teorema de existencia y unicidad

Este teorema aborda dos preguntas fundamentales sobre los problemas de valor inicial: ¿Existe una solución? y, si existe, ¿es única?.

*   **Teorema 1.1 (Existencia de una solución única):**
    Sea $R$ una región rectangular en el plano $xy$ definida por $a \le x \le b$, $c \le y \le d$, que contiene el punto $(x_0, y_0)$ en su interior. Si $f(x, y)$ y $\frac{\partial f}{\partial y}$ son continuas en $R$, entonces existe algún intervalo $I_0: (x_0 - h, x_0 + h), h > 0$, contenido en $[a, b]$, y una **función única** $y(x)$, definida en $I_0$, que es solución del problema de valor inicial.
*   **Condiciones:** Las condiciones del teorema son suficientes pero no necesarias; es decir, si no se cumplen, el problema aún podría tener solución (incluso única), múltiples soluciones o ninguna solución.
*   **Intervalo de Existencia:** El teorema garantiza la existencia en algún intervalo $I_0$, pero este intervalo puede no ser tan amplio como la región $R$ o el dominio de la función, por lo que la solución es única en un sentido local.


### 1.2 Ecuaciones diferenciales ordinarias

#### 1.2.1 Variables separables y reducibles
*   **Definición:** Una ecuación diferencial de primer orden de la forma $dy/dx = g(x)h(y)$ se dice que es separable o que tiene variables separables.
*   **Método de solución:** Al dividir entre $h(y)$, la ecuación se puede escribir como $p(y) dy = g(x) dx$, donde $p(y) = 1/h(y)$. La solución se obtiene integrando ambos lados: $\int p(y) dy = \int g(x) dx$,.
*   **Soluciones singulares:** Se debe tener cuidado al separar variables, ya que los divisores pueden ser cero. Si $r$ es un cero de la función $h(y)$, entonces $y = r$ es una solución constante que podría perderse durante la separación; esta se denomina solución singular,.
*   **Ecuaciones reducibles:** Una ecuación diferencial de la forma $dy/dx = f(Ax + By + C)$ siempre se puede reducir a una ecuación con variables separables mediante la sustitución $u = Ax + By + C$, donde $B \neq 0$.

#### 1.2.2 Homogéneas
*   **Definición de función homogénea:** Una función $f$ es homogénea de grado $\alpha$ si cumple la propiedad $f(tx, ty) = t^\alpha f(x, y)$.
*   **Definición de ED homogénea:** Una ecuación en forma diferencial $M(x, y) dx + N(x, y) dy = 0$ es homogénea si ambos coeficientes $M$ y $N$ son funciones homogéneas del *mismo* grado,.
*   **Método de solución:** Estas ecuaciones pueden reducirse a una ecuación separable mediante una sustitución algebraica. Se utilizan las sustituciones $y = ux$ o $x = vy$, donde $u$ y $v$ son nuevas variables dependientes. Esto transforma la ecuación a una forma donde las variables son separables.
    *   Específicamente, una ecuación homogénea se puede reescribir como $dy/dx = F(y/x)$.

#### 1.2.3 Exactas
*   **Definición:** Una expresión diferencial $M(x, y) dx + N(x, y) dy$ es una diferencial exacta si corresponde a la diferencial de alguna función $f(x, y)$. Una ecuación $M(x, y) dx + N(x, y) dy = 0$ es exacta si el lado izquierdo es una diferencial exacta,.
*   **Criterio de exactitud:** La condición necesaria y suficiente para que la ecuación sea exacta es que las derivadas parciales sean iguales: $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$.
*   **Método de solución:** Si la ecuación es exacta, existe una función $f$ tal que $\frac{\partial f}{\partial x} = M$ y $\frac{\partial f}{\partial y} = N$. Se encuentra $f$ integrando $M$ respecto a $x$ (añadiendo una "constante" de integración $g(y)$) y luego derivando ese resultado respecto a $y$ para determinar $g(y)$ igualándolo a $N$. La solución implícita es $f(x, y) = c$,.
*   **Factor integrante:** Si la ecuación no es exacta, a veces es posible encontrar un factor integrante $\mu(x, y)$ que la convierta en exacta al multiplicar la ecuación por él.
    *   Si $\frac{M_y - N_x}{N}$ depende solo de $x$, el factor integrante es $\mu(x) = e^{\int \frac{M_y - N_x}{N} dx}$.
    *   Si $\frac{N_x - M_y}{M}$ depende solo de $y$, el factor integrante es $\mu(y) = e^{\int \frac{N_x - M_y}{M} dy}$.

#### 1.2.4 Lineales
*   **Definición:** Una ecuación diferencial de primer orden es lineal si tiene la forma $a_1(x) \frac{dy}{dx} + a_0(x)y = g(x)$.
*   **Forma estándar:** Al dividir por $a_1(x)$, se obtiene la forma estándar $\frac{dy}{dx} + P(x)y = f(x)$.
*   **Factor integrante:** El método de solución implica multiplicar la ecuación en forma estándar por un factor integrante, definido como $e^{\int P(x) dx}$.
*   **Solución general:** La solución es la suma de dos partes: $y = y_c + y_p$, donde $y_c$ es la solución de la ecuación homogénea asociada (cuando $g(x)=0$) y $y_p$ es una solución particular,. La fórmula para la solución general es:
    $y = e^{-\int P(x)dx} \int e^{\int P(x)dx} f(x) dx + c e^{-\int P(x)dx}$.
*   **Transitorios:** En aplicaciones físicas, el término de la solución que tiende a cero cuando $x \to \infty$ (a menudo la parte $y_c$) se denomina *término transitorio*.

#### 1.2.5 De Bernoulli
*   **Definición:** Es una ecuación diferencial de la forma $\frac{dy}{dx} + P(x)y = f(x)y^n$, donde $n$ es cualquier número real.
*   **Casos especiales:** Si $n=0$ o $n=1$, la ecuación es lineal.
*   **Método de solución:** Para $n \neq 0$ y $n \neq 1$, la sustitución $u = y^{1-n}$ reduce la ecuación de Bernoulli a una ecuación lineal en términos de $u$. Una vez resuelta para $u$, se regresa a la variable original $y$.

### 1.3 Aplicaciones. 

### 1.3.1 Modelos Lineales
Estos modelos se basan en ecuaciones diferenciales lineales de primer orden.

**1. Crecimiento y Decaimiento (Dinámica Poblacional y Radiactividad)**
*   **Modelo de Malthus (Crecimiento Poblacional):** Se basa en la suposición de que la razón de crecimiento de una población $P(t)$ en un tiempo $t$ es proporcional a la población total en ese momento.
    *   **Ecuación:** $\frac{dP}{dt} = kP$, donde $k$ es una constante de proporcionalidad.
    *   Este modelo también se aplica al interés compuesto continuo ($dS/dt = rS$).
*   **Decaimiento Radiactivo:** La velocidad de desintegración de núcleos $A(t)$ es proporcional a la cantidad de sustancia remanente.
    *   **Ecuación:** $\frac{dA}{dt} = kA$ (donde $k < 0$),.
    *   Se utiliza para la datación de fósiles (Carbono-14) y la determinación de la vida media de medicamentos.

**2. Ley de Enfriamiento/Calentamiento de Newton**
*   Establece que la rapidez con la que cambia la temperatura $T(t)$ de un cuerpo es proporcional a la diferencia entre la temperatura del cuerpo y la del medio circundante $T_m$.
    *   **Ecuación:** $\frac{dT}{dt} = k(T - T_m)$.

**3. Mezclas**
*   Se utiliza para calcular la cantidad de una sustancia $A(t)$ (como sal) en un tanque donde entra y sale una solución (salmuera) a velocidades específicas.
    *   **Ecuación:** $\frac{dA}{dt} = R_{entrada} - R_{salida}$.
    *   Donde $R_{entrada}$ es la velocidad de entrada de la sustancia y $R_{salida}$ es la velocidad de salida.

**4. Circuitos en Serie**
*   Aplicando la segunda ley de Kirchhoff a un circuito con un inductor ($L$), un resistor ($R$) y una fuente de voltaje ($E(t)$), se obtiene una ecuación lineal para la corriente $i(t)$.
    *   **Ecuación (Circuito LR):** $L\frac{di}{dt} + Ri = E(t)$.
    *   También aplica para circuitos RC con carga $q(t)$: $R\frac{dq}{dt} + \frac{1}{C}q = E(t)$.

### 1.3.2 Modelos No Lineales
Estos modelos surgen cuando el fenómeno físico implica relaciones no lineales.

**1. Dinámica Poblacional (Ecuación Logística)**
*   El modelo de Malthus falla a largo plazo debido a recursos limitados. El modelo logístico, propuesto por Verhulst, introduce un término de inhibición que depende de la densidad de la población.
    *   **Ecuación:** $\frac{dP}{dt} = P(a - bP)$.
    *   Aquí, el término $-bP^2$ representa la inhibición o competencia por recursos.

**2. Reacciones Químicas**
*   Describe la velocidad de reacción cuando, por ejemplo, dos sustancias se combinan para formar una tercera. Si la velocidad es proporcional al producto de las cantidades restantes de los reactivos, se genera una ecuación no lineal (reacción de segundo orden).
    *   **Ecuación:** $\frac{dX}{dt} = k(a - X)(b - X)$, donde $X$ es la cantidad de producto formado.

**3. Ley de Torricelli (Drenado de un Tanque)**
*   Establece que la velocidad de salida del agua a través de un orificio es igual a la velocidad de un objeto en caída libre desde la altura del agua $h$.
    *   **Ecuación:** $\frac{dh}{dt} = -\frac{A_h}{A_w}\sqrt{2gh}$,.
    *   Donde $A_h$ es el área del orificio y $A_w$ es el área de la superficie del agua.

**4. Difusión de Enfermedades**
*   Asume que la razón de propagación es proporcional al número de encuentros entre personas infectadas $x(t)$ y personas sanas $y(t)$.
    *   **Ecuación:** $\frac{dx}{dt} = kx(n + 1 - x)$, para una población fija $n$,.

**5. Caída de Cuerpos con Resistencia del Aire**
*   Si se considera la resistencia del aire (fuerza de retardo), la aceleración no es constante. Si la resistencia es proporcional a la velocidad instantánea $v$:
    *   **Ecuación:** $m\frac{dv}{dt} = mg - kv$.
    *   En movimientos de alta velocidad, la resistencia puede ser proporcional al cuadrado de la velocidad ($kv^2$), generando un modelo no lineal.