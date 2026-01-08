<!--
::METADATA::
type: index
topic_id: ed-04-transformada-laplace
file_id: ED-04-Transformada-Laplace-Intro
status: stable
learning_role: introduction
difficulty: 4/5
prerequisites: ["ED-02", "CI-05"]
concepts: ["transformada-laplace", "transformada-inversa", "fracciones-parciales", "funcion-escalon"]
audience: student
last_updated: 2026-01-05
-->

> 🏠 **Navegación:** [← Volver al Índice](../00-Index.md) | [📚 Glosario](../../glossary.md) | [🗺️ Wiki](../../WIKI_INDEX.md)

---

# Transformada de Laplace

## Propósito del tema

Dominar la transformada de Laplace como herramienta para resolver ecuaciones diferenciales con condiciones iniciales, especialmente útil para funciones discontinuas y sistemas de control.

## Mapa de Recursos

| Recurso | Archivo | Descripción |
|---------|---------|-------------|
| 📘 Teoría | [ED-04-Teoria-Transformada-Laplace.md](theory/ED-04-Teoria-Transformada-Laplace.md) | Desarrollo completo |
| 🔧 Métodos | [ED-04-Metodos-Laplace.md](methods/ED-04-Metodos-Laplace.md) | Procedimientos paso a paso |
| 📝 Problemas | [ED-04-Problemas.md](problems/ED-04-Problemas.md) | Ejercicios de práctica |
| ✅ Soluciones | [ED-04-Respuestas.md](solutions/ED-04-Respuestas.md) | Respuestas y desarrollos |
| 📋 Fórmulas | [ED-04-Resumen-Formulas.md](ED-04-Resumen-Formulas.md) | Cheat sheet |

## Ruta de aprendizaje

1. **Definición**: $\mathcal{L}\{f(t)\} = \int_0^\infty e^{-st}f(t)\,dt$
2. **Transformadas básicas**: tabla de funciones elementales
3. **Propiedades**: linealidad, derivadas, integrales
4. **Transformada inversa**: fracciones parciales
5. **Convolución**: teorema de convolución
6. **Aplicaciones**: resolución de EDO, sistemas de control

## Conexiones

- **Prerrequisitos**: [EDO de segundo orden](../02-EDO-Segundo-Orden/ED-02-EDO-Segundo-Orden-Intro.md), [Integrales impropias](../../04-Calculo-Integral/05-Integrales-Impropias/CI-05-Integrales-Impropias-Intro.md)
- **Usos posteriores**: Control automático, Señales y sistemas, Ingeniería

## Vista previa de conceptos clave

### Transformadas fundamentales

| $f(t)$ | $\mathcal{L}\{f(t)\} = F(s)$ |
|--------|------------------------------|
| $1$ | $\frac{1}{s}$ |
| $t^n$ | $\frac{n!}{s^{n+1}}$ |
| $e^{at}$ | $\frac{1}{s-a}$ |
| $\sin(bt)$ | $\frac{b}{s^2+b^2}$ |
| $\cos(bt)$ | $\frac{s}{s^2+b^2}$ |

### Propiedades clave

| Propiedad | Fórmula |
|-----------|---------|
| [Derivada](../../glossary.md#transformada-de-laplace).
Para fórmulas rápidas: [ED-04-Resumen-Formulas.md](ED-04-Resumen-Formulas.md)
file_id: ED-04-Transformada-Laplace-Intro
-->
