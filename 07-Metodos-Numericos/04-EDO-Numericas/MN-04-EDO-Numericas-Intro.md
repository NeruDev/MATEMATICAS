<!--
---
title: Introducción a EDO Numéricas
type: index
topic: edo-numericas
tags: [métodos-numéricos, EDO, euler, runge-kutta, sistemas]
created: 2025-12-20
updated: 2025-12-20
---
-->

# Métodos Numéricos para EDO

## Descripción General

Los métodos numéricos para ecuaciones diferenciales ordinarias (EDO) permiten aproximar soluciones de problemas de valor inicial cuando no es posible encontrar una solución analítica. Estos métodos son fundamentales en simulación y modelado.

## Contenido del Módulo

### Métodos de Un Paso
- [[MN-04-T01-Euler|Método de Euler]]
- [[MN-04-T02-Euler-Mejorado|Método de Euler Mejorado (Heun)]]
- [[MN-04-T03-Runge-Kutta|Métodos de Runge-Kutta]]

### Métodos de Paso Múltiple
- [[MN-04-T04-Adams-Bashforth|Adams-Bashforth]]
- [[MN-04-T05-Adams-Moulton|Adams-Moulton]]

### Sistemas y Ecuaciones de Orden Superior
- [[MN-04-T06-Sistemas-EDO|Sistemas de EDO]]
- [[MN-04-T07-EDO-Orden-Superior|EDO de Orden Superior]]

### Recursos
- [[MN-04-Resumen-Formulas|Resumen de Fórmulas]]

## Objetivos de Aprendizaje

1. Implementar el método de Euler para problemas de valor inicial
2. Aplicar métodos de Runge-Kutta de diferentes órdenes
3. Resolver sistemas de EDO numéricamente
4. Analizar estabilidad y convergencia de los métodos

## Prerrequisitos

- Ecuaciones diferenciales ordinarias
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
