<!--
::METADATA::
type: reference
topic_id: meta-ia-contract
file_id: ia-contract
status: stable
audience: ai_context
last_updated: 2026-01-02
-->

# Contrato de IA para el Repositorio de Matemáticas

> **IMPORTANTE:** Este archivo es la guía principal para cualquier IA que interactúe con el repositorio.
> Lee este documento COMPLETAMENTE antes de generar o modificar contenido.

---

## 1. Estructura del Repositorio

### 1.1 Módulos Principales

| # | Módulo | Prefijo | Subtemas | Estado |
|---|--------|---------|----------|--------|
| 01 | Fundamentos | `FUN` | Simbología, Aritmética, Álgebra, Geometría, Trigonometría, Geometría Analítica | ✅ Completo |
| 02 | Álgebra Lineal | `AL` | Matrices, Determinantes, Sistemas Lineales, Espacios Vectoriales, Transformaciones, Valores Propios | ✅ Completo |
| 03 | Cálculo Diferencial | `CD` | Límites, Derivadas, Aplicaciones, Teoremas Fundamentales | ✅ Completo |
| 04 | Cálculo Integral | `CI` | Integral Indefinida, Técnicas, Integral Definida, Aplicaciones, Impropias | ✅ Completo |
| 05 | Cálculo Vectorial | `CV` | Vectores, Curvas, Funciones Vectoriales, Varias Variables, Integración Múltiple | ✅ Completo |
| 06 | Ecuaciones Diferenciales | `ED` | EDO Primer Orden, Segundo Orden, Sistemas, Laplace, Series de Potencias | ✅ Completo |
| 07 | Métodos Numéricos | `MN` | Raíces, Interpolación, Integración Numérica, EDO Numéricas | ✅ Completo |

### 1.2 Estructura de cada Subtema

```
XX-Nombre-Subtema/
├── manifest.json                    # Metadatos y configuración IA (OBLIGATORIO)
├── PREFIJO-XX-*-Intro.md            # Punto de entrada (OBLIGATORIO)
├── PREFIJO-XX-Resumen-Formulas.md   # Cheat sheet (OBLIGATORIO)
├── theory/
│   └── PREFIJO-XX-Teoria-*.md       # Teoría completa
├── methods/
│   └── PREFIJO-XX-Metodos-*.md      # Procedimientos paso a paso
├── problems/
│   └── PREFIJO-XX-Problemas.md      # Lista de problemas con IDs [Prob-XX]
├── solutions/
│   ├── PREFIJO-XX-Respuestas.md     # Tabla de TODAS las respuestas
│   └── prob-XX/                     # Soluciones desarrolladas (selectas)
│       └── solucion-metodo.md
├── applications/                    # (opcional)
└── media/                           # (opcional)
```

**⚠️ NO existen archivos `README.md` en los subtemas.** El punto de entrada es siempre `*-Intro.md`.

---

## 2. Sistema de Nomenclatura

### 2.1 Patrón de Nombres

Todos los archivos `.md` siguen: `[PREFIJO]-[XX]-[Contenido].md`

| Prefijo | Módulo |
|---------|--------|
| `FUN-XX` | 01-Fundamentos |
| `AL-XX` | 02-Algebra-Lineal |
| `CD-XX` | 03-Calculo-Diferencial |
| `CI-XX` | 04-Calculo-Integral |
| `CV-XX` | 05-Calculo-Vectorial |
| `ED-XX` | 06-Ecuaciones-Diferenciales |
| `MN-XX` | 07-Metodos-Numericos |

### 2.2 Excepciones

| Excepción | Razón |
|-----------|-------|
| `01-Simbologia-Matematica/theory/*` | Biblioteca de referencia sin secuencia |
| `solutions/prob-XX/solucion-*.md` | Contexto implícito por carpeta padre |
| `00-META/*` | Archivos de configuración del repositorio |
| `00-Index.md` | Archivo índice por módulo principal |

---

## 3. Metadatos Obligatorios

### 3.1 Bloque ::METADATA:: en archivos .md

Todo archivo `.md` debe comenzar con:

```markdown
<!--
::METADATA::
type: [theory | method | problem | solution | reference | index | cheatsheet | answer-key]
status: [draft | review | stable | active]
-->
```

Para archivos completos, incluir también:
- `topic_id`: ID del tema (coincide con `manifest.json`)
- `file_id`: Nombre del archivo sin extensión
- `audience`: student | ai_context | exam_review
- `last_updated`: YYYY-MM-DD

### 3.2 Estructura del manifest.json

```json
{
  "id": "prefijo-numero-tema",
  "topic": "Nombre Legible",
  "type": "learning_module",
  "status": "active",
  "tags": ["etiqueta1", "etiqueta2"],
  "resource_map": {
    "entry_point": "PREFIJO-XX-*-Intro.md",
    "formula_sheet": "PREFIJO-XX-Resumen-Formulas.md",
    "theory": "theory/",
    "methods": "methods/PREFIJO-XX-Metodos-*.md",
    "problems": "problems/PREFIJO-XX-Problemas.md",
    "solutions": "solutions/"
  },
  "ai_contract": {
    "allowed_tasks": ["explain_concept", "generate_problems", "verify_solution"],
    "solution_guidelines": {
      "format": "context + development + verification",
      "context_requirement": "Explicar concepto aplicable antes de resolver"
    }
  }
}
```

**Campos obligatorios:** `id`, `topic`, `type`, `status`, `tags`, `resource_map`, `ai_contract`

---

## 4. Reglas de Generación de Contenido

### 4.1 Separación Semántica

| Contenido | Ubicación | NO incluir |
|-----------|-----------|------------|
| Definiciones, teoremas, demostraciones | `theory/` | Procedimientos paso a paso |
| Algoritmos, métodos, pasos | `methods/` | Definiciones teóricas |
| Enunciados de problemas | `problems/` | Soluciones |
| Respuestas y desarrollos | `solutions/` | Enunciados completos |

### 4.2 Formato de Problemas (Tres Niveles)

**Nivel 1 - Problemas** (`problems/PREFIJO-XX-Problemas.md`):
- Un archivo único con TODOS los problemas
- Cada problema con ID: `### [Prob-XX] Título ⭐`
- Dificultad: ⭐ (básico), ⭐⭐ (intermedio), ⭐⭐⭐ (avanzado)

**Nivel 2 - Respuestas** (`solutions/PREFIJO-XX-Respuestas.md`):
- Tabla con TODAS las respuestas finales
- Formato: `| [Prob-XX] | respuesta | [Ver](./prob-XX/...) |`

**Nivel 3 - Soluciones desarrolladas** (`solutions/prob-XX/`):
- Solo para problemas selectos (difíciles, representativos)
- Archivo obligatorio: `solucion-metodo.md`

### 4.3 Formato de Soluciones

```markdown
**[Prob-XX])** *Contexto: [Explicación del concepto/método aplicable]*

[Desarrollo paso a paso de la solución]

**Verificación:** [Comprobación del resultado]
```

### 4.4 Notación Matemática en Tablas

⚠️ El símbolo `|` interfiere con tablas Markdown. Usar alternativas:

| Símbolo | Alternativa LaTeX |
|---------|-------------------|
| Valor absoluto `\|x\|` | `$\lvert x \rvert$` |
| Norma `\|\|v\|\|` | `$\lVert v \rVert$` |
| Evaluado en | `$\big\vert$` |
| Tal que (conjuntos) | `$\mid$` |

---

## 5. Sintaxis de Enlaces Internos (OBLIGATORIO)

> **⚠️ CRÍTICO:** La navegación del repositorio depende de enlaces correctamente formados.

### 5.1 Formato Estándar

```markdown
[Texto](ruta/relativa/archivo.md)
[Texto](ruta/relativa/archivo.md#ancla)
```

### 5.2 Patrones por Contexto

| Desde | Hacia | Sintaxis |
|-------|-------|----------|
| Cualquier archivo | Glosario | `[término](../glossary.md#ancla)` |
| Cualquier archivo | Índice principal | `[← Volver](../WIKI_INDEX.md)` |
| `00-Index.md` | Subtema Intro | `[Tema](./XX-Carpeta/PREFIJO-XX-Intro.md)` |
| Archivo en subtema | Teoría | `[Teoría](./theory/PREFIJO-XX-Teoria-X.md)` |
| Archivo en subcarpeta | Índice módulo | `[Índice](../00-Index.md)` |

### 5.3 Header de Navegación Obligatorio

Todo archivo `.md` de contenido debe incluir:

```markdown
> 🏠 **Navegación:** [← Volver al Índice Principal](../WIKI_INDEX.md) | [📚 Glosario](../glossary.md)
```

Ajustar `../` según profundidad (añadir `../` por cada nivel).

### 5.4 Prohibiciones en Enlaces

❌ **NO HACER:**
- `](../glossary.md)#term)` — paréntesis fuera del ancla
- `](..](../archivo.md)` — doble bracket
- `[texto](README.md)` — no existen README en subtemas
- Enlaces sin extensión `.md`
- Rutas absolutas del sistema de archivos

---

## 6. Tareas Permitidas

| Tarea | Descripción |
|-------|-------------|
| `explain_concept` | Explicar conceptos de teoría |
| `generate_problems` | Crear nuevos problemas |
| `verify_solution` | Verificar si una solución es correcta |
| `solve_problem` | Resolver problemas existentes |
| `convert_format` | Convertir entre formatos (Markdown, LaTeX) |
| `add_examples` | Agregar ejemplos a teoría existente |
| `create_summary` | Crear resúmenes de fórmulas |

---

## 7. Prohibiciones

❌ **NO hacer:**
- Mezclar teoría con métodos en el mismo archivo
- Incluir soluciones en archivos de problemas
- Crear archivos `README.md` en subtemas (usar `*-Intro.md`)
- Usar `|` para valor absoluto dentro de tablas
- Asumir conocimientos no declarados en prerequisitos
- Inventar métodos alternativos cuando hay `assigned_method`
- Usar nombres de archivo en inglés para contenido nuevo
- **Crear enlaces con sintaxis incorrecta** (ver sección 5.4)

---

## 8. Recursos de Referencia

| Recurso | Ubicación | Uso |
|---------|-----------|-----|
| Glosario | `glossary.md` | ~150 términos con analogías |
| Notación | `00-META/notation-cheatsheet.md` | Símbolos y convenciones |
| Plantilla respuestas | `00-META/plantilla-respuestas.md` | Formato de archivo de respuestas |
| Validador | `00-META/tools/validate_repo.py` | Verificar integridad del repo |
| **Generador de Gráficos** | `00-META/tools/graphics/` | Sistema de generación de figuras SVG/PNG |
| Nomenclatura detallada | `00-META/nomenclatura-estandar.md` | Especificaciones técnicas completas |
| **Directivas de enlaces** | `00-META/ai-directives.md` | Sintaxis correcta de hipervínculos |

### 8.1 Sistema de Gráficos Generados

Los gráficos matemáticos se generan con Python y se almacenan en `media/generated/`:

```
00-META/tools/graphics/
├── generate_graphics.py        # Motor principal
├── config.yaml                 # Configuración global
├── templates/                  # Estilos reutilizables
└── sources/{TOPIC}/            # Código fuente por tema
    └── nombre_grafico.py

{MODULO}/{SUBTEMA}/media/generated/
├── nombre_grafico.svg          # Para sitio web estático
├── nombre_grafico.png          # Para Markdown/GitHub
└── manifest.json               # Registro de gráficos
```

**Al crear nuevos gráficos:**
1. Crear archivo Python en `sources/{TOPIC}/`
2. Incluir `METADATA` con `topic_id`, `name`, `description`, `used_in`
3. Implementar función `generate()` que retorna `plt.Figure`
4. Ejecutar: `python generate_graphics.py --file {nombre}`
5. Referenciar en Markdown: `![Alt](media/generated/{nombre}.png)`

---

## 9. Flujo de Trabajo para Nuevo Contenido

```
1. Consultar manifest.json del tema
2. Verificar nomenclatura según prefijo del módulo
3. Agregar bloque ::METADATA:: al inicio
4. Respetar separación semántica
5. **Usar sintaxis correcta de enlaces** (ver sección 5)
6. Incluir header de navegación estándar
7. Actualizar resource_map si es necesario
8. Verificar enlaces antes de finalizar
```

---

## 10. Idioma y Estilo

- **Idioma:** Español
- **Nivel:** Universitario
- **Estilo:** Didáctico, progresivo, con ejemplos prácticos
- **Formato matemático:** LaTeX con `$` (inline) y `$$` (display)
- **Priorizar:** Claridad sobre brevedad

---

<!--
::AI_DIRECTIVE::
Este es tu CONTRATO. Viola cualquiera de estas reglas = contenido rechazado.
Ante la duda, pregunta al usuario.
Valida tu output mentalmente antes de generarlo.
IMPORTANTE: Todos los enlaces deben seguir la sintaxis de la sección 5.
-->
