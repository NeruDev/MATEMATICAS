<!--
::METADATA::
type: reference
topic_id: meta-ia-contract
file_id: ia-contract
status: stable
audience: ai_context
priority: LEVEL_2
last_updated: 2026-01-05
-->

# Contrato de IA para el Repositorio de Matemáticas

> **IMPORTANTE:** Este archivo es la guía principal para cualquier IA que interactúe con el repositorio.
> Lee este documento COMPLETAMENTE antes de generar o modificar contenido.
>
> **📍 PUNTO DE ENTRADA:** Si es una sesión nueva, lee primero [`.ai-bootstrap.md`](../.ai-bootstrap.md)

---

## 0. Jerarquía Normativa

> **⚠️ CRÍTICO:** Cuando exista conflicto entre documentos, aplicar en este orden:

| Nivel | Documento | Alcance | Prioridad |
|:-----:|-----------|---------|:---------:|
| **1** | `manifest.json` | Reglas del subtema específico | 🔴 Máxima |
| **1** | `_directives.md` | Directivas locales del subtema | 🔴 Máxima |
| **2** | `ia-contract.md` | **ESTE ARCHIVO** — Reglas globales | 🟠 Alta |
| **2** | `ai-directives.md` | Reglas técnicas (LaTeX, tablas) | 🟠 Alta |
| **3** | `nomenclatura-estandar.md` | Convenciones de nombrado | 🟡 Media |
| **4** | `README.md`, `WIKI_INDEX.md` | Información contextual | 🟢 Baja |

**Regla de resolución:**
```
manifest.json > ia-contract.md > nomenclatura-estandar.md > README.md
```

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
├── _directives.md                   # Directivas locales (OBLIGATORIO)
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
├── diagnostic/                      # Evaluaciones diagnósticas (opcional)
├── media/                           # Recursos multimedia (opcional)
└── Notas/                           # 🆕 SANDBOX - Contenido sin reglas
    └── README.md                    # Directiva de excepción
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
| **`*/Notas/*`** | 🆕 **SANDBOX:** Contenido exento de TODAS las reglas |

### 2.3 Carpetas Notas — Excepción Total (SANDBOX)

> **⚠️ DIRECTIVA CRÍTICA PARA IA:**

Las carpetas `Notas/` ubicadas en cada subtema son **zonas sandbox** completamente exentas del sistema normativo:

```
XX-Subtema/
└── Notas/                    # 🔓 SANDBOX - Sin reglas
    ├── README.md             # Directiva de excepción
    └── [cualquier contenido] # Sin validación
```

**Reglas que NO aplican en `Notas/`:**

| Categoría | Exención |
|-----------|----------|
| Nomenclatura | ❌ No se requiere prefijo ni formato estándar |
| Metadatos | ❌ No se requiere bloque `::METADATA::` |
| Validación | ❌ No se valida bibliografía ni estructura |
| Formato | ❌ No se aplican reglas de LaTeX ni tablas |
| Vinculación | ❌ No se auto-vincula al glosario |

**Contenido permitido:**
- 📄 Texto libre (notas, borradores, ideas)
- 🖼️ Multimedia (imágenes, diagramas, capturas)
- 💻 Código (scripts de prueba, experimentos)
- 📎 Archivos externos (PDFs, recursos descargados)

**Instrucción para IA:**
```
SI ruta contiene "/Notas/" → IGNORAR todas las reglas de validación
SI usuario pregunta por contenido en Notas/ → LEER COMPLETO para contexto
NO sugerir correcciones de nomenclatura para archivos en Notas/
TRATAR como sandbox aislado del repositorio principal
```

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

### 3.2 Campos Operativos (Opcionales pero Recomendados)

Estos campos permiten comportamiento contextual de la IA:

| Campo | Tipo | Valores | Propósito |
|-------|------|---------|-----------|
| `learning_role` | string | `introduction`, `reinforcement`, `assessment`, `reference` | Rol pedagógico del contenido |
| `difficulty` | string | `1/5` a `5/5` | Nivel de complejidad |
| `prerequisites` | array | `["CD-01", "FUN-03"]` | Temas que deben dominarse antes |
| `depends_on` | array | `["archivo.md"]` | Archivos referenciados directamente |
| `concepts` | array | `["derivada", "tangente"]` | Conceptos clave cubiertos |

**Ejemplo de metadatos completos:**

```markdown
<!--
::METADATA::
type: theory
topic_id: cd-02-derivadas
file_id: CD-02-Teoria-Derivadas
status: stable
learning_role: introduction
difficulty: 3/5
prerequisites: ["CD-01", "FUN-03"]
concepts: ["derivada", "tasa-de-cambio", "tangente"]
audience: student
last_updated: 2026-01-05
-->
```

### 3.3 Estructura del manifest.json

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

### 3.4 Perfiles de Uso en manifest.json (Recomendado)

Para comportamiento contextual, añadir `usage_profiles`:

```json
{
  "usage_profiles": {
    "study": {
      "description": "Aprendizaje profundo del tema",
      "preferred_resources": ["entry_point", "theory", "methods"],
      "explanation_depth": "high",
      "include_prerequisites": true
    },
    "quick_reference": {
      "description": "Consulta rápida de fórmulas",
      "preferred_resources": ["formula_sheet"],
      "explanation_depth": "minimal"
    },
    "assessment": {
      "description": "Práctica con problemas",
      "preferred_resources": ["problems"],
      "solutions_visible": false,
      "hints_allowed": true
    },
    "diagnostic": {
      "description": "Evaluar conocimientos previos",
      "preferred_resources": ["diagnostic"],
      "identify_gaps": true
    }
  }
}
```

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

### 4.5 Formato de Tablas (OBLIGATORIO)

⚠️ **Reglas críticas para tablas legibles:**

1. **Encabezados completos:** El número de columnas en la fila de encabezados DEBE coincidir con el número de columnas en los datos.
   
   ❌ **INCORRECTO:**
   ```markdown
   | Columna1 | Columna2 |
   |----------|:--------:|:-------:|:-----:|
   | dato1 | dato2 | dato3 | dato4 |
   ```
   
   ✅ **CORRECTO:**
   ```markdown
   | Columna1 | Columna2 | Columna3 | Columna4 |
   |----------|:--------:|:--------:|:--------:|
   | dato1 | dato2 | dato3 | dato4 |
   ```

2. **Separadores consistentes:** La fila de separadores `|---|` debe tener el mismo número de celdas que los encabezados.

3. **Alineación:**
   - `:---` = izquierda
   - `:---:` = centrado
   - `---:` = derecha

4. **Verificación:** Antes de guardar, contar manualmente las columnas en:
   - Fila de encabezados
   - Fila de separadores
   - Cada fila de datos

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
- `](../../..](` — patrón corrupto de enlace duplicado
- `[texto](README.md)` — no existen README en subtemas
- Enlaces sin extensión `.md`
- Rutas absolutas del sistema de archivos

### 5.5 Detección y Corrección de Enlaces Rotos

⚠️ **Patrón de error común detectado:**

```markdown
❌ INCORRECTO (enlace duplicado/corrupto):
| Columna | [texto](../../..](../../../glossary.md#termino) más texto

✅ CORRECTO:
| Columna | [texto](../../../glossary.md#termino) más texto
```

**Cómo detectar:** Buscar el patrón `](../../..](` o `](../..](` que indica un enlace mal cerrado.

**Cómo corregir:** Eliminar la parte duplicada `](../../..` o `](../..` y dejar solo un `](ruta/correcta.md#ancla)`.

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
| **Git LFS** | `.gitattributes` | Gestión de imágenes y archivos pesados |
| **Ignorados** | `.gitignore` | Exclusión de .venv y archivos basura |
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
