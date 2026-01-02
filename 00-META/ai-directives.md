<!--
::METADATA::
type: reference
topic_id: meta-ai-directives
file_id: ai-directives
status: stable
audience: ai_context
last_updated: 2025-12-30
-->

# Directivas Técnicas para IA — Repositorio de Matemáticas

> **Nota:** Este archivo complementa a `ia-contract.md` con reglas técnicas específicas.
> Para la guía principal, consultar [ia-contract.md](ia-contract.md).

---

## 1. Notación de Valor Absoluto en Tablas Markdown

**Problema:** El símbolo `|` para valor absoluto (`$|x|$`) interfiere con los separadores de columnas de las tablas Markdown.

**Directiva:** En tablas Markdown, usar notación LaTeX explícita:

| Incorrecto | Correcto |
|------------|----------|
| `$|x|$` | `$\lvert x \rvert$` |
| `$|a| < |b|$` | `$\lvert a \rvert < \lvert b \rvert$` |
| `$||v||$` | `$\lVert v \rVert$` |

**Nota:** Fuera de tablas, ambas notaciones son aceptables.

---

## 2. Formato de Soluciones

**Directiva:** Toda solución debe incluir contexto antes del desarrollo:

```markdown
**[Prob-XX])** *Contexto: [Concepto/método aplicable]*

[Desarrollo paso a paso]

**Verificación:** [Comprobación del resultado]
```

---

## 3. Símbolos Problemáticos en Tablas

| Símbolo | Uso | Alternativa LaTeX |
|---------|-----|-------------------|
| Valor absoluto | $\lvert x \rvert$ | `$\lvert x \rvert$` |
| Norma | $\lVert v \rVert$ | `$\lVert v \rVert$` |
| Evaluado en | $f(x)\big\vert_a^b$ | `$\big\vert$` |
| Tal que (conjuntos) | $\{x \mid x > 0\}$ | `$\mid$` |
| Divisibilidad | $a \mid b$ | `$\mid$` |

---

## 4. Formato LaTeX

- **Inline:** `$...$` — una línea
- **Display:** `$$...$$` — ecuaciones centradas
- **NO usar:** `\begin{equation}` en Markdown (no renderiza)
- **Alineación múltiple:** Usar `$$\begin{aligned}...\end{aligned}$$`

---

## 5. Idioma y Estilo

| Aspecto | Especificación |
|---------|----------------|
| Idioma | Español |
| Nivel | Universitario |
| Estilo | Didáctico, progresivo |
| Prioridad | Claridad sobre brevedad |
| Ejemplos | Incluir siempre que ayuden |

---

## 6. Referencias Cruzadas

Para términos del glosario, usar formato: `[→ término](../glossary.md#termino)`

Ejemplo: `[→ función](../glossary.md#funcion)`
