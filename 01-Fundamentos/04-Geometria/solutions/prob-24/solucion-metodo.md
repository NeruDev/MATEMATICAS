<!--
::METADATA::
type: solution
topic_id: fun-04-geometria
file_id: prob-24-solucion
problem_ref: Prob-24
status: stable
audience: student
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../WIKI_INDEX.md) | [📚 Glosario](../../../../glossary.md)

---

# Solución: Triángulo equilátero completo

## Problema
En un triángulo equilátero de lado 6 cm, encuentra la altura, el área y el radio del círculo inscrito.

---

## Método: Fórmulas del triángulo equilátero

### Paso 1: Calcular la altura
En un triángulo equilátero, la altura divide la [base](../../../..](../../../../glossary.md)#base) en dos partes iguales, formando dos triángulos rectángulos.

Usando el teorema de Pitágoras:
$$h^2 + \left(\frac{a}{2}\right)^2 = a^2$$

Donde $a = 6$ cm:
$$h^2 + 3^2 = 6^2$$
$$h^2 + 9 = 36$$
$$h^2 = 27$$
$$h = \sqrt{27} = \sqrt{9 \times 3} = 3\sqrt{3} \text{ cm}$$

### Paso 2: Calcular el área
$$A = \frac{1}{2} \times \text{[base](../../../..](../../../../glossary.md)#base)} \times \text{altura}$$
$$A = \frac{1}{2} \times 6 \times 3\sqrt{3}$$
$$A = 9\sqrt{3} \text{ cm}^2$$

**Verificación con fórmula directa:**
$$A = \frac{a^2\sqrt{3}}{4} = \frac{36\sqrt{3}}{4} = 9\sqrt{3} \text{ cm}^2 \checkmark$$

### Paso 3: Calcular el radio del círculo inscrito
El radio del círculo inscrito (incírculo) se relaciona con el área $A$ y el semiperímetro $s$:
$$r = \frac{A}{s}$$

**Semiperímetro:**
$$s = \frac{3 \times 6}{2} = 9 \text{ cm}$$

**Radio inscrito:**
$$r = \frac{9\sqrt{3}}{9} = \sqrt{3} \text{ cm}$$

**Fórmula alternativa para triángulo equilátero:**
$$r = \frac{a}{2\sqrt{3}} = \frac{a\sqrt{3}}{6} = \frac{6\sqrt{3}}{6} = \sqrt{3} \text{ cm} \checkmark$$

---

## Respuesta Final
$$\boxed{\begin{aligned}
\text{Altura: } & h = 3\sqrt{3} \text{ cm} \approx 5.196 \text{ cm} \\
\text{Área: } & A = 9\sqrt{3} \text{ cm}^2 \approx 15.59 \text{ cm}^2 \\
\text{Radio inscrito: } & r = \sqrt{3} \text{ cm} \approx 1.732 \text{ cm}
\end{aligned}}$$

---

## Diagrama
```
         A
         /\
        /  \
       /    \
    6 /  •   \ 6
     /   r    \
    /____h____\
   B    3 3    C
      ← 6 →
```

---

## Relaciones adicionales del triángulo equilátero
- Radio circunscrito: $R = \frac{a}{\sqrt{3}} = \frac{6}{\sqrt{3}} = 2\sqrt{3}$ cm
- Relación $R = 2r$: $2\sqrt{3} = 2 \times \sqrt{3}$ ✓
- El centroide, incentro, circuncentro y ortocentro coinciden
