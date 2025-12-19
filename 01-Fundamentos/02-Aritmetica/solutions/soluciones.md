# Soluciones — Aritmética

---

## 2.1 Sistemas numéricos

**1)** *Contexto: Aplicamos las definiciones de los conjuntos numéricos.*

| Número | Clasificación |
|--------|---------------|
| $-5$ | Entero (ℤ), Racional (ℚ) |
| $\frac{22}{7}$ | Racional (ℚ) — no es $\pi$ |
| $\sqrt{16} = 4$ | Natural (ℕ), Entero (ℤ), Racional (ℚ) |
| $\pi$ | Irracional |
| $0.\overline{6} = \frac{2}{3}$ | Racional (ℚ) |
| $\sqrt{2}$ | Irracional |

**2)** *Contexto: Verificamos las propiedades de inclusión de conjuntos numéricos.*
- Todo número natural es entero: **Verdadero** (ℕ ⊂ ℤ)
- Todo número entero es racional: **Verdadero** (ℤ ⊂ ℚ, pues $n = \frac{n}{1}$)
- $\sqrt{9}$ es irracional: **Falso** ($\sqrt{9} = 3$ ∈ ℕ)
- $0$ es un número natural: **Depende de la convención** (en algunas definiciones sí, en otras no)

**3)** *Contexto: Buscamos irracionales que al sumarse cancelen sus partes irracionales.*

$\sqrt{2}$ y $-\sqrt{2}$ son ambos irracionales, pero:
$$\sqrt{2} + (-\sqrt{2}) = 0 \in \mathbb{Q}$$

**4)** *Contexto: Usamos prueba por contradicción.*

Si $a + b$ fuera racional, entonces $b = (a + b) - a$ sería la diferencia de dos racionales, lo cual sería racional. Contradicción.
$$\boxed{a + b \text{ es irracional}}$$

**5)** *Contexto: Convertimos todo a decimales para comparar.*
- $\frac{3}{4} = 0.75$
- $0.7 = 0.70$
- $\frac{5}{7} \approx 0.714...$
- $0.\overline{72} = 0.7272...$

**Orden:** $0.7 < \frac{5}{7} < 0.\overline{72} < \frac{3}{4}$

**6)** *Contexto: Usamos la propiedad de densidad de ℚ.*

Un método simple: promedio $= \frac{\frac{1}{3} + \frac{1}{2}}{2} = \frac{\frac{5}{6}}{2} = \boxed{\frac{5}{12}}$

**7)** *Contexto: Un decimal es racional si y solo si es finito o periódico.*

Como el patrón no se repite (no es periódico), el número es **irracional**.

**8)** *Contexto: Convertimos decimal periódico a fracción.*

Sea $x = 3.\overline{14} = 3.141414...$
$$100x = 314.1414...$$
$$100x - x = 311$$
$$x = \frac{311}{99}$$

**9)** *Contexto: Usamos la definición de número racional.*

Si $a = \frac{p}{q}$ y $b = \frac{r}{s}$ con $p,q,r,s \in \mathbb{Z}$, $q,s \neq 0$:
$$a + b = \frac{ps + qr}{qs}$$
Como $ps + qr \in \mathbb{Z}$ y $qs \in \mathbb{Z} \setminus \{0\}$, entonces $a + b \in \mathbb{Q}$. ∎

**10)** *Contexto: Identificamos el rango de enteros.*

$\sqrt{50} \approx 7.07$, entonces $-\sqrt{50} \approx -7.07$

Enteros en $(-7.07, 7.07)$: $-7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7$

**Total: 15 enteros**

---

## 2.2 Operaciones fundamentales

**11)** *Contexto: Aplicamos PEMDAS — multiplicación y división antes de suma y resta.*
$$15 - 3 \times 4 + 8 \div 2 = 15 - 12 + 4 = \boxed{7}$$

**12)** *Contexto: Evaluamos numerador y denominador por separado.*
$$\frac{24 - 8 \times 2}{4 + 2^2} = \frac{24 - 16}{4 + 4} = \frac{8}{8} = \boxed{1}$$

**13)** *Contexto: Cuidado con los signos en potencias y productos.*
$$(-3)^2 - 3^2 + (-3)(-2) = 9 - 9 + 6 = \boxed{6}$$

**14)** *Contexto: Resolvemos de los paréntesis más internos hacia afuera.*
$$2 + 3 \times [4 - (5 - 12)] = 2 + 3 \times [4 - (-7)] = 2 + 3 \times 11 = 2 + 33 = \boxed{35}$$

**15)** *Contexto: Aplicamos la definición de valor absoluto.*
$$|{-5 + 3}| - |{-5}| + |{3}| = |{-2}| - 5 + 3 = 2 - 5 + 3 = \boxed{0}$$

**16)** *Contexto: Sustituimos valores y evaluamos.*
$$(-2)^3 - (3)^2 + (-2)(3) = -8 - 9 - 6 = \boxed{-23}$$

**17)** *Contexto: Expresamos todo en factores primos.*
$$\frac{(-2)^4 \times (-3)^2}{(-6)^2} = \frac{16 \times 9}{36} = \frac{144}{36} = \boxed{4}$$

**18)** *Contexto: Despejamos la variable.*
$$3x - 7 = 2x + 5 \Rightarrow x = 12$$

**19)** *Contexto: Evaluamos cada raíz por separado.*
$$\sqrt{25} - \sqrt{16} - \sqrt{9} = 5 - 4 - 3 = \boxed{-2}$$

**20)** *Contexto: $(-1)^n = 1$ si $n$ es par, $-1$ si $n$ es impar.*
$$(-1)^{100} + (-1)^{101} + (-1)^{102} = 1 + (-1) + 1 = \boxed{1}$$

---

## 2.3 Divisibilidad y números primos

**21)** *Contexto: Usamos criterios de divisibilidad.*
- Suma de dígitos: $2 + 8 + 4 + 7 = 21$
- 21 es divisible por 3 ✓ → 2847 es divisible por 3
- 21 no es divisible por 9 ✗ → 2847 no es divisible por 9

**22)** *Contexto: $60 = 2^2 \times 3 \times 5$*

Divisores: $1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60$ (12 divisores)

**23)** *Contexto: Dividimos sucesivamente por primos.*
$$504 = 2 \times 252 = 2^2 \times 126 = 2^3 \times 63 = 2^3 \times 3^2 \times 7$$
$$\boxed{504 = 2^3 \times 3^2 \times 7}$$

**24)** *Contexto: Probamos divisibilidad por primos hasta $\sqrt{127} \approx 11.3$*

Primos a probar: 2, 3, 5, 7, 11
- 127 es impar (no divisible por 2)
- $1+2+7=10$ no divisible por 3
- No termina en 0 o 5
- $127 = 7 \times 18 + 1$ (no divisible por 7)
- $127 = 11 \times 11 + 6$ (no divisible por 11)

**127 es primo** ✓

**25)** *Contexto: Buscamos $\text{MCM}(4,6,9) + 1$*
$$\text{MCM}(4,6,9) = \text{MCM}(2^2, 2 \times 3, 3^2) = 2^2 \times 3^2 = 36$$
$$\boxed{36 + 1 = 37}$$

**26)** *Contexto: Listamos primos en el rango.*

Primos entre 50 y 100: 53, 59, 61, 67, 71, 73, 79, 83, 89, 97

**Total: 10 primos**

**27)** *Contexto: Número de divisores de $n = p_1^{a_1} \times p_2^{a_2} \times ... = (a_1+1)(a_2+1)...$*
$$n = 2^3 \times 3^2 \times 5^1$$
Número de divisores $= (3+1)(2+1)(1+1) = 4 \times 3 \times 2 = \boxed{24}$

**28)** *Contexto: Dígitos $a + b = 8$ donde $10 \leq 10a + b \leq 99$*

Posibilidades: 17, 26, 35, 44, 53, 62, 71, 80

Primos: **17, 53, 71**

**29)** *Contexto: Usamos propiedades de paridad.*

Si $p > 2$ y $p$ es par, entonces $p = 2k$ para algún $k > 1$, lo que significa $2|p$. Pero entonces $p$ no sería primo (tendría a 2 como divisor propio). Contradicción.

Por lo tanto, si $p > 2$ es primo, $p$ debe ser impar. ∎

**30)** *Contexto: Estimamos con $\sqrt[3]{2431} \approx 13.4$*

Probamos primos cercanos a 13: **11, 13, 17**
$$11 \times 13 \times 17 = 143 \times 17 = 2431$$ ✓

---

## 2.4 MCD y MCM

**31)** *Contexto: Factorizamos ambos números.*
- $84 = 2^2 \times 3 \times 7$
- $126 = 2 \times 3^2 \times 7$

$\text{MCD} = 2^1 \times 3^1 \times 7^1 = \boxed{42}$

**32)** *Contexto: Aplicamos algoritmo de Euclides.*
$$252 = 198 \times 1 + 54$$
$$198 = 54 \times 3 + 36$$
$$54 = 36 \times 1 + 18$$
$$36 = 18 \times 2 + 0$$

$\text{MCD}(252, 198) = \boxed{18}$

**33)** *Contexto: $18 = 2 \times 3^2$, $24 = 2^3 \times 3$, $30 = 2 \times 3 \times 5$*

$\text{MCM} = 2^3 \times 3^2 \times 5 = \boxed{360}$

**34)** *Contexto: $a$ debe ser múltiplo de 12 tal que $\text{MCD}(a, 36) = 12$.*

$36 = 2^2 \times 3^2$ y $12 = 2^2 \times 3$

Para que $\text{MCD} = 12$, $a = 12k$ donde $\text{MCD}(k, 3) = 1$ (k no divisible por 3)

$a < 100$: $a \in \{12, 24, 48, 60, 84\}$ → verificamos MCD con 36:
- $\text{MCD}(12, 36) = 12$ ✓
- $\text{MCD}(24, 36) = 12$ ✓
- $\text{MCD}(48, 36) = 12$ ✓
- $\text{MCD}(60, 36) = 12$ ✓
- $\text{MCD}(84, 36) = 12$ ✓

**Valores: 12, 24, 48, 60, 84**

**35)** *Contexto: Buscamos MCM de vueltas.*

En $\text{MCM}(48, 60) = 240$ dientes, la rueda de 48 da $240/48 = 5$ vueltas.

**La primera rueda da 5 vueltas.**

**36)** *Contexto: Usamos la propiedad $\text{MCD}(a,b) \times \text{MCM}(a,b) = a \times b$*
$$a \times b = 6 \times 180 = \boxed{1080}$$

**37)** *Contexto: Calculamos MCM y encontramos primer múltiplo de 4 dígitos.*

$\text{MCM}(12, 15, 20) = \text{MCM}(2^2 \times 3, 3 \times 5, 2^2 \times 5) = 2^2 \times 3 \times 5 = 60$

Menor número de 4 dígitos: $\lceil 1000/60 \rceil \times 60 = 17 \times 60 = \boxed{1020}$

**38)** *Contexto: Dividimos numerador y denominador por su MCD.*

$\text{MCD}(252, 378) = 126$
$$\frac{252}{378} = \frac{252 \div 126}{378 \div 126} = \boxed{\frac{2}{3}}$$

**39)** *Contexto: Calculamos MCM de los intervalos.*

$\text{MCM}(20, 30, 45) = \text{MCM}(2^2 \times 5, 2 \times 3 \times 5, 3^2 \times 5) = 2^2 \times 3^2 \times 5 = 180$ min = 3 horas

**Coinciden a las 9:00 AM**

**40)** *Contexto: Usamos $n \times 12 = \text{MCD} \times \text{MCM}$*
$$n \times 12 = 4 \times 60 = 240$$
$$n = \boxed{20}$$

---

## 2.5 Fracciones

**41)** *Contexto: MCD de denominadores 4, 6, 3 es 12.*
$$\frac{3}{4} + \frac{5}{6} - \frac{1}{3} = \frac{9}{12} + \frac{10}{12} - \frac{4}{12} = \frac{15}{12} = \boxed{\frac{5}{4}}$$

**42)** *Contexto: Multiplicamos por el recíproco al dividir.*
$$\frac{2}{3} \times \frac{9}{14} \div \frac{3}{7} = \frac{2}{3} \times \frac{9}{14} \times \frac{7}{3} = \frac{2 \times 9 \times 7}{3 \times 14 \times 3} = \frac{126}{126} = \boxed{1}$$

**43)** *Contexto: Convertimos a denominador común (24).*
- $\frac{5}{8} = \frac{15}{24}$
- $\frac{7}{12} = \frac{14}{24}$
- $\frac{2}{3} = \frac{16}{24}$

**Orden:** $\frac{7}{12} < \frac{5}{8} < \frac{2}{3}$

**44)** *Contexto: Simplificamos $\frac{36}{48}$.*
$$\frac{36}{48} = \frac{36 \div 12}{48 \div 12} = \frac{3}{4}$$
$$a + b = 3 + 4 = \boxed{7}$$

**45)** *Contexto: Usamos fracciones parciales: $\frac{1}{n(n+1)} = \frac{1}{n} - \frac{1}{n+1}$*
$$= \left(1 - \frac{1}{2}\right) + \left(\frac{1}{2} - \frac{1}{3}\right) + \left(\frac{1}{3} - \frac{1}{4}\right) + \left(\frac{1}{4} - \frac{1}{5}\right) = 1 - \frac{1}{5} = \boxed{\frac{4}{5}}$$

**46)** *Contexto: Combinamos fracciones con igual denominador.*
$$\frac{5}{x} = \frac{5}{6} \Rightarrow x = \boxed{6}$$

**47)** *Contexto: Multiplicamos la cantidad por el factor de escala.*
$$\frac{2}{3} \times 1\frac{1}{2} = \frac{2}{3} \times \frac{3}{2} = \boxed{1 \text{ taza}}$$

**48)** *Contexto: Simplificamos numerador y denominador por separado.*
$$\frac{1 + \frac{1}{2}}{1 - \frac{1}{3}} = \frac{\frac{3}{2}}{\frac{2}{3}} = \frac{3}{2} \times \frac{3}{2} = \boxed{\frac{9}{4}}$$

**49)** *Contexto: $\frac{1}{4} = 0.25$ y $\frac{1}{3} \approx 0.333$*

Fracciones válidas: $\frac{4}{15} \approx 0.267$ y $\frac{5}{18} \approx 0.278$

O más simple: $\boxed{\frac{3}{11}}$ y $\boxed{\frac{5}{17}}$

**50)** *Contexto: Sea $t = \frac{a}{b}$, entonces $t + \frac{1}{t} = \frac{25}{12}$*
$$t^2 - \frac{25}{12}t + 1 = 0$$
$$12t^2 - 25t + 12 = 0$$
$$(3t - 4)(4t - 3) = 0$$
$$t = \frac{4}{3} \text{ o } t = \frac{3}{4}$$

---

## 2.6 Decimales y porcentajes

**51)** *Contexto: Dividimos numerador entre denominador.*
- $\frac{7}{8} = 0.875$
- $\frac{5}{11} = 0.\overline{45}$
- $\frac{17}{25} = 0.68$

**52)** *Contexto: Separamos parte no periódica de periódica.*

Sea $x = 0.3\overline{45}$
$$1000x = 345.\overline{45}$$
$$10x = 3.\overline{45}$$
$$990x = 342$$
$$x = \frac{342}{990} = \boxed{\frac{19}{55}}$$

**53)** *Contexto: Precio final = Precio × (1 - descuento)*
$$240 \times (1 - 0.15) = 240 \times 0.85 = \boxed{\$204}$$

**54)** *Contexto: % aumento = $\frac{\text{nuevo} - \text{original}}{\text{original}} \times 100$*
$$\frac{62 - 50}{50} \times 100 = \frac{12}{50} \times 100 = \boxed{24\%}$$

**55)** *Contexto: Si 35% de $x$ es 84, entonces $x = \frac{84}{0.35}$*
$$x = \frac{84}{0.35} = \boxed{240}$$

**56)** *Contexto: Calculamos el efecto combinado.*
$$P_{\text{final}} = P \times 1.20 \times 0.80 = P \times 0.96$$
El precio final es **menor** (4% menos que el original)

**57)** *Contexto: Convertimos todo a decimales.*
- $0.45 = 0.45$
- $\frac{4}{9} = 0.\overline{4} = 0.444...$
- $45\% = 0.45$
- $0.\overline{45} = 0.4545...$

**Orden:** $\frac{4}{9} < 0.45 = 45\% < 0.\overline{45}$

**58)** *Contexto: Similar al problema 56.*
$$100 \times 1.10 \times 0.90 = \boxed{\$99}$$

**59)** *Contexto: Precio con IVA = Precio sin IVA × 1.16*
$$\text{Precio sin IVA} = \frac{464}{1.16} = \boxed{\$400}$$

**60)** *Contexto: Porcentaje = fracción × 100*
$$\frac{7}{12} \times 100 = \boxed{58.33\%}$$

---

## 2.7 Potencias y raíces

**61)** *Contexto: Aplicamos $a^m \times a^n = a^{m+n}$ y $a^m \div a^n = a^{m-n}$*
$$2^3 \times 2^5 \div 2^4 = 2^{3+5-4} = 2^4 = \boxed{16}$$

**62)** *Contexto: Exponente negativo invierte la base.*
$$\left(\frac{3}{4}\right)^{-2} = \left(\frac{4}{3}\right)^2 = \boxed{\frac{16}{9}}$$

**63)** *Contexto: Expresamos en base prima.*
$$\frac{6^5 \times 9^2}{2^4 \times 27} = \frac{(2 \times 3)^5 \times (3^2)^2}{2^4 \times 3^3} = \frac{2^5 \times 3^5 \times 3^4}{2^4 \times 3^3} = 2^1 \times 3^6 = 2 \times 729 = \boxed{1458}$$

**64)** *Contexto: Evaluamos cada radical.*
$$\sqrt[3]{-27} + \sqrt{16} - \sqrt[4]{81} = -3 + 4 - 3 = \boxed{-2}$$

**65)** *Contexto: Multiplicamos por $\frac{\sqrt{3}}{\sqrt{3}}$*
$$\frac{6}{\sqrt{3}} = \frac{6\sqrt{3}}{3} = \boxed{2\sqrt{3}}$$

**66)** *Contexto: Simplificamos cada radical primero.*
$$\sqrt{50} + \sqrt{18} - \sqrt{8} = 5\sqrt{2} + 3\sqrt{2} - 2\sqrt{2} = \boxed{6\sqrt{2}}$$

**67)** *Contexto: Multiplicamos por el conjugado.*
$$\frac{4}{3 - \sqrt{5}} \times \frac{3 + \sqrt{5}}{3 + \sqrt{5}} = \frac{4(3 + \sqrt{5})}{9 - 5} = \frac{4(3 + \sqrt{5})}{4} = \boxed{3 + \sqrt{5}}$$

**68)** *Contexto: Evaluamos las potencias.*
$$2^x = 8 \Rightarrow x = 3$$
$$3^y = 27 \Rightarrow y = 3$$
$$2^x \times 3^y = 8 \times 27 = \boxed{216}$$

**69)** *Contexto: Aplicamos leyes de exponentes.*
$$(a^2 b^{-3})^{-2} \times (a^{-1} b^2)^3 = a^{-4} b^6 \times a^{-3} b^6 = a^{-7} b^{12} = \boxed{\frac{b^{12}}{a^7}}$$

**70)** *Contexto: Sea $x = \sqrt{12 + x}$, entonces $x^2 = 12 + x$*
$$x^2 - x - 12 = 0$$
$$(x-4)(x+3) = 0$$
$$x = \boxed{4}$$ (descartamos -3 por ser raíz cuadrada)

---

## 2.8 Razones y proporciones

**71)** *Contexto: Si la razón es 3:5, hay 3+5=8 partes.*
$$\text{Mujeres} = 40 \times \frac{5}{8} = \boxed{25}$$

**72)** *Contexto: Proporcionalidad inversa — más obreros, menos días.*
$$\text{Días} = 8 \times \frac{12}{16} = \boxed{6 \text{ días}}$$

**73)** *Contexto: Si están en razón 4:7, sean $4k$ y $7k$.*
$$4k + 7k = 132 \Rightarrow k = 12$$
Los números son $\boxed{48 \text{ y } 84}$

**74)** *Contexto: Proporcionalidad directa.*
$$\text{Piezas} = 450 \times \frac{10}{6} = \boxed{750}$$

**75)** *Contexto: Buscamos factor común para b.*
$$a:b = 2:3 = 8:12$$
$$b:c = 4:5 = 12:15$$
$$a:b:c = \boxed{8:12:15}$$

**76)** *Contexto: Escala significa 1 cm = 50000 cm = 500 m = 0.5 km*
$$8 \text{ cm} \times 0.5 \text{ km/cm} = \boxed{4 \text{ km}}$$

**77)** *Contexto: Reparto proporcional a la inversión.*

Total invertido: $2000 + 3000 + 5000 = 10000$
- Socio 1: $4000 \times \frac{2000}{10000} = \$800$
- Socio 2: $4000 \times \frac{3000}{10000} = \$1200$
- Socio 3: $4000 \times \frac{5000}{10000} = \$2000$

**78)** *Contexto: Sistema de ecuaciones con razones.*

Ahora: $\frac{A}{B} = \frac{3}{5}$ → $A = \frac{3B}{5}$

En 10 años: $\frac{A+10}{B+10} = \frac{5}{7}$ → $7A + 70 = 5B + 50$

Sustituyendo: $7 \times \frac{3B}{5} + 70 = 5B + 50$
$$\frac{21B}{5} + 70 = 5B + 50$$
$$21B + 350 = 25B + 250$$
$$B = 25, \quad A = 15$$

**Ana tiene 15 años, Beto tiene 25 años**

**79)** *Contexto: Proporcionalidad compuesta.*
$$\text{Artículos} = 200 \times \frac{8}{5} \times \frac{5}{4} = 200 \times \frac{40}{20} = \boxed{400}$$

**80)** *Contexto: Tasas de llenado se suman.*
$$\frac{1}{6} + \frac{1}{4} = \frac{2 + 3}{12} = \frac{5}{12} \text{ tanques/hora}$$
$$\text{Tiempo} = \frac{12}{5} = \boxed{2.4 \text{ horas}} = 2 \text{ h } 24 \text{ min}$$

---

## Problemas de Aplicación

**81)** *Contexto: Calculamos el porcentaje restante.*
$$100\% - 35\% - 25\% = 40\%$$
$$240 \times 0.40 = \boxed{96 \text{ pizzas}}$$

**82)** *Contexto: Cálculo secuencial.*
- Gastó en libros: $500 \times \frac{2}{5} = \$200$
- Resto: $500 - 200 = \$300$
- Gastó en comida: $300 \times \frac{1}{4} = \$75$
- Le queda: $300 - 75 = \boxed{\$225}$

**83)** *Contexto: Comparamos tiempos con velocidades diferentes.*
- Tiempo original: $\frac{240}{80} = 3$ horas
- Nueva velocidad: $80 \times 1.25 = 100$ km/h
- Nuevo tiempo: $\frac{240}{100} = 2.4$ horas
- Ahorra: $3 - 2.4 = \boxed{0.6 \text{ horas}} = 36$ minutos

**84)** *Contexto: Votos en blanco = total - votos de candidatos.*
$$\text{Votos en blanco} = 12000 \times (1 - 0.45 - 0.35) = 12000 \times 0.20 = \boxed{2400}$$

**85)** *Contexto: Reparto en partes proporcionales.*

Total de partes: $2 + 3 + 4 = 9$
- Hermano 1: $180000 \times \frac{2}{9} = \$40000$
- Hermano 2: $180000 \times \frac{3}{9} = \$60000$
- Hermano 3: $180000 \times \frac{4}{9} = \$80000$
