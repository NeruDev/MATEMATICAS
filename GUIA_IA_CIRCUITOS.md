<!--
::METADATA::
type: reference
topic_id: meta-ia-guide-circuits
file_id: GUIA_IA_CIRCUITOS
status: active
audience: ai_context
last_updated: 2025-12-30
-->

# Guía de IA para Repositorio de Circuitos Eléctricos

> **OBJETIVO:** Documento maestro para la creación y mantenimiento de un repositorio de Circuitos Eléctricos basado en los principios didácticos del repositorio de Matemáticas, integrando simulación con **Proteus 8.15**.

---

## 1. Principios Didácticos (Adaptados del Repo Matemáticas)

La estructura del conocimiento debe seguir un flujo lógico y compartimentado para maximizar el aprendizaje y facilitar la indexación por IA.

### 1.1 Estructura "Theory-First, Method-Second"

Para cada tema (ej. Análisis de Nodos, Teorema de Thevenin), el contenido debe dividirse estrictamente:

1. **Fundamentos Teóricos (`theory/`)**:
    * Definiciones, leyes físicas (Ohm, Kirchhoff) y demostraciones.
    * *No incluir ejemplos numéricos complejos aquí.*
2. **Metodología (`methods/`)**:
    * "Recetas" o algoritmos paso a paso para resolver circuitos.
    * Ejemplo: "Paso 1: Identificar nodos esenciales. Paso 2: Asignar nodo de referencia..."
3. **Problemas (`problems/`)**:
    * Enunciados limpios sin pistas de solución.
    * Diagramas esquemáticos claros.
4. **Soluciones (`solutions/`)**:
    * Desarrollo completo separado del enunciado.

### 1.2 Progresión de Dificultad

Los problemas deben etiquetarse por nivel:

* ⭐ **Conceptuales/Básicos**: Aplicación directa de fórmula (ej. Divisor de voltaje simple).
* ⭐⭐ **Intermedios**: Requieren sistema de ecuaciones o manipulación del circuito.
* ⭐⭐⭐ **Avanzados**: Circuitos mixtos complejos, fuentes dependientes, o análisis de potencia.

---

## 2. Estándar de Simulación con Proteus 8.15

Este repositorio utiliza **Proteus 8.15** como software de referencia para validación y generación de esquemáticos.

### 2.1 Reglas para Esquemáticos (ISIS)

* **Estilo Visual**:
  * Usar componentes genéricos (RES, CAP, IND) a menos que se especifique una parte real.
  * Textos y etiquetas legibles (Times New Roman o Arial, mínimo 12pt).
  * Fondo blanco para exportación de imágenes.
* **Archivos Fuente**:
  * Los archivos `.pdsprj` deben guardarse en una carpeta `simulation/` dentro de cada problema.
* **Instrumentación**:
  * Usar puntas de prueba (Voltage/Current Probes) en lugar de multímetros virtuales excesivos para mantener limpio el diagrama.

### 2.2 Validación de Resultados

* Al resolver problemas, la IA debe sugerir la configuración de simulación correspondiente.
* Comparar resultados teóricos vs. simulados en la sección de soluciones.
  * *Calculado: 5.0V | Simulado: 4.99V (Diferencia < 1%)*

---

## 3. Estructura de Directorios Propuesta

```text
CIRCUITOS/
├── 00-META/
│   ├── ia-contract.md         ← Este archivo adaptado
│   └── spice-models/          ← Modelos SPICE comunes
│
├── 01-Analisis-DC/
│   ├── 01-Leyes-Basicas/      ← Ohm, Kirchhoff
│   ├── 02-Metodos-Analisis/   ← Nodos, Mallas
│   ├── 03-Teoremas-Redes/     ← Thevenin, Norton, Superposicion
│   └── 04-OpAmps/             ← Amplificadores Operacionales ideales
│
├── 02-Analisis-AC/
│   ├── 01-Fasores/
│   ├── 02-Potencia-AC/
│   └── 03-Sistemas-Trifasicos/
│
└── 03-Semiconductores-Basicos/ (Opcional)
```

---

## 4. Contrato de IA para Circuitos

### 4.1 Definición de Archivos (`manifest.json` extendido)

Cada subtema debe tener un `manifest.json` que incluya:

```json
{
  "id": "DC-02-Nodos",
  "topic": "Análisis Nodal",
  "software_requirements": ["Proteus 8.15"],
  "resource_map": {
    "theory": "theory/DC-02-Teoria.md",
    "simulation_templates": "simulacion/templates/"
  }
}
```

### 4.2 Formato de Solución y Verificación

Toda solución generada por IA debe seguir el bloque:

```markdown
**[Prob-XX]** Solución

1. **Análisis Previo**:
   - Identificación de topología (ej. 3 mallas, sin fuentes de corriente).
   - Método seleccionado: Análisis de Mallas.

2. **Planteamiento**:
   - Ecuación Malla 1: ...
   - Ecuación Malla 2: ...

3. **Cálculo**:
   - Resolución del sistema lineal.
   - Resultados: I1 = 2A, I2 = -0.5A.

4. **Validación (Proteus 8.15)**:
   - "Se simula el circuito colocando sondas de corriente en las ramas principales."
   - "La simulación confirma los valores con un error de 0.0%."
```

### 4.3 Formato de Netlists y Diagramas

* Si se solicita código SPICE textual, usar sintaxis compatible con el motor de simulación de Proteus (basado en SPICE 3F5).
* Para diagramas: Describir las conexiones claramente si no se puede generar imagen: "R1 (10k) entre Vcc y N1".

---

## 5. Resumen de Adaptaciones

| Concepto Repo Matemáticas | Adaptación Circuitos | Razón |
|---------------------------|----------------------|-------|
| `validate_repo.py` | `validate_circuits.py` | Necesidad de verificar existencia de archivos `.pdsprj` |
| Métodos Numéricos | Simulación SPICE | La verificación en circuitos es experimental/simulada |
| Gráficas de funciones | Diagramas de Bode/Tiempo | Naturaleza de las señales eléctricas |
| Teoremas Matemáticos | Leyes Físicas | Contexto de ingeniería aplicada |

---
*Generado por IA Antigravity - 2025*
