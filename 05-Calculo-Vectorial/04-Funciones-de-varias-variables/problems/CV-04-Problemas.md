<!--
::METADATA::
type: problem-set
topic_id: cv-04-funciones-varias-variables
file_id: CV-04-Problemas
status: stable
audience: student
total_problems: 55
difficulty_distribution:
  basic: 20
  intermediate: 25
  advanced: 10
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../glossary.md)

---

# Problemas — Funciones de Varias Variables

> **Instrucciones:** Resuelve cada problema mostrando el procedimiento completo.
>
> **Respuestas:** Consulta [solutions/CV-04-Respuestas.md](../solutions/CV-04-Respuestas.md)

---

## 4.1 Dominio y Curvas de Nivel

**[Prob-01]** Encuentra y grafica el [dominio](../../../glossary.md#dominio) de $f(x, y) = \sqrt{9 - x^2 - y^2}$.

**[Prob-02]** Determina el [dominio](../../../glossary.md#dominio) de $f(x, y) = \ln(x - y^2)$.

**[Prob-03]** Encuentra el dominio de $f(x, y) = \frac{1}{\sqrt{x^2 + y^2 - 4}}$.

**[Prob-04]** Dibuja las curvas de nivel de $f(x, y) = x^2 + y^2$ para $c = 0, 1, 4, 9$.

**[Prob-05]** Dibuja las curvas de nivel de $f(x, y) = x^2 - y$ para $c = -2, 0, 2$.

**[Prob-06]** Encuentra y describe las superficies de nivel de $f(x, y, z) = x^2 + y^2 + z^2$.

---

## 4.2 Límites y Continuidad

**[Prob-07]** Calcula $\displaystyle\lim_{(x,y) \to (1,2)} (x^2y + xy^2 - 3)$.

**[Prob-08]** Evalúa $\displaystyle\lim_{(x,y) \to (0,0)} \frac{x^2 + y^2}{\sqrt{x^2 + y^2 + 1} - 1}$.

**[Prob-09]** Demuestra que $\displaystyle\lim_{(x,y) \to (0,0)} \frac{xy}{x^2 + y^2}$ no existe.\n\n📂 **Solución desarrollada:** [Ver paso a paso](../solutions/prob-09/solucion-metodo.md)

**[Prob-10]** Demuestra que $\displaystyle\lim_{(x,y) \to (0,0)} \frac{x^2y}{x^4 + y^2}$ no existe.

**[Prob-11]** Calcula $\displaystyle\lim_{(x,y) \to (0,0)} \frac{x^3 + y^3}{x^2 + y^2}$.

**[Prob-12]** Evalúa $\displaystyle\lim_{(x,y) \to (0,0)} \frac{\sin(x^2 + y^2)}{x^2 + y^2}$.

**[Prob-13]** Determina si la [función](../../../glossary.md#funcion) es continua en el origen:
$$f(x,y) = \begin{cases} \frac{x^2y}{x^2 + y^2} & (x,y) \neq (0,0) \\ 0 & (x,y) = (0,0) \end{cases}$$

---

## 4.3 Derivadas Parciales

**[Prob-14]** Encuentra $f_x$ y $f_y$ para $f(x, y) = x^3y^2 - 2x^2y + 5y$.

**[Prob-15]** Calcula las [derivadas](../../../glossary.md#derivadas) parciales de $f(x, y) = e^{xy}\sin(x + y)$.

**[Prob-16]** Si $f(x, y) = \ln(x^2 + y^2)$, encuentra $f_x$ y $f_y$.

**[Prob-17]** Para $f(x, y) = \arctan\left(\frac{y}{x}\right)$, calcula $f_x$ y $f_y$.

**[Prob-18]** Si $f(x, y, z) = xy^2z^3 + x^2yz$, encuentra $f_x$, $f_y$ y $f_z$.

**[Prob-19]** Usando la definición de límite, encuentra $f_x(0, 0)$ para $f(x, y) = \sqrt{|xy|}$.

---

## 4.4 Derivadas de Orden Superior

**[Prob-20]** Para $f(x, y) = x^4 - 3x^2y^2 + y^4$, calcula $f_{xx}$, $f_{yy}$ y $f_{xy}$.

**[Prob-21]** Verifica que $f_{xy} = f_{yx}$ para $f(x, y) = e^x\cos y$.

**[Prob-22]** Si $f(x, y) = \ln(x + y)$, calcula $f_{xxy}$.

**[Prob-23]** Demuestra que $u = e^{-t}\sin x$ satisface la ecuación del calor $u_t = u_{xx}$.

**[Prob-24]** Verifica que $u = \ln(x^2 + y^2)$ satisface la ecuación de Laplace $u_{xx} + u_{yy} = 0$.

---

## 4.5 Regla de la Cadena

**[Prob-25]** Si $z = x^2y + xy^2$, $x = t^2$ y $y = t^3$, encuentra $\frac{dz}{dt}$.

**[Prob-26]** Si $z = e^{xy}$, $x = s + t$ y $y = s - t$, encuentra $\frac{\partial z}{\partial s}$ y $\frac{\partial z}{\partial t}$.

**[Prob-27]** Si $w = x^2 + y^2 + z^2$, $x = \rho\sin\phi\cos\theta$, $y = \rho\sin\phi\sin\theta$, $z = \rho\cos\phi$, calcula $\frac{\partial w}{\partial \rho}$.

**[Prob-28]** Si $z = f(x^2 - y^2)$ donde $f$ es diferenciable, demuestra que $y\frac{\partial z}{\partial x} + x\frac{\partial z}{\partial y} = 0$.

**[Prob-29]** La temperatura en una placa es $T(x, y) = 100 - x^2 - y^2$. Un insecto camina sobre la placa según $x = \cos t$, $y = \sin t$. ¿A qué ritmo cambia la temperatura que experimenta?

---

## 4.6 Gradiente y Derivada Direccional

**[Prob-30]** Encuentra $\nabla f$ para $f(x, y) = x^2e^y + y\ln x$.

**[Prob-31]** Calcula el gradiente de $f(x, y, z) = xyz + x^2y^2z^2$ en $(1, 1, 1)$.

**[Prob-32]** Encuentra la [derivada](../../../glossary.md#derivada) direccional de $f(x, y) = x^2 + xy - y^2$ en $(2, 1)$ en dirección de $\mathbf{u} = \langle 3, 4 \rangle$.

**[Prob-33]** Para $f(x, y, z) = xy + yz + zx$, calcula $D_{\mathbf{u}}f$ en $(1, 1, 1)$ en dirección del [vector](../../../glossary.md#vector) $\langle 1, 2, 2 \rangle$.

**[Prob-34]** Encuentra la dirección de máximo crecimiento de $f(x, y) = xe^y$ en el punto $(2, 0)$.

**[Prob-35]** Si $f(x, y) = x^2 - xy + y^2$, ¿en qué dirección desde $(1, 1)$ es la [derivada](../../../glossary.md#derivada) direccional cero?

**[Prob-36]** La temperatura en un punto $(x, y, z)$ es $T = 100 - x^2 - 2y^2 - z^2$. Una abeja está en $(1, 1, 1)$. ¿En qué dirección debe volar para enfriarse más rápido?

---

## 4.7 Plano Tangente y Aproximación Lineal

**[Prob-37]** Encuentra la ecuación del plano [tangente](../../../glossary.md#tangente) a $z = x^2 + y^2$ en $(1, 2, 5)$.

**[Prob-38]** Halla el plano [tangente](../../../glossary.md#tangente) a $z = \ln(x^2 + y)$ en $(1, 1, \ln 2)$.

**[Prob-39]** Encuentra el plano tangente a la superficie $x^2 + 2y^2 + 3z^2 = 6$ en $(1, 1, 1)$.

**[Prob-40]** Usa la aproximación lineal para estimar $(1.02)^2(0.97)^3$.

**[Prob-41]** El radio de un cono circular recto es $r = 10$ cm y la altura $h = 25$ cm. Si $r$ aumenta 0.1 cm y $h$ disminuye 0.2 cm, estima el cambio en el volumen usando diferenciales.

---

## 4.8 Extremos Locales

**[Prob-42]** Encuentra los puntos críticos de $f(x, y) = x^2 + y^2 - 2x - 4y + 5$.

**[Prob-43]** Clasifica los puntos críticos de $f(x, y) = x^3 + y^3 - 3xy$.\n\n📂 **Solución desarrollada:** [Ver paso a paso](../solutions/prob-43/solucion-metodo.md)

**[Prob-44]** Encuentra y clasifica los extremos de $f(x, y) = x^2 - y^2$.

**[Prob-45]** Halla los extremos locales de $f(x, y) = xy - x^3 - y^3$.

**[Prob-46]** Encuentra los valores máximo y mínimo de $f(x, y) = x^2 + y^2 - 2x$ en el disco $x^2 + y^2 \leq 4$.

---

## 4.9 Multiplicadores de Lagrange

**[Prob-47]** Usa multiplicadores de Lagrange para encontrar los extremos de $f(x, y) = xy$ sujeto a $x^2 + y^2 = 1$.\n\n📂 **Solución desarrollada:** [Ver paso a paso](../solutions/prob-47/solucion-metodo.md)

**[Prob-48]** Encuentra los extremos de $f(x, y) = x + 2y$ sujeto a $x^2 + y^2 = 5$.

**[Prob-49]** Maximiza $f(x, y, z) = xyz$ sujeto a $x + y + z = 12$ con $x, y, z > 0$.

**[Prob-50]** Encuentra el punto del plano $2x + 3y + z = 14$ más cercano al origen.

**[Prob-51]** Halla las dimensiones del paralelepípedo de volumen máximo inscrito en la esfera $x^2 + y^2 + z^2 = 1$.

**[Prob-52]** Minimiza $f(x, y, z) = x^2 + y^2 + z^2$ sujeto a $x + y = 1$ y $y + z = 2$.

---

## 4.10 Problemas de Síntesis

**[Prob-53]** La producción de una fábrica está dada por $Q(L, K) = 60L^{1/3}K^{2/3}$ donde $L$ es mano de obra y $K$ es capital. Si el costo de L es \$100/unidad y de K es \$200/unidad:
a) Con presupuesto de \$30,000, encuentra L y K que maximizan Q
b) Calcula la producción máxima

**[Prob-54]** Demuestra que si $(a, b)$ es un [punto crítico](../../../glossary.md#punto-critico) de $f(x, y)$ y la [matriz](../../../glossary.md#matriz) Hessiana tiene [determinante](../../../glossary.md#determinante) positivo con $f_{xx}(a, b) > 0$, entonces $(a, b)$ es un mínimo local.

**[Prob-55]** La ecuación de estado de un gas ideal es $PV = nRT$. Si $n = 1$ mol, $R = 8.314$ J/(mol·K), $T = 300$ K, y las mediciones tienen errores $\Delta P = 0.02$ atm y $\Delta T = 0.5$ K:
a) Calcula V cuando $P = 1$ atm
b) Estima el error en V usando diferenciales

---

> 📚 **Respuestas:** [solutions/CV-04-Respuestas.md](../theory/)
> 📋 **Fórmulas:** [CV-04-Resumen-Formulas.md](../CV-04-Resumen-Formulas.md)
