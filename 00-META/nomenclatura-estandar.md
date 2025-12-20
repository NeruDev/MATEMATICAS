<!--
::METADATA::
type: reference
topic_id: meta-nomenclatura
file_id: nomenclatura-estandar
status: stable
audience: ai_context
-->

# Estándar de Nomenclatura de Archivos

Este documento define las convenciones de nombrado para todos los archivos del repositorio.

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
  "tags": ["tag1", "tag2"],
  "prereqs": ["ruta/prerequisito"],
  "resource_map": {
    "entry_point": "PREFIJO-XX-Intro.md",
    "main_theory": "theory/PREFIJO-XX-Teoria-Nombre.md",
    "cheat_sheet": "PREFIJO-XX-Resumen-Formulas.md",
    "methods": ["methods/PREFIJO-XX-Metodo-X.md"],
    "problems": ["problems/PREFIJO-XX-Problema-X.md"],
    "solutions": ["solutions/PREFIJO-XX-Solucion-X/"]
  },
  "ai_config": {
    "strict_mode": true,
    "allowed_tasks": ["explain_concept", "generate_problems", "verify_solution"]
  }
}
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

## 6. Migración de Archivos Existentes

Para migrar archivos del formato antiguo:

1. Crear nuevo archivo con nomenclatura semántica
2. Agregar bloque `::METADATA::`
3. Actualizar `resource_map` en `manifest.json`
4. Opcionalmente, listar archivos antiguos en `legacy_files`
5. Eliminar archivos antiguos cuando se confirme la migración

---

<!--
IA: Este es el documento de referencia para la nomenclatura del repositorio.
Consulta siempre este archivo antes de crear nuevos archivos.
file_id: nomenclatura-estandar
-->
