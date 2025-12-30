<!--
::METADATA::
type: reference
topic_id: meta-prompts
file_id: prompts-for-students
status: stable
audience: student
last_updated: 2025-12-30
-->

# Prompts listos para estudiantes (copiar/pegar)

Usa estos prompts con tu asistente de IA (Copilot, ChatGPT, etc.) para aprovechar mejor el contenido del repositorio.

## 1. Modo tutor con quiz

```
Eres mi tutor — usando el archivo `theory/CD-01-Teoria-Limites.md` actúa así: hazme un quiz de 5 preguntas conceptuales; espera mis respuestas y no des las soluciones hasta que solicite 'revelar'.
```

## 2. Generador de ejercicios

```
Genera 3 ejercicios de práctica nivel intermedio basados en `03-Calculo-Diferencial/01-Limites/problems/CD-01-Problemas.md` y devuelve solo enunciados y tags en JSON.
```

## 3. Simplificador de conceptos

```
Convierte `theory/CD-01-Teoria-Limites.md` a lenguaje natural apto para explicar a alguien sin matemáticas en 6 frases.
```

## 4. Verificador de soluciones

```
Revisa mi solución paso a paso del problema [Prob-05] en `problems/CD-01-Problemas.md` y dime si hay errores. No me des la respuesta, solo indícame dónde me equivoqué.
```

## 5. Mapa de dependencias

```
Analiza el `manifest.json` del tema y dime qué prerequisitos necesito dominar antes de estudiarlo.
```

## 6. Resumen personalizado

```
Lee `CD-01-Resumen-Formulas.md` y genera una versión más corta de máximo 5 puntos para usar en una hoja de referencia de examen.
```

## 7. Explicación alternativa

```
No entiendo el concepto de [límite/derivada/integral]. Explícamelo usando una analogía diferente a la del archivo de teoría.
```

## 8. Preparación de examen

```
Basándote en los problemas de `problems/AL-02-Problemas.md`, identifica los 5 tipos de ejercicios más importantes para un examen y dame un ejemplo de cada uno.
```

---

**Tip:** Sustituye los nombres de archivo por los del tema que estés estudiando. El formato es siempre `PREFIJO-XX-Tipo-Nombre.md`.
