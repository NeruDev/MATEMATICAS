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
├── manifest.json     # Metadatos, conexiones, tags, ai_contract
├── README.md         # Entrada principal con roadmap visual
├── summary.md        # Resumen de fórmulas clave
├── theory/           # Definiciones, teoremas, pruebas
├── methods/          # Procedimientos paso a paso
├── problems/         # Enunciados (sin soluciones)
├── solutions/        # Soluciones organizadas por problema
├── applications/     # Casos aplicados
├── diagnostic/       # Pre-test de prerequisitos
└── media/            # Videos, GeoGebra, imágenes
```

## Reglas para generación automática

1. **Nunca mezclar teoría con métodos.**
   - Teoría va en `theory/`: definiciones, teoremas, demostraciones
   - Métodos van en `methods/`: algoritmos paso a paso
   - Son archivos separados con propósitos distintos

2. **Nunca incluir soluciones dentro de `problems/`.**
   - Los problemas solo contienen enunciados y pistas opcionales
   - Las soluciones van en `solutions/[nombre-problema]/`
   - Cada solución tiene `problem-statement.md` y `method-solution.md`

3. **Respetar siempre `assigned_method`.**
   - Si un problema tiene un método asignado, la solución debe usar ese método
   - No introducir métodos alternativos en `method-solution.md`

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
