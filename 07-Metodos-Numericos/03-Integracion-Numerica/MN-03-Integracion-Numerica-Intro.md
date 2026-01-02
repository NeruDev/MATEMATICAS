<!--
---
title: Introducción a [Integración Numérica](../../glossary.md#integración-numérica)
type: index
topic: integracion-numerica
tags: [métodos-numéricos, integración, trapecios, simpson, cuadratura]
created: 2025-12-20
updated: 2025-12-20
---
-->

# Integración Numérica (Cuadratura)

## Descripción General

La integración numérica consiste en aproximar el valor de integrales definidas $\int_a^b f(x)\,dx$ cuando no es posible obtener una [antiderivada](../../glossary.md#antiderivada) en forma cerrada o cuando solo se dispone de valores tabulados de la [función](../../glossary.md#función).

## Contenido del Módulo

### Fórmulas de Newton-Cotes
- [[MN-03-T01-Regla-Trapecios|Regla del Trapecio]]
- [[MN-03-T02-Regla-Simpson|Regla de Simpson]]
- [[MN-03-T03-Simpson-3-8|[Regla de Simpson](../../glossary.md#regla-de-simpson) 3/8]]

### Métodos Compuestos
- [[MN-03-T04-Trapecios-Compuesto|Trapecio Compuesto]]
- [[MN-03-T05-Simpson-Compuesto|Simpson Compuesto]]

### Análisis de Error
- [[MN-03-T06-Errores-[Cuadratura](../../glossary.md#cuadratura)|Análisis de Errores]]

### Recursos
- [[MN-03-Resumen-Formulas|Resumen de Fórmulas]]

## Objetivos de Aprendizaje

1. Aplicar la [regla del trapecio](../../glossary.md#regla-del-trapecio) simple y compuesta
2. Implementar las reglas de Simpson 1/3 y 3/8
3. Estimar y acotar el error de integración numérica
4. Seleccionar el método apropiado según la precisión requerida

## Prerrequisitos

- [Cálculo integral](../../glossary.md#cálculo-integral) ([integral definida](../../glossary.md#integral-definida))
- [Interpolación](../../glossary.md#interpolación) polinomial
- Serie de Taylor

## Mapa Conceptual

```
Integración Numérica
├── Newton-Cotes (Cerradas)
│   ├── Trapecio (n=1)
│   ├── Simpson 1/3 (n=2)
│   └── Simpson 3/8 (n=3)
├── Métodos Compuestos
│   ├── Trapecio Compuesto
│   └── Simpson Compuesto
└── Análisis de Error
    ├── Error de Truncamiento
    └── Orden de Precisión
```

## Navegación

| Anterior | Índice | Siguiente |
|----------|--------|-----------|
| [[MN-02-Interpolacion-Intro]] | [[00-Index]] | [[MN-04-[EDO](../../glossary.md#edo)-Numericas-Intro]] |
