<!--
HUMANO:
Teoría avanzada de aritmética, orientada a ingeniería. No incluye métodos ni ejercicios.

IA:
Contenido puramente teórico; no mezclar con procedimientos ni soluciones.

---
content_type: theory
expected_output:
  default: markdown
audience: self-study
formality: technical
---
-->

# Fundamentos de Aritmética Superior y Estructuras Algebraicas Básicas

## 1. Rol de la aritmética en la ingeniería

La aritmética (trabajo con $\mathbb{N}$ y sus extensiones) es la base lógica para estructuras de mayor complejidad. En ingeniería sustenta:
- Diseño de algoritmos discretos y análisis de complejidad.
- Criptografía y codificación (factorización y congruencias).
- Análisis de señales y discretización del continuo.

El Teorema Fundamental de la Aritmética (TFA) es el principio organizador: asegura la descomposición única en primos, análogo a la descomposición atómica en química.

## 2. Fundamentación axiomática de $\mathbb{N}$ (Axiomas de Peano)

### 2.1 Axiomas de Peano
Sea $N$ un conjunto y $S: N \to N$ la función sucesor. Existe un elemento distinguido $1 \in N$ tal que:
1. **Existencia del elemento inicial:** $1 \in N$.
2. **Clausura bajo sucesión:** $\forall n \in N,\ S(n) \in N$.
3. **Inyectividad:** $S(n)=S(m) \Rightarrow n=m$.
4. **Elemento no sucesor:** $\nexists n \in N$ tal que $S(n)=1$.
5. **Inducción:** Si $A \subseteq N$ cumple $1 \in A$ y $n \in A \Rightarrow S(n) \in A$, entonces $A=N$.

### 2.2 Inducción y buen orden
- **Principio de inducción:** permite probar enunciados $P(n)$ para todo $n \in N$.
- **Principio de buen orden:** todo subconjunto no vacío de $N$ tiene mínimo. Es equivalente al principio de inducción y clave para demostrar la factorización prima.

## 3. Operaciones aritméticas y propiedades algebraicas

### 3.1 Definiciones recursivas
- **Suma:** $n+1 = S(n)$; $n+S(m)=S(n+m)$.
- **Producto:** $n\cdot 1 = n$; $n\cdot S(m)=n\cdot m + n$.

### 3.2 Propiedades estructurales (para $a,b,c \in N$)
- Asociatividad: $(a+b)+c=a+(b+c)$ y $(a\cdot b)\cdot c=a\cdot(b\cdot c)$.
- Conmutatividad: $a+b=b+a$ y $a\cdot b=b\cdot a$.
- Distributividad: $a\cdot(b+c)=a\cdot b + a\cdot c$.
- Cancelación multiplicativa: si $a\cdot b=a\cdot c$ y $a\neq 0$, entonces $b=c$.

### 3.3 Principio de inducción y buen orden (enunciados formales)

- **Principio de inducción:** si $P(1)$ es verdadero y $P(k)\Rightarrow P(k+1)$ para todo $k\in N$, entonces $P(n)$ es verdadero para todo $n\in N$.
- **Principio de buen orden:** todo subconjunto no vacío de $N$ tiene elemento mínimo. Es equivalente al principio de inducción y se usa para demostrar existencia de factorización prima.

## 4. Teoría de la divisibilidad

### 4.1 Definición
Para $a,b \in N$, $a$ divide a $b$ ($a\mid b$) si $\exists k \in N$ tal que $b=a\,k$.

### 4.2 Propiedades
- Reflexividad: $a\mid a$.
- Transitividad: $a\mid b$ y $b\mid c \Rightarrow a\mid c$.
- Antisimetría: $a\mid b$ y $b\mid a \Rightarrow a=b$.
- Comparabilidad parcial: si $a\mid b$ y $a\neq b$, entonces $a<b$.

## 5. Números primos e irreducibles

### 5.1 Definiciones
Sea $p>1$.
- **Irreducible:** sus únicos divisores positivos son $1$ y $p$.
- **Primo:** si $p\mid ab$ entonces $p\mid a$ o $p\mid b$.

### 5.2 Lema de Euclides
En $\mathbb{N}$, todo irreducible es primo. Por tanto, en $\mathbb{N}$ y $\mathbb{Z}$ ambos conceptos coinciden.

## 6. Teorema Fundamental de la Aritmética (TFA)

### 6.1 Enunciado
Para todo $n>1$ existen primos $p_1,\dots,p_k$ tales que $n=p_1p_2\cdots p_k$. Esta factorización es única salvo el orden de los factores.

### 6.2 Forma canónica
Todo $n>1$ puede escribirse como $n=\prod_{i=1}^r p_i^{\alpha_i}$ con $p_i$ primos distintos y $\alpha_i\in \mathbb{N}$.

### 6.3 Esbozo de prueba (existencia y unicidad)

- **Existencia:** por buen orden, si hubiera un $n>1$ sin factorización prima, el mínimo tal $n$ no sería primo y se escribiría $n=ab$ con $1<a,b<n$, contradiciendo la minimalidad al factorizar $a$ y $b$.
- **Unicidad:** si $n=p_1\cdots p_k=q_1\cdots q_m$, el Lema de Euclides implica que $p_1$ divide a alguno de los $q_j$; como todos son primos, $p_1=q_j$. Cancelando y repitiendo por inducción se obtiene igualdad de conjuntos de primos.

## 7. Consecuencias estructurales

Dados $a,b>0$ con descomposiciones $a=\prod p_i^{\alpha_i}$, $b=\prod p_i^{\beta_i}$ (exponentes cero si un primo no aparece):
- Divisibilidad: $a\mid b \iff \alpha_i \le \beta_i\ \forall i$.
- **Definición formal de $\gcd$:** $\gcd(a,b)$ es el mayor entero positivo que divide simultáneamente a $a$ y $b$.
- **Definición formal de $\operatorname{mcm}$:** $\operatorname{mcm}(a,b)$ es el menor entero positivo múltiplo de ambos.
- Fórmula por exponentes: $\gcd(a,b)=\prod p_i^{\min(\alpha_i,\beta_i)}$.
- Fórmula por exponentes: $\operatorname{mcm}(a,b)=\prod p_i^{\max(\alpha_i,\beta_i)}$.
- Relación fundamental: $a\cdot b = \gcd(a,b)\cdot \operatorname{mcm}(a,b)$.

## 8. Nociones puente y conexiones

- **Álgebra abstracta:** $\mathbb{N}$ bajo multiplicación es un monoide conmutativo libre generado por los primos; $\mathbb{Z}$ es un dominio de factorización única.
- **Lógica matemática:** la codificación de enunciados en $\mathbb{N}$ (Gödel) se apoya en la unicidad de la factorización.
- **Análisis:** la construcción de $\mathbb{N}\subset \mathbb{Z}\subset \mathbb{Q}\subset \mathbb{R}$ parte de estas propiedades; la densidad de $\mathbb{Q}$ en $\mathbb{R}$ y la completitud de $\mathbb{R}$ dependen de esta base.

---

<!--
IA: No incluir ejercicios ni pasos de método aquí. Para problemas, usa problems/. Para procedimientos, usa methods/.
-->
