# Directivas para IA — Repositorio de Matemáticas

Este archivo contiene las directivas globales que la IA debe seguir al generar o modificar contenido en este repositorio.

---

## 1. Notación de Valor Absoluto en Tablas Markdown

**Problema:** El símbolo `|` para valor absoluto (`$|x|$`) interfiere con los separadores de columnas de las tablas Markdown, causando renderizado incorrecto.

**Directiva:** En contextos donde el valor absoluto aparezca dentro de una tabla Markdown, usar la notación LaTeX explícita:

| Incorrecto | Correcto |
|------------|----------|
| `$|x|$` | `$\lvert x \rvert$` |
| `$|a| < |b|$` | `$\lvert a \rvert < \lvert b \rvert$` |
| `$|x - c|$` | `$\lvert x - c \rvert$` |

**Nota:** Fuera de tablas, ambas notaciones son aceptables.

---

## 2. Directrices de Soluciones

**Directiva:** Antes de presentar cualquier solución a un problema, incluir un **contexto** que explique:
- Qué concepto matemático aplica
- Por qué es relevante para el problema
- Qué método se utilizará

**Formato:**
```markdown
**N)** *Contexto: [Breve explicación del concepto/método aplicable]*

[Desarrollo de la solución]
```

---

## 3. Estructura de Archivos por Carpeta Temática

Cada carpeta temática debe contener un archivo `_directives.md` que especifique:
- Tipo de contenido esperado
- Audiencia objetivo
- Formato de salida predeterminado
- Tareas permitidas para la IA

---

## 4. Nomenclatura de Archivos

**Directiva:** Los archivos deben tener nombres descriptivos que indiquen su contenido:

| Tipo de contenido | Nombre del archivo | Ubicación |
|-------------------|--------------------|-----------|
| Teoría principal | `teoria.md` | `theory/` |
| Métodos/Procedimientos | `metodos.md` | `methods/` |
| Problemas | `problemas.md` | `problems/` |
| Soluciones | `soluciones.md` | `solutions/` |
| Descripción del tema | `resumen-[tema].md` | Raíz del tema |
| Directivas para IA | `_directives.md` | Raíz del tema |

**Excepción:** Solo el archivo `README.md` en la raíz del repositorio conserva ese nombre.

---

## 5. Formato de Tablas con Contenido Matemático

**Directiva:** Al crear tablas que contengan expresiones matemáticas:

1. Evitar símbolos que puedan confundirse con separadores (`|`, `||`)
2. Usar notación LaTeX explícita para operadores ambiguos
3. Verificar que la tabla se renderice correctamente en Markdown Preview Enhanced

**Alternativas para símbolos problemáticos:**

| Símbolo | Alternativa LaTeX |
|---------|-------------------|
| `|` (valor absoluto) | `\lvert \rvert` |
| `||` (norma) | `\lVert \rVert` |
| `|` (evaluado en) | `\big\vert` |
| `|` (tal que, conjuntos) | `\mid` |

---

## 6. Idioma y Estilo

- **Idioma:** Español
- **Nivel:** Universitario (comprensión sólida)
- **Estilo:** Didáctico, progresivo, con ejemplos prácticos
- **Formato matemático:** LaTeX con delimitadores `$` (inline) y `$$` (display)
