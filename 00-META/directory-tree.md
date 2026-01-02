<!--
::METADATA::
type: reference
topic_id: meta-directory
file_id: directory-tree
status: stable
audience: ai_context
last_updated: 2025-12-30
change_log: "Eliminado hide_frontmatter.py (integrado en validate_repo.py), actualizada estructura"
-->

# Árbol de Directorios del Repositorio de Matemáticas

*Última actualización: 2025-12-30*

> **Nota:** Este archivo debe actualizarse con cada cambio estructural en el repositorio.

```
MATEMATICAS GITHUB/
│
├── .assets/
│   └── .gitkeep
│
├── .github/
│   └── PULL_REQUEST_TEMPLATE.md
│
├── 00-META/
│   ├── ai-directives.md
│   ├── audit-file-list.md
│   ├── directory-tree.md              ← Estás aquí
│   ├── ia-contract.md
│   ├── nomenclatura-estandar.md       ← Estándar de nombrado
│   ├── notation-cheatsheet.md
│   ├── plantilla-respuestas.md
│   ├── prompts-for-students.md
│   ├── repo-tests.md
│   ├── study-guide.md
│   └── tools/
│       └── validate_repo.py           # Validador consolidado del repositorio
│
├── 01-Fundamentos/
│   ├── 00-Index.md
│   │
│   ├── 01-Simbologia-Matematica/      ⚠️ EXCEPCIÓN: reference_library
│   │   ├── manifest.json
│   │   ├── [FUN-01-Simbologia-Intro.md](FUN-01-Simbologia-Intro.md)
│   │   ├── _directives.md
│   │   └── theory/
│   │       └── Tablas-de-Simbolos-Matematicos.md
│   │
│   ├── 02-Aritmetica/
│   │   ├── manifest.json
│   │   ├── [FUN-02-Aritmetica-Intro.md](FUN-02-Aritmetica-Intro.md)
│   │   ├── [FUN-02-Resumen-Formulas.md](FUN-02-Resumen-Formulas.md)
│   │   ├── _directives.md
│   │   ├── applications/
│   │   ├── diagnostic/
│   │   ├── media/
│   │   ├── methods/
│   │   │   └── [FUN-02-Metodos-Aritmetica.md](FUN-02-Metodos-Aritmetica.md)
│   │   ├── problems/
│   │   │   └── [FUN-02-Problemas.md](FUN-02-Problemas.md)
│   │   ├── solutions/
│   │   │   ├── [FUN-02-Respuestas.md](FUN-02-Respuestas.md)
│   │   │   └── [prob-XX/]
│   │   └── theory/
│   │       └── [FUN-02-Teoria-Aritmetica.md](FUN-02-Teoria-Aritmetica.md)
│   │
│   ├── 03-Algebra/
│   │   ├── manifest.json
│   │   ├── [FUN-03-Algebra-Intro.md](FUN-03-Algebra-Intro.md)
│   │   ├── [FUN-03-Resumen-Formulas.md](FUN-03-Resumen-Formulas.md)
│   │   └── ...
│   │
│   ├── 04-Geometria/
│   │   ├── manifest.json
│   │   ├── [FUN-04-Geometria-Intro.md](FUN-04-Geometria-Intro.md)
│   │   ├── [FUN-04-Resumen-Formulas.md](FUN-04-Resumen-Formulas.md)
│   │   └── ...
│   │
│   ├── 05-Trigonometria/
│   │   ├── manifest.json
│   │   ├── [FUN-05-Trigonometria-Intro.md](FUN-05-Trigonometria-Intro.md)
│   │   ├── [FUN-05-Resumen-Formulas.md](FUN-05-Resumen-Formulas.md)
│   │   └── ...
│   │
│   └── 06-Geometria-Analitica/
│       ├── manifest.json
│       ├── [FUN-06-Geometria-Analitica-Intro.md](FUN-06-Geometria-Analitica-Intro.md)
│       ├── [FUN-06-Resumen-Formulas.md](FUN-06-Resumen-Formulas.md)
│       └── ...
│
├── 02-Algebra-Lineal/
│   ├── 00-Index.md
│   │
│   ├── 01-Matrices/
│   │   ├── manifest.json
│   │   ├── [AL-01-Matrices-Intro.md](AL-01-Matrices-Intro.md)
│   │   ├── [AL-01-Resumen-Formulas.md](AL-01-Resumen-Formulas.md)
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
| `[prob-XX/]` | Carpetas de soluciones desarrolladas (selectas) |
| `⚠️ EXCEPCIÓN` | Módulo exento de nomenclatura estándar |
| `...` | Estructura estándar (ver plantilla abajo) |

---

## Estadísticas del Repositorio

| Módulo | Subtemas | Prefijo | Estado |
|--------|----------|---------|--------|
| 00-META | N/A | — | ✅ Configuración |
| 01-Fundamentos | 6 | `FUN` | ✅ Estructura completa |
| 02-Algebra-Lineal | 6 | `AL` | ✅ Completo |
| 03-Calculo-Diferencial | 4 | `CD` | ✅ Estructura completa |
| 04-Calculo-Integral | 5 | `CI` | ✅ Estructura completa |
| 05-Calculo-Vectorial | 5 | `CV` | ⚠️ En desarrollo |
| 06-Ecuaciones-Diferenciales | 5 | `ED` | ✅ Completo |
| 07-Metodos-Numericos | 4 | `MN` | ⚠️ En desarrollo |

---

## Estructura Estándar por Subtema

```
XX-Nombre-Subtema/
├── manifest.json                    # Metadatos (REQUERIDO)
├── PREFIJO-XX-Nombre-Intro.md       # Punto de entrada (REQUERIDO)
├── PREFIJO-XX-Resumen-Formulas.md   # Cheat sheet (REQUERIDO)
├── _directives.md                   # Directivas específicas (opcional)
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
├── applications/                    # (opcional)
├── diagnostic/                      # (opcional)
└── media/                           # (opcional)
```

---

<!--
::AI_DIRECTIVE::
Este archivo es la referencia autoritativa de la estructura del repositorio.
Cualquier cambio estructural debe reflejarse aquí antes de considerarse completo.
last_updated: 2024-12-23
-->
