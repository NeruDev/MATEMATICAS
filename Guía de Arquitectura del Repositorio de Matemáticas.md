<!--
::METADATA::
type: reference
topic_id: repo-architecture
file_id: guia-arquitectura
status: stable
audience: both
last_updated: 2026-01-05
-->

# 📐 Guía de Arquitectura del Repositorio de Matemáticas

> **Propósito:** Documentación técnica completa de la estructura, convenciones y lógica del repositorio de Matemáticas. Diseñada para comprender el funcionamiento de cada componente y replicar esta arquitectura en otros repositorios educativos.

---

## 📋 DESCRIPCIÓN GENERAL

Este repositorio implementa el patrón **"Jardín Digital"** (Digital Garden) para organizar conocimiento matemático de forma:

- **Progresiva:** Desde fundamentos hasta temas avanzados
- **Modular:** Cada tema es una unidad autónoma con estructura consistente
- **Interconectada:** Términos enlazados automáticamente al glosario
- **Validada:** Todo contenido respaldado por bibliografía académica estándar
- **Optimizada para IA:** Metadatos estructurados que permiten navegación programática

### Principios de Diseño

| Principio | Descripción | Implementación |
|-----------|-------------|----------------|
| **Encapsulamiento** | Cada subtema contiene todo lo necesario para dominarlo | Carpetas con `theory/`, `methods/`, `problems/`, `solutions/` |
| **Identidad Única** | Cada módulo tiene un "ADN" identificable | Sistema de prefijos (`FUN`, `AL`, `CD`, etc.) |
| **Separación Semántica** | Distinguir "el qué" del "cómo" | `theory/` vs `methods/` |
| **Automatización** | Scripts mantienen integridad sin intervención | `00-META/tools/*.py` |
| **Doble Audiencia** | Navegable por humanos e interpretable por IA | Markdown + JSON + `::METADATA::` |

---

## 🧬 ANATOMÍA DEL REPOSITORIO

### Nivel 0 — Raíz del Repositorio

```
MATEMATICAS-GITHUB/
│
├── 📄 ARCHIVOS DE NAVEGACIÓN PRINCIPAL
│   ├── README.md                        # Portada del repositorio, skill tree visual
│   ├── WIKI_INDEX.md                    # Mapa de navegación centralizado (TOC maestro)
│   └── glossary.md                      # ~150 términos matemáticos con definiciones
│
├── 📄 ARCHIVOS DE DOCUMENTACIÓN
│   ├── Guía de Arquitectura del Repositorio de Matemáticas.md  # Este archivo
│   └── AUDITORIA_ESTADO_REPO.md         # Reporte de salud e integridad
│
├── 🎛️ 00-META/                          # CENTRO DE CONTROL (configuración global)
│   ├── ia-contract.md                   # ⚖️ LEY SUPREMA para asistentes IA
│   ├── ai-directives.md                 # Reglas técnicas complementarias
│   ├── nomenclatura-estandar.md         # Convenciones de nombrado de archivos
│   ├── bibliografia-general.md          # Biblioteca central de referencias
│   ├── notation-cheatsheet.md           # Símbolos LaTeX y convenciones
│   ├── study-guide.md                   # Guía de estudio para estudiantes
│   ├── directory-tree.md                # Árbol de directorios actualizado
│   ├── audit-file-list.md               # Lista de archivos para auditoría
│   ├── audit-table-issues.md            # Registro de issues de tablas
│   ├── repo-tests.md                    # Pruebas lógicas de integridad
│   ├── prompts-for-students.md          # Prompts prediseñados para IA
│   ├── plantilla-respuestas.md          # Modelo para archivos de soluciones
│   └── tools/                           # 🔧 Scripts de automatización
│       ├── validate_repo.py             # Auditor general de estructura
│       ├── link_knowledge_base.py       # Auto-vinculador al glosario
│       ├── check_tables.py              # Validador de tablas Markdown
│       └── graphics/                    # Subsistema de generación visual
│
├── 📚 MÓDULOS DE CONTENIDO
│   ├── 01-Fundamentos/                  # Simbología, Aritmética, Álgebra, Geometría...
│   ├── 02-Algebra-Lineal/               # Matrices, Determinantes, Sistemas...
│   ├── 03-Calculo-Diferencial/          # Límites, Derivadas, Aplicaciones...
│   ├── 04-Calculo-Integral/             # Integral Indefinida, Técnicas...
│   ├── 05-Calculo-Vectorial/            # Vectores, Curvas, Varias Variables...
│   ├── 06-Ecuaciones-Diferenciales/     # EDO, Sistemas, Laplace...
│   └── 07-Metodos-Numericos/            # Raíces, Interpolación, Integración...
│
└── 🐍 .venv/                            # Entorno virtual Python (ignorado)
```

---

## 📄 ARCHIVOS RAÍZ — DESCRIPCIÓN DETALLADA

### 1. `README.md` — Portada del Repositorio

**Función:** Primera impresión y punto de entrada. Define la identidad del proyecto como "Jardín Digital Interconectado".

**Contenido clave:**
- Explicación de la filosofía del repositorio
- Instrucciones diferenciadas para humanos y para IAs
- Tabla de módulos con prefijos, estados y bibliografía
- Skill tree (diagrama Mermaid de dependencias)
- Enlaces rápidos a recursos principales

**Extracto del bloque de metadatos:**
```markdown
<!--
::METADATA::
type: index
topic_id: repo-readme
file_id: README
status: stable
audience: student
last_updated: 2026-01-03
-->
```

### 2. `WIKI_INDEX.md` — Mapa de Navegación Centralizado

**Función:** Tabla de contenidos maestra que enlaza jerárquicamente todos los módulos, subtemas, teoría, métodos, problemas y soluciones.

**Uso:** Permite encontrar cualquier recurso desde un solo lugar sin necesidad de explorar carpetas.

### 3. `glossary.md` — Diccionario Centralizado

**Función:** Proporciona un vocabulario común con definiciones consistentes para todo el repositorio.

**Características especiales:**
- Cada término tiene: definición formal + analogía intuitiva
- Los términos se convierten en destinos de enlaces automáticos
- El script `link_knowledge_base.py` vincula automáticamente la primera mención de cada término en los archivos de contenido

**Estructura de un término:**
```markdown
### función

> **Definición formal:** Una regla que asigna a cada elemento de un conjunto A 
> exactamente un elemento del conjunto B.
> 
> **Analogía:** Piensa en una máquina expendedora: insertas una moneda (entrada) 
> y siempre obtienes el mismo producto (salida).
>
> **Ver también:** [dominio](#dominio), [rango](#rango)
```

### 4. `AUDITORIA_ESTADO_REPO.md` — Reporte de Salud

**Función:** Documento auto-generado que certifica la integridad del repositorio.

**Contenido:**
- Estadísticas (número de archivos, temas completos)
- Estado de enlaces internos (rotos vs. funcionales)
- Registro de correcciones realizadas
- Sello de certificación: "ÓPTIMO PARA IA"

---

## 🎛️ CARPETA `00-META` — CENTRO DE CONTROL

Esta carpeta actúa como el **"cerebro"** administrativo del repositorio. Contiene las reglas, estándares y herramientas que mantienen la coherencia del proyecto.

### Jerarquía de Archivos

```
00-META/
├── 🤖 DIRECTIVAS PARA IA (Core legislativo)
│   ├── ia-contract.md              # LEY SUPREMA - Toda IA debe leerlo primero
│   └── ai-directives.md            # Reglas técnicas complementarias
│
├── 📏 ESTÁNDARES Y NORMAS
│   ├── nomenclatura-estandar.md    # Convenciones de nombrado
│   ├── notation-cheatsheet.md      # Símbolos LaTeX estándar
│   └── bibliografia-general.md     # Fuentes académicas autorizadas
│
├── 🔍 HERRAMIENTAS DE AUDITORÍA
│   ├── audit-file-list.md          # Lista de archivos que DEBEN existir
│   ├── audit-table-issues.md       # Problemas detectados en tablas
│   ├── directory-tree.md           # Árbol de directorios ideal
│   └── repo-tests.md               # Pruebas lógicas de integridad
│
├── 🎓 RECURSOS PARA ESTUDIANTES
│   ├── study-guide.md              # Guía de navegación para humanos
│   ├── prompts-for-students.md     # Prompts listos para usar con IA
│   └── plantilla-respuestas.md     # Modelo para crear soluciones
│
└── 🔧 tools/                        # Scripts de automatización
    ├── validate_repo.py
    ├── link_knowledge_base.py
    ├── check_tables.py
    └── graphics/                    # Subsistema gráfico
```

---

## ⚖️ SISTEMA DE DIRECTIVAS PARA IA

### `ia-contract.md` — La Ley Suprema

Este es el **documento más importante para cualquier asistente de IA**. Define las reglas fundamentales que gobiernan toda interacción con el repositorio.

**Estructura del contrato:**

```markdown
## 1. Estructura del Repositorio
   - Tabla de módulos con prefijos y estados
   - Estructura obligatoria de cada subtema

## 2. Sistema de Nomenclatura
   - Patrón: [PREFIJO]-[XX]-[Contenido].md
   - Excepciones documentadas

## 3. Metadatos Obligatorios
   - Bloque ::METADATA:: en archivos .md
   - Estructura del manifest.json

## 4. Reglas de Generación de Contenido
   - Separación semántica (theory vs methods)
   - Formato de problemas (tres niveles)
   - Notación matemática en tablas
```

**Prefijos definidos en el contrato:**

```python
# Extraído de validate_repo.py
PREFIXES = {
    "01-Fundamentos": "FUN",
    "02-Algebra-Lineal": "AL",
    "03-Calculo-Diferencial": "CD",
    "04-Calculo-Integral": "CI",
    "05-Calculo-Vectorial": "CV",
    "06-Ecuaciones-Diferenciales": "ED",
    "07-Metodos-Numericos": "MN",
}
```

### `ai-directives.md` — Reglas Técnicas

Complementa el contrato con soluciones a problemas técnicos recurrentes:

**Problema crítico: Valor absoluto en tablas**

El símbolo `|` para valor absoluto (`\$|x|\$`) interfiere con los separadores de columnas Markdown.

```markdown
| ❌ Incorrecto | ✅ Correcto |
|---------------|-------------|
| `\$|x|\$`       | `\$\lvert x \rvert\$` |
| `\$||v||\$`     | `\$\lVert v \rVert\$` |
```

**Formato obligatorio de soluciones:**

```markdown
**[Prob-XX])** *Contexto: [Concepto/método aplicable]*

[Desarrollo paso a paso]

**Verificación:** [Comprobación del resultado]
```

---

## 🏷️ SISTEMA DE NOMENCLATURA

### Patrón de Nombres

```
[PREFIJO]-[XX]-[Contenido]-[Tipo].md

Donde:
- PREFIJO: 2-3 letras del módulo (FUN, AL, CD, CI, CV, ED, MN)
- XX: Número del subtema (01, 02, ...)
- Contenido: Nombre descriptivo en PascalCase
- Tipo: Teoria, Metodos, Problemas, Respuestas, Intro, Resumen-Formulas
```

**Ejemplos válidos:**
- `FUN-02-Aritmetica-Intro.md`
- `AL-01-Teoria-Matrices.md`
- `CD-02-Metodos-Derivadas.md`
- `CI-03-Problemas.md`

### Excepciones Documentadas

El script `validate_repo.py` define las excepciones formalmente:

```python
class NomenclatureExceptions:
    # Carpetas completamente exentas del sistema de prefijos
    EXEMPT_FOLDERS = {
        "01-Fundamentos/01-Simbologia-Matematica/theory": 
            "Biblioteca de referencia sin secuencia de aprendizaje",
        "00-META": 
            "Carpeta de metadatos del repositorio",
    }
    
    # Patrones de archivos exentos
    EXEMPT_FILE_PATTERNS = [
        r"^_directives\.md\$",           # Archivos de directivas
        r"^manifest\.json\$",            # Manifiestos
        r"^solucion-.*\.md\$",           # Soluciones dentro de prob-XX/
        r"^00-Index\.md\$",              # Índices de módulo
    ]
    
    # Carpetas donde los archivos internos están exentos
    EXEMPT_INTERNAL_FOLDERS = [
        "prob-",                        # Carpetas de soluciones prob-XX/
        "media",                        # Recursos multimedia
    ]
    
    # 🆕 Carpetas SANDBOX — Exentas de TODAS las reglas
    SANDBOX_FOLDERS = [
        "Notas",                        # Zona libre para recursos sin clasificar
    ]
```

> **🔓 Carpetas Notas (SANDBOX):** Cada subtema contiene una carpeta `Notas/` que actúa como **zona libre** para el usuario. Cualquier contenido dentro de `*/Notas/*` está **completamente exento** de todas las reglas del repositorio (nomenclatura, metadatos, formato, etc.). Esta carpeta sirve como buzón temporal para recursos que serán clasificados posteriormente.

---

## 📂 ESTRUCTURA DE MÓDULOS

### Nivel 1 — Módulo Principal (Materia)

Cada módulo corresponde a una asignatura o área matemática completa.

```
XX-Nombre-Modulo/
├── 00-Index.md                      # Índice maestro de la categoría
├── 01-[Subtema-1]/                  # Primer subtema
├── 02-[Subtema-2]/                  # Subtemas en orden progresivo
├── ...
└── NN-[Subtema-N]/                  # Último subtema
```

### Nivel 2 — Subtema (Unidad Atómica de Aprendizaje)

**Estructura completa con comentarios:**

```
XX-Nombre-Subtema/                    [NIVEL 2] UNIDAD DE CONOCIMIENTO
│
├── 📋 ARCHIVOS DE CONFIGURACIÓN (Cerebro del módulo)
│   ├── manifest.json                # ⚙️ Metadatos para IA: recursos, tags, bibliografía
│   └── _directives.md               # 🤖 Instrucciones específicas para este tema
│
├── 📚 ARCHIVOS DE CONTENIDO PRINCIPAL
│   ├── PREFIJO-XX-*-Intro.md        # 🚀 PORTADA: Introducción y mapa del tema
│   └── PREFIJO-XX-Resumen-Formulas.md # 📝 CHEATSHEET: Fórmulas clave para repaso
│
├── 📖 CARPETAS DE CONTENIDO SEMÁNTICO
│   ├── theory/                      # 📐 EL "QUÉ": Definiciones, teoremas, demostraciones
│   │   └── PREFIJO-XX-Teoria-*.md
│   │
│   ├── methods/                     # 🔧 EL "CÓMO": Algoritmos, procedimientos paso a paso
│   │   └── PREFIJO-XX-Metodos-*.md
│   │
│   ├── problems/                    # ✏️ PRÁCTICA: Banco de ejercicios sin resolver
│   │   └── PREFIJO-XX-Problemas.md
│   │
│   └── solutions/                   # ✅ VALIDACIÓN: Sistema de 3 niveles
│       ├── PREFIJO-XX-Respuestas.md       # Nivel 1: Solo resultado final
│       ├── PREFIJO-XX-Soluciones-Desarrolladas.md  # Nivel 2: Desarrollo con contexto
│       └── prob-XX/                       # Nivel 3: Solución individual extensa
│           └── solucion-metodo.md
│
├── 📁 CARPETAS OPCIONALES
│   ├── applications/                # 🌍 Conexiones con el mundo real
│   ├── diagnostic/                  # 🩺 Evaluaciones de conocimientos previos
│   └── media/                       # 🖼️ Imágenes, diagramas, gráficos
│       └── generated/               # Gráficos auto-generados por Python
│
└── 🔓 ZONA SANDBOX (Exenta de reglas)
    └── Notas/                       # 📝 Recursos sin clasificar del usuario
        └── README.md                # Directiva de excepción para IA
```

---

## � CARPETAS NOTAS — ZONA SANDBOX

### Concepto

Cada subtema contiene una carpeta `Notas/` que funciona como **buzón temporal** para el usuario. Esta zona está **completamente exenta** de todas las reglas del repositorio, permitiendo agregar cualquier tipo de contenido sin preocuparse por nomenclatura, formato o metadatos.

### Propósito

| Característica | Descripción |
|----------------|-------------|
| **Almacenamiento temporal** | Lugar para guardar recursos que aún no están clasificados |
| **Flexibilidad total** | Acepta cualquier tipo de archivo y formato |
| **Sin validación** | La IA no aplicará reglas ni sugerirá correcciones |
| **Clasificación futura** | El contenido puede ser organizado posteriormente en carpetas formales |

### Contenido Permitido

- 📄 **Documentos:** Apuntes, borradores, resúmenes personales
- 🖼️ **Multimedia:** Imágenes, capturas, diagramas externos
- 💻 **Código:** Scripts de cualquier lenguaje, experimentos
- 📎 **Archivos externos:** PDFs, referencias, material complementario
- 📝 **Cualquier formato:** Sin restricción de extensión ni estructura

### Comportamiento de la IA

| Acción | Comportamiento |
|--------|----------------|
| Validar nomenclatura | ⛔ OMITIR |
| Sugerir correcciones de formato | ⛔ OMITIR |
| Solicitar metadatos `::METADATA::` | ⛔ OMITIR |
| Leer contenido | ✅ COMPLETO (`READ_FULL_CONTEXT`) |
| Integrar información | ✅ Como contexto adicional |
| Vincular a manifest.json | ⛔ NO REQUERIDO |

### Estructura del README de Notas

Cada carpeta `Notas/` contiene un `README.md` con metadatos especiales:

```markdown
<!--
::METADATA::
type: sandbox
topic_id: notas-usuario
file_id: Notas-README
status: exempt
scope: local_only
ai_directive: READ_FULL_CONTEXT
validation: NONE
rules_exempt: true
-->

# 📝 Notas del Usuario — Zona Libre

Esta carpeta es una **zona sandbox** exenta de todas las reglas...
```

### Flujo de Trabajo Sugerido

```
1. Usuario encuentra recurso útil (apunte, imagen, código)
2. Lo guarda en Notas/ del subtema más cercano
3. Cuando tenga tiempo, lo clasifica:
   - Si es teoría → mueve a theory/
   - Si es ejercicio → mueve a problems/
   - Si es multimedia → mueve a media/
4. Al mover, aplica nomenclatura estándar y metadatos
```

### Patrón de Ruta de Excepción

La IA detecta automáticamente cualquier ruta que contenga `/Notas/` y desactiva todas las validaciones:

```
Patrón: */Notas/*

Ejemplos detectados como SANDBOX:
✅ 01-Fundamentos/02-Aritmetica/Notas/apunte.md
✅ 03-Calculo-Diferencial/01-Limites/Notas/grafico.png
✅ 02-Algebra-Lineal/04-Espacios-Vectoriales/Notas/codigo.py
```

---

## �📄 FUNCIÓN DETALLADA DE CADA ARCHIVO

### 1. `manifest.json` — El Contrato Central del Subtema

El `manifest.json` es el **archivo más importante** de cada subtema para la IA. Actúa como:

| Función | Descripción |
|---------|-------------|
| **Mapa de recursos** | Indica exactamente dónde está cada archivo |
| **Contrato IA** | Define tareas permitidas y formato de respuestas |
| **Registro bibliográfico** | Documenta fuentes de validación académica |
| **Metadatos** | Estado, dificultad, tiempo estimado, tags |

**Estructura completa con explicación línea por línea:**

```json
{
  // ═══════════════════════════════════════════════════════════
  // IDENTIFICACIÓN — ¿Qué es este módulo?
  // ═══════════════════════════════════════════════════════════
  "id": "fun-02-aritmetica",          // ID único: prefijo-número-nombre (minúsculas)
  "topic": "Aritmética",              // Nombre legible para humanos
  "type": "learning_module",          // Tipo: learning_module | reference_library
  "status": "active",                 // Estado: active | draft | deprecated
  "last_updated": "2024-12-23",       // Fecha ISO de última modificación
  
  // ═══════════════════════════════════════════════════════════
  // PROPÓSITO Y CLASIFICACIÓN — ¿Para qué sirve?
  // ═══════════════════════════════════════════════════════════
  "human_purpose": "Dominar operaciones numéricas básicas y razonamiento aritmético",
  "tags": ["numeros", "operaciones", "fracciones", "porcentajes"],
  "skill_nodes": ["aritmetica:operaciones-basicas", "aritmetica:fracciones"],
  "difficulty": "básico",             // básico | intermedio | avanzado
  "estimated_time": "4-6 horas",
  
  // ═══════════════════════════════════════════════════════════
  // MAPA DE RECURSOS — ¿Dónde está cada archivo?
  // La IA usa esto para navegar sin explorar carpetas
  // ═══════════════════════════════════════════════════════════
  "resource_map": {
    "entry_point": "FUN-02-Aritmetica-Intro.md",           // Primera lectura
    "main_theory": "theory/FUN-02-Teoria-Aritmetica.md",   // Teoría completa
    "cheat_sheet": "FUN-02-Resumen-Formulas.md",           // Referencia rápida
    "methods": ["methods/FUN-02-Metodos-Aritmetica.md"],   // Lista de procedimientos
    "problems": ["problems/FUN-02-Problemas.md"],          // Banco de ejercicios
    "answers": "solutions/FUN-02-Respuestas.md",           // Tabla de respuestas
    "solutions": ["solutions/FUN-02-Soluciones-Desarrolladas.md"]
  },
  
  // ═══════════════════════════════════════════════════════════
  // SUBTEMAS INTERNOS — Desglose del contenido
  // ═══════════════════════════════════════════════════════════
  "subtopics": [
    {"id": "2.1", "title": "Sistemas numéricos", "concepts": ["ℕ", "ℤ", "ℚ", "ℝ"]},
    {"id": "2.2", "title": "Operaciones fundamentales", "concepts": ["Suma", "Resta", "Multiplicación", "División"]},
    {"id": "2.3", "title": "Divisibilidad y primos", "concepts": ["Criterios", "Factorización"]},
    {"id": "2.4", "title": "MCD y MCM", "concepts": ["Algoritmo de Euclides"]},
    {"id": "2.5", "title": "Fracciones", "concepts": ["Operaciones", "Simplificación"]},
    {"id": "2.6", "title": "Decimales y porcentajes", "concepts": ["Conversiones"]},
    {"id": "2.7", "title": "Potencias y raíces", "concepts": ["Leyes de exponentes"]},
    {"id": "2.8", "title": "Razones y proporciones", "concepts": ["Regla de tres"]}
  ],
  
  // ═══════════════════════════════════════════════════════════
  // CONTRATO IA — ¿Cómo debe comportarse el asistente?
  // ═══════════════════════════════════════════════════════════
  "ai_contract": {
    "default_output": "markdown",
    "allowed_tasks": [
      "explain_concept",    // Explicar conceptos teóricos
      "generate_problems",  // Crear problemas nuevos
      "convert_format",     // Convertir entre formatos
      "verify_solution",    // Verificar soluciones del estudiante
      "diagnostic_check"    // Evaluación diagnóstica
    ],
    "solution_guidelines": {
      "require_context": true,        // SIEMPRE dar contexto antes de resolver
      "step_by_step": true,           // Mostrar pasos intermedios
      "didactic_tone": "Guía al estudiante como tutor personal"
    }
  },
  
  // ═══════════════════════════════════════════════════════════
  // VALIDACIÓN BIBLIOGRÁFICA — Fuentes académicas
  // ═══════════════════════════════════════════════════════════
  "references": [
    {
      "citation": "Baldor, A. (2017). Aritmética. 2ª ed. Patria.",
      "mapping": {
        "Capítulo 1-5": "Sistemas numéricos y operaciones",
        "Capítulo 6-10": "Divisibilidad, MCD, MCM"
      }
    }
  ],
  "validation_status": {
    "validated": true,
    "date": "2024-12-23",
    "validator": "Auditoría bibliográfica",
    "notes": "Contenido verificado contra Baldor y Stewart"
  }
}
```

**Campos obligatorios según `validate_repo.py`:**

```python
REQUIRED_MANIFEST_FIELDS = ["id", "topic", "type", "status", "tags"]
VALID_MANIFEST_TYPES = ["learning_module", "reference_library"]
```

---

### 2. `_directives.md` — Instrucciones Específicas para IA

Este archivo **hereda** las directivas globales de `00-META/ia-contract.md` y añade reglas específicas del subtema.

**Estructura típica:**

```markdown
# Directivas — Aritmética

## Clasificación del Contenido

| Carpeta/Archivo | Archivo Principal | Descripción |
|-----------------|-------------------|-------------|
| `theory/` | `FUN-02-Teoria-Aritmetica.md` | Teoría completa |
| `methods/` | `FUN-02-Metodos-Aritmetica.md` | 12 procedimientos paso a paso |
| `problems/` | `FUN-02-Problemas.md` | 85 problemas (10+ por subtema) |
| `solutions/` | `FUN-02-Respuestas.md` | Soluciones contextualizadas |

## Subtemas (2.1 - 2.8)

1. **2.1** Sistemas numéricos (ℕ, ℤ, ℚ, ℝ)
2. **2.2** Operaciones fundamentales y PEMDAS
3. **2.3** Divisibilidad y números primos
...

## Directivas Específicas para IA

- **Audiencia:** Autoestudio universitario
- **Formato de salida:** Markdown con LaTeX
- **Tareas permitidas:** explain_concept, generate_problems, verify_solution
- **Al generar soluciones:** Incluir contexto explicando qué concepto/método aplica

## Notas de Formato Especiales

- En tablas, usar `\lvert \rvert` para valor absoluto en lugar de `| |`
- Cada problema debe indicar a qué subtema pertenece (ej: [2.3])
- Las soluciones siguen el formato: `**N)** *Contexto: [explicación]*`
```

---

### 3. `PREFIJO-XX-*-Intro.md` — Punto de Entrada

**El archivo más importante para el estudiante.** Es la puerta de entrada que orienta sobre el contenido disponible.

**Estructura obligatoria:**

```markdown
<!--
::METADATA::
type: index
topic_id: fun-02-aritmetica
file_id: FUN-02-Aritmetica-Intro
status: stable
audience: student
-->

> 🏠 **Navegación:** [← Volver al Índice Principal](../../WIKI_INDEX.md) | [📚 Glosario](../../glossary.md)

---

# Aritmética

## Propósito del tema
Dominar operaciones numéricas básicas y razonamiento aritmético para soportar álgebra y cálculo.

## Mapa de recursos

├── theory/      → Desarrollo teórico completo
├── methods/     → Procedimientos paso a paso
├── problems/    → 85 ejercicios de práctica
└── solutions/   → Respuestas y desarrollos

## Ruta de aprendizaje

1. **Sistemas numéricos**: \$\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}\$
2. **Operaciones fundamentales**: propiedades conmutativa, asociativa, distributiva
3. **Divisibilidad y primos**: criterios, factorización
...

## Tabla de fórmulas clave

| Concepto | Fórmula |
|----------|---------|
| MCD/MCM | Por exponentes mínimos/máximos |
| Fracciones | \$\frac{a}{b} + \frac{c}{d} = \frac{ad+bc}{bd}\$ |
| Potencias | \^m \cdot a^n = a^{m+n}\$ |
```

---

### 4. Carpeta `theory/` — El "Qué"

Contiene **desarrollo teórico completo**: definiciones, teoremas, demostraciones, propiedades.

**Convenciones de formato:**

| Elemento | Formato |
|----------|---------|
| Definiciones | **Negrita** o bloques `> ` |
| Teoremas | `### Teorema X.Y: Nombre` |
| Demostraciones | Bloques colapsables `<details>` |
| Fórmulas importantes | `\$\$...\$\$` (display mode) |
| Ejemplos | `#### Ejemplo X.Y.Z` |

---

### 5. Carpeta `methods/` — El "Cómo"

Contiene **procedimientos paso a paso** para resolver tipos específicos de problemas.

**Estructura de un método:**

```markdown
## Método: Factorización Prima

### Cuándo usar
Cuando necesites descomponer un número en sus factores primos.

### Pasos

1. **Dividir** el número entre el menor primo que lo divida exactamente
2. **Repetir** con el cociente hasta obtener 1
3. **Expresar** como producto de potencias de primos

### Ejemplo Resuelto

**Problema:** Factorizar 360

**Solución:**
- 360 ÷ 2 = 180
- 180 ÷ 2 = 90
- 90 ÷ 2 = 45
- 45 ÷ 3 = 15
- 15 ÷ 3 = 5
- 5 ÷ 5 = 1

**Resultado:** \ = 2^3 \cdot 3^2 \cdot 5\$

### Errores Comunes
- ❌ Olvidar que el 1 no es primo
- ✅ Siempre comenzar por el 2
```

---

### 6. Sistema de Soluciones de 3 Niveles

```
solutions/
├── PREFIJO-XX-Respuestas.md              # Nivel 1: Tabla de respuestas finales
├── PREFIJO-XX-Soluciones-Desarrolladas.md # Nivel 2: Desarrollos con contexto
└── prob-XX/                              # Nivel 3: Soluciones individuales extensas
    └── solucion-metodo.md
```

**Diagrama de decisión:**

```
ESTUDIANTE BUSCA SOLUCIÓN
           │
           ▼
    ¿Solo verificar resultado?
           │
    ┌──────┴──────┐
    │ SÍ          │ NO
    ▼             ▼
Respuestas.md   ¿Necesita explicación detallada?
(tabla rápida)    │
                  ├──────────────┐
                  │ BÁSICA       │ EXTENSA
                  ▼              ▼
    Soluciones-      prob-XX/
    Desarrolladas    solucion-metodo.md
```

---

## 🔧 SCRIPTS DE AUTOMATIZACIÓN

### Ubicación: `00-META/tools/`

```
tools/
├── validate_repo.py             # Auditor general de estructura
├── link_knowledge_base.py       # Auto-vinculador al glosario
├── check_tables.py              # Validador de tablas Markdown
└── graphics/                    # Subsistema de generación visual
    ├── config.yaml              # Configuración global
    ├── generate_graphics.py     # Motor de renderizado
    ├── requirements.txt         # Dependencias Python
    ├── templates/               # Estilos visuales reutilizables
    │   ├── style_common.py      # Colores, fuentes, configuraciones
    │   └── style_2d.py          # Configuración para gráficos 2D
    └── sources/                 # Código fuente de cada gráfico
        ├── FUN-04/              # Gráficos de Geometría
        ├── CV-01/               # Gráficos de Cálculo Vectorial
        └── ...
```

---

### 1. `validate_repo.py` — El Auditor

**Función:** Recorre todo el repositorio verificando que se cumpla el `ia-contract.md`.

**Lo que valida:**

```python
# Extracto de validate_repo.py

# 1. Metadatos ::METADATA:: en archivos .md
VALID_METADATA_TYPES = [
    "theory", "method", "problem", "solution", "reference", 
    "index", "cheatsheet", "problem_set", "answer-key"
]

# 2. Estructura de manifest.json
REQUIRED_MANIFEST_FIELDS = ["id", "topic", "type", "status", "tags"]

# 3. Nomenclatura de archivos
VALID_SUFFIXES = [
    "-Intro", "-Resumen-Formulas", "-Teoria", "-Metodos",
    "-Problemas", "-Respuestas", "-Diagnostico"
]

# 4. Prefijos correctos por módulo
PREFIXES = {
    "01-Fundamentos": "FUN",
    "02-Algebra-Lineal": "AL",
    ...
}
```

**Salida:** Genera el archivo `AUDITORIA_ESTADO_REPO.md` con estadísticas e issues encontrados.

---

### 2. `link_knowledge_base.py` — El Bibliotecario Automático

**Función:** Transforma el repositorio en un "Jardín Digital" interconectado:

1. Extrae todos los términos del `glossary.md`
2. Escanea archivos de contenido (`theory/`, `problems/`, etc.)
3. Vincula automáticamente la primera mención de cada término

**Configuración clave:**

```python
# Carpetas a escanear para contenido
CONTENT_FOLDERS = [
    "01-Fundamentos",
    "02-Algebra-Lineal",
    "03-Calculo-Diferencial",
    ...
]

# Subcarpetas que contienen contenido enlazable
CONTENT_SUBFOLDERS = ["theory", "problems", "methods", "applications", "solutions"]

# Términos mínimos para vincular
MIN_TERM_LENGTH = 3

# Modo seguro (True = solo muestra cambios, False = aplica)
DRY_RUN = True
```

**Ejemplo de transformación:**

```markdown
# Antes:
La derivada de una función...

# Después:
La [derivada](../../glossary.md#derivada) de una [función](../../glossary.md#funcion)...
```

---

### 3. `check_tables.py` — Validador de Tablas

**Función:** Detecta tablas Markdown con columnas desalineadas.

**Problema que resuelve:**

```markdown
❌ INCORRECTO (columnas no coinciden):
| Columna1 | Columna2 |
|----------|:--------:|:-------:|
| dato1 | dato2 | dato3 |

✅ CORRECTO:
| Columna1 | Columna2 | Columna3 |
|----------|:--------:|:--------:|
| dato1 | dato2 | dato3 |
```

---

### 4. Subsistema Gráfico (`tools/graphics/`)

**Filosofía:** "Gráficos como Código" — En lugar de crear imágenes manualmente, se definen matemáticamente en Python.

**Ventajas:**
- Estilo visual consistente en todo el repositorio
- Fácil actualización (cambiar un color en `templates/` actualiza todo)
- Versionable en Git
- Regenerable automáticamente

**Configuración global (`config.yaml`):**

```yaml
# Estilos visuales globales
style:
  # Paleta de colores (accesible y consistente)
  colors:
    primary: "#2563eb"      # Azul - figuras principales
    secondary: "#dc2626"    # Rojo - elementos destacados
    accent: "#059669"       # Verde - elementos auxiliares
    grid: "#e5e7eb"         # Gris claro - cuadrículas
    
  # Grosores de línea
  line_widths:
    default: 2.0
    thin: 1.0
    thick: 3.0

# Mapeo de prefijos a módulos
modules:
  FUN: "01-Fundamentos"
  AL: "02-Algebra-Lineal"
  ...
```

**Estructura de un script de gráfico:**

```python
# sources/FUN-04/triangulo_altura.py

METADATA = {
    "topic_id": "FUN-04",
    "name": "triangulo_altura",
    "description": "Triángulo con altura marcada",
    "used_in": ["theory/FUN-04-Teoria-Geometria.md"],
    "section": "4.3"
}

def generate() -> plt.Figure:
    fig, ax = plt.subplots()
    # ... código para dibujar el triángulo ...
    return fig
```

**Uso:**

```bash
python generate_graphics.py                    # Genera todos
python generate_graphics.py --topic FUN-04     # Solo geometría
python generate_graphics.py --file triangulo   # Archivo específico
```

---

## ✅ BLOQUE `::METADATA::` — Metadatos de Archivos

Todo archivo `.md` debe comenzar con un bloque de metadatos HTML:

```markdown
<!--
::METADATA::
type: [theory | method | problem | solution | reference | index | cheatsheet | answer-key]
topic_id: [id-del-tema]
file_id: [nombre-archivo-sin-extension]
status: [draft | review | stable | active]
audience: [student | ai_context | both | exam_review]
last_updated: YYYY-MM-DD
-->
```

**Tipos válidos según `validate_repo.py`:**

| type | Descripción | Ubicación típica |
|------|-------------|------------------|
| `theory` | Desarrollo teórico | `theory/*.md` |
| `method` | Procedimiento paso a paso | `methods/*.md` |
| `problem` | Enunciados de problemas | `problems/*.md` |
| `solution` | Soluciones desarrolladas | `solutions/*.md` |
| `reference` | Material de consulta | `00-META/*.md` |
| `index` | Índice o punto de entrada | `*-Intro.md`, `00-Index.md` |
| `cheatsheet` | Resumen de fórmulas | `*-Resumen-Formulas.md` |
| `answer-key` | Tabla de respuestas | `*-Respuestas.md` |

---

## 🔗 SISTEMA DE ENLACES

### Sintaxis Obligatoria

```markdown
[Texto visible](ruta/relativa/archivo.md)
[Texto visible](ruta/relativa/archivo.md#ancla)
```

### Ejemplos por Tipo

| Tipo | Sintaxis | Ejemplo |
|------|----------|---------|
| Mismo directorio | `[texto](archivo.md)` | `[Intro](FUN-02-Intro.md)` |
| Subdirectorio | `[texto](carpeta/archivo.md)` | `[Teoría](theory/FUN-02-Teoria.md)` |
| Directorio padre | `[texto](../archivo.md)` | `[Índice](../00-Index.md)` |
| Al glosario | `[término](../glossary.md#ancla)` | `[función](../glossary.md#funcion)` |
| Entre módulos | `[texto](../Modulo/archivo.md)` | `[Matrices](../02-Algebra-Lineal/)` |

### Header de Navegación Estándar

Todo archivo de contenido debe incluir al inicio:

```markdown
> 🏠 **Navegación:** [← Volver al Índice Principal](../../WIKI_INDEX.md) | [📚 Glosario](../../glossary.md)
```

---

## 📚 VALIDACIÓN BIBLIOGRÁFICA

### Arquitectura

```
                    00-META/bibliografia-general.md
                    (BIBLIOTECA CENTRAL)
                              │
         ┌────────────────────┼────────────────────┐
         ▼                    ▼                    ▼
   manifest.json        manifest.json        manifest.json
   (references)         (references)         (references)
```

### Bibliografía Estándar por Módulo

| Módulo | Autores Principales |
|--------|---------------------|
| Fundamentos | Baldor, Sullivan, Swokowski |
| Álgebra Lineal | Grossman, Lay, Strang |
| Cálculo Diferencial/Integral | Stewart, Larson, Thomas |
| Cálculo Vectorial | Stewart, Marsden |
| Ecuaciones Diferenciales | Zill, Boyce, Nagle |
| Métodos Numéricos | Burden, Chapra, Mathews |

---

## 🗂️ RESUMEN: MÓDULOS DEL REPOSITORIO

| # | Prefijo | Módulo | Subtemas |
|---|---------|--------|----------|
| 01 | `FUN` | **Fundamentos** | Simbología, Aritmética, Álgebra, Geometría, Trigonometría, Geometría Analítica |
| 02 | `AL` | **Álgebra Lineal** | Matrices, Determinantes, Sistemas Lineales, Espacios Vectoriales, Transformaciones, Valores Propios |
| 03 | `CD` | **Cálculo Diferencial** | Límites, Derivadas, Aplicaciones, Teoremas Fundamentales |
| 04 | `CI` | **Cálculo Integral** | Integral Indefinida, Técnicas, Integral Definida, Aplicaciones, Impropias |
| 05 | `CV` | **Cálculo Vectorial** | Vectores, Curvas, Funciones Vectoriales, Varias Variables, Integración Múltiple |
| 06 | `ED` | **Ecuaciones Diferenciales** | EDO Primer Orden, Segundo Orden, Sistemas, Laplace, Series de Potencias |
| 07 | `MN` | **Métodos Numéricos** | Raíces, Interpolación, Integración Numérica, EDO Numéricas |

---

## 🔄 FLUJO DE TRABAJO PARA CONTRIBUIR

### 1. Entrada al módulo
Usuario/IA entra por `*-Intro.md` para obtener contexto.

### 2. Aprendizaje
- Para entender conceptos → `theory/`
- Para aprender a calcular → `methods/`

### 3. Práctica
Ejercitar con `problems/`

### 4. Verificación
- Resultado rápido → `solutions/Respuestas.md`
- Desarrollo paso a paso → `solutions/Soluciones-Desarrolladas.md` o `prob-XX/`

### 5. Mantenimiento automático
Los scripts en `00-META/tools/` validan que la estructura se mantenga íntegra.

---

## 📋 CHECKLIST PARA REPLICAR ESTA ARQUITECTURA

### Fase 1: Estructura Base
- [ ] Crear `README.md` con skill tree
- [ ] Crear `WIKI_INDEX.md` vacío
- [ ] Crear `glossary.md` con términos iniciales
- [ ] Crear carpeta `00-META/` con:
  - [ ] `ia-contract.md` — Definir prefijos y reglas
  - [ ] `nomenclatura-estandar.md` — Convenciones de nombrado
  - [ ] `bibliografia-general.md` — Fuentes académicas

### Fase 2: Módulos
- [ ] Crear carpetas de módulos (`01-XX/` a `NN-XX/`)
- [ ] Crear `00-Index.md` en cada módulo
- [ ] Definir prefijos para cada módulo

### Fase 3: Subtemas
- [ ] Crear estructura de carpetas por subtema
- [ ] Crear `manifest.json` con campos obligatorios
- [ ] Crear `_directives.md` heredando de `ia-contract.md`
- [ ] Crear `*-Intro.md` como punto de entrada

### Fase 4: Contenido
- [ ] Poblar `theory/` con desarrollo teórico
- [ ] Crear `methods/` con procedimientos
- [ ] Crear `problems/` con ejercicios
- [ ] Implementar sistema de 3 niveles en `solutions/`

### Fase 5: Automatización
- [ ] Adaptar `validate_repo.py` con nuevos prefijos
- [ ] Configurar `link_knowledge_base.py` con carpetas de contenido
- [ ] (Opcional) Configurar subsistema gráfico

---

**Última actualización:** 2026-01-05  
**Versión:** 5.0 — Documentación técnica completa  
**Estado:** 7 módulos, ~35 subtemas, validación bibliográfica activa

