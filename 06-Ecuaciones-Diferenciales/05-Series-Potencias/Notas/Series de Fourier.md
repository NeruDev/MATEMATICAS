
# 5. Introducción a las series de Fourier. 
Basado en el texto "Matemáticas avanzadas para ingeniería. Ecuaciones diferenciales 1" de Zill y Cullen (específicamente el Capítulo 10), aquí está la información relevante sobre la **Teoría preliminar** de las Series de Fourier.

Esta sección establece las bases matemáticas tratando a las funciones como una generalización de los vectores, introduciendo conceptos como el producto interno y la ortogonalidad para funciones definidas en un intervalo.

### 5.1 Teoría preliminar: Funciones Ortogonales

#### 5.1.1 Producto Interno de Funciones
Para extender el concepto de producto punto (escalar) de vectores a funciones, se define el **producto interno** de dos funciones $f_1$ y $f_2$ en un intervalo $[a, b]$ como la integral definida de su producto:
$$ (f_1, f_2) = \int_{a}^{b} f_1(x)f_2(x) \, dx $$
Esta definición es fundamental porque permite trasladar propiedades geométricas de vectores al análisis de funciones.

#### 5.1.2 Funciones Ortogonales
Dos funciones $f_1$ y $f_2$ se dicen **ortogonales** en un intervalo $[a, b]$ si su producto interno es cero:
$$ (f_1, f_2) = \int_{a}^{b} f_1(x)f_2(x) \, dx = 0 $$
A diferencia de los vectores, donde la ortogonalidad implica perpendicularidad geométrica, en este contexto no tiene un significado visual geométrico directo, sino analítico.

#### 5.1.3 Conjuntos Ortogonales y Ortonormales
*   **Conjunto Ortogonal:** Un conjunto infinito de funciones con valores reales $\{\phi_0(x), \phi_1(x), \phi_2(x), \dots\}$ es ortogonal en $[a, b]$ si $(\phi_m, \phi_n) = 0$ para todo $m \neq n$.
    *   *Ejemplo Clásico:* El conjunto de funciones trigonométricas $\{1, \cos x, \cos 2x, \dots\}$ es ortogonal en el intervalo $[-\pi, \pi]$.
*   **Norma:** La norma (o longitud generalizada) de una función $\phi_n$ se define como:
    $$ ||\phi_n(x)|| = \sqrt{(\phi_n, \phi_n)} = \sqrt{\int_{a}^{b} \phi_n^2(x) \, dx} $$
    El cuadrado de la norma, $||\phi_n(x)||^2$, es muy útil en los cálculos de coeficientes.
*   **Conjunto Ortonormal:** Si un conjunto ortogonal tiene la propiedad de que la norma de cada función es 1 (es decir, $||\phi_n(x)|| = 1$ para todo $n$), se dice que el conjunto es ortonormal. Cualquier conjunto ortogonal puede normalizarse dividiendo cada función por su norma.

#### 5.1.4 Expansión en Series Ortogonales
La idea central de este tema es representar una función arbitraria $f(x)$ definida en $[a, b]$ como una serie infinita de funciones ortogonales:
$$ f(x) = c_0\phi_0(x) + c_1\phi_1(x) + \dots + c_n\phi_n(x) + \dots $$
Esta serie se conoce como **serie generalizada de Fourier** o expansión en series ortogonales.

**Cálculo de los coeficientes ($c_n$):**
Los coeficientes $c_n$ se determinan aprovechando la propiedad de ortogonalidad. Multiplicando la serie por $\phi_m(x)$ e integrando, todos los términos se anulan excepto cuando $n=m$, lo que permite despejar $c_n$:
$$ c_n = \frac{(f, \phi_n)}{||\phi_n||^2} = \frac{\int_{a}^{b} f(x)\phi_n(x) \, dx}{\int_{a}^{b} \phi_n^2(x) \, dx} $$
Esta fórmula es análoga a encontrar los componentes de un vector en el espacio tridimensional.

#### 5.1.5 Ortogonalidad con Función de Peso
El concepto se generaliza introduciendo una **función de peso** $w(x) > 0$. Un conjunto de funciones es ortogonal respecto a $w(x)$ en $[a, b]$ si:
$$ \int_{a}^{b} w(x)\phi_m(x)\phi_n(x) \, dx = 0, \quad m \neq n $$
En este caso, la fórmula para los coeficientes de la expansión incluye a $w(x)$ dentro de las integrales del numerador y denominador.

#### 5.1.6 Conjuntos Completos
Para que la expansión en serie sea válida y pueda representar a la función $f(x)$, se asume que el conjunto ortogonal es **completo**. Esto significa que la única función continua que es ortogonal a cada miembro del conjunto es la función cero, lo que evita que existan "huecos" en la representación.

Basado en el texto "Matemáticas avanzadas para ingeniería. Ecuaciones diferenciales 1" de Zill y Cullen (específicamente el Capítulo 10), aquí está la información relevante sobre las **Series de Fourier**.

### 5.2 Series de Fourier

La serie de Fourier es un método para expandir una función $f(x)$ definida en un intervalo $(-p, p)$ en una serie infinita compuesta por funciones trigonométricas ortogonales.

#### 5.2.1 Definición y Fórmulas
La serie de Fourier de una función $f$ definida en el intervalo $(-p, p)$ está dada por la expresión:
$$ f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left( a_n \cos \frac{n\pi}{p}x + b_n \text{sen} \frac{n\pi}{p}x \right) $$
Esta serie utiliza el conjunto ortogonal de funciones trigonométricas $\{1, \cos \frac{n\pi}{p}x, \text{sen} \frac{n\pi}{p}x\}$,.

**Coeficientes de Fourier:**
Los coeficientes $a_0$, $a_n$ y $b_n$ se calculan utilizando las propiedades de ortogonalidad e integración:
*   **$a_0$:** $$ a_0 = \frac{1}{p} \int_{-p}^{p} f(x) \, dx $$
*   **$a_n$:** $$ a_n = \frac{1}{p} \int_{-p}^{p} f(x) \cos \frac{n\pi}{p}x \, dx $$
*   **$b_n$:** $$ b_n = \frac{1}{p} \int_{-p}^{p} f(x) \text{sen} \frac{n\pi}{p}x \, dx $$


#### 5.2.2 Convergencia de una Serie de Fourier
El **Teorema 10.1** establece las condiciones suficientes para la convergencia de la serie:
*   Si $f$ y su derivada $f'$ son continuas por tramos en el intervalo $(-p, p)$, la serie converge hacia el valor de la función $f(x)$ en los puntos donde la función es continua.
*   En un punto de discontinuidad $x$, la serie de Fourier converge al **promedio** de los límites por la izquierda y por la derecha:
    $$ \frac{f(x^+) + f(x^-)}{2} $$
   .

#### 5.2.3 Extensión Periódica
Aunque la función $f$ esté definida originalmente solo en el intervalo $(-p, p)$, la serie de Fourier asociada representa una función periódica con periodo $T = 2p$. Esto significa que la serie no solo representa a la función en el intervalo original, sino que también define la **extensión periódica** de $f$ fuera de dicho intervalo,.

#### 5.2.4 Secuencia de Sumas Parciales
La aproximación de la función mediante la serie se puede visualizar a través de la secuencia de sumas parciales $S_N(x)$. A medida que se agregan más términos (aumenta $N$), la suma parcial se aproxima más a la función $f(x)$, excepto cerca de los puntos de discontinuidad, donde puede ocurrir un "disparo" o sobrepaso en la aproximación conocido como el **fenómeno de Gibbs**,.

Basado en el texto "Matemáticas avanzadas para ingeniería. Ecuaciones diferenciales 1" de Zill y Cullen (específicamente la Sección 10.3), aquí está la información relevante sobre las **Series de Fourier en cosenos, senos y de medio intervalo**.

Este subtema se centra en cómo las propiedades de simetría de una función (par o impar) simplifican el cálculo de los coeficientes de Fourier y cómo se pueden expandir funciones definidas solo en un intervalo positivo.

### 5.3 Series de Fourier en cosenos, senos y de medio intervalo

#### 5.3.1 Funciones Pares e Impares
El esfuerzo para evaluar los coeficientes de Fourier se reduce significativamente si la función $f$ es par o impar en un intervalo simétrico $(-p, p)$.
*   **Función Par:** Su gráfica es simétrica respecto al eje $y$. Cumple que $f(-x) = f(x)$. Ejemplo: $x^2$, $\cos x$.
*   **Función Impar:** Su gráfica es simétrica respecto al origen. Cumple que $f(-x) = -f(x)$. Ejemplo: $x^3$, $\text{sen } x$.
*   **Propiedades de Integración:**
    *   Si $f$ es par: $\int_{-a}^{a} f(x) \, dx = 2 \int_{0}^{a} f(x) \, dx$.
    *   Si $f$ es impar: $\int_{-a}^{a} f(x) \, dx = 0$,.

#### 5.3.2 Serie de Fourier de Cosenos
Si la función $f$ es **par** en el intervalo $(-p, p)$:
*   Los coeficientes $b_n$ (asociados al seno) son cero.
*   La serie solo contiene términos coseno y el término constante.
*   **Fórmula:**
    $$ f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} a_n \cos \frac{n\pi}{p}x $$
    Donde los coeficientes se calculan integrando solo en la mitad del intervalo y multiplicando por 2:
    $$ a_0 = \frac{2}{p} \int_{0}^{p} f(x) \, dx $$
    $$ a_n = \frac{2}{p} \int_{0}^{p} f(x) \cos \frac{n\pi}{p}x \, dx $$,.

#### 5.3.3 Serie de Fourier de Senos
Si la función $f$ es **impar** en el intervalo $(-p, p)$:
*   Los coeficientes $a_n$ (asociados al coseno y la constante) son cero.
*   La serie solo contiene términos seno.
*   **Fórmula:**
    $$ f(x) = \sum_{n=1}^{\infty} b_n \text{sen} \frac{n\pi}{p}x $$
    Donde el coeficiente es:
    $$ b_n = \frac{2}{p} \int_{0}^{p} f(x) \text{sen} \frac{n\pi}{p}x \, dx $$,.

#### 5.3.4 Desarrollos de Medio Intervalo (Series de Medio Rango)
En muchas aplicaciones, se desea representar una función que está definida solamente para un intervalo positivo $0 < x < L$, en lugar de un intervalo simétrico. Para lograr esto, se realiza una **extensión** artificial de la función hacia el intervalo $-L < x < 0$.
Existen tres formas principales de hacer esto:

1.  **Serie de Cosenos (Reflexión Par):** Se refleja la gráfica de la función respecto al eje $y$. Esto crea una función par en $(-L, L)$. Se identifica $p = L$ y se calculan los coeficientes $a_0$ y $a_n$ usando las fórmulas de la serie de cosenos (integrando de 0 a $L$ y multiplicando por $2/L$). La serie converge a una extensión periódica par con periodo $2L$,.
2.  **Serie de Senos (Reflexión Impar):** Se refleja la gráfica a través del origen. Esto crea una función impar en $(-L, L)$. Se identifica $p = L$ y se calculan los coeficientes $b_n$ usando la fórmula de la serie de senos. La serie converge a una extensión periódica impar con periodo $2L$,.
3.  **Reflexión Identidad (Serie de Fourier completa):** Se define la función en $-L < x < 0$ mediante $f(x) = f(x + L)$, lo que implica una extensión periódica de periodo $L$ (en lugar de $2L$). En este caso, $p = L/2$,.

#### 5.3.5 Fenómeno de Gibbs
El texto también menciona el fenómeno de Gibbs en el contexto de las series de senos. Cerca de un punto de discontinuidad, las sumas parciales de la serie de Fourier no se ajustan suavemente a la función, sino que presentan picos pronunciados o "disparos" que no desaparecen incluso cuando aumenta el número de términos de la serie,.