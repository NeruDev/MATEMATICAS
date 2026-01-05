<!--
::METADATA::
type: index
topic_id: cd-02-derivadas
file_id: CD-02-Derivadas-Intro
status: stable
learning_role: introduction
difficulty: 3/5
prerequisites: ["CD-01"]
concepts: ["derivada", "tasa-de-cambio", "tangente", "regla-de-la-cadena"]
audience: student
last_updated: 2026-01-05
-->

> 🏠 **Navegación:** [← Volver al Índice](../00-Index.md) | [📚 Glosario](../../glossary.md) | [🗺️ Wiki](../../WIKI_INDEX.md)

---

# Derivadas

## Descripción General

La **derivada** es una medida de cómo cambia una función cuando su variable independiente cambia. Representa la tasa de cambio instantánea y es el concepto central del cálculo diferencial.

## Mapa de Recursos

| Recurso | Archivo | Descripción |
|---------|---------|-------------|
| 📘 Teoría | [CD-02-Teoria-Derivadas.md](theory/CD-02-Teoria-Derivadas.md) | Definiciones y teoremas |
| 🔧 Métodos | [CD-02-Metodos-Derivadas.md](methods/CD-02-Metodos-Derivadas.md) | Procedimientos paso a paso |
| 📝 Problemas | [CD-02-Problemas.md](problems/CD-02-Problemas.md) | Ejercicios de práctica |
| ✅ Soluciones | [CD-02-Respuestas.md](solutions/CD-02-Respuestas.md) | Respuestas y desarrollos |
| 📋 Fórmulas | [CD-02-Resumen-Formulas.md](CD-02-Resumen-Formulas.md) | Cheat sheet |

## Objetivos de Aprendizaje

1. Entender la derivada como límite del cociente incremental
2. Interpretar la derivada como pendiente de la recta tangente
3. Aplicar las reglas de derivación (potencia, producto, cociente)
4. Calcular derivadas de funciones compuestas (regla de la cadena)
5. Derivar funciones trigonométricas, exponenciales y logarítmicas
6. Calcular derivadas de orden superior

## Ruta de Aprendizaje

```
2.1 Definición de derivada
        ↓
2.2 Interpretación geométrica
        ↓
2.3 Reglas básicas ──→ 2.4 Regla de la cadena
        ↓                      ↓
2.5 Derivadas especiales ←─────┘
        ↓
2.6 Derivadas de orden superior
```

## Interpretaciones de la Derivada

| Interpretación | Descripción |
|----------------|-------------|
| **Geométrica** | Pendiente de la recta tangente a la curva |
| **Física** | Velocidad instantánea, tasa de cambio |
| **Analítica** | Límite del cociente incremental |

## Conexiones

- **Prerrequisitos**: [Límites](../01-Limites/CD-01-Limites-Intro.md), Continuidad
- **Usos posteriores**: [Aplicaciones de la derivada](../03-Aplicaciones-de-la-derivada/CD-03-Aplicaciones-Intro.md), Optimización
- **En otras áreas**: Física (cinemática), Economía (marginalidad), Ingeniería (tasas)

## Vista Previa de Fórmulas Clave

| Regla | Fórmula |
|-------|---------|
| Potencia | $\frac{d}{dx}[x^n] = nx^{n-1}$ |
| Producto | $\frac{d}{dx}[fg] = f'g + fg'$ |
| Cociente | $\frac{d}{dx}\left[\frac{f}{g}\right] = \frac{f'g - fg'}{g^2}$ |
| Cadena | $\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)$ |

---

> **Nota**: La derivada es una de las herramientas más poderosas de las matemáticas. Domina las reglas de derivación para poder enfocarte en las aplicaciones.
