<!--
::METADATA::
type: reference
topic_id: meta-audit
file_id: audit-file-list
status: stable
audience: ai_context
last_updated: 2026-01-05
-->

# Lista de Archivos para Auditoría

*Lista de archivos validados por `00-META/tools/validate_repo.py`.*

---

## 1. Archivos Críticos (Obligatorios)

### 1.1 manifest.json por Subtema (35 total)

Cada subtema DEBE tener un `manifest.json` con campos obligatorios: `id`, `topic`, `type`, `status`, `tags`, `resource_map`, `ai_contract`.

```
01-Fundamentos/
├── 01-Simbologia-Matematica/manifest.json
├── 02-Aritmetica/manifest.json
├── 03-Algebra/manifest.json
├── 04-Geometria/manifest.json
├── 05-Trigonometria/manifest.json
└── 06-Geometria-Analitica/manifest.json

02-Algebra-Lineal/
├── 01-Matrices/manifest.json
├── 02-Determinantes/manifest.json
├── 03-Sistemas-Lineales/manifest.json
├── 04-Espacios-Vectoriales/manifest.json
├── 05-Transformaciones-Lineales/manifest.json
└── 06-Valores-Vectores-Propios/manifest.json

03-Calculo-Diferencial/
├── 01-Limites/manifest.json
├── 02-Derivadas/manifest.json
├── 03-Aplicaciones-de-la-derivada/manifest.json
└── 04-Teoremas-fundamentales/manifest.json

04-Calculo-Integral/
├── 01-Integral-Indefinida/manifest.json
├── 02-Tecnicas-Integracion/manifest.json
├── 03-Integral-Definida/manifest.json
├── 04-Aplicaciones-Integral/manifest.json
└── 05-Integrales-Impropias/manifest.json

05-Calculo-Vectorial/
├── 01-Vectores-en-el-espacio/manifest.json
├── 02-Curvas-planas-parametricas-y-polares/manifest.json
├── 03-Funciones-vectoriales/manifest.json
├── 04-Funciones-de-varias-variables/manifest.json
└── 05-Integracion-multiple/manifest.json

06-Ecuaciones-Diferenciales/
├── 01-EDO-Primer-Orden/manifest.json
├── 02-EDO-Segundo-Orden/manifest.json
├── 03-Sistemas-EDO/manifest.json
├── 04-Transformada-Laplace/manifest.json
└── 05-Series-Potencias/manifest.json

07-Metodos-Numericos/
├── 01-Raices-Ecuaciones/manifest.json
├── 02-Interpolacion/manifest.json
├── 03-Integracion-Numerica/manifest.json
└── 04-EDO-Numericas/manifest.json
```

---

### 1.2 Archivos *-Intro.md (Punto de Entrada)

Cada subtema DEBE tener un archivo de entrada con nomenclatura `PREFIJO-XX-*-Intro.md`.

**⚠️ NO se usan archivos `README.md` en subtemas.**

| Módulo | Prefijo | Ejemplo |
|--------|---------|---------|
| 01-Fundamentos | `FUN-XX` | `FUN-02-Aritmetica-Intro.md` |
| 02-Algebra-Lineal | `AL-XX` | `AL-01-Matrices-Intro.md` |
| 03-Calculo-Diferencial | `CD-XX` | `CD-01-Limites-Intro.md` |
| 04-Calculo-Integral | `CI-XX` | `CI-02-Tecnicas-Integracion-Intro.md` |
| 05-Calculo-Vectorial | `CV-XX` | `CV-01-Vectores-Intro.md` |
| 06-Ecuaciones-Diferenciales | `ED-XX` | `ED-01-EDO-Primer-Orden-Intro.md` |
| 07-Metodos-Numericos | `MN-XX` | `MN-01-Raices-Intro.md` |

---

### 1.3 Archivos *-Resumen-Formulas.md (Cheat Sheet)

Cada subtema (excepto bibliotecas de referencia) DEBE tener un resumen de fórmulas.

**⚠️ NO se usan archivos `summary.md`.**

Patrón: `PREFIJO-XX-Resumen-Formulas.md`

---

## 2. Archivos de Contenido por Carpeta

### 2.1 Estructura Esperada

```
XX-Nombre-Subtema/
├── manifest.json                    # Obligatorio
├── PREFIJO-XX-*-Intro.md            # Obligatorio
├── PREFIJO-XX-Resumen-Formulas.md   # Obligatorio (excepto reference_library)
├── _directives.md                   # Obligatorio (directivas IA)
├── theory/
│   └── PREFIJO-XX-Teoria-*.md
├── methods/
│   └── PREFIJO-XX-Metodos-*.md
├── problems/
│   └── PREFIJO-XX-Problemas.md
├── solutions/
│   ├── PREFIJO-XX-Respuestas.md     # Tabla de respuestas (obligatorio)
│   └── prob-XX/
│       └── solucion-metodo.md
└── Notas/                           # 🔓 SANDBOX — Zona libre (exenta de reglas)
    └── README.md                    # Directiva de excepción
```

> **⚠️ Nota:** La carpeta `Notas/` es una **zona sandbox** exenta de todas las reglas del repositorio. Ver [nomenclatura-estandar.md](nomenclatura-estandar.md#carpetas-notas--zona-sandbox-exención-total).

### 2.2 Ejemplo: 02-Algebra-Lineal/01-Matrices

```
01-Matrices/
├── manifest.json
├── [AL-01-Matrices-Intro.md](AL-01-Resumen-Formulas.md)
├── theory/
│   └── [AL-01-Teoria-Matrices.md](AL-01-Metodos-Operaciones.md)
├── problems/
│   └── [AL-01-Problemas.md](AL-01-Respuestas.md)
    └── prob-01/
        └── solucion-metodo.md
```

---

## 3. Archivos META

```
00-META/
├── ai-directives.md        # Directivas técnicas para IA
├── audit-file-list.md      # Este archivo
├── directory-tree.md       # Estructura del repositorio
├── ia-contract.md          # Contrato principal para IA
├── nomenclatura-estandar.md # Especificaciones técnicas detalladas
├── notation-cheatsheet.md  # Símbolos y convenciones
├── plantilla-respuestas.md # Plantilla para archivos de respuestas
├── prompts-for-students.md # Prompts de ejemplo
├── repo-tests.md           # Documentación del validador
├── study-guide.md          # Guía de estudio
└── tools/
    └── validate_repo.py    # Script de validación
```

---

## 4. Archivos Índice de Módulos

```
01-Fundamentos/00-Index.md
02-Algebra-Lineal/00-Index.md
03-Calculo-Diferencial/00-Index.md
04-Calculo-Integral/00-Index.md
05-Calculo-Vectorial/00-Index.md
06-Ecuaciones-Diferenciales/00-Index.md
07-Metodos-Numericos/00-Index.md
```

---

## 5. Archivos Raíz

```
README.md       # Único README permitido
glossary.md     # Glosario global
```

---

## 6. Resumen de Conteo

| Categoría | Cantidad |
|-----------|----------|
| manifest.json | 35 |
| *-Intro.md | 35 |
| *-Resumen-Formulas.md | ~35 |
| 00-Index.md | 7 |
| Archivos 00-META | 11 |
| Archivos raíz | 2 |
| Archivos theory/ | ~50+ |
| Archivos methods/ | ~40+ |
| Archivos problems/ | ~35 |
| Archivos solutions/ | ~100+ |

**Total estimado: ~350+ archivos**

---

## 7. Validaciones del Script

### Para manifest.json

- ✅ Campos obligatorios: `id`, `topic`, `type`, `status`, `tags`
- ✅ Campo `resource_map` con `entry_point`
- ✅ Campo `ai_contract` con `allowed_tasks`

### Para archivos .md

- ✅ Bloque `::METADATA::` con campos `type` y `status`
- ✅ Nomenclatura correcta según prefijo del módulo
- ✅ Sin tablas con `|` problemático (excepto `\|` escapado)

### Comando de Validación

```bash
cd "g:\MATEMATICAS GITHUB"
python 00-META/tools/validate_repo.py
```
