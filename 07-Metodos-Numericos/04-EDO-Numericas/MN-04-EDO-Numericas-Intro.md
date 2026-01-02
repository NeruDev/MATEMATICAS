<!--
---
title: Introducción a [EDO Numéricas](../../glossary.md#edo)-numericas
tags: [métodos-numéricos, [EDO](../../glossary.md#edo), euler, runge-kutta, sistemas]
created: 2025-12-20
updated: 2025-12-20
---
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../glossary.md)

---

# Métodos Numéricos para EDO

## Descripción General

Los [métodos numéricos](../../glossary.md#ecuaciones-diferenciales) ordinarias (EDO) permiten aproximar soluciones de problemas de valor inicial cuando no es posible encontrar una solución analítica. Estos métodos son fundamentales en simulación y modelado.

## Contenido del Módulo

### Métodos de Un Paso
- [[MN-04-T01-Euler|Método de Euler]]
- [[MN-04-T02-Euler-Mejorado|[Método de Euler](../../glossary.md#metodo-de-euler) Mejorado (Heun)]]
- [[MN-04-T03-Runge-Kutta|Métodos de Runge-Kutta]]

### Métodos de Paso Múltiple
- [[MN-04-T04-Adams-Bashforth|Adams-Bashforth]]
- [[MN-04-T05-Adams-Moulton|Adams-Moulton]]

### Sistemas y Ecuaciones de Orden Superior
- [[MN-04-T06-Sistemas-EDO|Sistemas de EDO]]
- [[MN-04-T07-EDO-[Orden](../../glossary.md#orden)-Superior|EDO de Orden Superior]]

### Recursos
- [[MN-04-Resumen-Formulas|Resumen de Fórmulas]]

## Objetivos de Aprendizaje

1. Implementar el [método de Euler](../../glossary.md#convergencia) de los métodos

## Prerrequisitos

- [Ecuaciones diferenciales](../../glossary.md#ecuaciones-diferenciales) ordinarias
- Serie de Taylor
- Sistemas de ecuaciones

## Problema de Valor Inicial (PVI)

$$\frac{dy}{dx} = f(x, y), \quad y(x_0) = y_0$$

El objetivo es encontrar $y(x)$ para $x > x_0$.

## Mapa Conceptual

```
EDO Numéricas
├── Un Paso
│   ├── Euler
│   ├── Euler Mejorado (Heun)
│   └── Runge-Kutta (RK2, RK4)
├── Paso Múltiple
│   ├── Adams-Bashforth (explícito)
│   └── Adams-Moulton (implícito)
└── Extensiones
    ├── Sistemas de EDO
    └── EDO de Orden Superior
```

## Navegación

| Anterior | Índice | Siguiente |
|----------|--------|-----------|
| [[MN-03-Integracion-Numerica-Intro]] | [[00-Index]] | — |
