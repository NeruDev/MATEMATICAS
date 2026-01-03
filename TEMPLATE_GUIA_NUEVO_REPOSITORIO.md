# 🏗️ Plantilla para Crear Repositorios de Conocimiento Estructurado

> **Propósito:** Esta guía abstrae los patrones exitosos del repositorio de Matemáticas para replicarlos en nuevos dominios de conocimiento. Está diseñada como un prompt conceptual para IA o como referencia para humanos.

---

## 📋 PROMPT MAESTRO PARA CREAR NUEVO REPOSITORIO

```markdown
Eres un arquitecto de repositorios de conocimiento. Tu tarea es diseñar la estructura
completa para un repositorio educativo sobre [DOMINIO] siguiendo el patrón "Digital Garden".

El repositorio debe:
1. Organizar conocimiento de manera progresiva (de básico a avanzado)
2. Incluir teoría, métodos prácticos, problemas y soluciones
3. Ser navegable tanto por humanos como por IA
4. Mantener consistencia en nomenclatura y formato
5. Usar Markdown con soporte para LaTeX/código según el dominio
```

---

## 🧬 ANATOMÍA DEL REPOSITORIO

### Nivel 0 — Raíz

```
NOMBRE-REPOSITORIO/
├── README.md                        ← Entrada principal, skill tree visual
├── WIKI_INDEX.md                    ← Índice central de navegación
├── glossary.md                      ← ~100-150 términos con definiciones
├── 00-META/                         ← Configuración y guías del repositorio
├── 01-[Módulo-Básico]/              ← Primer módulo (fundamentos)
├── 02-[Módulo-Intermedio]/          ← Módulos progresivos...
├── ...
└── NN-[Módulo-Avanzado]/            ← Último módulo
```

### Nivel 1 — Módulo

```
XX-Nombre-Modulo/
├── 00-Index.md                      ← Visión general del módulo
├── 01-[Subtema-1]/                  ← Primer subtema
├── 02-[Subtema-2]/                  ← Subtemas progresivos
├── ...
└── NN-[Subtema-N]/
```

### Nivel 2 — Subtema (unidad atómica)

```
XX-Nombre-Subtema/
├── manifest.json                    ← OBLIGATORIO: Metadatos del tema
├── _directives.md                   ← Instrucciones para IA
├── PREFIJO-XX-Subtema-Intro.md      ← 🚀 PUNTO DE ENTRADA
├── PREFIJO-XX-Resumen-Formulas.md   ← Cheat sheet / quick reference
├── theory/                          ← Conceptos, definiciones, teoremas
│   └── PREFIJO-XX-Teoria-*.md
├── methods/                         ← Procedimientos paso a paso
│   └── PREFIJO-XX-Metodos-*.md
├── problems/                        ← Enunciados de ejercicios
│   └── PREFIJO-XX-Problemas.md
├── solutions/                       ← Sistema de 3 niveles
│   ├── PREFIJO-XX-Respuestas.md     ← Nivel 1: Respuestas rápidas
│   ├── prob-04/                     ← Nivel 2: Soluciones desarrolladas
│   │   └── solucion-metodo.md
│   └── prob-XX/
├── applications/                    ← (Opcional) Casos de uso reales
└── media/                           ← (Opcional) Imágenes, diagramas
```

---

## 📁 ARCHIVOS CLAVE Y SUS ESTRUCTURAS

### 1. `manifest.json` — Contrato del subtema

```json
{
  "id": "prefijo-xx-nombre",
  "topic": "Título del Tema",
  "type": "learning_module",
  "status": "active",
  "last_updated": "YYYY-MM-DD",
  "human_purpose": "Descripción breve del propósito",
  "resource_map": {
    "entry_point": "PREFIJO-XX-Nombre-Intro.md",
    "main_theory": "theory/PREFIJO-XX-Teoria-Nombre.md",
    "cheat_sheet": "PREFIJO-XX-Resumen-Formulas.md",
    "methods": ["methods/PREFIJO-XX-Metodos-Nombre.md"],
    "problems": "problems/PREFIJO-XX-Problemas.md",
    "answers": "solutions/PREFIJO-XX-Respuestas.md",
    "solutions": [
      "solutions/prob-04/",
      "solutions/prob-10/"
    ]
  },
  "ai_contract": {"strict_mode": true},
  "prerequisites": ["id-tema-previo"],
  "learning_objectives": [
    "Objetivo de aprendizaje 1",
    "Objetivo de aprendizaje 2"
  ],
  "estimated_time": "X-Y horas",
  "difficulty": "básico|intermedio|avanzado",
  "subtopics": [
    {"id": "X.1", "title": "Subtema 1", "description": "..."},
    {"id": "X.2", "title": "Subtema 2", "description": "..."}
  ],
  "tags": ["tag1", "tag2"]
}
```

### 2. Bloque `::METADATA::` — Encabezado de archivos .md

```markdown
<!--
::METADATA::
type: theory|method|problem|solution|reference
topic_id: prefijo-xx-nombre
file_id: nombre-archivo
status: draft|review|stable
audience: student|ai_context|both
last_updated: YYYY-MM-DD
-->
```

### 3. `glossary.md` — Glosario con auto-enlace

```markdown
# Glosario

## A

### **algoritmo**
> Un conjunto ordenado y finito de instrucciones que permite resolver un problema.
> 
> **Ver también:** [complejidad](#complejidad), [pseudocódigo](#pseudocódigo)
```

### 4. `00-Index.md` — Índice de módulo

```markdown
# [Módulo]: [Título]

## Visión General
Descripción del módulo...

## Temas Incluidos

| # | Tema | Descripción | Dificultad |
|---|------|-------------|------------|
| 01 | [Tema 1](01-Tema/) | Descripción | ⭐ |
| 02 | [Tema 2](02-Tema/) | Descripción | ⭐⭐ |

## Skill Tree
[Diagrama Mermaid mostrando dependencias]

## Ruta de Estudio Recomendada
1. Comenzar con...
2. Luego estudiar...
```

---

## 🏷️ SISTEMA DE PREFIJOS

| Prefijo | Descripción | Ejemplo de Archivo |
|---------|-------------|-------------------|
| `XX-NN` | Módulo-Subtema | `02-03` = Módulo 2, Subtema 3 |
| `PREFIJO` | Abreviatura del módulo (2-3 letras) | `AL`, `CD`, `VHDL` |

**Convención de nombres:** `PREFIJO-NN-Contenido-Tipo.md`
- Ejemplo: `VHDL-02-Combinacional-Teoria.md`

---

## 🔗 SISTEMA DE ENLACES

### Tipos de enlaces

1. **Internos al subtema:** `[texto](archivo.md)` o `[texto](carpeta/archivo.md)`
2. **Entre subtemas:** `[texto](../XX-Otro-Tema/archivo.md)`
3. **Al glosario:** `[término](../glossary.md#término)`
4. **A soluciones:**
   - Respuesta rápida: `[Solución](#prob-XX)` → enlaza a `Respuestas.md#prob-XX`
   - Solución desarrollada: `[Solución](solutions/prob-XX/solucion-metodo.md)`

### Reglas críticas

- ✅ Usar rutas relativas siempre
- ✅ Anclas en minúsculas con guiones: `#prob-04`, `#definicion`
- ✅ Sin espacios en nombres de archivo
- ❌ No usar rutas absolutas
- ❌ No usar `./` al inicio (redundante)

---

## 📊 SISTEMA DE SOLUCIONES (3 NIVELES)

```
PROBLEMA → ¿Tiene solución desarrollada?
    │
    ├── SÍ → Enlace a: solutions/prob-XX/solucion-metodo.md
    │        (Contiene desarrollo paso a paso)
    │
    └── NO → Enlace a: solutions/PREFIJO-XX-Respuestas.md#prob-XX
             (Solo respuesta final)
```

### Estructura de `Respuestas.md`

```markdown
## Respuestas Rápidas

### Prob-01
**Respuesta:** 42

---

### Prob-02
**Respuesta:** x = 5, y = 3

[Ver solución desarrollada →](prob-02/solucion-metodo.md)
```

### Estructura de solución desarrollada

```markdown
# Solución — Problema XX

## Enunciado
[Copiar enunciado del problema]

## Solución

### Paso 1: [Título]
...

### Paso 2: [Título]
...

## Respuesta Final
**R:** ...
```

---

## 🎯 EJEMPLO APLICADO: REPOSITORIO "DISEÑO DIGITAL"

### Propuesta de Módulos

| # | Prefijo | Módulo | Descripción |
|---|---------|--------|-------------|
| 01 | `FDD` | **Fundamentos** | Sistemas numéricos, álgebra booleana, compuertas |
| 02 | `LOG` | **Lógica Combinacional** | Mux, demux, decodificadores, sumadores |
| 03 | `SEC` | **Lógica Secuencial** | Flip-flops, registros, contadores, FSM |
| 04 | `VHDL` | **VHDL** | Sintaxis, modelado, simulación, síntesis |
| 05 | `FPGA` | **Implementación FPGA** | Flujo de diseño, constraints, timing |
| 06 | `MCU` | **Microcontroladores** | Arquitectura, periféricos, programación |
| 07 | `PRY` | **Proyectos Integrados** | Proyectos que combinan todo |

### Estructura Ejemplo: Módulo VHDL

```
04-VHDL/
├── 00-Index.md
├── 01-Introduccion-VHDL/
│   ├── manifest.json
│   ├── _directives.md
│   ├── VHDL-01-Intro.md
│   ├── VHDL-01-Resumen-Sintaxis.md
│   ├── theory/
│   │   ├── VHDL-01-Teoria-Historia.md
│   │   └── VHDL-01-Teoria-Conceptos.md
│   ├── methods/
│   │   └── VHDL-01-Metodos-Entorno.md
│   ├── problems/
│   │   └── VHDL-01-Problemas.md
│   └── solutions/
│       ├── VHDL-01-Respuestas.md
│       └── prob-05/
│           └── solucion-codigo.md
├── 02-Modelado-Combinacional/
├── 03-Modelado-Secuencial/
├── 04-Testbenches/
├── 05-Maquinas-Estados/
└── 06-Sintesis/
```

### Ejemplo de `manifest.json` para VHDL

```json
{
  "id": "vhdl-01-introduccion",
  "topic": "Introducción a VHDL",
  "type": "learning_module",
  "status": "active",
  "last_updated": "2025-01-XX",
  "human_purpose": "Fundamentos del lenguaje VHDL: historia, estructura básica, entidades y arquitecturas.",
  "resource_map": {
    "entry_point": "VHDL-01-Intro.md",
    "main_theory": "theory/VHDL-01-Teoria-Conceptos.md",
    "cheat_sheet": "VHDL-01-Resumen-Sintaxis.md",
    "methods": ["methods/VHDL-01-Metodos-Entorno.md"],
    "problems": "problems/VHDL-01-Problemas.md",
    "answers": "solutions/VHDL-01-Respuestas.md",
    "solutions": ["solutions/prob-05/"]
  },
  "ai_contract": {"strict_mode": true},
  "prerequisites": ["fdd-01-fundamentos", "log-02-combinacional"],
  "learning_objectives": [
    "Comprender la historia y propósito de VHDL",
    "Escribir entidades y arquitecturas básicas",
    "Diferenciar entre modelado estructural y comportamental",
    "Configurar un entorno de desarrollo VHDL"
  ],
  "estimated_time": "3-4 horas",
  "difficulty": "intermedio",
  "subtopics": [
    {"id": "4.1", "title": "Historia de VHDL", "description": "Origen y evolución del lenguaje"},
    {"id": "4.2", "title": "Estructura básica", "description": "Entidad, arquitectura, configuración"},
    {"id": "4.3", "title": "Tipos de datos", "description": "std_logic, std_logic_vector, integer"},
    {"id": "4.4", "title": "Operadores", "description": "Lógicos, aritméticos, relacionales"}
  ],
  "tags": ["vhdl", "hdl", "fpga", "síntesis", "simulación"]
}
```

### Glosario Sugerido (términos iniciales)

```markdown
# Glosario — Diseño Digital

## A

### **arquitectura (VHDL)**
> Bloque que describe el comportamiento o estructura interna de una entidad.

### **asíncrono**
> Circuito o señal que no depende de una señal de reloj.

## C

### **combinacional**
> Circuito cuya salida depende únicamente de las entradas actuales.

### **constraint**
> Restricción de diseño (timing, ubicación de pines) para síntesis en FPGA.

## E

### **entidad (VHDL)**
> Declaración de la interfaz externa de un módulo: puertos de entrada/salida.

## F

### **flip-flop**
> Elemento de memoria básico que almacena un bit.

### **FSM (Finite State Machine)**
> Máquina de estados finitos: modelo de circuito secuencial con estados discretos.

### **FPGA**
> Field Programmable Gate Array: circuito integrado reconfigurable.

## L

### **latch**
> Elemento de memoria sensible a nivel (no recomendado en diseño síncrono).

## M

### **microcontrolador**
> Circuito integrado que incluye CPU, memoria y periféricos en un solo chip.

## S

### **secuencial**
> Circuito cuya salida depende de las entradas y del estado anterior.

### **síntesis**
> Proceso de convertir código HDL en una implementación de hardware.

## T

### **testbench**
> Módulo de prueba para verificar el comportamiento de un diseño mediante simulación.

## V

### **VHDL**
> VHSIC Hardware Description Language: lenguaje de descripción de hardware.
```

---

## ✅ CHECKLIST DE IMPLEMENTACIÓN

### Fase 1: Estructura base
- [ ] Crear carpeta raíz del repositorio
- [ ] Crear README.md con skill tree
- [ ] Crear WIKI_INDEX.md vacío (llenar después)
- [ ] Crear glossary.md con ~50 términos iniciales
- [ ] Crear carpeta 00-META/ con archivos base

### Fase 2: Módulos
- [ ] Crear carpetas de módulos (01-XX/ a NN-XX/)
- [ ] Crear 00-Index.md en cada módulo
- [ ] Definir subtemas por módulo

### Fase 3: Subtemas
- [ ] Crear estructura de carpetas por subtema
- [ ] Crear manifest.json para cada subtema
- [ ] Crear _directives.md para cada subtema
- [ ] Crear archivo *-Intro.md como punto de entrada

### Fase 4: Contenido
- [ ] Poblar archivos de teoría
- [ ] Crear métodos/procedimientos
- [ ] Crear problemas con soluciones
- [ ] Implementar sistema de 3 niveles de soluciones

### Fase 5: Navegación
- [ ] Completar WIKI_INDEX.md con todos los enlaces
- [ ] Verificar enlaces internos
- [ ] Agregar auto-enlaces del glosario

---

## 🤖 PROMPT PARA INICIAR CREACIÓN DE CONTENIDO

```markdown
Crea el contenido para el subtema [NOMBRE] del módulo [MÓDULO] siguiendo estas directivas:

1. **Punto de entrada** (`*-Intro.md`):
   - Párrafo motivacional (¿por qué es importante?)
   - Objetivos de aprendizaje (lista)
   - Prerequisitos con enlaces
   - Mapa de recursos del tema

2. **Teoría** (`theory/*.md`):
   - Definiciones precisas
   - Teoremas/propiedades con demostración cuando aplique
   - Ejemplos ilustrativos
   - Notación estándar según cheatsheet

3. **Métodos** (`methods/*.md`):
   - Título descriptivo del procedimiento
   - Pasos numerados
   - Ejemplos resueltos paso a paso
   - Casos especiales y errores comunes

4. **Problemas** (`problems/*.md`):
   - Organizados por dificultad (⭐, ⭐⭐, ⭐⭐⭐)
   - Identificador único (### Prob-XX)
   - Enunciado claro y completo
   - Enlace a solución

5. **Soluciones** (`solutions/`):
   - Respuestas.md: Solo respuesta final
   - prob-XX/: Desarrollo completo cuando amerite

Formato: Markdown con código VHDL en bloques ```vhdl``` y fórmulas en LaTeX $...$ cuando aplique.
```

---

## 📚 REFERENCIA RÁPIDA — MÓDULOS SUGERIDOS PARA DISEÑO DIGITAL

### Opción A: Enfoque académico completo

```
01-Fundamentos-Digitales/    → Sistemas numéricos, Boole, compuertas
02-Circuitos-Combinacionales/ → Análisis, síntesis, minimización
03-Circuitos-Secuenciales/   → Flip-flops, contadores, registros, FSM
04-VHDL-Basico/              → Sintaxis, modelado, simulación
05-VHDL-Avanzado/            → Síntesis, optimización, buenas prácticas
06-Microcontroladores/       → Arquitectura, periféricos, programación
07-Proyectos/                → Integraciones prácticas
```

### Opción B: Enfoque práctico/profesional

```
01-Fundamentos/              → Lo esencial de lógica digital
02-VHDL-y-Simulacion/        → Lenguaje + verificación
03-FPGAs-y-Sintesis/         → Implementación real
04-ARM-Microcontrollers/     → Arquitectura ARM Cortex
05-Embedded-Systems/         → Integración hardware-software
06-Proyectos-Capstone/       → Proyectos completos
```

---

**Última actualización:** 2025-01-XX  
**Basado en:** Repositorio de Matemáticas v2.0 (Digital Garden)
