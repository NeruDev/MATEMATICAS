<!--
::METADATA::
type: reference
topic_id: limites
file_id: _directives
status: stable
audience: ai_context
-->

# Directivas: Límites

## Clasificación del Contenido

| Carpeta/Archivo | Archivo Principal | Descripción |
|-----------------|-------------------|-------------|
| `theory/` | `CD-01-Teoria-Limites.md` | Teoría de límites |
| `methods/` | `CD-01-Metodos-Limites.md` | Procedimientos paso a paso |
| `problems/` | `CD-01-Problemas.md` | Enunciados de problemas |
| `solutions/` | `CD-01-Respuestas.md`, `CD-01-Soluciones-Desarrolladas.md` | Soluciones desarrolladas |
| `CD-01-Limites-Intro.md` | — | Entrada principal del tema |
| `CD-01-Resumen-Formulas.md` | — | Resumen de fórmulas |
| `manifest.json` | — | Metadatos y configuración |

## Clasificación del Tema

| Campo | Valor |
|-------|-------|
| **Módulo** | 03-Calculo-Diferencial |
| **Código** | 01 |
| **Nombre** | Límites |
| **Prerequisitos** | Funciones, Álgebra |
| **Nivel** | Intermedio |

---

## Subtemas

| Código | Subtema | Tipo |
|--------|---------|------|
| 1.1 | Concepto de límite | conceptual |
| 1.2 | Límites laterales | conceptual |
| 1.3 | Propiedades de los límites | procedimental |
| 1.4 | Técnicas de evaluación | procedimental |
| 1.5 | Límites trigonométricos | procedimental |
| 1.6 | Límites al infinito | procedimental |
| 1.7 | Límites infinitos | procedimental |
| 1.8 | Continuidad | conceptual |
| 1.9 | Teorema del valor intermedio | aplicado |

---

## Notación Estándar

| Símbolo | Significado |
|---------|-------------|
| $\lim_{x \to a} f(x)$ | Límite cuando $x$ tiende a $a$ |
| $\lim_{x \to a^+}$ | Límite por la derecha |
| $\lim_{x \to a^-}$ | Límite por la izquierda |
| $\lim_{x \to \infty}$ | Límite cuando $x$ crece sin límite |
| $\varepsilon$ | Épsilon (tolerancia en $y$) |
| $\delta$ | Delta (tolerancia en $x$) |

---

## Límites Fundamentales

$$\lim_{x \to 0} \frac{\sin x}{x} = 1$$

$$\lim_{x \to 0} \frac{1 - \cos x}{x} = 0$$

$$\lim_{x \to 0} \frac{1 - \cos x}{x^2} = \frac{1}{2}$$

$$\lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x = e$$

$$\lim_{x \to 0} \frac{e^x - 1}{x} = 1$$

$$\lim_{x \to 0} \frac{\ln(1+x)}{x} = 1$$

---

## Formas Indeterminadas

| Forma | Técnica típica |
|-------|----------------|
| $\frac{0}{0}$ | Factorización, racionalización, L'Hôpital |
| $\frac{\infty}{\infty}$ | División por mayor potencia, L'Hôpital |
| $0 \cdot \infty$ | Reescribir como $\frac{0}{1/\infty}$ o $\frac{\infty}{1/0}$ |
| $\infty - \infty$ | Racionalización, común denominador |
| $0^0, 1^\infty, \infty^0$ | Tomar logaritmo |

---

## Preferencias de Formato

1. **Notación de límite:** Siempre escribir $\lim_{x \to a}$ con subíndice
2. **Valor absoluto en tablas:** Usar `$\lvert x \rvert$`
3. **Proceso:** Mostrar cada paso de simplificación
4. **Verificación:** Para límites complicados, confirmar con valores numéricos cercanos
