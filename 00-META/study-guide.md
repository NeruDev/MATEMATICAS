<!--
::METADATA::
type: reference
topic_id: meta-study-guide
file_id: study-guide
status: stable
audience: student
last_updated: 2026-01-02
-->

# Guía de Estudio

## Cómo usar este repositorio

### 1. Estructura de navegación

El repositorio está organizado en **7 módulos** numerados:

| # | Módulo | Descripción |
|---|--------|-------------|
| 01 | **Fundamentos** | Simbología, Aritmética, Álgebra, Geometría, Trigonometría, Geometría Analítica |
| 02 | **Álgebra Lineal** | Matrices, Determinantes, Sistemas Lineales, Espacios Vectoriales, Transformaciones |
| 03 | **Cálculo Diferencial** | Límites, Derivadas, Aplicaciones, Teoremas Fundamentales |
| 04 | **Cálculo Integral** | Integral Indefinida/Definida, Técnicas, Aplicaciones, Impropias |
| 05 | **Cálculo Vectorial** | Vectores, Curvas, Funciones Vectoriales, Varias Variables, Integración Múltiple |
| 06 | **Ecuaciones Diferenciales** | EDO Primer/Segundo Orden, Sistemas, Laplace, Series de Potencias |
| 07 | **Métodos Numéricos** | Raíces, Interpolación, Integración Numérica, EDO Numéricas |

### 2. Dentro de cada tema

Cada subtema sigue esta estructura estándar:

```
XX-Nombre-Tema/
├── manifest.json                    ← Metadatos y configuración
├── PREFIJO-XX-*-Intro.md            ← 🚀 EMPIEZA AQUÍ
├── PREFIJO-XX-Resumen-Formulas.md   ← Fórmulas clave (cheat sheet)
├── theory/                          ← Conceptos y definiciones
├── methods/                         ← Procedimientos paso a paso
├── problems/                        ← Ejercicios para practicar
├── solutions/                       ← Soluciones detalladas
├── applications/                    ← Casos aplicados (opcional)
└── media/                           ← Recursos visuales (opcional)
```

**Nota:** El punto de entrada siempre es el archivo `*-Intro.md`, no hay archivos `README.md` en los subtemas.

### 3. Sistema de prefijos

Los archivos usan prefijos que indican su módulo:

| Prefijo | Módulo | Ejemplo |
|---------|--------|---------|
| `FUN-XX` | Fundamentos | `FUN-02-Aritmetica-Intro.md` |
| `AL-XX` | Álgebra Lineal | `AL-03-Sistemas-Teoria.md` |
| `CD-XX` | Cálculo Diferencial | `CD-02-Derivadas-Metodos.md` |
| `CI-XX` | Cálculo Integral | `CI-04-Aplicaciones-Problemas.md` |
| `CV-XX` | Cálculo Vectorial | `CV-01-Vectores-Intro.md` |
| `ED-XX` | Ecuaciones Diferenciales | `ED-02-Segundo-Orden-Teoria.md` |
| `MN-XX` | Métodos Numéricos | `MN-03-Integracion-Numerica.md` |

### 4. Orden recomendado de estudio

1. **Lee el archivo `*-Intro.md`** del tema (visión general)
2. **Estudia la teoría** en `theory/` (definiciones, teoremas)
3. **Aprende los métodos** en `methods/` (procedimientos paso a paso)
4. **Practica** con `problems/` (ejercicios clasificados por dificultad)
5. **Verifica** tus respuestas en `solutions/`
6. **Consulta** el `*-Resumen-Formulas.md` para repasos rápidos

### 5. Uso con IA (Copilot/ChatGPT)

La IA puede ayudarte a:
- 📚 Explicar conceptos de forma alternativa
- ✏️ Generar problemas adicionales de práctica
- ✅ Verificar si tus soluciones son correctas
- 🔍 Identificar qué prerequisitos necesitas reforzar

La IA respeta los métodos definidos en cada tema y no asume conocimientos fuera de los prerequisitos declarados.

### 6. Recursos de consulta rápida

| Recurso | Ubicación | Uso |
|---------|-----------|-----|
| Glosario | [`glossary.md`](../glossary.md) | Definiciones y términos clave |
| Notación | [`notation-cheatsheet.md`](notation-cheatsheet.md) | Símbolos y convenciones |
| Índice principal | [`WIKI_INDEX.md`](../WIKI_INDEX.md) | Navegación centralizada |
| Fórmulas | `PREFIJO-XX-Resumen-Formulas.md` | Por cada tema |

## Prerequisitos generales

Antes de comenzar, debes tener conocimientos básicos de:
- ✓ Álgebra elemental (operaciones, ecuaciones)
- ✓ Geometría analítica básica (coordenadas, rectas)
- ✓ Trigonometría básica (funciones, identidades fundamentales)

El módulo **[01-Fundamentos](../01-Fundamentos/00-Index.md)** te ayuda a reforzar estos conceptos si es necesario.
