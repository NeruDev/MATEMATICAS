<!--
HUMANO:
Este archivo contiene definiciones y términos clave usados en todo el repositorio.
Permite tener un vocabulario común y consistente.

IA:
Usa este glosario como referencia para terminología.
Consulta las secciones de ANALOGÍAS para explicar conceptos a estudiantes.
Las referencias cruzadas [→ término] indican conceptos relacionados.

---
content_type: glossary
expected_output:
  default: markdown
audience: self-study
formality: technical
ai_usage:
  - Usar analogías para explicaciones iniciales
  - Referenciar términos relacionados con [→ término]
  - Priorizar intuición antes que rigor formal para principiantes
---
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](README.md)

---

# Glosario de Matemáticas

---

## Índice por Módulo

- [Fundamentos](#álgebra-lineal)
- [Cálculo Diferencial](#cálculo-integral)
- [Ecuaciones Diferenciales](#métodos-numéricos)
- [Conceptos Abstractos y Analogías](#notación-común)

---

## Fundamentos

### Funciones y Relaciones

| Término | Definición | Intuición |
|---------|------------|-----------|
| **Función** | Relación que asigna a cada elemento del dominio exactamente un elemento del codominio | Como una máquina: entra un número, sale exactamente uno. [→ Analogía: Máquina] |
| **Dominio** | Conjunto de todos los valores de entrada válidos para una función | Los "ingredientes permitidos" para la máquina |
| **Codominio** | Conjunto donde pueden caer los valores de salida | El "tipo de resultado posible" |
| **Rango (Imagen)** | Subconjunto del codominio que realmente se alcanza | Los resultados que realmente salen |
| **Función inyectiva** | Función donde diferentes entradas producen diferentes salidas | Cada salida tiene a lo más un origen |
| **Función sobreyectiva** | Función que alcanza todo el codominio | Ningún valor de salida queda "huérfano" |
| **Función biyectiva** | Función inyectiva y sobreyectiva simultáneamente | Correspondencia perfecta uno a uno. [→ Isomorfismo] |
| **Función inversa** | Función que "deshace" lo que hace la original | El botón de "deshacer". Solo existe para biyecciones |
| **Composición** | Aplicar una función al resultado de otra: $(f \circ g)(x) = f(g(x))$ | Encadenar máquinas: la salida de una es entrada de otra |

### Aritmética Superior

| Término | Definición | Intuición |
|---------|------------|-----------|
| **MCD** | Máximo Común Divisor: el mayor número que divide a dos o más números | El "bloque más grande" que cabe exactamente en todos |
| **MCM** | Mínimo Común Múltiplo: el menor número divisible por todos los dados | El primer punto donde todos los "ritmos" coinciden |
| **Número primo** | Número mayor que 1 divisible solo por 1 y sí mismo | Los "átomos" de los números: no se pueden descomponer más |
| **Factorización** | Expresar un número como producto de primos | Encontrar los "ingredientes atómicos" |
| **Congruencia modular** | $a \equiv b \pmod{n}$ si $n$ divide a $a-b$ | Los números son "iguales" si dan el mismo resto. Como las horas del reloj |

### Álgebra Fundamental

| Término | Definición | Intuición |
|---------|------------|-----------|
| **Polinomio** | Expresión con sumas de potencias de $x$ con coeficientes | Una "receta" que usa solo sumas, restas y multiplicaciones |
| **Raíz de un polinomio** | Valor de $x$ que hace el polinomio igual a cero | Donde la gráfica toca el eje $x$ |
| **Factorizar** | Escribir una expresión como producto de factores más simples | "Desarmar" una expresión en sus piezas multiplicativas |
| **Expresión racional** | Cociente de dos polinomios | Una fracción donde arriba y abajo hay polinomios |

### Trigonometría

| Término | Definición | Intuición |
|---------|------------|-----------|
| **Radián** | Ángulo cuyo arco tiene longitud igual al radio | Medir ángulos en "radios de pizza" en lugar de grados |
| **Seno** | Razón: cateto opuesto / hipotenusa; coordenada $y$ en círculo unitario | La "altura" de un punto que gira en un círculo |
| **Coseno** | Razón: cateto adyacente / hipotenusa; coordenada $x$ en círculo unitario | La "posición horizontal" de un punto que gira |
| **Tangente** | Razón: seno / coseno; pendiente de la recta al punto en el círculo | Qué tan "empinada" está la línea hacia el punto |
| **Identidad trigonométrica** | Ecuación verdadera para todos los valores del ángulo | "Leyes" que siempre se cumplen, como $\sin^2\theta + \cos^2\theta = 1$ |

---

## Álgebra Lineal

### Matrices y Operaciones

| Término | Definición | Intuición |
|---------|------------|-----------|
| **Matriz** | Arreglo rectangular de números ordenados en filas y columnas | Una tabla de números con estructura. [→ Analogía: Hoja de cálculo] |
| **Matriz cuadrada** | Matriz con igual número de filas y columnas | Una tabla "cuadrada" |
| **Matriz identidad** | Matriz con 1s en la diagonal y 0s en el resto | El "no hacer nada" de las matrices. Multiplicar por ella no cambia nada |
| **Matriz inversa** | Matriz $A^{-1}$ tal que $AA^{-1} = I$ | La que "deshace" lo que hace $A$ |
| **Transpuesta** | Matriz con filas y columnas intercambiadas | "Voltear" la tabla por su diagonal |
| **Matriz simétrica** | Matriz igual a su transpuesta | Se ve igual si la volteas por la diagonal |
| **Traza** | Suma de los elementos de la diagonal | El "resumen diagonal" de una matriz cuadrada |

### Determinantes

| Término | Definición | Intuición |
|---------|------------|-----------|
| **Determinante** | Número que caracteriza una matriz cuadrada | Mide cuánto "estira o encoge" el espacio una transformación. [→ Analogía: Factor de escala] |
| **Cofactor** | Determinante de submatriz con signo alternante | Pieza del rompecabezas para calcular determinantes grandes |
| **Menor** | Determinante de submatriz obtenida al eliminar fila y columna | El determinante "más pequeño" que queda |
| **Matriz singular** | Matriz con determinante cero | Una transformación que "aplasta" el espacio a menor dimensión |
| **Regla de Cramer** | Método para resolver sistemas usando determinantes | Usar cocientes de determinantes para encontrar soluciones |

### Espacios Vectoriales

| Término | Definición | Intuición |
|---------|------------|-----------|
| **Espacio vectorial** | Conjunto con operaciones de suma y multiplicación por escalar que cumplen axiomas | Un "universo" donde puedes sumar cosas y escalarlas. [→ Analogía: Arena de juego] |
| **Vector** | Elemento de un espacio vectorial | Una "flecha" con magnitud y dirección (en $\mathbb{R}^n$) |
| **Subespacio** | Subconjunto de un EV que también es EV | Un "sub-universo" cerrado bajo las mismas operaciones |
| **Combinación lineal** | Suma de vectores multiplicados por escalares: $c_1v_1 + c_2v_2 + ...$ | "Mezclar" vectores con diferentes proporciones |
| **Span (Generado)** | Conjunto de todas las combinaciones lineales de un conjunto de vectores | Todo lo que puedes "alcanzar" combinando esos vectores |
| **Independencia lineal** | Ningún vector puede escribirse como combinación de los otros | Cada vector aporta una "dirección nueva" |
| **Base** | Conjunto linealmente independiente que genera todo el espacio | El "sistema de coordenadas mínimo" para describir todo |
| **Dimensión** | Número de vectores en cualquier base | Cuántas "direcciones independientes" tiene el espacio |

### Transformaciones Lineales

| Término | Definición | Intuición |
|---------|------------|-----------|
| **Transformación lineal** | Función entre EV que preserva suma y producto por escalar | Una función que "respeta" la estructura. [→ Analogía: Transformación geométrica] |
| **Núcleo (Kernel)** | Vectores que la transformación envía al cero | Lo que la transformación "destruye" o "ignora" |
| **Imagen (Rango)** | Vectores que son salida de la transformación | Todo lo que la transformación puede "producir" |
| **Isomorfismo** | Transformación lineal biyectiva | Dos espacios son "esencialmente iguales" |
| **Matriz asociada** | Matriz que representa una transformación lineal respecto a bases | La "receta numérica" de la transformación |

### Valores y Vectores Propios

| Término | Definición | Intuición |
|---------|------------|-----------|
| **Valor propio (Eigenvalor)** | Escalar $\lambda$ tal que $Av = \lambda v$ para algún $v \neq 0$ | Cuánto "estira" la matriz en ciertas direcciones especiales |
| **Vector propio (Eigenvector)** | Vector $v$ que solo se escala (no rota) bajo $A$ | Las direcciones "privilegiadas" que la matriz solo estira |
| **Polinomio característico** | $\det(A - \lambda I)$, sus raíces son los eigenvalores | La "ecuación mágica" que revela los eigenvalores |
| **Diagonalización** | Escribir $A = PDP^{-1}$ con $D$ diagonal | Encontrar el "sistema de coordenadas natural" donde $A$ solo estira |
| **Multiplicidad algebraica** | Veces que aparece $\lambda$ como raíz del polinomio característico | Cuántas veces se "repite" un eigenvalor en la ecuación |
| **Multiplicidad geométrica** | Dimensión del eigenespacio asociado a $\lambda$ | Cuántos eigenvectores independientes hay para ese $\lambda$ |

---

## Cálculo Diferencial

### Límites

| Término | Definición | Intuición |
|---------|------------|-----------|
| **Límite** | Valor al que se aproxima $f(x)$ cuando $x$ se acerca a un punto | Hacia dónde "apunta" la función sin necesariamente llegar. [→ Analogía: Destino] |
| **Límite lateral** | Límite acercándose solo por un lado (izquierda o derecha) | Mirar hacia el destino desde un solo camino |
| **Continuidad** | El límite existe, la función está definida, y coinciden | La función "fluye" sin saltos ni huecos |
| **Discontinuidad removible** | Hay un "hueco" que se puede "tapar" redefiniendo un punto | Un agujero que se puede rellenar |
| **Asíntota** | Recta a la que la función se aproxima indefinidamente | Una "barrera invisible" que la función persigue sin alcanzar |
| **Forma indeterminada** | Expresiones como $0/0$, $\infty/\infty$ que requieren más análisis | Cuando la respuesta "depende" y hay que investigar más |

### Derivadas

| Término | Definición | Intuición |
|---------|------------|-----------|
| **Derivada** | $\lim_{h\to 0} \frac{f(x+h) - f(x)}{h}$: tasa de cambio instantánea | Qué tan rápido cambia la función en cada punto. [→ Analogía: Velocímetro] |
| **Diferenciabilidad** | La derivada existe en un punto | La función es "suave" allí, sin picos ni esquinas |
| **Regla de la cadena** | Derivada de composición: $(f \circ g)' = f'(g(x)) \cdot g'(x)$ | Derivar "de afuera hacia adentro" multiplicando |
| **Derivada implícita** | Derivar una ecuación donde $y$ está mezclada con $x$ | Derivar aunque no tengas $y = f(x)$ explícitamente |
| **Punto crítico** | Donde $f'(x) = 0$ o no existe | Candidatos a máximos, mínimos o puntos de inflexión |
| **Máximo/Mínimo local** | Valor mayor/menor que todos los cercanos | Las "cimas" y "valles" de la función |
| **Punto de inflexión** | Donde la concavidad cambia | Donde la curva pasa de "sonreír" a "fruncir" o viceversa |
| **Concavidad** | Hacia dónde se "curva" la gráfica (arriba o abajo) | Si la curva "sostiene agua" (cóncava arriba) o no |

---

## Cálculo Integral

### Integral Indefinida

| Término | Definición | Intuición |
|---------|------------|-----------|
| **Antiderivada** | Función cuya derivada es la función dada | La operación inversa de derivar. [→ Analogía: Deshacer] |
| **Integral indefinida** | Familia de todas las antiderivadas: $F(x) + C$ | Todas las funciones que al derivar dan $f(x)$ |
| **Constante de integración** | La $C$ que aparece porque infinitas funciones tienen la misma derivada | La "información perdida" al derivar (derivada de constante es 0) |
| **Primitiva** | Sinónimo de antiderivada | Otra palabra para "la función antes de derivar" |

### Integral Definida

| Término | Definición | Intuición |
|---------|------------|-----------|
| **Suma de Riemann** | Aproximar área con rectángulos: $\sum f(x_i^*)\Delta x$ | Rellenar el área con "ladrillos" cada vez más delgados. [→ Analogía: Pixelación] |
| **Integral definida** | Límite de sumas de Riemann: área con signo bajo la curva | El área "exacta" cuando los ladrillos son infinitamente delgados |
| **Teorema Fundamental del Cálculo** | Conecta integral definida con antiderivada: $\int_a^b f = F(b) - F(a)$ | La derivada y la integral son operaciones inversas |
| **Valor promedio** | $\frac{1}{b-a}\int_a^b f(x)dx$ | La "altura promedio" de la función en el intervalo |

### Técnicas de Integración

| Término | Definición | Intuición |
|---------|------------|-----------|
| **Sustitución** | Cambiar variable para simplificar: $u = g(x)$ | "Renombrar" parte de la expresión para que se vea más simple |
| **Integración por partes** | $\int u\,dv = uv - \int v\,du$ | "Pasar" la derivada de un factor al otro |
| **Fracciones parciales** | Descomponer fracción racional en suma de fracciones simples | "Desarmar" una fracción complicada en pedazos integrables |
| **Sustitución trigonométrica** | Usar identidades trig para eliminar raíces cuadradas | Convertir raíces en expresiones trigonométricas manejables |

### Integrales Impropias

| Término | Definición | Intuición |
|---------|------------|-----------|
| **Integral impropia** | Integral con límite infinito o integrando discontinuo | Área que se extiende "hasta el infinito" o pasa por un "agujero" |
| **Convergencia** | La integral impropia tiene un valor finito | El área infinita suma un número finito |
| **Divergencia** | La integral impropia no tiene valor finito | El área "se escapa" al infinito |
| **Criterio de comparación** | Comparar con integrales conocidas para determinar convergencia | Si una integral más grande converge, la pequeña también |

---

## Ecuaciones Diferenciales

### Conceptos Básicos

| Término | Definición | Intuición |
|---------|------------|-----------|
| **Ecuación diferencial** | Ecuación que involucra derivadas de una función desconocida | Una "pista" sobre cómo cambia algo, de la cual deducir qué es. [→ Analogía: Reconstrucción] |
| **EDO** | Ecuación diferencial ordinaria: una variable independiente | Cambio respecto a una sola cosa (usualmente tiempo) |
| **EDP** | Ecuación diferencial parcial: varias variables independientes | Cambio respecto a varias cosas simultáneamente |
| **Orden** | La derivada más alta que aparece | Cuántas veces hay que integrar para resolver |
| **Linealidad** | La función incógnita y sus derivadas aparecen linealmente | Se puede aplicar superposición de soluciones |
| **Problema de valor inicial (PVI)** | EDO + condiciones en un punto | Conoces dónde empiezas, quieres saber a dónde vas |
| **Problema de valores en la frontera** | EDO + condiciones en varios puntos | Conoces los extremos, quieres el camino entre ellos |

### Métodos de Solución

| Término | Definición | Intuición |
|---------|------------|-----------|
| **Variables separables** | EDO donde se pueden separar $y$ y $x$ a cada lado | Juntar todo lo de $y$ con $dy$ y todo lo de $x$ con $dx$ |
| **Factor integrante** | Función que multiplica para hacer la ecuación exacta | Un "arreglo" que vuelve la ecuación integrable directamente |
| **Ecuación homogénea** | EDO lineal con término independiente cero | La versión "limpia" sin término que "empuja" |
| **Solución particular** | Una solución específica de una EDO no homogénea | Un ejemplo concreto que satisface la ecuación completa |
| **Solución general** | Todas las soluciones: homogénea + particular | La familia completa de soluciones |
| **Wronskiano** | Determinante que mide independencia lineal de soluciones | Verifica si las soluciones son "diferentes" |

### Sistemas y Transformadas

| Término | Definición | Intuición |
|---------|------------|-----------|
| **Sistema de EDO** | Varias EDO acopladas | Múltiples cantidades que cambian e influyen entre sí |
| **Transformada de Laplace** | $\mathcal{L}\{f(t)\} = \int_0^\infty e^{-st}f(t)dt$ | Convertir EDO en álgebra, resolver, y "des-convertir". [→ Analogía: Traductor] |
| **Función de transferencia** | Relación entrada/salida en dominio de Laplace | La "firma" de un sistema lineal |
| **Convolución** | Operación que combina dos funciones: $(f * g)(t)$ | La salida de un sistema ante una entrada general |

---

## Métodos Numéricos

### Raíces de Ecuaciones

| Término | Definición | Intuición |
|---------|------------|-----------|
| **Raíz numérica** | Aproximación a donde $f(x) = 0$ | Encontrar el cero "a ojo" refinando paso a paso. [→ Analogía: Búsqueda del tesoro] |
| **Método de bisección** | Partir intervalo a la mitad repetidamente | Juego de "frío/caliente" dividiendo siempre por la mitad |
| **Método de Newton-Raphson** | Usar tangente para aproximar: $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$ | "Deslizarse" por la tangente hacia el eje $x$ |
| **Convergencia** | Qué tan rápido se acerca a la solución | Cuántos pasos para alcanzar cierta precisión |
| **Orden de convergencia** | Potencia que mide velocidad de convergencia | Cuántos dígitos correctos se ganan por iteración |
| **Criterio de paro** | Condición para detener las iteraciones | Cuándo estamos "suficientemente cerca" |

### Interpolación

| Término | Definición | Intuición |
|---------|------------|-----------|
| **Interpolación** | Construir función que pase por puntos dados | "Conectar los puntos" con una curva suave. [→ Analogía: Dibujar entre puntos] |
| **Polinomio de Lagrange** | Interpolación usando productos de factores lineales | Una fórmula directa para el polinomio que pasa por los puntos |
| **Diferencias divididas** | Coeficientes para interpolación de Newton | Otra forma de construir el polinomio interpolador |
| **Spline cúbico** | Polinomios cúbicos por tramos, suaves en las uniones | Curva flexible que no oscila bruscamente |
| **Error de interpolación** | Diferencia entre función real e interpolador | Cuánto nos equivocamos entre los puntos conocidos |
| **Fenómeno de Runge** | Oscilaciones al usar polinomios de grado alto | Por qué a veces "más puntos" da peor resultado |

### Integración Numérica

| Término | Definición | Intuición |
|---------|------------|-----------|
| **Cuadratura** | Aproximación numérica de una integral definida | Calcular áreas usando geometría simple. [→ Analogía: Contar cuadritos] |
| **Regla del trapecio** | Aproximar área con trapecios | Conectar puntos con líneas rectas y sumar áreas |
| **Regla de Simpson** | Aproximar con parábolas cada 3 puntos | Curvas más suaves que rectas dan mejor aproximación |
| **Método de Romberg** | Mejorar trapecio con extrapolación de Richardson | "Adivinar" el límite a partir de aproximaciones sucesivas |
| **Cuadratura de Gauss** | Elegir puntos óptimos para máxima precisión | Puntos "inteligentes" dan mucha precisión con pocas evaluaciones |

### EDO Numéricas

| Término | Definición | Intuición |
|---------|------------|-----------|
| **Método de Euler** | Aproximar con recta tangente: $y_{n+1} = y_n + hf(x_n, y_n)$ | Caminar en línea recta siguiendo la pendiente actual. [→ Analogía: GPS con actualizaciones lentas] |
| **Método de Heun** | Promediar pendientes al inicio y fin del paso | Mirar adelante antes de dar el paso |
| **Runge-Kutta 4** | Combinar 4 evaluaciones de pendiente por paso | El "estándar de oro" para precisión vs. costo |
| **Métodos multipaso** | Usar información de pasos anteriores | Recordar el camino recorrido para predecir mejor |
| **Estabilidad numérica** | La solución numérica no "explota" | El método se comporta bien aunque haya pequeños errores |
| **EDO rígida (stiff)** | EDO con componentes de escalas muy diferentes | Algunos cambios son muy rápidos, otros muy lentos |
| **Paso adaptativo** | Ajustar $h$ según el error estimado | Pasos pequeños donde es difícil, grandes donde es fácil |

---

## Conceptos Abstractos y Analogías

<!--
IA: Esta sección contiene analogías y conceptos fuera de las matemáticas puras.
Úsalas para explicaciones iniciales o cuando el estudiante tenga dificultad con la abstracción.
Referencia: [→ Analogía: Nombre] en las definiciones técnicas.
-->

### Analogías para Explicar Conceptos

| Analogía | Concepto matemático | Descripción |
|----------|---------------------|-------------|
| **Máquina** | Función | Una máquina que toma entrada y produce salida. Siempre da el mismo resultado para la misma entrada. No puede dar dos resultados diferentes. |
| **Velocímetro** | Derivada | El velocímetro de un carro muestra la velocidad instantánea, no cuánto has recorrido. La derivada es el "velocímetro" de cualquier función. |
| **Odómetro** | Integral | El odómetro suma todo el camino recorrido. La integral "acumula" todo lo que ha pasado. |
| **Destino** | Límite | Un avión puede acercarse a un aeropuerto sin nunca aterrizar (asíntota) o puede aterrizar suavemente (límite existe). El destino está determinado aunque no llegues. |
| **Traductor** | Transformada de Laplace | Traduce un problema difícil (EDO) a un idioma más fácil (álgebra), resuelve, y traduce de vuelta. |
| **GPS con actualizaciones lentas** | Método de Euler | Un GPS que solo actualiza cada 10 segundos te dice "sigue recto" aunque la carretera curve. Con actualizaciones más frecuentes (paso $h$ pequeño), sigue mejor el camino. |
| **Búsqueda del tesoro** | Métodos de raíces | Bisección: "¿más frío o más caliente?" dividiendo por la mitad. Newton: seguir una pista directa (la tangente). |
| **Dibujar entre puntos** | Interpolación | Dado un dibujo con solo algunos puntos, conectarlos suavemente para reconstruir la imagen. |
| **Pixelación** | Suma de Riemann | Una imagen de baja resolución (pocos píxeles) aproxima una imagen real. Con más píxeles (rectángulos más delgados), se ve mejor. |
| **Reconstrucción** | Ecuación diferencial | Un detective tiene pistas sobre cómo cambiaron las cosas (derivadas) y debe reconstruir qué pasó (la función). |
| **Hoja de cálculo** | Matriz | Una tabla de Excel es una matriz. Las fórmulas que combinan celdas son operaciones matriciales. |
| **Factor de escala** | Determinante | Si aplicas una transformación a una figura, el determinante dice cuántas veces más grande (o pequeña) queda el área. Cero significa que la aplastaste a una línea. |
| **Arena de juego** | Espacio vectorial | Un lugar donde puedes "jugar" con vectores: sumarlos, escalarlos. Las reglas del juego son los axiomas. |
| **Sistema de coordenadas** | Base | Diferentes formas de describir el mismo punto. GPS (lat, long) vs. direcciones desde una esquina. La base es tu sistema de referencia. |
| **Transformación geométrica** | Transformación lineal | Rotar, estirar, reflejar, proyectar. Todas son transformaciones lineales que puedes describir con matrices. |
| **Resonancia** | Eigenvalor | Cuando empujas un columpio con su frecuencia natural (eigenvalor), la amplitud crece. Cada sistema tiene sus "frecuencias especiales". |
| **Contador cuadritos** | Cuadratura numérica | Estimar el área de una figura irregular contando los cuadritos de papel milimetrado que cubre. |

### Conceptos de Pensamiento Matemático

| Concepto | Descripción | Uso en matemáticas |
|----------|-------------|-------------------|
| **Abstracción** | Ignorar detalles irrelevantes para enfocarse en la estructura esencial | La clave del álgebra lineal: vectores pueden ser flechas, funciones, señales, etc. Lo importante son las operaciones. |
| **Generalización** | Extender un resultado de casos particulares a reglas generales | De "3² + 4² = 5²" a "Para cualquier triángulo rectángulo, $a² + b² = c²$" |
| **Analogía estructural** | Reconocer que sistemas diferentes siguen las mismas reglas | Suma de números, suma de vectores, suma de funciones: todas siguen las mismas leyes. |
| **Invariante** | Propiedad que no cambia bajo ciertas operaciones | El determinante no cambia si sumas múltiplo de una fila a otra. |
| **Dualidad** | Dos perspectivas complementarias del mismo objeto | Punto-recta en geometría proyectiva; tiempo-frecuencia en Fourier. |
| **Aproximación sucesiva** | Acercarse a la respuesta por pasos, cada vez más preciso | Base de todos los métodos numéricos: empezar con algo y mejorarlo. |
| **Linealidad** | Principio de superposición: el todo es la suma de las partes | Si conoces la respuesta a problemas simples, puedes combinarlas para problemas complejos. |
| **Continuidad del pensamiento** | Pequeños cambios en entrada producen pequeños cambios en salida | Intuición de que las matemáticas son "suaves" y "predecibles" |
| **Existencia vs. Construcción** | Saber que algo existe vs. saber cómo encontrarlo | Teoremas de existencia vs. métodos numéricos para calcular. |

### Vocabulario de Precisión

| Término | Significado preciso | Error común |
|---------|---------------------|-------------|
| **Implica (⇒)** | Si A entonces B | No significa "A y B son equivalentes" |
| **Si y solo si (⇔)** | A implica B Y B implica A | Equivalencia completa, no solo una dirección |
| **Para todo (∀)** | Sin excepción, cada uno | No "para la mayoría" o "usualmente" |
| **Existe (∃)** | Al menos uno | No necesariamente único |
| **Tal que** | Con la propiedad de que | Introduce una condición |
| **Necesario** | Sin esto, no puede ser verdad | Condición mínima |
| **Suficiente** | Con esto, garantizado que es verdad | Condición que basta |
| **Trivial** | Obvio o caso degenerado | No significa "fácil" necesariamente |
| **Bien definido** | No depende de cómo lo calcules | El resultado es único |

---

## Notación Común

### Símbolos Fundamentales

| Símbolo | Significado | Ejemplo |
|---------|-------------|---------|
| $f(x)$ | Función de $x$ | $f(x) = x^2$ |
| $f: A \to B$ | Función de $A$ a $B$ | $f: \mathbb{R} \to \mathbb{R}$ |
| $f \circ g$ | Composición | $(f \circ g)(x) = f(g(x))$ |
| $f^{-1}$ | Función inversa | $\sin^{-1}(x) = \arcsin(x)$ |
| $\lim_{x \to a}$ | Límite cuando $x$ tiende a $a$ | $\lim_{x \to 0} \frac{\sin x}{x} = 1$ |
| $\frac{dy}{dx}$ o $y'$ | Derivada de $y$ respecto a $x$ | $\frac{d}{dx}(x^2) = 2x$ |
| $\frac{\partial f}{\partial x}$ | Derivada parcial | Para funciones de varias variables |
| $\int f(x)\,dx$ | Integral indefinida | $\int x\,dx = \frac{x^2}{2} + C$ |
| $\int_a^b f(x)\,dx$ | Integral definida | $\int_0^1 x\,dx = \frac{1}{2}$ |

### Símbolos de Conjuntos

| Símbolo | Significado | Ejemplo |
|---------|-------------|---------|
| $\mathbb{N}$ | Números naturales | $\{1, 2, 3, ...\}$ |
| $\mathbb{Z}$ | Números enteros | $\{..., -2, -1, 0, 1, 2, ...\}$ |
| $\mathbb{Q}$ | Números racionales | Fracciones $p/q$ |
| $\mathbb{R}$ | Números reales | Toda la recta numérica |
| $\mathbb{C}$ | Números complejos | $a + bi$ |
| $\in$ | Pertenece a | $3 \in \mathbb{N}$ |
| $\subset$ | Subconjunto | $\mathbb{N} \subset \mathbb{Z}$ |
| $\cup$ | Unión | $A \cup B$ |
| $\cap$ | Intersección | $A \cap B$ |
| $\emptyset$ | Conjunto vacío | Sin elementos |

### Símbolos de Álgebra Lineal

| Símbolo | Significado | Ejemplo |
|---------|-------------|---------|
| $\vec{v}$ o $\mathbf{v}$ | Vector | $\vec{v} = (1, 2, 3)$ |
| $\|\vec{v}\|$ | Norma (longitud) | $\|(3,4)\| = 5$ |
| $\vec{u} \cdot \vec{v}$ | Producto punto | $\vec{u} \cdot \vec{v} = u_1v_1 + u_2v_2 + ...$ |
| $\vec{u} \times \vec{v}$ | Producto cruz | Vector perpendicular (en $\mathbb{R}^3$) |
| $A^T$ | Transpuesta | Intercambiar filas y columnas |
| $A^{-1}$ | Inversa | $AA^{-1} = I$ |
| $\det(A)$ o $\lvert A \rvert$ | Determinante | Número que caracteriza $A$ |
| $\text{tr}(A)$ | Traza | Suma de la diagonal |
| $\text{ker}(A)$ | Núcleo | Soluciones de $Ax = 0$ |
| $\text{im}(A)$ | Imagen | Columnas de $A$ generan |
| $\text{dim}(V)$ | Dimensión | Número de vectores en base |

### Símbolos de Ecuaciones Diferenciales

| Símbolo | Significado | Ejemplo |
|---------|-------------|---------|
| $y'$ | Primera derivada | $\frac{dy}{dx}$ |
| $y''$ | Segunda derivada | $\frac{d^2y}{dx^2}$ |
| $y^{(n)}$ | Derivada $n$-ésima | $\frac{d^ny}{dx^n}$ |
| $\mathcal{L}\{f\}$ | Transformada de Laplace | $\mathcal{L}\{e^{at}\} = \frac{1}{s-a}$ |
| $\mathcal{L}^{-1}\{F\}$ | Transformada inversa | Recuperar $f(t)$ de $F(s)$ |
| $\delta(t)$ | Delta de Dirac | Impulso unitario |
| $u(t)$ | Escalón unitario | 0 para $t<0$, 1 para $t≥0$ |

---

<!--
IA: Este glosario es referencia primaria para terminología.
- Usa las analogías para explicaciones iniciales
- Las referencias [→ término] conectan conceptos relacionados
- Actualiza cuando se introduzcan nuevos conceptos en el repositorio
- Para estudiantes con dificultad, comienza siempre con la columna "Intuición"
-->
