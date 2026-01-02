<!--
---
type: solution
problem-id: CD-02-44
topic: [Derivadas](../../../../glossary.md#derivadas)
subtopic: Derivación implícita
difficulty: avanzado
tags: [derivada, implícita, segunda-[derivada](../../../../glossary.md#derivada), círculo-unitario]
created: 2024-12-22
---
-->

# Solución: Segunda derivada de x² + y² = 1

## Problema

Si $x^2 + y^2 = 1$ (círculo unitario), encontrar $\dfrac{d^2y}{dx^2}$.

---

## Método de Solución: Derivación implícita doble

### Parte A: Primera derivada implícita

#### Paso 1: Derivar la ecuación original respecto a x

$$\frac{d}{dx}[x^2 + y^2] = \frac{d}{dx}[1]$$

$$2x + 2y\frac{dy}{dx} = 0$$

#### Paso 2: Despejar dy/dx

$$2y\frac{dy}{dx} = -2x$$

$$\frac{dy}{dx} = -\frac{x}{y}$$

> **Primera [derivada](../../../../glossary.md#derivada):** $\boxed{y' = -\dfrac{x}{y}}$ (válida para $y \neq 0$)

---

### Parte B: Segunda derivada implícita

#### Paso 3: Derivar y' respecto a x

Tenemos $y' = -\dfrac{x}{y}$

Aplicamos la regla del cociente:

$$\frac{d^2y}{dx^2} = \frac{d}{dx}\left[-\frac{x}{y}\right] = -\frac{d}{dx}\left[\frac{x}{y}\right]$$

$$= -\frac{y \cdot \dfrac{d}{dx}[x] - x \cdot \dfrac{d}{dx}[y]}{y^2}$$

$$= -\frac{y \cdot 1 - x \cdot \dfrac{dy}{dx}}{y^2}$$

$$= -\frac{y - x \cdot y'}{y^2}$$

#### Paso 4: Sustituir y' = -x/y

$$\frac{d^2y}{dx^2} = -\frac{y - x\left(-\dfrac{x}{y}\right)}{y^2}$$

$$= -\frac{y + \dfrac{x^2}{y}}{y^2}$$

#### Paso 5: Simplificar el numerador

Reescribimos el numerador con denominador común:

$$y + \frac{x^2}{y} = \frac{y^2 + x^2}{y}$$

Entonces:

$$\frac{d^2y}{dx^2} = -\frac{\dfrac{y^2 + x^2}{y}}{y^2} = -\frac{y^2 + x^2}{y \cdot y^2} = -\frac{x^2 + y^2}{y^3}$$

#### Paso 6: Usar la restricción original

Dado que $x^2 + y^2 = 1$:

$$\frac{d^2y}{dx^2} = -\frac{1}{y^3}$$

---

## Respuesta

$$\boxed{\frac{d^2y}{dx^2} = -\frac{1}{y^3}}$$

---

## Verificación

### Método 1: Derivación explícita

Resolvemos explícitamente para $y$:
$$y = \pm\sqrt{1-x^2}$$

Tomemos $y = \sqrt{1-x^2}$ (semicírculo superior):

**Primera derivada:**
$$y' = \frac{1}{2\sqrt{1-x^2}} \cdot (-2x) = -\frac{x}{\sqrt{1-x^2}} = -\frac{x}{y} \checkmark$$

**Segunda derivada:**
$$y'' = -\frac{d}{dx}\left[\frac{x}{\sqrt{1-x^2}}\right]$$

Usando la regla del cociente:
$$= -\frac{\sqrt{1-x^2} - x \cdot \dfrac{-x}{\sqrt{1-x^2}}}{1-x^2}$$

$$= -\frac{\sqrt{1-x^2} + \dfrac{x^2}{\sqrt{1-x^2}}}{1-x^2}$$

$$= -\frac{\dfrac{1-x^2+x^2}{\sqrt{1-x^2}}}{1-x^2} = -\frac{1}{(1-x^2)^{3/2}} = -\frac{1}{y^3} \checkmark$$

### Método 2: Verificación en un punto específico

En el punto $\left(\dfrac{\sqrt{2}}{2}, \dfrac{\sqrt{2}}{2}\right)$:

**Usando nuestra fórmula:**
$$y'' = -\frac{1}{\left(\frac{\sqrt{2}}{2}\right)^3} = -\frac{1}{\frac{2\sqrt{2}}{8}} = -\frac{8}{2\sqrt{2}} = -\frac{4}{\sqrt{2}} = -2\sqrt{2} \approx -2.828$$

**Verificación numérica** con $y = \sqrt{1-x^2}$ en $x = \dfrac{\sqrt{2}}{2}$:

Aproximando con diferencias finitas (h = 0.001):
$$y'' \approx \frac{y(x+h) - 2y(x) + y(x-h)}{h^2} \approx -2.828 \checkmark$$

---

## Interpretación geométrica

### Curvatura del círculo

La curvatura $\kappa$ de una curva está relacionada con la segunda derivada:

$$\kappa = \frac{|y''|}{(1 + (y')^2)^{3/2}}$$

Para el círculo unitario:
- $y' = -\dfrac{x}{y}$
- $y'' = -\dfrac{1}{y^3}$

$$\kappa = \frac{\left|\frac{-1}{y^3}\right|}{\left(1 + \frac{x^2}{y^2}\right)^{3/2}} = \frac{\frac{1}{|y|^3}}{\left(\frac{y^2+x^2}{y^2}\right)^{3/2}} = \frac{\frac{1}{|y|^3}}{\frac{1}{|y|^3}} = 1$$

> **Resultado notable:** La curvatura del círculo unitario es constante e igual a 1, que corresponde al recíproco del radio ($\kappa = 1/r = 1/1 = 1$). ✓

---

## Resumen de resultados

| Derivada | Expresión general | En términos de la restricción |
|----------|-------------------|-------------------------------|
| $y'$ | $-\dfrac{x}{y}$ | — |
| $y''$ | $-\dfrac{x^2+y^2}{y^3}$ | $-\dfrac{1}{y^3}$ |

---

## Notas adicionales

> **[Dominio](../../../../glossary.md#dominio):** Las [derivadas](../../../../glossary.md#derivadas) están definidas para $y \neq 0$, es decir, en todos los puntos del círculo excepto $(\pm 1, 0)$.

> **Signo de y'':** 
> - Si $y > 0$ (semicírculo superior): $y'' < 0$ → cóncava hacia abajo
> - Si $y < 0$ (semicírculo inferior): $y'' > 0$ → cóncava hacia arriba

Esto coincide con la forma del círculo: curvado hacia el origen.
