<!--
HUMANO:
Este archivo define las reglas que la IA debe seguir
al interactuar con el repositorio.

IA:
ESTE ES TU CONTRATO. Léelo SIEMPRE antes de generar contenido.

---
content_type: meta
expected_output:
  default: markdown
audience: ai-assistant
formality: technical
---
-->

# Contrato de IA para Generación de Contenido

## Estructura del Repositorio (actualizado 2025)

Este repositorio contiene **7 módulos principales**:

| Módulo | Temas | Estado |
|--------|-------|--------|
| 01-Fundamentos | Funciones, Aritmética, Álgebra, Geometría, Trigonometría, Geometría Analítica | ✅ Completo |
| 02-Algebra-Lineal | Matrices, Determinantes, Sistemas de Ecuaciones, Espacios Vectoriales, Transformaciones, Valores Propios | ✅ Completo |
| 03-Calculo-Diferencial | Límites, Derivadas, Aplicaciones de la Derivada, Series y Sucesiones | ✅ Completo |
| 04-Calculo-Integral | Integral Indefinida, Integral Definida, Técnicas de Integración, Aplicaciones, Integrales Impropias | ✅ Completo |
| 05-Calculo-Vectorial | Funciones Vectoriales, Gradiente y Derivadas Direccionales, Integrales de Línea, Integrales de Superficie, Teoremas Integrales | ✅ Completo |
| 06-Ecuaciones-Diferenciales | EDO de Primer Orden, EDO de Orden Superior, Sistemas de EDO, Transformada de Laplace | ✅ Completo |
| 07-Metodos-Numericos | Raíces de Ecuaciones, Interpolación, Integración Numérica, EDO Numéricas | ✅ Completo |

## Estructura de cada tema

Cada tema sigue la estructura:
```
tema/
├── manifest.json          # Metadatos con resource_map
├── [PREFIJO]-Intro.md     # Entrada principal (entry_point)
├── [PREFIJO]-Resumen.md   # Fórmulas clave (cheat_sheet)
├── theory/                # Definiciones, teoremas, pruebas
│   └── [PREFIJO]-Teoria-[subtema].md
├── methods/               # Procedimientos paso a paso
│   └── [PREFIJO]-Metodo-[nombre].md
├── problems/              # Enunciados (sin soluciones)
├── solutions/             # Soluciones organizadas por problema
├── applications/          # Casos aplicados
├── diagnostic/            # Pre-test de prerequisitos
└── media/                 # Videos, GeoGebra, imágenes
```

---

## Sistema de Nomenclatura de Archivos (Anti-Confusión)

### Regla de prefijos semánticos
Los archivos deben seguir el patrón: `[PREFIJO]-[Contenido].md`

**Prefijos por módulo:**
| Módulo | Prefijo |
|--------|---------|
| 01-Fundamentos | `FUN-XX` |
| 02-Algebra-Lineal | `AL-XX` |
| 03-Calculo-Diferencial | `CD-XX` |
| 04-Calculo-Integral | `CI-XX` |
| 05-Calculo-Vectorial | `CV-XX` |
| 06-Ecuaciones-Diferenciales | `ED-XX` |
| 07-Metodos-Numericos | `MN-XX` |

Donde `XX` es el número del subtema (01, 02, etc.)

**Ejemplos de aplicación:**
- `01-Vectores.../README.md` → `CV-01-Vectores-Intro.md`
- `01-Vectores.../theory/README.md` → `theory/CV-01-Teoria-Vectores.md`
- `01-Vectores.../summary.md` → `CV-01-Resumen-Formulas.md`

**Beneficio:** La IA no encontrará 50 archivos con el mismo nombre, sino archivos con identificadores únicos que dan contexto inmediato.

---

## Estándar de Metadatos YAML (::METADATA::)

Todo archivo `.md` debe comenzar con este bloque de metadatos:

```markdown
<!--
::METADATA::
type: [theory | method | problem | solution | reference | index | cheatsheet]
topic_id: [id-del-tema-en-manifest]
file_id: [identificador-unico-del-archivo]
status: [draft | review | stable]
audience: [student | ai_context | exam_review]
requires: [lista-de-dependencias-opcional]
-->
```

**Campos obligatorios:**
- `type`: Función técnica del archivo
- `topic_id`: Coincide con el `id` del `manifest.json`
- `file_id`: Identificador único (igual al nombre del archivo sin extensión)
- `status`: Estado de revisión
- `audience`: Audiencia objetivo

---

## Estructura del manifest.json (Mapeo Flexible)

El `manifest.json` actúa como mapa de recursos con la siguiente estructura:

```json
{
  "id": "modulo-subtema",
  "topic": "Nombre del Tema",
  "type": "learning_module",
  "status": "active",
  "tags": ["etiqueta1", "etiqueta2"],
  "prereqs": ["ruta/prerequisito"],
  "resource_map": {
    "entry_point": "PREFIJO-XX-Intro.md",
    "main_theory": "theory/PREFIJO-XX-Teoria-Nombre.md",
    "cheat_sheet": "PREFIJO-XX-Resumen-Formulas.md",
    "methods": ["methods/PREFIJO-XX-Metodo-Nombre.md"],
    "problems": ["problems/PREFIJO-XX-Problema-Nombre.md"]
  },
  "ai_config": {
    "strict_mode": true,
    "allowed_tasks": ["explain_concept", "generate_problems", "verify_solution"]
  }
}
```

**Ventaja:** Permite cambiar nombres de archivo legibles mientras la IA siempre sabe cuál es el `entry_point` consultando el mapa.

---

## Tipos Especiales de Módulos

### `reference_library` (Bibliotecas de Referencia)
Para recursos como "Simbología Matemática" o "Tablas de Integrales":
- Establecer `"type": "reference_library"` en el manifest
- **No requieren** carpetas de `problems/`, `solutions/`, o `methods/`
- Requisitos mínimos: archivo índice y contenido listado en `resource_map`

```json
{
  "id": "ref-simbologia",
  "topic": "Simbología Matemática",
  "type": "reference_library",
  "status": "active",
  "resource_map": {
    "entry_point": "REF-Simbologia-Index.md",
    "content": ["REF-Simbologia-Griegos.md", "REF-Simbologia-Operadores.md"]
  }
}
```

---

## Reglas para generación automática

1. **Nunca mezclar teoría con métodos.**
   - Teoría va en `theory/`: definiciones, teoremas, demostraciones
   - Métodos van en `methods/`: algoritmos paso a paso
   - Son archivos separados con propósitos distintos

2. **FORMATO HÍBRIDO DE TRES NIVELES para Problemas y Soluciones (OBLIGATORIO).**
   
   ```
   [modulo]/[tema]/
   ├── problems/
   │   └── XX-NN-Problemas.md           # Nivel 1: Lista de problemas
   │
   └── solutions/
       ├── XX-NN-Respuestas.md          # Nivel 2: Respuestas rápidas (TODAS)
       └── prob-XX/                      # Nivel 3: Soluciones desarrolladas
           └── solucion-metodo.md
   ```
   
   **Nivel 1 - Problemas (`PREFIJO-XX-Problemas.md`):**
   - Un archivo único por tema con TODOS los problemas
   - Cada problema DEBE tener ID explícito: `### [Prob-XX] Título ⭐`
   - IDs secuenciales (01, 02, ...) únicos dentro del tema
   - Indicadores: ⭐ (básico), ⭐⭐ (intermedio), ⭐⭐⭐ (avanzado)
   
   **Nivel 2 - Respuestas (`PREFIJO-XX-Respuestas.md`):**
   - Archivo OBLIGATORIO con TODAS las respuestas finales en tabla
   - Formato: `| [Prob-XX] | respuesta | [Ver](./prob-XX/solucion-metodo.md) |`
   - Enlaza a soluciones desarrolladas cuando existen
   
   **Nivel 3 - Soluciones desarrolladas (`solutions/prob-XX/`):**
   - Carpetas individuales solo para problemas selectos (representativos, difíciles)
   - Archivo obligatorio: `solucion-metodo.md` (solución paso a paso)
   - Archivo opcional: `solucion-detallada.md` (explicación extendida)
   
   **NAVEGACIÓN PARA IA:**
   1. Para obtener cualquier respuesta → `solutions/XX-NN-Respuestas.md`
   2. Para obtener el proceso de resolución → `solutions/prob-XX/solucion-metodo.md`
   
   **Prohibido:**
   - ❌ Archivos monolíticos de soluciones (ej: `Soluciones-Completas.md`)
   - ❌ Problemas sin ID explícito `[Prob-XX]`
   - ❌ Temas sin archivo de respuestas rápidas
   - ❌ Usar nombres en inglés (`method-solution.md`, `detailed-solution.md`)

3. **Respetar siempre `assigned_method`.**
   - Si un problema tiene un método asignado, la solución debe usar ese método
   - No introducir métodos alternativos en `solucion-metodo.md`

4. **No inventar prerequisitos no declarados.**
   - Solo asumir conocimientos listados en las conexiones del tema
   - Consultar `study-guide.md` para prerequisitos generales
   - Las conexiones se definen en `manifest.json`

5. **Usar Markdown válido y limpio.**
   - LaTeX entre `$...$` para inline, `$$...$$` para bloques
   - **NO usar comandos LaTeX de tablas** (como `\multicolumn`) en Markdown
   - Usar encabezados jerárquicos correctamente
   - Incluir frontmatter YAML en todos los archivos

6. **Ocultar metadatos del renderizado humano.**
   - El frontmatter YAML SIEMPRE debe estar dentro de un comentario HTML.
   - Formato obligatorio para todo archivo `.md`:
     ```markdown
     <!--
     HUMANO:
     [Descripción breve para el lector humano]

     IA:
     [Instrucciones para la IA]

     ---
     content_type: [tipo]
     expected_output:
       default: markdown
     audience: [audiencia]
     ---
     -->

     # Título del documento
     ```
   - Nunca colocar `---` fuera del comentario HTML.
   - El contenido visible para humanos comienza después de `-->`.

7. **Priorizar claridad sobre brevedad.**
   - Mejor explicar de más que de menos
   - Usar ejemplos cuando ayuden a la comprensión
   - Incluir intuiciones y analogías donde sea útil

8. **No asumir contexto fuera del tema actual.**
   - Cada tema es autocontenido
   - Consultar `manifest.json` para saber qué está permitido
   - Usar referencias cruzadas `[→ término]` al glosario

9. **Validar campos obligatorios en `manifest.json`.**
   - Campos requeridos: `id`, `topic`, `status`, `tags`, `ai_contract`
   - El campo `tags` debe contener etiquetas relevantes al tema
   - El campo `ai_contract` referencia este archivo

10. **Seguir convenciones de nombrado.**
    - Archivos: `nombre-descriptivo.md` (kebab-case)
    - Carpetas de soluciones: `solutions/nombre-del-problema/`
    - IDs en manifest: formato `módulo-subtema` (ej: `fund-funciones`)

## Tareas permitidas por defecto

- `explain_concept` - Explicar conceptos de teoría
- `generate_problems` - Crear nuevos problemas
- `solve_problem` - Resolver problemas existentes
- `convert_format` - Convertir entre formatos (Markdown, LaTeX, etc.)
- `verify_solution` - Verificar si una solución es correcta
- `add_examples` - Agregar ejemplos a teoría existente
- `create_summary` - Crear resúmenes de fórmulas

## Estructura de respuestas

Al generar contenido nuevo:

1. Identificar el `content_type` apropiado
2. Incluir frontmatter YAML completo dentro de comentario HTML
3. Seguir la plantilla correspondiente al tipo de archivo
4. Incluir comentarios para humano e IA
5. Verificar que el contenido sea compatible con Markdown puro

## Recursos de referencia

- `glossary.md` - Glosario con ~150 términos y analogías
- `00-META/notation-cheatsheet.md` - Convenciones de notación
- `00-META/study-guide.md` - Guía de estudio y rutas de aprendizaje
- `00-META/tools/validate_repo.py` - Script de validación del repositorio

---

<!--
IA: Viola cualquiera de estas reglas = contenido rechazado.
Ante la duda, pregunta al usuario.
Valida tu output mentalmente antes de generarlo.
-->
