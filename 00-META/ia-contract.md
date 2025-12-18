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

## Reglas para generación automática

1. **Nunca mezclar teoría con métodos.**
   - Teoría va en `theory/`
   - Métodos van en `methods/`
   - Son archivos separados con propósitos distintos

2. **Nunca incluir soluciones dentro de `problems/`.**
   - Los problemas solo contienen enunciados y pistas opcionales
   - Las soluciones van en `solutions/[nombre-problema]/`

3. **Respetar siempre `assigned_method`.**
   - Si un problema tiene un método asignado, la solución debe usar ese método
   - No introducir métodos alternativos en `method-solution.md`

4. **No inventar prerequisitos no declarados.**
   - Solo asumir conocimientos listados en las conexiones del tema
   - Consultar `study-guide.md` para prerequisitos generales

5. **Usar Markdown válido y limpio.**
   - LaTeX entre `$...$` para inline, `$$...$$` para bloques
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

8. **No asumir contexto fuera del tema actual.**
   - Cada tema es autocontenido
   - Consultar `manifest.json` para saber qué está permitido

## Tareas permitidas por defecto

- `explain_concept` - Explicar conceptos de teoría
- `generate_problems` - Crear nuevos problemas
- `convert_format` - Convertir entre formatos (Markdown, LaTeX, etc.)
- `verify_solution` - Verificar si una solución es correcta

## Estructura de respuestas

Al generar contenido nuevo:

1. Identificar el `content_type` apropiado
2. Incluir frontmatter YAML completo
3. Seguir la plantilla correspondiente
4. Incluir comentarios para humano e IA

---

<!--
IA: Viola cualquiera de estas reglas = contenido rechazado.
Ante la duda, pregunta al usuario.
-->
