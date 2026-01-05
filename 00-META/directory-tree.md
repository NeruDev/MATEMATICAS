<!--
::METADATA::
type: reference
topic_id: meta-directory
file_id: directory-tree
status: stable
audience: ai_context
last_updated: 2026-01-05
change_log: "Añadido .ai-bootstrap.md y audit-meta-files.md, actualizada jerarquía normativa"
-->

# Árbol de Directorios del Repositorio de Matemáticas

*Última actualización: 2026-01-05*

> **Nota:** Este archivo debe actualizarse con cada cambio estructural en el repositorio.

```
MATEMATICAS GITHUB/
│
├── .github/
│   └── PULL_REQUEST_TEMPLATE.md
│
├── 📄 ARCHIVOS RAÍZ
│   ├── .ai-bootstrap.md               # 🤖 PUNTO DE ENTRADA PARA IA (leer primero)
│   ├── README.md                      # Portada y skill tree visual
│   ├── WIKI_INDEX.md                  # Tabla de contenidos maestra
│   ├── glossary.md                    # ~150 términos matemáticos
│   ├── AUDITORIA_ESTADO_REPO.md       # Estado de integridad del repo
│   ├── Guía de Arquitectura del Repositorio de Matemáticas.md  # Documentación técnica específica
│   └── Plantilla de Arquitectura Modular Universal.md          # ← Plantilla para otros repositorios
│
├── 00-META/                           # 🎛️ CENTRO DE CONTROL
│   │
│   ├── 📜 DOCUMENTOS NORMATIVOS (Prioridad para IA)
│   │   ├── ia-contract.md             # LEY SUPREMA para IAs (Nivel 2)
│   │   ├── ai-directives.md           # Reglas técnicas complementarias (Nivel 2)
│   │   └── nomenclatura-estandar.md   # Estándar de nombrado (Nivel 3)
│   │
│   ├── 🗂️ DOCUMENTOS DE ESTRUCTURA
│   │   ├── directory-tree.md          ← Estás aquí
│   │   ├── audit-file-list.md         # Lista de archivos obligatorios
│   │   └── audit-meta-files.md        # 🆕 Auditoría de 00-META
│   │
│   ├── 📚 DOCUMENTOS DE REFERENCIA
│   │   ├── bibliografia-general.md    # Biblioteca central
│   │   ├── notation-cheatsheet.md     # Símbolos LaTeX
│   │   └── plantilla-respuestas.md    # Template para soluciones
│   │
│   ├── 👨‍🎓 DOCUMENTOS PARA ESTUDIANTES
│   │   ├── study-guide.md             # Guía de estudio
│   │   └── prompts-for-students.md    # Prompts prediseñados
│   │
│   ├── 🔍 DOCUMENTOS DE VALIDACIÓN
│   │   ├── repo-tests.md              # Pruebas de integridad
│   │   └── audit-table-issues.md      # Registro histórico
│   │
│   └── tools/
│       ├── validate_repo.py           # Validador consolidado del repositorio
│       ├── link_knowledge_base.py     # Auto-vinculador al glosario
│       ├── check_tables.py            # Validador de tablas Markdown
│       └── graphics/                  # Subsistema de generación visual
│           ├── config.yaml
│           ├── generate_graphics.py
│           ├── requirements.txt
│           ├── templates/
│           └── sources/
│
├── 01-Fundamentos/
│   ├── 00-Index.md
│   │
│   ├── 01-Simbologia-Matematica/      ⚠️ EXCEPCIÓN: reference_library
│   │   ├── manifest.json
│   │   ├── FUN-01-Simbologia-Intro.md
│   │   ├── _directives.md
│   │   ├── Notas/                     # 🔓 SANDBOX
│   │   │   └── README.md
│   │   └── theory/
│   │       └── Tablas-de-Simbolos-Matematicos.md
│   │
│   ├── 02-Aritmetica/
│   │   ├── manifest.json
│   │   ├── FUN-02-Aritmetica-Intro.md
│   │   ├── FUN-02-Resumen-Formulas.md
│   │   ├── _directives.md
│   │   ├── diagnostic/
│   │   ├── media/
│   │   ├── methods/
│   │   │   └── FUN-02-Metodos-Aritmetica.md
│   │   ├── Notas/                     # 🔓 SANDBOX
│   │   │   └── README.md
│   │   ├── problems/
│   │   │   └── FUN-02-Problemas.md
│   │   ├── solutions/
│   │   │   ├── FUN-02-Respuestas.md
│   │   │   └── prob-XX/
│   │   └── theory/
│   │       └── FUN-02-Teoria-Aritmetica.md
│   │
│   ├── 03-Algebra/
│   │   ├── manifest.json
│   │   ├── FUN-03-Algebra-Intro.md
│   │   ├── FUN-03-Resumen-Formulas.md
│   │   └── ...
│   │
│   ├── 04-Geometria/
│   │   ├── manifest.json
│   │   ├── FUN-04-Geometria-Intro.md
│   │   ├── FUN-04-Resumen-Formulas.md
│   │   └── ...
│   │
│   ├── 05-Trigonometria/
│   │   ├── manifest.json
│   │   ├── FUN-05-Trigonometria-Intro.md
│   │   ├── FUN-05-Resumen-Formulas.md
│   │   └── ...
│   │
│   └── 06-Geometria-Analitica/
│       ├── manifest.json
│       ├── FUN-06-Geometria-Analitica-Intro.md
│       ├── FUN-06-Resumen-Formulas.md
│       └── ...
│
├── 02-Algebra-Lineal/
│   ├── 00-Index.md
│   │
│   ├── 01-Matrices/
│   │   ├── manifest.json
│   │   ├── AL-01-Matrices-Intro.md
│   │   ├── AL-01-Resumen-Formulas.md
│   │   └── ...
│   │
│   ├── 02-Determinantes/       → AL-02-*
│   ├── 03-Sistemas-Lineales/   → AL-03-*
│   ├── 04-Espacios-Vectoriales/ → AL-04-*
│   ├── 05-Transformaciones-Lineales/ → AL-05-*
│   └── 06-Valores-Vectores-Propios/ → AL-06-*
│
├── 03-Calculo-Diferencial/
│   ├── 00-Index.md
│   │
│   ├── 01-Limites/             → CD-01-*
│   ├── 02-Derivadas/           → CD-02-*
│   ├── 03-Aplicaciones-de-la-derivada/ → CD-03-*
│   └── 04-Teoremas-fundamentales/ → CD-04-*
│
├── 04-Calculo-Integral/
│   ├── 00-Index.md
│   │
│   ├── 01-Integral-Indefinida/ → CI-01-*
│   ├── 02-Tecnicas-Integracion/ → CI-02-*
│   ├── 03-Integral-Definida/   → CI-03-*
│   ├── 04-Aplicaciones-Integral/ → CI-04-*
│   └── 05-Integrales-Impropias/ → CI-05-*
│
├── 05-Calculo-Vectorial/
│   ├── 00-Index.md
│   │
│   ├── 01-Vectores-en-el-espacio/ → CV-01-*
│   ├── 02-Curvas-planas-parametricas-y-polares/ → CV-02-*
│   ├── 03-Funciones-vectoriales/ → CV-03-*
│   ├── 04-Funciones-de-varias-variables/ → CV-04-*
│   └── 05-Integracion-multiple/ → CV-05-*
│
├── 06-Ecuaciones-Diferenciales/
│   ├── 00-Index.md
│   │
│   ├── 01-EDO-Primer-Orden/    → ED-01-*
│   ├── 02-EDO-Segundo-Orden/   → ED-02-*
│   ├── 03-Sistemas-EDO/        → ED-03-*
│   ├── 04-Transformada-Laplace/ → ED-04-*
│   └── 05-Series-Potencias/    → ED-05-*
│
├── 07-Metodos-Numericos/
│   ├── 00-Index.md
│   │
│   ├── 01-Raices-Ecuaciones/   → MN-01-*
│   ├── 02-Interpolacion/       → MN-02-*
│   ├── 03-Integracion-Numerica/ → MN-03-*
│   └── 04-EDO-Numericas/       → MN-04-*
│
├── glossary.md
└── README.md
```

---

## Leyenda

| Símbolo | Significado |
|---------|-------------|
| `→ XX-NN-*` | Prefijo estándar para archivos del tema |
| `prob-XX/` | Carpetas de soluciones desarrolladas (selectas) |
| `⚠️ EXCEPCIÓN` | Módulo exento de nomenclatura estándar |
| `🔓 SANDBOX` | Carpeta Notas — Exenta de TODAS las reglas |
| `...` | Estructura estándar (ver plantilla abajo) |

---

## Estadísticas del Repositorio

| Módulo | Subtemas | Prefijo | Carpetas Notas | Estado |
|--------|----------|---------|:--------------:|--------|
| 00-META | N/A | — | — | ✅ Configuración |
| 01-Fundamentos | 6 | `FUN` | 6 | ✅ Completo |
| 02-Algebra-Lineal | 6 | `AL` | 6 | ✅ Completo |
| 03-Calculo-Diferencial | 4 | `CD` | 4 | ✅ Completo |
| 04-Calculo-Integral | 5 | `CI` | 5 | ✅ Completo |
| 05-Calculo-Vectorial | 5 | `CV` | 5 | ✅ Completo |
| 06-Ecuaciones-Diferenciales | 5 | `ED` | 5 | ✅ Completo |
| 07-Metodos-Numericos | 4 | `MN` | 4 | ✅ Completo |
| **TOTAL** | **35** | — | **35** | — |

---

## Estructura Estándar por Subtema

```
XX-Nombre-Subtema/
├── manifest.json                    # Metadatos (REQUERIDO)
├── PREFIJO-XX-Nombre-Intro.md       # Punto de entrada (REQUERIDO)
├── PREFIJO-XX-Resumen-Formulas.md   # Cheat sheet (REQUERIDO)
├── _directives.md                   # Directivas específicas (REQUERIDO)
│
├── theory/
│   └── PREFIJO-XX-Teoria-Nombre.md
├── methods/
│   └── PREFIJO-XX-Metodos-Nombre.md
├── problems/
│   └── PREFIJO-XX-Problemas.md
├── solutions/
│   ├── PREFIJO-XX-Respuestas.md     # Tabla de respuestas rápidas
│   └── prob-XX/                     # Soluciones desarrolladas
│       └── solucion-metodo.md
│
├── diagnostic/                      # Evaluaciones (opcional)
├── media/                           # Multimedia (opcional)
└── Notas/                           # 🔓 SANDBOX - Sin reglas
    └── README.md                    # Directiva de excepción
```

### Carpeta Notas/ — Zona Sandbox

> **⚠️ DIRECTIVA PARA IA:** La carpeta `Notas/` en cada subtema es una zona de excepción total.

**NO aplican:**
- Nomenclatura estándar
- Metadatos `::METADATA::`
- Validación de estructura
- Vinculación al glosario
- Reglas de formato

**Contenido permitido:**
- 📄 Texto libre (notas, borradores)
- 🖼️ Multimedia (imágenes, diagramas)
- 💻 Código de prueba
- 📎 Archivos externos
- 🧪 Experimentos sin relación con el repo

---

<!--
::AI_DIRECTIVE::
Este archivo es la referencia autoritativa de la estructura del repositorio.
Cualquier cambio estructural debe reflejarse aquí antes de considerarse completo.
last_updated: 2026-01-05
-->
