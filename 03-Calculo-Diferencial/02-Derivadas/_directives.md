<!--
IA:
Directivas específicas para el tema de Derivadas.
-->

# Directivas: La Derivada

## Clasificación del Tema

| Campo | Valor |
|-------|-------|
| **Módulo** | 02-Calculo-Diferencial |
| **Código** | 02 |
| **Nombre** | La Derivada |
| **Prerequisitos** | Límites |
| **Nivel** | Intermedio |

---

## Subtemas

| Código | Subtema | Tipo |
|--------|---------|------|
| 2.1 | Definición de derivada | conceptual |
| 2.2 | Derivadas elementales | procedimental |
| 2.3 | Reglas de diferenciación | procedimental |
| 2.4 | Regla de la cadena | procedimental |
| 2.5 | Derivación implícita | procedimental |
| 2.6 | Derivadas de orden superior | procedimental |
| 2.7 | Derivadas de funciones inversas | procedimental |
| 2.8 | Derivación logarítmica | procedimental |

---

## Tabla de Derivadas

### Algebraicas
| $f(x)$ | $f'(x)$ |
|--------|---------|
| $c$ | $0$ |
| $x^n$ | $nx^{n-1}$ |
| $\sqrt{x}$ | $\frac{1}{2\sqrt{x}}$ |

### Exponenciales y Logarítmicas
| $f(x)$ | $f'(x)$ |
|--------|---------|
| $e^x$ | $e^x$ |
| $a^x$ | $a^x \ln a$ |
| $\ln x$ | $\frac{1}{x}$ |
| $\log_a x$ | $\frac{1}{x \ln a}$ |

### Trigonométricas
| $f(x)$ | $f'(x)$ |
|--------|---------|
| $\sin x$ | $\cos x$ |
| $\cos x$ | $-\sin x$ |
| $\tan x$ | $\sec^2 x$ |

### Trigonométricas Inversas
| $f(x)$ | $f'(x)$ |
|--------|---------|
| $\arcsin x$ | $\frac{1}{\sqrt{1-x^2}}$ |
| $\arccos x$ | $-\frac{1}{\sqrt{1-x^2}}$ |
| $\arctan x$ | $\frac{1}{1+x^2}$ |

---

## Reglas Fundamentales

- **Producto:** $(fg)' = f'g + fg'$
- **Cociente:** $\left(\frac{f}{g}\right)' = \frac{f'g - fg'}{g^2}$
- **Cadena:** $[f(g(x))]' = f'(g(x)) \cdot g'(x)$

---

## Preferencias de Formato

1. **Notación:** Usar $f'(x)$ o $\frac{dy}{dx}$ según contexto
2. **Simplificación:** Siempre simplificar la respuesta final
3. **Valor absoluto:** Usar `$\lvert x \rvert$` en tablas
