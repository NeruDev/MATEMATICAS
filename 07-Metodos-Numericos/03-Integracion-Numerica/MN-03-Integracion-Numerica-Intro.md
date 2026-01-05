<!--
::METADATA::
type: index
topic_id: mn-03-integracion-numerica
file_id: MN-03-Integracion-Numerica-Intro
status: stable
learning_role: introduction
difficulty: 3/5
prerequisites: ["CI-03", "MN-02"]
concepts: ["integracion-numerica", "trapecio", "simpson", "cuadratura", "newton-cotes"]
audience: student
last_updated: 2026-01-05
-->

> 🏠 **Navegación:** [← Volver al Índice](../00-Index.md) | [📚 Glosario](../../glossary.md) | [🗺️ Wiki](../../WIKI_INDEX.md)

---

# Integración Numérica (Cuadratura)

## Descripción General

La integración numérica permite aproximar integrales definidas cuando no es posible encontrar una antiderivada en forma cerrada o cuando solo se dispone de valores tabulados de la función.

## Mapa de Recursos

| Recurso | Archivo | Descripción |
|---------|---------|-------------|
| 📘 Teoría | [MN-03-Teoria-Integracion-Numerica.md](theory/MN-03-Teoria-Integracion-Numerica.md) | Desarrollo completo |
| 🔧 Métodos | [MN-03-Metodos-Integracion-Numerica.md](methods/MN-03-Metodos-Integracion-Numerica.md) | Procedimientos paso a paso |
| 📝 Problemas | [MN-03-Problemas.md](problems/MN-03-Problemas.md) | Ejercicios de práctica |
| ✅ Soluciones | [MN-03-Respuestas.md](solutions/MN-03-Respuestas.md) | Respuestas y desarrollos |
| 📋 Fórmulas | [MN-03-Resumen-Formulas.md](MN-03-Resumen-Formulas.md) | Cheat sheet |

## Contenido del Módulo

### Fórmulas de Newton-Cotes
- Regla del Trapecio
- Regla de Simpson 1/3
- Regla de Simpson 3/8

### Métodos Compuestos
- Trapecio Compuesto
- Simpson Compuesto

### Análisis de Error
- Error de truncamiento
- Orden de precisión

## Objetivos de Aprendizaje

1. Aplicar la regla del trapecio para aproximar integrales
2. Utilizar las reglas de Simpson para mayor precisión
3. Estimar el error de las aproximaciones
4. Implementar métodos compuestos para intervalos grandes

## Prerrequisitos

- Integral definida y cálculo integral
- Interpolación polinomial

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

## Conexiones

- **Prerrequisitos**: [Interpolación](../02-Interpolacion/MN-02-Interpolacion-Intro.md), [Integral definida](../../04-Calculo-Integral/03-Integral-Definida/CI-03-Integral-Definida-Intro.md)
- **Usos posteriores**: [EDO Numéricas](../04-EDO-Numericas/MN-04-EDO-Numericas-Intro.md), Simulación

---

> **Nota**: La integración numérica es fundamental para aplicaciones donde las integrales analíticas no son posibles.

## Navegación

| Anterior | Índice | Siguiente |
|----------|--------|-----------|
| [[MN-02-Interpolacion-Intro]] | [[00-Index]] | [[MN-04-[EDO](../../glossary.md#edo)-Numericas-Intro]] |
