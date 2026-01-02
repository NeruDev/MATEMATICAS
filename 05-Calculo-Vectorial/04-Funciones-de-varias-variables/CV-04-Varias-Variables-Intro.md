<!--
::METADATA::
type: index
topic_id: cv-04-funciones-varias-variables
file_id: CV-04-Varias-Variables-Intro
status: stable
audience: student
requires: [CD-01-Limites, CD-02-[Derivadas](../../glossary.md#derivadas), CV-01-Vectores]
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../glossary.md)

---

# Funciones de varias variables

## Propósito del tema

Extender el [cálculo diferencial](../../glossary.md#limites), [continuidad](../../glossary.md#derivadas) parciales, gradiente y optimización para modelar superficies y fenómenos multidimensionales.

## Ruta de aprendizaje

1. **Funciones de varias variables:** [dominio](../../glossary.md#limites) y [continuidad](../../glossary.md#orden) superior.
4. **[Diferenciabilidad](../../glossary.md#tangente), aproximación lineal.
5. **[Regla de la cadena](../../glossary.md#derivada) direccional:** máxima tasa de cambio, dirección.
7. **Extremos:** puntos críticos, criterio de la segunda [derivada](CV-04-Varias-Variables-Intro.md)  ← Estás aquí
[CV-04-Resumen-Formulas.md](theory/CV-04-Teoria-Varias.md)     ← Desarrollo completo de la teoría
methods/
  └── [métodos paso a paso]
problems/
  └── [enunciados de práctica]
solutions/
  └── [soluciones detalladas]
```

## Conexiones

- **Prerequisitos:** límites, derivadas, vectores en el espacio.
- **Usos posteriores:** integración múltiple, campos vectoriales, optimización.

## Vista previa de conceptos clave

| Concepto | Descripción breve |
|----------|-------------------|
| Derivada parcial | $\frac{\partial f}{\partial x}$: derivada manteniendo otras variables constantes |
| Gradiente | $\nabla f = \langle f_x, f_y, f_z \rangle$ |
| Derivada direccional | $D_{\mathbf{u}}f = \nabla f \cdot \mathbf{u}$ |
| Plano [tangente](../../glossary.md#tangente) | $z - z_0 = f_x(P)(x-x_0) + f_y(P)(y-y_0)$ |
| Multiplicadores de Lagrange | Optimización con restricciones |

---

<!--
IA: Este es el punto de entrada (entry_point) para el tema de funciones de varias variables.
Consulta el manifest.json para el resource_map completo.
file_id: CV-04-Varias-Variables-Intro
-->
