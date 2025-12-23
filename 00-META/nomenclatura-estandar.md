<!--
::METADATA::
type: reference
topic_id: meta-nomenclatura
file_id: nomenclatura-estandar
status: stable
audience: ai_context
last_updated: 2024-12-23
-->

# Estándar de Nomenclatura de Archivos

Este documento define las convenciones de nombrado para todos los archivos del repositorio.

---

## 0. Directiva de Control de Cambios

> **⚠️ OBLIGATORIO:** Todo cambio en el repositorio debe seguir este protocolo.

### 0.1 Reglas de Modificación

1. **Metadatos obligatorios:** Todo archivo `.md` nuevo o modificado debe incluir el bloque `::METADATA::` con campo `last_updated`.
2. **Actualización del directorio:** Cualquier cambio estructural (nuevos archivos, renombrados, eliminaciones) debe reflejarse en `00-META/directory-tree.md`.
3. **Registro de cambios:** Documentar brevemente el cambio realizado en el commit o en el archivo correspondiente.

### 0.2 Campos de Control Temporal

```markdown
<!--
::METADATA::
...campos existentes...
last_updated: YYYY-MM-DD
change_log: "Descripción breve del último cambio"
-->
```

### 0.3 Flujo de Trabajo para Cambios

```
1. Realizar modificación en archivo(s)
2. Actualizar campo `last_updated` en ::METADATA::
3. Si es cambio estructural → Actualizar 00-META/directory-tree.md
4. Commit con mensaje descriptivo
```

---

## 0.5 Excepciones al Estándar

### 01-Simbologia-Matematica (Biblioteca de Referencia)

La carpeta `01-Fundamentos/01-Simbologia-Matematica/` está **exenta** del sistema de nomenclatura `[PREFIJO]-[XX]-[Contenido].md` por las siguientes razones:

- **Propósito:** Material de consulta rápida, no secuencia de aprendizaje
- **Uso:** Referencia para errores de escritura LaTeX, símbolos y notación
- **Independencia:** No tiene prerequisitos ni dependencias con otros módulos

**Estructura permitida:**
```
01-Simbologia-Matematica/
├── manifest.json                      # type: "reference_library"
├── FUN-01-Simbologia-Intro.md         # Punto de entrada (único archivo con prefijo)
└── theory/
    └── Tablas-de-Simbolos-Matematicos.md  # Contenido libre de nomenclatura
```

**manifest.json tipo `reference_library`:**
```json
{
  "id": "ref-simbologia",
  "topic": "Simbología Matemática",
  "type": "reference_library",
  "status": "active",
  "exception": {
    "reason": "Material de consulta directa sin secuencia de aprendizaje",
    "applies_to": ["theory/*"]
  }
}
```

---

## 1. Sistema de Prefijos Semánticos

### Regla General
Todos los archivos `.md` siguen el patrón: `[PREFIJO]-[XX]-[Contenido].md`

### Prefijos por Módulo

| Módulo | Prefijo | Ejemplo |
|--------|---------|---------|
| 01-Fundamentos | `FUN` | `FUN-01-Funciones-Intro.md` |
| 02-Algebra-Lineal | `AL` | `AL-03-Sistemas-Teoria.md` |
| 03-Calculo-Diferencial | `CD` | `CD-02-Derivadas-Resumen.md` |
| 04-Calculo-Integral | `CI` | `CI-04-Aplicaciones-Metodos.md` |
| 05-Calculo-Vectorial | `CV` | `CV-01-Vectores-Intro.md` |
| 06-Ecuaciones-Diferenciales | `ED` | `ED-02-Orden-Superior-Teoria.md` |
| 07-Metodos-Numericos | `MN` | `MN-03-Integracion-Problemas.md` |
| Referencias/Meta | `REF` | `REF-Simbologia-Index.md` |

### Sufijos por Tipo de Contenido

| Tipo | Sufijo | Ubicación |
|------|--------|-----------|
| Entrada principal | `-Intro` | Raíz del tema |
| Resumen de fórmulas | `-Resumen-Formulas` | Raíz del tema |
| Teoría completa | `-Teoria-[subtema]` | `theory/` |
| Método paso a paso | `-Metodo-[nombre]` | `methods/` |
| Problema | `-Problema-[nombre]` | `problems/` |
| Solución | `-Solucion-[nombre]` | `solutions/` |
| Aplicación | `-Aplicacion-[nombre]` | `applications/` |
| Diagnóstico | `-Diagnostico` | `diagnostic/` |

---

## 2. Estructura de Metadatos ::METADATA::

Todo archivo `.md` **debe** comenzar con este bloque:

```markdown
<!--
::METADATA::
type: [theory | method | problem | solution | reference | index | cheatsheet]
topic_id: [id-del-manifest]
file_id: [nombre-archivo-sin-extension]
status: [draft | review | stable]
audience: [student | ai_context | exam_review]
requires: [lista-de-dependencias]
-->
```

### Campos Obligatorios

| Campo | Descripción | Valores válidos |
|-------|-------------|-----------------|
| `type` | Función técnica del archivo | `theory`, `method`, `problem`, `solution`, `reference`, `index`, `cheatsheet` |
| `topic_id` | ID que coincide con `manifest.json` | Ej: `cv-01-vectores-espacio` |
| `file_id` | Identificador único (= nombre archivo) | Ej: `CV-01-Teoria-Vectores` |
| `status` | Estado de revisión | `draft`, `review`, `stable` |
| `audience` | Audiencia objetivo | `student`, `ai_context`, `exam_review` |

### Campo Opcional

| Campo | Descripción |
|-------|-------------|
| `requires` | Lista de dependencias (file_ids o topic_ids) |

---

## 3. Estructura del manifest.json

```json
{
  "id": "prefijo-numero-tema",
  "topic": "Nombre Legible del Tema",
  "type": "learning_module | reference_library",
  "status": "active | draft | deprecated",
  "last_updated": "YYYY-MM-DD",
  "tags": ["tag1", "tag2"],
  "prereqs": ["ruta/prerequisito"],
  "resource_map": {
    "entry_point": "PREFIJO-XX-Intro.md",
    "main_theory": "theory/PREFIJO-XX-Teoria-Nombre.md",
    "cheat_sheet": "PREFIJO-XX-Resumen-Formulas.md",
    "methods": ["methods/PREFIJO-XX-Metodo-X.md"],
    "problems": ["problems/PREFIJO-XX-Problemas.md"],
    "answers": "solutions/PREFIJO-XX-Respuestas.md",
    "solutions": ["solutions/prob-XX/"]
  },
  "ai_config": {
    "strict_mode": true,
    "allowed_tasks": ["explain_concept", "generate_problems", "verify_solution"]
  }
}
```

### Campos Obligatorios del manifest.json

| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| `id` | Identificador único del tema | `"al-01-matrices"` |
| `topic` | Nombre legible para humanos | `"Matrices y Operaciones"` |
| `type` | Tipo de módulo | `"learning_module"` |
| `status` | Estado del contenido | `"active"` |
| `last_updated` | Fecha última modificación | `"2024-12-23"` |
| `resource_map` | Mapa de archivos del tema | (ver estructura) |

### Campos del resource_map

| Campo | Descripción | Obligatorio |
|-------|-------------|-------------|
| `entry_point` | Archivo de entrada principal | ✅ Sí |
| `main_theory` | Teoría completa | ✅ Sí |
| `cheat_sheet` | Resumen de fórmulas | ✅ Sí |
| `methods` | Lista de métodos | ❌ Opcional |
| `problems` | Archivo(s) de problemas | ❌ Opcional |
| `answers` | Tabla de respuestas rápidas | ❌ Opcional |
| `solutions` | Carpetas de soluciones desarrolladas | ❌ Opcional |
```

### Tipos de Módulo

| Tipo | Descripción | Carpetas requeridas |
|------|-------------|---------------------|
| `learning_module` | Tema de estudio completo | Todas |
| `reference_library` | Material de consulta | Solo `entry_point` y `content` |

---

## 4. Ejemplos Completos

### 4.1 Módulo de Aprendizaje (CV-01)

**Estructura de carpetas:**
```
05-Calculo-Vectorial/01-Vectores-en-el-espacio/
├── manifest.json
├── CV-01-Vectores-Intro.md          # entry_point
├── CV-01-Resumen-Formulas.md        # cheat_sheet
├── theory/
│   └── CV-01-Teoria-Vectores.md     # main_theory
├── methods/
│   └── CV-01-Metodo-Producto-Cruz.md
├── problems/
│   └── CV-01-Problema-Recta-Plano.md
└── solutions/
    └── CV-01-Solucion-Recta-Plano/
```

### 4.2 Biblioteca de Referencia

**manifest.json para Simbología:**
```json
{
  "id": "ref-simbologia",
  "topic": "Simbología Matemática",
  "type": "reference_library",
  "status": "active",
  "resource_map": {
    "entry_point": "REF-Simbologia-Index.md",
    "content": [
      "REF-Simbologia-Griegos.md",
      "REF-Simbologia-Operadores.md",
      "REF-Simbologia-Conjuntos.md"
    ]
  }
}
```

---

## 5. Beneficios del Sistema

1. **Anti-confusión:** No más 50 archivos llamados `README.md` o `teoria.md`
2. **Contexto inmediato:** `CV-01-Teoria-Vectores.md` indica módulo, tema y contenido
3. **Indexación eficiente:** La IA encuentra rápidamente el archivo correcto
4. **Mapeo flexible:** El `manifest.json` permite renombrar sin romper referencias
5. **Validación automática:** El campo `::METADATA::` permite verificación por scripts

---

## 6. Formato Híbrido de Problemas y Soluciones (Tres Niveles)

Este formato estandariza la organización de problemas y soluciones para optimizar tanto la lectura humana como el procesamiento por IA.

### 6.1 Estructura de Tres Niveles

```
[modulo]/[tema]/
├── problems/
│   └── XX-NN-Problemas.md           # Nivel 1: Lista completa de problemas
│
└── solutions/
    ├── XX-NN-Respuestas.md          # Nivel 2: Tabla de respuestas rápidas (TODAS)
    └── prob-XX/                      # Nivel 3: Soluciones desarrolladas (selectas)
        └── solucion-metodo.md
```

### 6.2 Nivel 1: Archivo de Problemas

**Archivo único por tema:** `problems/PREFIJO-XX-Problemas.md`

- **Propósito:** Lista maestra de todos los problemas del tema
- **Usuario principal:** Estudiantes y profesores
- **Requisito:** Cada problema debe tener un ID único `[Prob-XX]`

```markdown
## Sección Temática

### [Prob-01] Título del Problema ⭐
Enunciado del problema...

> 📁 Solución: `solutions/prob-01/`

### [Prob-02] Otro Problema ⭐⭐
Enunciado del problema...

> 📁 Solución: `solutions/prob-02/`
```

**Convenciones de ID:**
- Formato: `[Prob-XX]` donde XX es secuencial (01, 02, ..., 99)
- El ID debe coincidir exactamente con el nombre de la carpeta en `solutions/`
- Los IDs son únicos dentro de cada tema (no del repositorio completo)

**Indicadores de dificultad:**
- ⭐ = Básico
- ⭐⭐ = Intermedio  
- ⭐⭐⭐ = Avanzado

### 6.3 Nivel 2: Archivo de Respuestas Rápidas

**Archivo obligatorio:** `solutions/PREFIJO-XX-Respuestas.md`

- **Propósito:** Consulta rápida de TODAS las respuestas finales
- **Usuario principal:** Estudiantes verificando resultados
- **Formato:** Tabla con ID, respuesta y enlace a solución (si existe)

```markdown
| ID | Respuesta | Solución |
|----|-----------|----------|
| [Prob-01] | $6$ | — |
| [Prob-02] | $\begin{pmatrix} 4 & 6 \\ 10 & 12 \end{pmatrix}$ | [Ver](./prob-02/solucion-metodo.md) |
| [Prob-03] | No existe | — |
```

**Metadatos requeridos:**
```markdown
<!--
::METADATA::
type: answer-key
topic_id: [prefijo]-[num]-[tema]
file_id: PREFIJO-XX-Respuestas
status: [draft|review|stable]
total_problems: [número]
solved_detailed: [número con carpeta]
-->
```

### 6.4 Nivel 3: Carpetas de Soluciones Desarrolladas

**Una carpeta por problema selecto:** `solutions/prob-XX/`

- **Propósito:** Soluciones paso a paso para problemas representativos
- **Usuario principal:** Estudiantes aprendiendo métodos, IA generando explicaciones
- **Criterio de inclusión:** Problemas de mayor dificultad, métodos importantes, o ejemplos representativos

```
solutions/
├── PREFIJO-XX-Respuestas.md    # Nivel 2: TODAS las respuestas
├── prob-04/
│   └── solucion-metodo.md      # Solución concisa
├── prob-09/
│   ├── solucion-metodo.md      # Solución concisa
│   └── solucion-detallada.md   # (Opcional) Explicación extendida
└── ...
```

**Archivos dentro de cada carpeta:**

| Archivo | Requerido | Descripción |
|---------|-----------|-------------|
| `solucion-metodo.md` | ✅ Sí | Solución directa usando el método indicado |
| `solucion-detallada.md` | ❌ Opcional | Explicación extendida, verificaciones, métodos alternativos |

**Metadatos para `solucion-metodo.md`:**
```markdown
<!--
::METADATA::
type: solution
topic_id: [id-del-manifest]
file_id: prob-XX-solucion-metodo
problem_ref: [Prob-XX]
method: [nombre-del-metodo]
status: stable
audience: student
-->
```

### 6.5 Flujo de Consulta

```
Estudiante quiere verificar respuesta
         │
         ▼
┌─────────────────────────┐
│  XX-NN-Respuestas.md    │ ◄── Consulta rápida (TODAS las respuestas)
│  (Tabla de respuestas)  │
└───────────┬─────────────┘
            │ ¿Necesita ver el proceso?
            ▼
┌─────────────────────────┐
│  prob-XX/               │ ◄── Solución desarrollada (si existe)
│  solucion-metodo.md     │
└─────────────────────────┘
```

### 6.6 Ejemplo Completo

**Estructura de carpetas para AL-01 (Matrices):**
```
02-Algebra-Lineal/01-Matrices/
├── problems/
│   └── AL-01-Problemas.md          # 32 problemas con [Prob-01] a [Prob-32]
└── solutions/
    ├── AL-01-Respuestas.md         # 32 respuestas en tabla
    ├── prob-04/
    │   └── solucion-metodo.md
    ├── prob-09/
    │   ├── solucion-metodo.md
    │   └── solucion-detallada.md
    └── prob-24/
        └── solucion-metodo.md
```

### 6.7 Metadatos para Problemas

```markdown
<!--
::METADATA::
type: problem_set
topic_id: [id-del-manifest]
file_id: PREFIJO-XX-Problemas
status: stable
audience: student
problem_count: 32
difficulty_distribution: {basico: 12, intermedio: 14, avanzado: 6}
-->
```

---

## 7. Migración de Archivos Existentes

Para migrar archivos del formato antiguo:

1. Crear nuevo archivo con nomenclatura semántica
2. Agregar bloque `::METADATA::`
3. Actualizar `resource_map` en `manifest.json`
4. Opcionalmente, listar archivos antiguos en `legacy_files`
5. Eliminar archivos antiguos cuando se confirme la migración

### 7.1 Migración de Problemas/Soluciones al Formato de Tres Niveles

**Paso 1: Problemas**
- Consolidar en un único archivo `PREFIJO-XX-Problemas.md`
- Agregar IDs `[Prob-XX]` a cada problema existente
- Clasificar con indicadores: ⭐ (básico), ⭐⭐ (intermedio), ⭐⭐⭐ (avanzado)

**Paso 2: Respuestas Rápidas (NUEVO)**
- Crear archivo `solutions/PREFIJO-XX-Respuestas.md`
- Tabla con TODAS las respuestas finales
- Usar plantilla: `00-META/plantilla-respuestas.md`

**Paso 3: Soluciones Desarrolladas**
- Crear carpeta `solutions/prob-XX/` solo para problemas selectos
- Renombrar: `method-solution.md` → `solucion-metodo.md`
- Separar soluciones monolíticas en archivos individuales

**Paso 4: Vincular**
- En problemas: `> 📁 Solución: solutions/prob-XX/`
- En respuestas: `[✅](./prob-XX/solucion-metodo.md)` o `➖`

### 7.2 Estado de Migración por Módulo

| Módulo | Problemas | Respuestas | Soluciones | Estado |
|:-------|:---------:|:----------:|:----------:|:------:|
| **01-Fundamentos** ||||
| FUN-02 Aritmética | ✅ (85) | ✅ | ⏳ | **Nivel 2 completado** |
| FUN-03 Álgebra | ✅ (108) | ✅ | ⏳ | **Nivel 2 completado** |
| FUN-04 Geometría | ✅ (110) | ✅ | ⏳ | **Nivel 2 completado** |
| FUN-05 Trigonometría | ✅ (105) | ✅ | ⏳ | **Nivel 2 completado** |
| FUN-06 Geometría Analítica | ✅ (87) | ✅ | ⏳ | **Nivel 2 completado** |
| **02-Algebra-Lineal** ||||
| AL-01 Matrices | ✅ (32) | ✅ | ✅ (9) | **Completado** |
| AL-02 Determinantes | ✅ (28) | ✅ | ⏳ | **Nivel 2 completado** |
| AL-03 Sistemas Lineales | ✅ (23) | ✅ | ⏳ | **Nivel 2 completado** |
| AL-04 Espacios Vectoriales | ✅ (32) | ✅ | ⏳ | **Nivel 2 completado** |
| AL-05 Transformaciones | ✅ (28) | ✅ | ⏳ | **Nivel 2 completado** |
| AL-06 Valores Propios | ✅ (28) | ✅ | ⏳ | **Nivel 2 completado** |
| **03-Calculo-Diferencial** ||||
| CD-01 Límites | ✅ (57) | ✅ | ✅ (5) | **Completado** |
| CD-02 Derivadas | ✅ (59) | ✅ | ⏳ | **Nivel 2 completado** |
| CD-03 Aplicaciones | ✅ (48) | ✅ | ⏳ | **Nivel 2 completado** |
| CD-04 Teoremas | ✅ (80) | ✅ | ⏳ | **Nivel 2 completado** |
| **04-Calculo-Integral** ||||
| CI-01 Integral Indefinida | ✅ (60) | ✅ | ⏳ | **Nivel 2 completado** |
| CI-02 Técnicas Integración | ✅ (70) | ✅ | ⏳ | **Nivel 2 completado** |
| CI-03 Integral Definida | ✅ (42) | ✅ | ⏳ | **Nivel 2 completado** |
| CI-04 Aplicaciones | ✅ (45) | ✅ | ⏳ | **Nivel 2 completado** |
| CI-05 Integrales Impropias | ✅ (40) | ✅ | ⏳ | **Nivel 2 completado** |
| **06-Ecuaciones-Diferenciales** ||||
| ED-01 EDO Primer Orden | ✅ (28) | ✅ | ⏳ | **Nivel 2 completado** |
| ED-02 EDO Segundo Orden | ✅ (30) | ✅ | ⏳ | **Nivel 2 completado** |
| ED-03 Sistemas EDO | ✅ (23) | ✅ | ⏳ | **Nivel 2 completado** |
| ED-04 Transformada Laplace | ✅ (24) | ✅ | ⏳ | **Nivel 2 completado** |
| ED-05 Series Potencias | ✅ (20) | ✅ | ⏳ | **Nivel 2 completado** |
| **07-Metodos-Numericos** ||||
| MN-01 Raíces Ecuaciones | ✅ (32) | ✅ | ⏳ | **Nivel 2 completado** |
| MN-02 Interpolación | ✅ (30) | ✅ | ⏳ | **Nivel 2 completado** |
| MN-03 Integración Numérica | ✅ (37) | ✅ | ⏳ | **Nivel 2 completado** |
| MN-04 EDO Numéricas | ✅ (34) | ✅ | ⏳ | **Nivel 2 completado** |

**Resumen:** 
- **1,425 problemas** con IDs estandarizados `[Prob-XX]`
- **29 archivos de respuestas** creados
- **14 carpetas de soluciones** desarrolladas (AL-01: 9, CD-01: 5)

> ⏳ = Pendiente | ✅ = Completado | 🔄 = En progreso

---

<!--
IA: Este es el documento de referencia para la nomenclatura del repositorio.
Consulta siempre este archivo antes de crear nuevos archivos.
Para problemas y soluciones, usa el FORMATO HÍBRIDO DE TRES NIVELES (Sección 6).
Plantilla de respuestas: 00-META/plantilla-respuestas.md
file_id: nomenclatura-estandar
-->
