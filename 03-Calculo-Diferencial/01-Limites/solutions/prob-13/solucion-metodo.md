<!--
::METADATA::
type: solution
topic_id: cd-01-limites
file_id: prob-13-solucion
problem_ref: Prob-13
status: stable
audience: student
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../WIKI_INDEX.md) | [📚 Glosario](../../../../glossary.md)

---

# Solución: Teorema del emparedado

## Problema
Usa el teorema del emparedado para evaluar $\displaystyle\lim_{x \to 0} x^2 \cos\left(\frac{1}{x}\right)$

---

## Teorema del Emparedado (Sandwich)
Si $g(x) \leq f(x) \leq h(x)$ para todo $x$ cerca de $a$ (excepto posiblemente en $a$), y
$$\lim_{x \to a} g(x) = \lim_{x \to a} h(x) = L$$
entonces $\displaystyle\lim_{x \to a} f(x) = L$.

---

## Solución

### Paso 1: Analizar el factor problemático
$\cos\left(\frac{1}{x}\right)$ oscila infinitamente cuando $x \to 0$, pero está acotado:
$$-1 \leq \cos\left(\frac{1}{x}\right) \leq 1 \quad \text{para todo } x \neq 0$$

### Paso 2: Multiplicar por x²
Multiplicamos la desigualdad por $x^2 \geq 0$:
$$-x^2 \leq x^2 \cos\left(\frac{1}{x}\right) \leq x^2$$

### Paso 3: Identificar las funciones acotantes
- $g(x) = -x^2$
- $f(x) = x^2 \cos\left(\frac{1}{x}\right)$
- $h(x) = x^2$

### Paso 4: Calcular los límites de las cotas
$$\lim_{x \to 0} (-x^2) = 0$$
$$\lim_{x \to 0} x^2 = 0$$

### Paso 5: Aplicar el teorema del emparedado
Como:
- $-x^2 \leq x^2 \cos\left(\frac{1}{x}\right) \leq x^2$
- $\displaystyle\lim_{x \to 0} (-x^2) = \lim_{x \to 0} x^2 = 0$

Por el teorema del emparedado:
$$\lim_{x \to 0} x^2 \cos\left(\frac{1}{x}\right) = 0$$

---

## Respuesta Final
$$\boxed{\lim_{x \to 0} x^2 \cos\left(\frac{1}{x}\right) = 0}$$

---

## Visualización
```
         y
         ↑
    x²   |    /\  
         |   /  \    ← x² cos(1/x) oscila
         |  /    \      entre -x² y x²
    ─────┼─•──────────→ x
         | \    /
         |  \  /
   -x²   |   \/
```

---

## Nota importante
El [límite](../../../../glossary.md#limite) existe a pesar de que $\cos\left(\frac{1}{x}\right)$ no tiene límite cuando $x \to 0$. El factor $x^2$ "aplasta" las oscilaciones hacia cero.

Este es un ejemplo clásico donde la [sustitución](../../../../glossary.md#sustitucion) directa no funciona pero el teorema del emparedado sí.
