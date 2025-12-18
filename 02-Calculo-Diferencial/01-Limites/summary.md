---
content_type: cheatsheet
expected_output: markdown
audience: exam-review
---

# Resumen rápido — Límites

- **Definición:** $$\lim_{x\to a} f(x) = L \iff \forall \varepsilon>0, \exists \delta>0 : 0 < |x-a| < \delta \Rightarrow |f(x)-L| < \varepsilon$$

## Métodos clave:
1. **Sustitución directa:** Si $f(a)$ existe y no da forma indeterminada, el límite es $f(a)$.
2. **Factorización:** Cuando obtienes $\frac{0}{0}$, factoriza y simplifica.
3. **Racionalización:** Multiplica por el conjugado cuando hay radicales.

## Regla rápida:
- Si obtienes $\frac{0}{0}$ → intenta factorizar.
- Si obtienes $\frac{c}{0}$ (con $c \neq 0$) → el límite no existe o es $\pm\infty$.
- Si hay radicales → racionaliza.

## Fórmulas comunes:

| Límite | Resultado |
|--------|-----------|
| $\lim_{x \to a} c$ | $c$ |
| $\lim_{x \to a} x$ | $a$ |
| $\lim_{x \to a} [f(x) + g(x)]$ | $\lim f(x) + \lim g(x)$ |
| $\lim_{x \to a} [f(x) \cdot g(x)]$ | $\lim f(x) \cdot \lim g(x)$ |
| $\lim_{x \to 0} \frac{\sin x}{x}$ | $1$ |

## Límites laterales:
- **Por la derecha:** $\lim_{x \to a^+} f(x)$
- **Por la izquierda:** $\lim_{x \to a^-} f(x)$
- El límite existe si y solo si ambos límites laterales existen e son iguales.

---

<!--
IA: Este resumen es para repaso rápido. Para explicaciones detalladas, consulta theory/.
-->
