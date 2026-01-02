<!--
::METADATA::
type: reference
topic_id: meta-ai-directives
file_id: ai-directives
status: stable
audience: ai_context
last_updated: 2026-01-02
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

## 6. Sintaxis de Enlaces (OBLIGATORIO)

> **⚠️ DIRECTIVA CRÍTICA:** Todos los enlaces internos DEBEN seguir esta sintaxis para garantizar navegación funcional en VS Code y GitHub.

### 6.1 Formato Correcto de Enlaces

```markdown
[Texto visible](ruta/relativa/archivo.md)
[Texto visible](ruta/relativa/archivo.md#ancla)
```

### 6.2 Ejemplos por Tipo de Enlace

| Tipo | Sintaxis Correcta | Ejemplo |
|------|-------------------|---------|
| **Glosario** | `[término](../glossary.md#ancla)` | `[función](../glossary.md#funcion)` |
| **Índice principal** | `[texto](../WIKI_INDEX.md)` | `[← Volver](../WIKI_INDEX.md)` |
| **Archivo en misma carpeta** | `[texto](./archivo.md)` | `[Intro](./AL-01-Matrices-Intro.md)` |
| **Archivo en subcarpeta** | `[texto](./subcarpeta/archivo.md)` | `[Teoría](./theory/AL-01-Teoria-Matrices.md)` |
| **Archivo en carpeta padre** | `[texto](../carpeta/archivo.md)` | `[Índice](../00-Index.md)` |
| **Otro módulo** | `[texto](../Modulo/carpeta/archivo.md)` | `[Álgebra](../02-Algebra-Lineal/00-Index.md)` |

### 6.3 Errores Comunes (NO HACER)

| ❌ Incorrecto | ✅ Correcto | Problema |
|---------------|-------------|----------|
| `](../glossary.md)#term)` | `](../glossary.md#term)` | Paréntesis fuera del ancla |
| `](..](../glossary.md)` | `](../glossary.md)` | Doble bracket |
| `[texto](README.md)` | `[texto](*-Intro.md)` | No existen README en subtemas |
| `[texto](archivo)` | `[texto](archivo.md)` | Falta extensión .md |

### 6.4 Navegación Estándar (Header)

Todo archivo de contenido debe incluir este header de navegación:

```markdown
> 🏠 **Navegación:** [← Volver al Índice Principal](../WIKI_INDEX.md) | [📚 Glosario](../glossary.md)
```

Ajustar la ruta relativa según la profundidad del archivo:
- Nivel 1 (`01-Fundamentos/00-Index.md`): `../WIKI_INDEX.md`
- Nivel 2 (`01-Fundamentos/02-Aritmetica/FUN-02-Intro.md`): `../../WIKI_INDEX.md`
- Nivel 3 (`01-Fundamentos/02-Aritmetica/theory/FUN-02-Teoria.md`): `../../../WIKI_INDEX.md`

### 6.5 Validación de Enlaces

Antes de finalizar cualquier contenido nuevo:
1. Verificar que todas las rutas relativas existen
2. Probar enlaces en VS Code Markdown Preview
3. Ejecutar script de validación si está disponible

---

## 7. Referencias Cruzadas al Glosario

Para términos del glosario, usar formato: `[término](../glossary.md#ancla)`

**Anclas válidas:** El ancla debe coincidir con el ID del término en `glossary.md` (en minúsculas, guiones en lugar de espacios).

Ejemplos:
- `[función](../glossary.md#funcion)`
- `[valor absoluto](../glossary.md#valor-absoluto)`
- `[regla de la cadena](../glossary.md#regla-de-la-cadena)`
