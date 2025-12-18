---
content_type: application
expected_output: markdown
audience: general
---

# Velocidad instantánea (ejemplo real)

## Contexto

Un radar de velocidad mide la posición de un auto en diferentes momentos. La posición $s(t)$ del auto en metros después de $t$ segundos es:

$$s(t) = t^2 + 2t$$

## ¿Qué es la velocidad instantánea?

La **velocidad promedio** entre $t = 2$ y $t = 2 + h$ segundos es:

$$v_{prom} = \frac{s(2+h) - s(2)}{h}$$

La **velocidad instantánea** en $t = 2$ es el límite cuando $h \to 0$:

$$v_{inst} = \lim_{h \to 0} \frac{s(2+h) - s(2)}{h}$$

## Cálculo

Calculemos $s(2+h)$:
$$s(2+h) = (2+h)^2 + 2(2+h) = 4 + 4h + h^2 + 4 + 2h = 8 + 6h + h^2$$

Y $s(2) = 4 + 4 = 8$

Entonces:
$$v_{inst} = \lim_{h \to 0} \frac{(8 + 6h + h^2) - 8}{h} = \lim_{h \to 0} \frac{6h + h^2}{h} = \lim_{h \to 0} (6 + h) = 6 \text{ m/s}$$

## Conexión con el tema

Este ejemplo muestra cómo los límites permiten calcular tasas de cambio instantáneas, que es la base del concepto de derivada.

---

<!--
IA: Usa este ejemplo para ilustrar aplicaciones prácticas de límites en física.
-->
