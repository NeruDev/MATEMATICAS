<!--
::METADATA::
type: index
topic_id: mn-02-interpolacion
file_id: MN-02-Interpolacion-Intro
status: stable
learning_role: introduction
difficulty: 3/5
prerequisites: ["FUN-03", "AL-01"]
concepts: ["interpolacion", "lagrange", "newton", "splines", "diferencias-divididas"]
audience: student
last_updated: 2026-01-05
-->

> 🏠 **Navegación:** [← Volver al Índice](../00-Index.md) | [📚 Glosario](../../glossary.md) | [🗺️ Wiki](../../WIKI_INDEX.md)

---

# Métodos de Interpolación

## Descripción General

La interpolación es el proceso de construir una función que pase exactamente por un conjunto de puntos dados $(x_i, y_i)$. Es fundamental para aproximar funciones, construir curvas suaves y estimar valores intermedios.

## Mapa de Recursos

| Recurso | Archivo | Descripción |
|---------|---------|-------------|
| 📘 Teoría | [MN-02-Teoria-Interpolacion.md](theory/MN-02-Teoria-Interpolacion.md) | Desarrollo completo |
| 🔧 Métodos | [MN-02-Metodos-Interpolacion.md](methods/MN-02-Metodos-Interpolacion.md) | Procedimientos paso a paso |
| 📝 Problemas | [MN-02-Problemas.md](problems/MN-02-Problemas.md) | Ejercicios de práctica |
| ✅ Soluciones | [MN-02-Respuestas.md](solutions/MN-02-Respuestas.md) | Respuestas y desarrollos |
| 📋 Fórmulas | [MN-02-Resumen-Formulas.md](MN-02-Resumen-Formulas.md) | Cheat sheet |

## Contenido del Módulo

### Interpolación Polinomial
- Interpolación de Lagrange
- Diferencias Divididas de Newton
- Diferencias Finitas

### Interpolación por Tramos
- Splines Lineales
- Splines Cúbicos

## Objetivos de Aprendizaje

1. Construir polinomios interpolantes usando el método de Lagrange
2. Aplicar diferencias divididas de Newton
3. Estimar el error de interpolación
4. Implementar splines cúbicos para curvas suaves

## Prerrequisitos

- Polinomios y sus propiedades
- Sistemas de ecuaciones lineales
- Matrices y determinantes

## Mapa Conceptual

```
Interpolación
├── Polinomial
│   ├── Lagrange
│   ├── Newton (Diferencias Divididas)
│   └── Diferencias Finitas
└── Por Tramos
    ├── Splines Lineales
    └── Splines Cúbicos
```

## Conexiones

- **Prerrequisitos**: [Raíces de Ecuaciones](../01-Raices-Ecuaciones/MN-01-Raices-Intro.md), Álgebra Lineal
- **Usos posteriores**: [Integración Numérica](../03-Integracion-Numerica/MN-03-Integracion-Numerica-Intro.md), Ajuste de curvas

---

> **Nota**: La interpolación es la base de muchos métodos numéricos. Entender el error de interpolación es crucial para aplicaciones prácticas.
