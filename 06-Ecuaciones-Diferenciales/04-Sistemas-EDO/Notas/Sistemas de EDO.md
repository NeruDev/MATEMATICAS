Basado en el texto "Matemáticas avanzadas para ingeniería. Ecuaciones diferenciales 1" de Zill y Cullen (específicamente el Capítulo 8 que corresponde a su solicitud), aquí está la información relevante sobre la teoría preliminar de sistemas de ecuaciones diferenciales lineales.

### 4.1 Teoría preliminar

Esta sección establece el marco teórico necesario para entender y resolver sistemas de ecuaciones diferenciales lineales de primer orden.

#### 4.1.1 Sistemas de ecuaciones diferenciales lineales

*   **Definición y Forma Normal:** Un sistema de $n$ ecuaciones diferenciales de primer orden es lineal si cada una de las funciones de la derivada es lineal respecto a las variables dependientes $x_1, x_2, \dots, x_n$. La forma normal de un sistema lineal es:
    $$ \frac{dx_1}{dt} = a_{11}(t)x_1 + a_{12}(t)x_2 + \dots + a_{1n}(t)x_n + f_1(t) $$
    $$ \frac{dx_2}{dt} = a_{21}(t)x_1 + a_{22}(t)x_2 + \dots + a_{2n}(t)x_n + f_2(t) $$
    $$ \vdots $$
    $$ \frac{dx_n}{dt} = a_{n1}(t)x_1 + a_{n2}(t)x_2 + \dots + a_{nn}(t)x_n + f_n(t) $$
    Se asume que los coeficientes $a_{ij}(t)$ y las funciones $f_i(t)$ son continuos en un intervalo común $I$.
*   **Forma Matricial:** El sistema anterior se puede escribir de manera compacta como:
    $$ \mathbf{X}' = \mathbf{A}(t)\mathbf{X} + \mathbf{F}(t) $$
    Donde $\mathbf{X}$ es la matriz columna (vector) de las incógnitas, $\mathbf{A}(t)$ es la matriz de coeficientes y $\mathbf{F}(t)$ es la matriz columna de las funciones de entrada o forzadas,.
*   **Existencia y Unicidad:** Si las entradas de las matrices $\mathbf{A}(t)$ y $\mathbf{F}(t)$ son funciones continuas en un intervalo común $I$ que contiene a $t_0$, entonces existe una solución única para el problema de valor inicial $\mathbf{X}' = \mathbf{A}(t)\mathbf{X} + \mathbf{F}(t)$, sujeto a $\mathbf{X}(t_0) = \mathbf{X}_0$ en ese intervalo.

#### 4.1.2 Sistemas de ecuaciones diferenciales lineales homogéneos

*   **Definición:** Un sistema lineal se dice que es **homogéneo** si la matriz de funciones de entrada es cero, es decir, $\mathbf{F}(t) = \mathbf{0}$. Su forma matricial es:
    $$ \mathbf{X}' = \mathbf{A}\mathbf{X} $$
   ,.
*   **Principio de Superposición:** Si $\mathbf{X}_1, \mathbf{X}_2, \dots, \mathbf{X}_k$ es un conjunto de vectores solución del sistema homogéneo en un intervalo $I$, entonces cualquier combinación lineal de ellos:
    $$ \mathbf{X} = c_1\mathbf{X}_1 + c_2\mathbf{X}_2 + \dots + c_k\mathbf{X}_k $$
    es también una solución en el intervalo, donde las $c_i$ son constantes arbitrarias.
*   **Independencia Lineal:** Un conjunto de vectores solución es linealmente independiente en un intervalo si la única forma de que la combinación lineal $c_1\mathbf{X}_1 + \dots + c_k\mathbf{X}_k$ sea igual a cero para toda $t$ en el intervalo es que todas las constantes $c_i$ sean cero,.
*   **Criterio del Wronskiano:** Para verificar la independencia lineal de $n$ vectores solución, se utiliza el Wronskiano, denotado como $W(\mathbf{X}_1, \mathbf{X}_2, \dots, \mathbf{X}_n)$, que es el determinante de la matriz formada por estos vectores. Los vectores son linealmente independientes en un intervalo si y solo si el Wronskiano es diferente de cero para toda $t$ en dicho intervalo,.
*   **Conjunto Fundamental:** Cualquier conjunto de $n$ vectores solución linealmente independientes de un sistema homogéneo en un intervalo $I$ se denomina conjunto fundamental de soluciones.

#### 4.1.3 Solución general y solución particular de sistemas de ecuaciones diferenciales lineales

*   **Solución General (Sistema Homogéneo):** Si $\mathbf{X}_1, \mathbf{X}_2, \dots, \mathbf{X}_n$ es un conjunto fundamental de soluciones del sistema homogéneo $\mathbf{X}' = \mathbf{A}\mathbf{X}$ en un intervalo $I$, entonces la solución general del sistema en ese intervalo es:
    $$ \mathbf{X} = c_1\mathbf{X}_1 + c_2\mathbf{X}_2 + \dots + c_n\mathbf{X}_n $$
   .
*   **Solución Particular:** Una solución particular, denotada como $\mathbf{X}_p$, es cualquier vector libre de parámetros arbitrarios cuyos elementos satisfacen el sistema no homogéneo $\mathbf{X}' = \mathbf{A}\mathbf{X} + \mathbf{F}(t)$.
*   **Solución General (Sistema No Homogéneo):** Sea $\mathbf{X}_p$ una solución particular dada del sistema no homogéneo en un intervalo $I$, y sea $\mathbf{X}_c$ la solución general del sistema homogéneo asociado (también llamada **función complementaria**). Entonces, la solución general del sistema no homogéneo es:
    $$ \mathbf{X} = \mathbf{X}_c + \mathbf{X}_p $$
    Esto significa que la solución general se compone de la suma de la función complementaria y una solución particular.

### 4.2 Métodos de solución para sistemas de ecuaciones diferenciales lineales

Basado en el texto "Matemáticas avanzadas para ingeniería. Ecuaciones diferenciales 1" de Zill y Cullen (específicamente el Capítulo 8), los métodos de solución para sistemas de ecuaciones diferenciales lineales se centran principalmente en el uso de matrices, valores propios (eigenvalores) y vectores propios (eigenvectores).

A continuación, detallo los métodos principales presentados en el texto para resolver sistemas de la forma $\mathbf{X}' = \mathbf{A}\mathbf{X} + \mathbf{F}(t)$ y su contraparte homogénea.

### 4.2.1 Método de los Valores y Vectores Propios (Sistemas Homogéneos)

Para un sistema homogéneo $\mathbf{X}' = \mathbf{A}\mathbf{X}$ con coeficientes constantes, se busca una solución de la forma $\mathbf{X} = \mathbf{K}e^{\lambda t}$. Esto conduce a la ecuación característica $\det(\mathbf{A} - \lambda\mathbf{I}) = 0$, cuyas raíces son los valores propios.

Se distinguen tres casos fundamentales:

1.  **Valores propios reales distintos:**
    Si la matriz $\mathbf{A}$ de $n \times n$ tiene $n$ valores propios reales y distintos ($\lambda_1, \lambda_2, \dots, \lambda_n$), siempre se puede encontrar un conjunto de $n$ vectores propios linealmente independientes ($\mathbf{K}_1, \mathbf{K}_2, \dots, \mathbf{K}_n$). La solución general es la superposición:
    $$ \mathbf{X} = c_1\mathbf{K}_1e^{\lambda_1 t} + c_2\mathbf{K}_2e^{\lambda_2 t} + \dots + c_n\mathbf{K}_ne^{\lambda_n t} $$.

2.  **Valores propios repetidos:**
    Cuando un valor propio $\lambda_1$ tiene multiplicidad $m$:
    *   Si es posible encontrar $m$ vectores propios independientes, la solución sigue siendo la combinación lineal estándar exponencial.
    *   Si solo hay un vector propio asociado, se deben buscar soluciones adicionales de la forma:
        $$ \mathbf{X}_2 = \mathbf{K}te^{\lambda t} + \mathbf{P}e^{\lambda t} $$
        donde $\mathbf{K}$ es el vector propio y $\mathbf{P}$ se determina resolviendo $(\mathbf{A} - \lambda\mathbf{I})\mathbf{P} = \mathbf{K}$.

3.  **Valores propios complejos:**
    Si $\lambda_1 = \alpha + i\beta$ es un valor propio complejo, sus soluciones implican términos con funciones seno y coseno. Se generan soluciones linealmente independientes reales utilizando la parte real e imaginaria de los vectores propios complejos:
    $$ \mathbf{X}_1 = [\mathbf{B}_1 \cos \beta t - \mathbf{B}_2 \text{sen } \beta t]e^{\alpha t} $$
    $$ \mathbf{X}_2 = [\mathbf{B}_2 \cos \beta t + \mathbf{B}_1 \text{sen } \beta t]e^{\alpha t} $$
    donde $\mathbf{K}_1 = \mathbf{B}_1 + i\mathbf{B}_2$ es el vector propio asociado.

### 4.2.2 Solución mediante Diagonalización

Este método es útil para **desacoplar** un sistema. Si la matriz $\mathbf{A}$ es diagonalizable, existe una matriz $\mathbf{P}$ tal que $\mathbf{P}^{-1}\mathbf{A}\mathbf{P} = \mathbf{D}$, donde $\mathbf{D}$ es una matriz diagonal.
*   Haciendo el cambio de variable $\mathbf{X} = \mathbf{P}\mathbf{Y}$, el sistema original se convierte en $\mathbf{Y}' = \mathbf{D}\mathbf{Y}$.
*   Este nuevo sistema consiste en ecuaciones diferenciales no acopladas de la forma $y'_i = \lambda_i y_i$, cuyas soluciones son inmediatas ($y_i = c_i e^{\lambda_i t}$).
*   Finalmente, se recupera la solución original mediante $\mathbf{X} = \mathbf{P}\mathbf{Y}$.

### 4.2.3 Métodos para Sistemas No Homogéneos

Para sistemas de la forma $\mathbf{X}' = \mathbf{A}\mathbf{X} + \mathbf{F}(t)$, la solución general es $\mathbf{X} = \mathbf{X}_c + \mathbf{X}_p$, donde $\mathbf{X}_c$ es la solución complementaria (del sistema homogéneo) y $\mathbf{X}_p$ es una solución particular.

1.  **Coeficientes Indeterminados:**
    Se asume una forma para el vector solución particular $\mathbf{X}_p$ basada en las funciones presentes en el vector de entrada $\mathbf{F}(t)$ (constantes, polinomios, exponenciales, senos/cosenos). Este método es válido solo si $\mathbf{A}$ es una matriz de constantes.

2.  **Variación de Parámetros:**
    Es un método más general que utiliza la **matriz fundamental** $\mathbf{\Phi}(t)$ (formada por las columnas de los vectores solución homogéneos). La solución particular se obtiene mediante la fórmula:
    $$ \mathbf{X}_p = \mathbf{\Phi}(t) \int \mathbf{\Phi}^{-1}(t)\mathbf{F}(t) \, dt $$
    Este método requiere calcular la inversa de la matriz fundamental e integrar matrices.

### 4.2.4 Matriz Exponencial

Este es un método poderoso y elegante basado en la definición de la exponencial de una matriz mediante series de potencias:
$$ e^{\mathbf{A}t} = \mathbf{I} + \mathbf{A}t + \mathbf{A}^2 \frac{t^2}{2!} + \dots $$
*   La solución para el sistema homogéneo es simplemente $\mathbf{X} = e^{\mathbf{A}t}\mathbf{C}$.
*   La matriz $e^{\mathbf{A}t}$ es en sí misma una matriz fundamental.
*   Para sistemas no homogéneos, la solución general toma la forma:
    $$ \mathbf{X} = e^{\mathbf{A}t}\mathbf{C} + e^{\mathbf{A}t} \int_{t_0}^{t} e^{-\mathbf{A}s}\mathbf{F}(s) \, ds $$
    Este método es especialmente útil pues $e^{\mathbf{A}t}$ se puede calcular utilizando la transformada de Laplace: $e^{\mathbf{A}t} = \mathcal{L}^{-1}\{(s\mathbf{I} - \mathbf{A})^{-1}\}$.

### 4.3 Método de los Operadores para Sistemas de Ecuaciones Diferenciales Lineales

Basado en el texto "Ecuaciones diferenciales con aplicaciones de modelado" de Zill y Cullen, la información referente al **Método de los operadores** para la resolución de sistemas de ecuaciones diferenciales lineales (que en el texto se presenta bajo la sección de **Eliminación sistemática**) se detalla a continuación.

Este método se fundamenta en el uso del **operador diferencial** $D$ para transformar y manipular el sistema de ecuaciones como si fueran ecuaciones algebraicas polinomiales, permitiendo eliminar variables dependientes hasta obtener una sola ecuación diferencial de orden superior con una sola incógnita.

### 1. Notación del Operador Diferencial
Para aplicar este método, primero se reescribe el sistema utilizando la notación de operador $D$, donde $D = d/dt$, $D^2 = d^2/dt^2$, y así sucesivamente. Una ecuación diferencial lineal de $n$-ésimo orden con coeficientes constantes:
$$ a_n y^{(n)} + a_{n-1} y^{(n-1)} + \dots + a_0 y = g(t) $$
se escribe como un polinomio en $D$:
$$ (a_n D^n + a_{n-1} D^{n-1} + \dots + a_0)y = g(t) $$
o simplemente $L(y) = g(t)$, donde $L$ es el operador lineal.

### 2. Fundamento del Método: Eliminación Sistemática
El método se basa en el principio algebraico de eliminación de variables. Dado que los operadores diferenciales lineales con coeficientes constantes se pueden factorizar y los factores conmutan (es decir, el orden de operación no altera el resultado), se puede operar sobre las ecuaciones del sistema para eliminar variables dependientes,.

**El procedimiento general es:**
1.  **Reescritura:** Escribir todas las ecuaciones del sistema en notación de operador, agrupando los términos de las mismas variables ($x, y, z$, etc.).
2.  **Eliminación:** Multiplicar las ecuaciones por operadores adecuados para igualar los coeficientes de una de las variables y luego sumar o restar las ecuaciones para eliminar dicha variable. Esto es análogo a resolver sistemas algebraicos simples,.
3.  **Solución:** El resultado de la eliminación es una ecuación diferencial lineal de orden superior en una sola variable (por ejemplo, en $x$). Se resuelve esta ecuación utilizando los métodos estándar para obtener $x(t)$.
4.  **Repetición:** Se repite el proceso para eliminar la otra variable y obtener una ecuación diferencial para ella (por ejemplo, en $y$), resolviéndola para obtener $y(t)$.

### 3. El Problema de las Constantes Arbitrarias
Un aspecto crítico de este método es que las soluciones obtenidas para $x(t)$ y $y(t)$ de forma independiente contendrán más constantes arbitrarias de las que realmente son necesarias o independientes para el sistema original.

*   Si se resuelve una ecuación de segundo orden para $x(t)$ y una de segundo orden para $y(t)$, se obtendrán cuatro constantes ($c_1, c_2, c_3, c_4$). Sin embargo, el sistema original impone restricciones que relacionan estas constantes entre sí.
*   **Corrección:** Para determinar la relación entre las constantes, se deben sustituir las soluciones obtenidas ($x(t)$ y $y(t)$) en una de las ecuaciones **originales** del sistema. Al agrupar términos y simplificar, se obtendrán ecuaciones que relacionan unas constantes con otras (por ejemplo, $c_3$ podría ser un múltiplo de $c_1$), reduciendo el número de parámetros libres al orden correcto del sistema,.

### Ejemplo Conceptual
Para un sistema:
$$ \frac{dx}{dt} = 3y $$
$$ \frac{dy}{dt} = 2x $$
En notación de operador:
$$ Dx - 3y = 0 $$
$$ -2x + Dy = 0 $$
Se aplica el operador $D$ a la primera ecuación ($D^2x - 3Dy = 0$) y se multiplica la segunda por 3 ($ -6x + 3Dy = 0$). Al sumar, se elimina $y$ y queda $(D^2 - 6)x = 0$, que se resuelve para $x(t)$. Luego se realiza un proceso similar para hallar $y(t)$, y finalmente se sustituyen en el sistema original para relacionar las constantes de integración,.

Basado en los textos de Zill (específicamente la **Sección 4.6** en la fuente 1 y la **Sección 7.6** en la fuente 2), aquí está la información relevante sobre la resolución de sistemas de ecuaciones diferenciales lineales utilizando la transformada de Laplace.

### 4.4 Utilizando la transformada de Laplace para sistemas

El uso de la transformada de Laplace para resolver sistemas de ecuaciones diferenciales lineales con coeficientes constantes es una alternativa a los métodos de eliminación sistemática o matriciales. Su principal característica es que convierte el sistema de ecuaciones diferenciales en un sistema de ecuaciones algebraicas.

#### 1. Fundamento del Método
Cuando se aplican las condiciones iniciales, la transformada de Laplace reduce un sistema de ecuaciones diferenciales lineales con coeficientes constantes a un conjunto de **ecuaciones algebraicas simultáneas** en función de las variables transformadas (usualmente $X(s)$ y $Y(s)$),,.

#### 2. Procedimiento de Solución
El proceso general descrito en los textos es el siguiente:

1.  **Transformación:** Se aplica la transformada de Laplace a cada término de cada ecuación del sistema.
    *   Debido a la propiedad de linealidad, la transformada de una combinación lineal es una combinación lineal de las transformadas.
    *   Las derivadas (como $x'$ o $x''$) se transforman usando las propiedades operacionales que incorporan las condiciones iniciales (por ejemplo, $\mathcal{L}\{x'(t)\} = sX(s) - x(0)$).
2.  **Resolución Algebraica:** El resultado es un sistema de ecuaciones lineales algebraicas donde las incógnitas son las transformadas $X(s)$, $Y(s)$, etc. Se resuelve este sistema utilizando técnicas algebraicas estándar (como la regla de Cramer o eliminación) para despejar $X(s)$ y $Y(s)$,.
3.  **Transformada Inversa:** Se aplica la transformada inversa de Laplace a las expresiones obtenidas para recuperar las funciones en el dominio del tiempo, $x(t)$ y $y(t)$,.

#### 3. Ventajas
*   **Condiciones Iniciales:** A diferencia de otros métodos que requieren encontrar la solución general y luego aplicar las constantes, la transformada de Laplace incorpora las condiciones iniciales $x(0), y(0), x'(0)$, etc., directamente en el paso de transformación, lo que lleva a la solución particular de inmediato.
*   **Sistemas Acoplados:** Es particularmente útil para sistemas acoplados donde múltiples variables dependientes interactúan entre sí.

#### 4. Aplicaciones Comunes
Los textos ilustran este método principalmente con dos tipos de sistemas físicos:

*   **Resortes Acoplados:** Se utiliza para resolver el movimiento de dos masas unidas por resortes, modelado por un sistema de ecuaciones de segundo orden (ley de Newton). Ejemplo:
    $$ m_1 x_1'' = -k_1 x_1 + k_2(x_2 - x_1) $$
    $$ m_2 x_2'' = -k_2(x_2 - x_1) $$
    La transformada convierte esto en ecuaciones algebraicas que permiten hallar la posición de las masas,,.

*   **Redes Eléctricas:** Se aplica a circuitos complejos (mallas) con inductores, resistores y capacitores. Las ecuaciones integrodiferenciales derivadas de las leyes de Kirchhoff se transforman fácilmente al dominio $s$, permitiendo resolver para las corrientes $i_1(t)$ e $i_2(t)$,,.

*   **Péndulo Doble:** Para pequeños desplazamientos, el sistema no lineal que describe un péndulo doble se linealiza y se resuelve utilizando este método,.

Basado en el texto "Ecuaciones diferenciales con aplicaciones de modelado" de Zill (específicamente la **Sección 3.3** y partes del **Capítulo 8** en la fuente 2), aquí está la información relevante sobre las aplicaciones de los sistemas de ecuaciones diferenciales lineales.

### 4.5 Aplicaciones de sistemas de ecuaciones diferenciales lineales

Los sistemas de ecuaciones diferenciales lineales se utilizan para describir fenómenos físicos en los que interactúan múltiples variables dependientes del tiempo. Estas interacciones generan sistemas "acoplados".

#### 1. Series Radiactivas
Se utilizan para modelar el decaimiento de una serie de elementos radiactivos donde un elemento se transforma en otro, que a su vez se transforma en un tercero (por ejemplo, $U-238 \to Th-234 \to \dots \to Pb-206$).
*   **El Modelo:** Si $x(t)$, $y(t)$ y $z(t)$ son las cantidades de las sustancias, el sistema lineal se describe como:
    $$ \frac{dx}{dt} = -\lambda_1 x $$
    $$ \frac{dy}{dt} = \lambda_1 x - \lambda_2 y $$
    $$ \frac{dz}{dt} = \lambda_2 y $$
    Aquí, la sustancia $Y$ gana átomos del decaimiento de $X$ (tasa positiva $\lambda_1 x$) y pierde átomos por su propio decaimiento (tasa negativa $-\lambda_2 y$),.

#### 2. Mezclas en Tanques Conectados
Este modelo extiende el problema de un solo tanque a dos o más tanques interconectados donde fluye una solución (como salmuera) entre ellos.
*   **El Sistema:** La razón de cambio de la cantidad de soluto (sal) en cada tanque es igual a la tasa de entrada menos la tasa de salida. Si $x_1(t)$ y $x_2(t)$ son las libras de sal en los tanques A y B:
    $$ \frac{dx_1}{dt} = (\text{entrada externa}) + (\text{entrada desde B}) - (\text{salida hacia B}) - (\text{salida externa}) $$
    Esto genera un sistema lineal de la forma:
    $$ \frac{dx_1}{dt} = a_{11}x_1 + a_{12}x_2 $$
    $$ \frac{dx_2}{dt} = a_{21}x_1 + a_{22}x_2 $$
    Los coeficientes dependen de las tasas de flujo y los volúmenes de los tanques,,.

#### 3. Redes Eléctricas
Los sistemas lineales modelan circuitos con múltiples mallas (lazos) que contienen resistores, inductores y capacitores.
*   **Leyes de Kirchhoff:**
    1.  **Ley de Nodos:** La suma de corrientes que entran a un nodo es igual a la suma de las que salen ($i_1 = i_2 + i_3$).
    2.  **Ley de Mallas:** La suma de caídas de voltaje en una malla cerrada es igual al voltaje aplicado.
*   **El Modelo:** Para una red con dos mallas, se obtiene un sistema de ecuaciones de primer orden para las corrientes (o cargas) en las diferentes ramas. Por ejemplo, en un circuito con inductores y resistores:
    $$ L_1 \frac{di_2}{dt} + (R_1 + R_2)i_2 + R_1 i_3 = E(t) $$
    Este sistema permite determinar cómo se comportan las corrientes simultáneamente en diferentes partes del circuito,,.

#### 4. Sistemas Mecánicos Acoplados (Resortes)
Se utilizan para describir el movimiento de dos o más masas conectadas entre sí por resortes.
*   **Fuerzas:** La segunda ley de Newton se aplica a cada masa. La fuerza neta sobre una masa depende no solo de su desplazamiento, sino también del desplazamiento de la masa adyacente (debido al resorte que las une).
*   **Ecuaciones:** Para dos masas $m_1$ y $m_2$, el sistema es:
    $$ m_1 x''_1 = -k_1 x_1 + k_2(x_2 - x_1) $$
    $$ m_2 x''_2 = -k_2(x_2 - x_1) $$
    Este es un sistema de segundo orden que puede resolverse directamente o reducirse a un sistema de primer orden más grande.

#### 5. Modelos Biológicos (Competencia y Depredación)
Aunque muchos modelos biológicos son no lineales (como el modelo depredador-presa de Lotka-Volterra que involucra términos $xy$), existen versiones lineales para ciertos escenarios.
*   **Competencia Lineal:** Si dos especies compiten por recursos y su interacción reduce sus tasas de crecimiento de manera lineal, el modelo es:
    $$ \frac{dx}{dt} = ax + by $$
    $$ \frac{dy}{dt} = cx + dy $$
    Donde los coeficientes reflejan las tasas de nacimiento/muerte y los efectos de la competencia (generalmente negativos),.