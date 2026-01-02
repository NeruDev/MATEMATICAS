<!--
HUMANO:
Referencia completa de símbolos matemáticos usados en el repositorio.

IA:
Tablas organizadas por tipo de símbolo y materia.

---
content_type: reference
expected_output:
  default: markdown
audience: self-study
---
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../WIKI_INDEX.md) | [📚 Glosario](../../../glossary.md)

---

# Simbología Matemática

Guía de referencia rápida para todos los símbolos matemáticos utilizados en este repositorio.

---

## 1. Aritmética y Álgebra Básica

### Operaciones Fundamentales

| Símbolo | Nombre | LaTeX | Uso / Significado |
| :---: | :--- | :--- | :--- |
| $+$ | Suma | `+` | Adición |
| $-$ | Resta / Negativo | `-` | Sustracción o inverso aditivo |
| $\times$ | Producto cruz | `\times` | Multiplicación aritmética o producto cruz |
| $\cdot$ | Producto punto | `\cdot` | Multiplicación algebraica o producto escalar |
| $/$ | División | `/` | Fracción en línea |
| $\div$ | División | `\div` | Operador clásico de división |

### Relaciones de Igualdad y Orden

| Símbolo | Nombre | LaTeX | Uso / Significado |
| :---: | :--- | :--- | :--- |
| $=$ | Igualdad | `=` | Identidad de valores |
| $\neq$ | Desigualdad | `\neq` | No son iguales |
| $\approx$ | Aproximación | `\approx` | Valor numérico cercano |
| $\sim$ | Asintóticamente | `\sim` | Comportamiento similar (o distribución) |
| $\equiv$ | Idénticamente igual | `\equiv` | Igualdad en todo el [dominio](../../../glossary.md#dominio) |
| $\propto$ | Proporcional | `\propto` | Relación de proporcionalidad ($y=kx$) |
| $<$ | [Menor](../../../glossary.md#menor) que | `<` | Comparación estricta |
| $>$ | Mayor que | `>` | Comparación estricta |
| $\leq$ | [Menor](../../../glossary.md#menor) o igual | `\leq` | Comparación inclusiva |
| $\geq$ | Mayor o igual | `\geq` | Comparación inclusiva |
| $\ll$ | Mucho menor que | `\ll` | Despreciable frente a otro valor |
| $\gg$ | Mucho mayor que | `\gg` | Dominante frente a otro valor |
| $\pm$ | Más-menos | `\pm` | Tolerancia o solución dual |
| $\mp$ | Menos-más | `\mp` | Signo opuesto a $\pm$ |

### Notación de Funciones y Potencias

| Símbolo | Nombre | LaTeX | Uso / Significado |
| :---: | :--- | :--- | :--- |
| $x^n$ | Potencia | `x^n` | $x$ elevado a la $n$ |
| $\sqrt{x}$ | Raíz cuadrada | `\sqrt{x}` | $x^{1/2}$ |
| $\sqrt[n]{x}$ | Raíz n-ésima | `\sqrt[n]{x}` | $x^{1/n}$ |
| $\lvert x \rvert$ | Valor absoluto | `\lvert x \rvert` | Magnitud sin signo |
| $n!$ | Factorial | `n!` | Producto $1 \cdot 2 \cdots n$ |
| $\binom{n}{k}$ | Coeficiente binomial | `\binom{n}{k}` | Combinaciones de $n$ en $k$ |
| $\lfloor x \rfloor$ | Piso | `\lfloor x \rfloor` | Mayor entero $\leq x$ |
| $\lceil x \rceil$ | Techo | `\lceil x \rceil$ | Menor entero $\geq x$ |

---

## 2. Lógica y Conjuntos

### Cuantificadores

| Símbolo | Nombre | LaTeX | Uso / Significado |
| :---: | :--- | :--- | :--- |
| $\forall$ | Para todo | `\forall` | Cuantificador universal |
| $\exists$ | Existe | `\exists` | Cuantificador existencial |
| $\exists!$ | Existe único | `\exists!` | Existe exactamente uno |
| $\nexists$ | No existe | `\nexists` | Negación de existencia |

### Operaciones con Conjuntos

| Símbolo | Nombre | LaTeX | Uso / Significado |
| :---: | :--- | :--- | :--- |
| $\in$ | Pertenece | `\in` | Elemento dentro de conjunto |
| $\notin$ | No pertenece | `\notin` | Elemento fuera de conjunto |
| $\subset$ | Subconjunto propio | `\subset` | Contenido estrictamente |
| $\subseteq$ | Subconjunto | `\subseteq` | Contenido o igual |
| $\supset$ | Superconjunto | `\supset` | Contiene estrictamente |
| $\supseteq$ | Superconjunto o igual | `\supseteq` | Contiene o igual |
| $\cup$ | Unión | `\cup` | Elementos en A o B |
| $\cap$ | Intersección | `\cap` | Elementos en A y B |
| $\setminus$ | Diferencia | `\setminus` | Elementos en A pero no en B |
| $\emptyset$ | Vacío | `\emptyset` | Conjunto nulo |
| $\mathcal{P}(A)$ | Conjunto potencia | `\mathcal{P}(A)` | Todos los subconjuntos de A |
| $A^c$ | Complemento | `A^c` | Elementos no en A |

### Conjuntos Numéricos

| Símbolo | Nombre | LaTeX | Descripción |
| :---: | :--- | :--- | :--- |
| $\mathbb{N}$ | Naturales | `\mathbb{N}` | $\{1, 2, 3, \ldots\}$ |
| $\mathbb{Z}$ | Enteros | `\mathbb{Z}` | $\{\ldots, -1, 0, 1, \ldots\}$ |
| $\mathbb{Q}$ | Racionales | `\mathbb{Q}` | Fracciones $p/q$ |
| $\mathbb{R}$ | Reales | `\mathbb{R}` | Toda la recta numérica |
| $\mathbb{C}$ | Complejos | `\mathbb{C}` | Números $a + bi$ |
| $\mathbb{R}^n$ | Espacio n-dimensional | `\mathbb{R}^n` | n-tuplas de reales |

### Conectores Lógicos

| Símbolo | Nombre | LaTeX | Uso / Significado |
| :---: | :--- | :--- | :--- |
| $\land$ | Conjunción (Y) | `\land` | Ambas verdaderas |
| $\lor$ | Disyunción (O) | `\lor` | Al menos una verdadera |
| $\neg$ | Negación | `\neg` | Inversión de valor de verdad |
| $\Rightarrow$ | Implicación | `\Rightarrow` | Si P entonces Q |
| $\Leftarrow$ | Implicación inversa | `\Leftarrow` | Q implica P |
| $\Leftrightarrow$ | Si y solo si | `\Leftrightarrow` | Equivalencia lógica |
| $\therefore$ | Por lo tanto | `\therefore` | Conclusión |
| $\because$ | Porque | `\because` | Justificación |

---

## 3. Cálculo Diferencial

### Límites

| Símbolo | Nombre | LaTeX | Uso / Significado |
| :---: | :--- | :--- | :--- |
| $\lim$ | [Límite](../../../glossary.md#limite) | `\lim` | Valor al que tiende una [función](../../../glossary.md#funcion) |
| $\lim_{x \to a}$ | [Límite](../../../glossary.md#limite) cuando x tiende a a | `\lim_{x \to a}` | Comportamiento cerca de $a$ |
| $\lim_{x \to a^+}$ | Límite por derecha | `\lim_{x \to a^+}` | Aproximación desde valores mayores |
| $\lim_{x \to a^-}$ | Límite por izquierda | `\lim_{x \to a^-}` | Aproximación desde valores menores |
| $\infty$ | Infinito | `\infty` | Concepto de no acotado |

### Derivadas

| Símbolo | Nombre | LaTeX | Uso / Significado |
| :---: | :--- | :--- | :--- |
| $f'(x)$ | [Derivada](../../../glossary.md#derivada) (prima) | `f'(x)` | Primera derivada de $f$ |
| $f''(x)$ | Segunda [derivada](../../../glossary.md#derivada) | `f''(x)` | Derivada de la derivada |
| $f^{(n)}(x)$ | Derivada n-ésima | `f^{(n)}(x)` | Derivada de [orden](../../../glossary.md#orden) $n$ |
| $\frac{dy}{dx}$ | Derivada (Leibniz) | `\frac{dy}{dx}` | Tasa de cambio instantánea |
| $\frac{d^n y}{dx^n}$ | Derivada n-ésima | `\frac{d^n y}{dx^n}` | Derivada de [orden](../../../glossary.md#orden) $n$ (Leibniz) |
| $\dot{y}$ | Derivada temporal | `\dot{y}` | $\frac{dy}{dt}$ (física) |
| $\ddot{y}$ | Segunda derivada temporal | `\ddot{y}$ | $\frac{d^2y}{dt^2}$ (aceleración) |

### Series y Sumatorias

| Símbolo | Nombre | LaTeX | Uso / Significado |
| :---: | :--- | :--- | :--- |
| $\sum$ | Sumatoria | `\sum` | Suma de serie discreta |
| $\sum_{i=1}^{n}$ | Suma de 1 a n | `\sum_{i=1}^{n}` | Suma finita indexada |
| $\prod$ | Productoria | `\prod` | Producto de secuencia |
| $\prod_{i=1}^{n}$ | Producto de 1 a n | `\prod_{i=1}^{n}` | Producto finito indexado |

---

## 4. Cálculo Integral

### Integrales

| Símbolo | Nombre | LaTeX | Uso / Significado |
| :---: | :--- | :--- | :--- |
| $\int$ | [Integral indefinida](../../../glossary.md#integral-indefinida) | `\int` | [Antiderivada](../../../glossary.md#antiderivada) |
| $\int_a^b$ | [Integral definida](../../../glossary.md#integral-definida) | `\int_a^b` | Área bajo la curva de $a$ a $b$ |
| $\oint$ | Integral de línea cerrada | `\oint` | Integral sobre curva cerrada |
| $\iint$ | Integral doble | `\iint` | Integral de superficie |
| $\iiint$ | Integral triple | `\iiint` | Integral de volumen |
| $\idotsint$ | Integral múltiple | `\idotsint` | Integral n-dimensional |

### Notación de Integración

| Símbolo | Nombre | LaTeX | Uso / Significado |
| :---: | :--- | :--- | :--- |
| $dx$ | Diferencial | `dx` | Elemento infinitesimal |
| $du$ | Cambio de variable | `du` | [Sustitución](../../../glossary.md#sustitucion) |
| $\Big\vert_a^b$ | Evaluación | `\Big\vert_a^b` | $F(b) - F(a)$ |
| $+ C$ | [Constante de integración](../../../glossary.md#constante-de-integracion) | `+ C` | Familia de antiderivadas |

---

## 5. Cálculo Vectorial

### Operador Nabla

| Símbolo | Nombre | LaTeX | Uso / Significado |
| :---: | :--- | :--- | :--- |
| $\nabla$ | Nabla (Del) | `\nabla` | Operador diferencial vectorial |
| $\nabla f$ | Gradiente | `\nabla f` | [Vector](../../../glossary.md#vector) de máxima variación |
| $\nabla \cdot \vec{F}$ | [Divergencia](../../../glossary.md#divergencia) | `\nabla \cdot \vec{F}` | Flujo escalar de un campo |
| $\nabla \times \vec{F}$ | Rotacional | `\nabla \times \vec{F}` | Tendencia a rotar (circulación) |
| $\nabla^2$ | Laplaciano | `\nabla^2` | [Divergencia](../../../glossary.md#divergencia) del gradiente |
| $\nabla^2 f$ | Laplaciano escalar | `\nabla^2 f` | $\frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} + \frac{\partial^2 f}{\partial z^2}$ |

### Derivadas Parciales

| Símbolo | Nombre | LaTeX | Uso / Significado |
| :---: | :--- | :--- | :--- |
| $\frac{\partial f}{\partial x}$ | Derivada parcial | `\frac{\partial f}{\partial x}` | Cambio respecto a una variable |
| $\frac{\partial^2 f}{\partial x^2}$ | Segunda parcial | `\frac{\partial^2 f}{\partial x^2}` | Derivada parcial de orden 2 |
| $\frac{\partial^2 f}{\partial x \partial y}$ | Parcial mixta | `\frac{\partial^2 f}{\partial x \partial y}` | Derivada respecto a $x$ luego $y$ |
| $f_x$ | Notación subíndice | `f_x` | $\frac{\partial f}{\partial x}$ |
| $f_{xy}$ | Mixta subíndice | `f_{xy}$ | $\frac{\partial^2 f}{\partial y \partial x}$ |

### Integrales de Línea y Superficie

| Símbolo | Nombre | LaTeX | Uso / Significado |
| :---: | :--- | :--- | :--- |
| $\int_C$ | Integral de línea | `\int_C` | Integral sobre curva C |
| $\oint_C$ | Integral cerrada | `\oint_C` | Integral sobre curva cerrada |
| $\iint_S$ | Integral de superficie | `\iint_S` | Integral sobre superficie S |
| $\oiint_S$ | Superficie cerrada | `\oiint_S` | Integral sobre superficie cerrada |
| $d\vec{r}$ | Elemento de arco vectorial | `d\vec{r}` | Desplazamiento infinitesimal |
| $d\vec{S}$ | Elemento de superficie | `d\vec{S}` | Área infinitesimal con normal |

---

## 6. Álgebra Lineal

### Matrices

| Símbolo | Nombre | LaTeX | Uso / Significado |
| :---: | :--- | :--- | :--- |
| $A^T$ | [Transpuesta](../../../glossary.md#transpuesta) | `A^T` o `A^\top` | Filas por columnas |
| $A^{-1}$ | Inversa | `A^{-1}` | [Matriz](../../../glossary.md#matriz) [tal que](../../../glossary.md#tal-que) $AA^{-1}=I$ |
| $A^\dagger$ | Hermitiana (adjunta) | `A^\dagger` | [Transpuesta](../../../glossary.md#transpuesta) conjugada |
| $A^*$ | Conjugada | `A^*` | Conjugado de cada entrada |
| $\det(A)$ | [Determinante](../../../glossary.md#determinante) | `\det(A)` | [Factor de escala](../../../glossary.md#factor-de-escala) / invertibilidad |
| $\text{tr}(A)$ | [Traza](../../../glossary.md#traza) | `\text{tr}(A)` | Suma de elementos diagonales |
| $\text{rank}(A)$ | Rango | `\text{rank}(A)` | [Dimensión](../../../glossary.md#dimension) del espacio columna |
| $I$ | [Matriz identidad](../../../glossary.md#matriz-identidad) | `I` | Diagonal de unos |
| $O$ | [Matriz](../../../glossary.md#matriz) cero | `O` | Todos los elementos son cero |

### Vectores

| Símbolo | Nombre | LaTeX | Uso / Significado |
| :---: | :--- | :--- | :--- |
| $\vec{v}$ | [Vector](../../../glossary.md#vector) (flecha) | `\vec{v}` | Notación física de vector |
| $\mathbf{v}$ | Vector (negrita) | `\mathbf{v}` | Notación algebraica de vector |
| $\hat{v}$ | Vector unitario | `\hat{v}` | Vector de magnitud 1 |
| $\hat{i}, \hat{j}, \hat{k}$ | [Base](../../../glossary.md#base) canónica | `\hat{i}, \hat{j}, \hat{k}` | Vectores unitarios en $\mathbb{R}^3$ |
| $\lVert v \rVert$ | Norma | `\lVert v \rVert` | Longitud/magnitud del vector |
| $\langle u, v \rangle$ | Producto interno | `\langle u, v \rangle` | [Generalización](../../../glossary.md#generalizacion) del producto punto |
| $u \cdot v$ | Producto punto | `u \cdot v` | Producto escalar |
| $u \times v$ | Producto cruz | `u \times v` | Producto vectorial |

### Eigenvalores y Espacios

| Símbolo | Nombre | LaTeX | Uso / Significado |
| :---: | :--- | :--- | :--- |
| $\lambda$ | Eigenvalor | `\lambda` | Valor propio |
| $\mathbf{v}$ | Eigenvector | `\mathbf{v}` | Vector propio |
| $\text{ker}(A)$ | Núcleo | `\text{ker}(A)` | Espacio nulo |
| $\text{Im}(A)$ | Imagen | `\text{Im}(A)$ | Espacio columna |
| $\dim(V)$ | [Dimensión](../../../glossary.md#dimension) | `\dim(V)` | Número de vectores en [base](../../../glossary.md#base) |
| $\text{span}\{v_1, \ldots\}$ | Espacio generado | `\text{span}\{\}` | Combinaciones lineales |
| $\oplus$ | Suma directa | `\oplus` | Suma de subespacios |
| $\otimes$ | Producto tensorial | `\otimes` | Producto de Kronecker |

---

## 7. Trigonometría y Geometría

### Funciones Trigonométricas

| Símbolo | Nombre | LaTeX | Uso / Significado |
| :---: | :--- | :--- | :--- |
| $\sin \theta$ | [Seno](../../../glossary.md#seno) | `\sin` | Razón opuesto/hipotenusa |
| $\cos \theta$ | [Coseno](../../../glossary.md#coseno) | `\cos` | Razón adyacente/hipotenusa |
| $\tan \theta$ | [Tangente](../../../glossary.md#tangente) | `\tan` | Razón [seno](../../../glossary.md#seno)/[coseno](../../../glossary.md#coseno) |
| $\cot \theta$ | Cotangente | `\cot` | Inverso de [tangente](../../../glossary.md#tangente) |
| $\sec \theta$ | Secante | `\sec` | Inverso de coseno |
| $\csc \theta$ | Cosecante | `\csc` | Inverso de seno |

### Funciones Trigonométricas Inversas

| Símbolo | Nombre | LaTeX | Uso / Significado |
| :---: | :--- | :--- | :--- |
| $\arcsin x$ | Arcoseno | `\arcsin` | Ángulo cuyo seno es $x$ |
| $\arccos x$ | Arcocoseno | `\arccos` | Ángulo cuyo coseno es $x$ |
| $\arctan x$ | Arcotangente | `\arctan` | Ángulo cuya tangente es $x$ |
| $\sin^{-1} x$ | Notación alternativa | `\sin^{-1}` | Equivalente a $\arcsin$ |

### Funciones Hiperbólicas

| Símbolo | Nombre | LaTeX | Uso / Significado |
| :---: | :--- | :--- | :--- |
| $\sinh x$ | Seno hiperbólico | `\sinh` | $\frac{e^x - e^{-x}}{2}$ |
| $\cosh x$ | Coseno hiperbólico | `\cosh` | $\frac{e^x + e^{-x}}{2}$ |
| $\tanh x$ | Tangente hiperbólica | `\tanh` | $\frac{\sinh x}{\cosh x}$ |
| $\text{sech } x$ | Secante hiperbólica | `\text{sech}` | $\frac{1}{\cosh x}$ |
| $\text{csch } x$ | Cosecante hiperbólica | `\text{csch}` | $\frac{1}{\sinh x}$ |
| $\coth x$ | Cotangente hiperbólica | `\coth` | $\frac{\cosh x}{\sinh x}$ |

### Notación Geométrica

| Símbolo | Nombre | LaTeX | Uso / Significado |
| :---: | :--- | :--- | :--- |
| $\angle$ | Ángulo | `\angle` | Denotación geométrica |
| $\perp$ | Perpendicular | `\perp` | Ángulo de 90 grados |
| $\parallel$ | Paralelo | `\parallel` | Líneas equidistantes |
| $\triangle$ | Triángulo | `\triangle` | Polígono de 3 lados |
| $\square$ | Cuadrado | `\square` | Polígono de 4 lados iguales |
| $\pi$ | Pi | `\pi` | Relación circunferencia/diámetro |
| $^\circ$ | Grados | `^\circ` | Medida angular sexagesimal |
| $\text{rad}$ | Radianes | `\text{rad}` | Medida angular natural |

---

## 8. Números Complejos

### Notación Básica

| Símbolo | Nombre | LaTeX | Uso / Significado |
| :---: | :--- | :--- | :--- |
| $i$ | Unidad imaginaria (Mat.) | `i` | $\sqrt{-1}$ (matemáticas) |
| $j$ | Unidad imaginaria (Ing.) | `j` | $\sqrt{-1}$ (ingeniería) |
| $z = a + bi$ | Forma rectangular | `a + bi` | Número complejo |
| $z = r e^{i\theta}$ | Forma exponencial | `r e^{i\theta}` | Notación polar exponencial |
| $z = r(\cos\theta + i\sin\theta)$ | Forma polar | `r\text{cis}\theta` | Notación trigonométrica |

### Operaciones

| Símbolo | Nombre | LaTeX | Uso / Significado |
| :---: | :--- | :--- | :--- |
| $\bar{z}$ | Conjugado | `\bar{z}` | Cambio de signo en parte imag. |
| $z^*$ | Conjugado (alternativo) | `z^*` | Equivalente a $\bar{z}$ |
| $\lvert z \rvert$ | Módulo | `\lvert z \rvert` | Magnitud: $\sqrt{a^2 + b^2}$ |
| $\Re(z)$ | Parte real | `\Re(z)` | Componente real |
| $\Im(z)$ | Parte imaginaria | `\Im(z)` | Componente imaginaria |
| $\arg(z)$ | Argumento | `\arg(z)` | Ángulo en forma polar |
| $\angle z$ | Ángulo/Fase | `\angle z` | Equivalente a argumento |

---

## 9. Ecuaciones Diferenciales

### Notación de EDO

| Símbolo | Nombre | LaTeX | Uso / Significado |
| :---: | :--- | :--- | :--- |
| $y'$ | Primera derivada | `y'` | $\frac{dy}{dx}$ |
| $y''$ | Segunda derivada | `y''` | $\frac{d^2y}{dx^2}$ |
| $y^{(n)}$ | Derivada n-ésima | `y^{(n)}` | $\frac{d^n y}{dx^n}$ |
| $\mathcal{L}\{f\}$ | [Transformada de Laplace](../../../glossary.md#transformada-de-laplace) | `\mathcal{L}\{f\}` | Transformación integral |
| $\mathcal{L}^{-1}\{F\}$ | Laplace inversa | `\mathcal{L}^{-1}\{F\}` | Transformación inversa |
| $s$ | Variable de Laplace | `s` | [Dominio](../../../glossary.md#dominio) de frecuencia |
| $\delta(t)$ | Delta de Dirac | `\delta(t)` | Impulso unitario |
| $u(t)$ | Escalón unitario | `u(t)` | [Función](../../../glossary.md#funcion) Heaviside |

### Operadores Diferenciales

| Símbolo | Nombre | LaTeX | Uso / Significado |
| :---: | :--- | :--- | :--- |
| $D$ | Operador derivada | `D` | $D = \frac{d}{dx}$ |
| $D^n$ | Operador n-ésima derivada | `D^n` | $\frac{d^n}{dx^n}$ |
| $L[y]$ | Operador lineal | `L[y]` | Operador diferencial lineal |

---

## 10. Métodos Numéricos

### Notación de Error

| Símbolo | Nombre | LaTeX | Uso / Significado |
| :---: | :--- | :--- | :--- |
| $\epsilon$ | Error absoluto | `\epsilon` | Diferencia valor real - aproximado |
| $\epsilon_r$ | Error relativo | `\epsilon_r` | $\frac{\epsilon}{\text{valor real}}$ |
| $O(h^n)$ | Orden de error | `O(h^n)` | Error proporcional a $h^n$ |
| $\approx$ | Aproximadamente | `\approx` | Valor numérico aproximado |

### Iteración

| Símbolo | Nombre | LaTeX | Uso / Significado |
| :---: | :--- | :--- | :--- |
| $x_n$ | Iteración n-ésima | `x_n` | Valor en paso $n$ |
| $x_{n+1}$ | Siguiente iteración | `x_{n+1}` | Nuevo valor calculado |
| $h$ | Tamaño de paso | `h` | Incremento en [métodos numéricos](../../../glossary.md#metodos-numericos) |
| $\Delta x$ | Incremento | `\Delta x` | Cambio en $x$ |

---

## 11. Estadística y Probabilidad

### Probabilidad

| Símbolo | Nombre | LaTeX | Uso / Significado |
| :---: | :--- | :--- | :--- |
| $P(A)$ | Probabilidad | `P(A)` | Probabilidad de evento A |
| $P(A \mid B)$ | Prob. condicional | `P(A \mid B)` | Probabilidad de A dado B |
| $P(A \cap B)$ | Prob. conjunta | `P(A \cap B)` | A y B simultáneamente |
| $P(A \cup B)$ | Prob. de unión | `P(A \cup B)` | A o B (o ambos) |
| $A'$ o $A^c$ | Complemento | `A'` o `A^c` | No ocurre A |

### Estadística Descriptiva

| Símbolo | Nombre | LaTeX | Uso / Significado |
| :---: | :--- | :--- | :--- |
| $\mu$ | Media poblacional | `\mu` | Promedio esperado |
| $\bar{x}$ | Media muestral | `\bar{x}` | Promedio de una muestra |
| $\sigma$ | Desviación estándar | `\sigma` | Dispersión de datos |
| $\sigma^2$ | Varianza | `\sigma^2` | Dispersión al cuadrado |
| $s$ | Desv. estándar muestral | `s` | Estimador de $\sigma$ |
| $s^2$ | Varianza muestral | `s^2` | Estimador de $\sigma^2$ |
| $\tilde{x}$ | Mediana | `\tilde{x}` | Valor central |

### Distribuciones y Esperanza

| Símbolo | Nombre | LaTeX | Uso / Significado |
| :---: | :--- | :--- | :--- |
| $E[X]$ | Esperanza | `E[X]` | Valor esperado |
| $\text{Var}(X)$ | Varianza | `\text{Var}(X)` | $E[(X-\mu)^2]$ |
| $\text{Cov}(X,Y)$ | Covarianza | `\text{Cov}(X,Y)` | Variación conjunta |
| $\rho_{XY}$ | Correlación | `\rho_{XY}` | Correlación lineal |
| $\mathcal{N}(\mu, \sigma^2)$ | Dist. Normal | `\mathcal{N}(\mu, \sigma^2)` | Campana de Gauss |
| $X \sim$ | Se distribuye como | `X \sim` | X tiene distribución... |

---

## Guía de Estilo LaTeX

### Convenciones del Repositorio

| Elemento | Notación Preferida | Evitar |
| :--- | :--- | :--- |
| Valor absoluto | `\lvert x \rvert` | `|x|` |
| Norma de vector | `\lVert v \rVert` | `||v||` |
| Derivada parcial | `\frac{\partial f}{\partial x}` | `df/dx` (para parciales) |
| Vectores | `\vec{v}` o `\mathbf{v}` | $v$ sin notación |
| Matrices | Mayúscula: $A$, $B$ | Minúscula |
| Escalares | Minúscula: $a$, $b$ | Mayúscula |
| Funciones | `\sin`, `\cos`, `\ln` | `sin`, `cos`, `ln` |
