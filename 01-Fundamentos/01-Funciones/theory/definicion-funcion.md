<!--
HUMANO:
Aquí va teoría pura: definiciones, intuición, teoremas.
No se resuelven problemas aquí.

IA:
Este archivo define CONCEPTOS.
No generes procedimientos ni ejercicios aquí.
-->

---
content_type: theory
expected_output:
  default: markdown
audience: self-study
---

# Definición de Función

## Definición formal

<!--
Matemática precisa. LaTeX permitido.
-->

Una **función** $f$ de un conjunto $A$ a un conjunto $B$ es una regla que asigna a cada elemento $x \in A$ exactamente un elemento $y \in B$.

$$f: A \to B$$
$$x \mapsto f(x) = y$$

Donde:
- $A$ se llama **dominio** de $f$, denotado $\text{Dom}(f)$
- $B$ se llama **codominio** de $f$
- El conjunto de todas las imágenes se llama **rango** o **imagen** de $f$, denotado $\text{Ran}(f)$

## Intuición

<!--
Explicación conceptual, no operativa.
-->

Piensa en una función como una "máquina":
- Introduces un valor (entrada)
- La máquina procesa ese valor
- Obtienes exactamente un resultado (salida)

**Analogía:** Una función es como una máquina expendedora: introduces dinero (entrada) y obtienes un producto específico (salida). No puedes obtener dos productos diferentes con la misma cantidad de dinero en la misma máquina.

## Qué NO es

<!--
Errores comunes y confusiones típicas.
-->

**NO es función si:**
- Un valor de entrada produce múltiples salidas
- Existen valores en el dominio sin asignar

**Error común:** Confundir una relación con una función. Toda función es una relación, pero no toda relación es función.

**Ejemplo de NO función:**
$$x^2 + y^2 = 1$$
(Un valor de $x$ puede producir dos valores de $y$)

## Representaciones

<!--
Algebraica, geométrica, gráfica, física si aplica.
-->

### Representación algebraica
$$f(x) = x^2 + 2x - 1$$

### Representación por tabla
| $x$ | $f(x)$ |
|-----|--------|
| -1  | -2     |
| 0   | -1     |
| 1   | 2      |

### Representación gráfica
Una curva en el plano cartesiano donde cada línea vertical corta la curva en **máximo un punto** (prueba de la línea vertical).

### Representación por diagrama de flechas
Diagramas de Venn con flechas que van de cada elemento del dominio a su imagen única en el codominio.

---

<!--
IA: Este archivo es solo teoría. Para procedimientos, consulta methods/.
-->
