<!--
::METADATA::
type: cheatsheet
topic_id: fun-02-aritmetica
file_id: FUN-02-Resumen-Formulas
status: stable
audience: exam_review
requires: []
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../WIKI_INDEX.md) | [📚 Glosario](../../glossary.md)

---

# Resumen rápido — Aritmética

## Jerarquía de conjuntos numéricos

$$\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$$

## Orden de operaciones (PEMDAS)

1. **P**aréntesis
2. **E**xponentes
3. **M**ultiplicación / **D**ivisión (izq → der)
4. **A**dición / **S**ustracción (izq → der)

## Propiedades fundamentales

| Propiedad | Suma | Multiplicación |
|-----------|------|----------------|
| Conmutativa | $a+b=b+a$ | $ab=ba$ |
| Asociativa | $(a+b)+c=a+(b+c)$ | $(ab)c=a(bc)$ |
| Neutro | $a+0=a$ | $a \cdot 1=a$ |
| Inverso | $a+(-a)=0$ | $a \cdot \frac{1}{a}=1$ |

**Distributiva:** $a(b+c)=ab+ac$

## Fracciones

| Operación | Fórmula |
|-----------|---------|
| Suma | $\frac{a}{b}+\frac{c}{d}=\frac{ad+bc}{bd}$ |
| Multiplicación | $\frac{a}{b} \cdot \frac{c}{d}=\frac{ac}{bd}$ |
| División | $\frac{a}{b} \div \frac{c}{d}=\frac{ad}{bc}$ |

## Potencias y raíces

| Ley | Fórmula |
|-----|---------|
| Producto | $a^m \cdot a^n = a^{m+n}$ |
| Cociente | $\frac{a^m}{a^n} = a^{m-n}$ |
| Potencia de potencia | $(a^m)^n = a^{mn}$ |
| Exponente negativo | $a^{-n} = \frac{1}{a^n}$ |
| Exponente fraccionario | $a^{m/n} = \sqrt[n]{a^m}$ |

## MCD y MCM

Dados $a=\prod p_i^{\alpha_i}$, $b=\prod p_i^{\beta_i}$:

$$\gcd(a,b)=\prod p_i^{\min(\alpha_i,\beta_i)}$$
$$\text{[mcm](../..](../../glossary.md)#mcm)}(a,b)=\prod p_i^{\max(\alpha_i,\beta_i)}$$

**Relación:** $\gcd(a,b) \cdot \text{[mcm](../..](../../glossary.md)#mcm)}(a,b) = a \cdot b$

## Porcentajes

- $p\%$ de $x$ = $\frac{p}{100} \cdot x$
- Cambio % = $\frac{\text{nuevo}-\text{original}}{\text{original}} \times 100\%$

---

<!--
IA: Hoja de referencia rápida.
Para desarrollo completo: [theory/FUN-02-Teoria-Aritmetica.md](theory/FUN-02-Teoria-Aritmetica.md)
file_id: FUN-02-Resumen-Formulas
-->
