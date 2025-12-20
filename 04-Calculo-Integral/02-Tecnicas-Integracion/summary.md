# Resumen: Técnicas de Integración

## Sustitución
$$\int f(g(x))g'(x) \, dx = \int f(u) \, du, \quad u = g(x)$$

## Integración por Partes
$$\int u \, dv = uv - \int v \, du$$

Regla LIATE para elegir $u$: **L**ogarítmicas, **I**nversas trig., **A**lgebraicas, **T**rigonométricas, **E**xponenciales

## Integrales Trigonométricas

### Potencias de sen y cos
- $\sin^n x \cos^m x$: si $n$ o $m$ es impar, separar y usar identidad
- Ambos pares: usar fórmulas de reducción

### Identidades útiles
- $\sin^2 x = \frac{1 - \cos 2x}{2}$
- $\cos^2 x = \frac{1 + \cos 2x}{2}$

## Sustitución Trigonométrica

| Expresión | Sustitución | Identidad usada |
|-----------|-------------|-----------------|
| $\sqrt{a^2 - x^2}$ | $x = a\sin\theta$ | $1 - \sin^2\theta = \cos^2\theta$ |
| $\sqrt{a^2 + x^2}$ | $x = a\tan\theta$ | $1 + \tan^2\theta = \sec^2\theta$ |
| $\sqrt{x^2 - a^2}$ | $x = a\sec\theta$ | $\sec^2\theta - 1 = \tan^2\theta$ |

## Fracciones Parciales (para $\frac{P(x)}{Q(x)}$ con grado $P <$ grado $Q$)

| Factor en denominador | Forma de descomposición |
|----------------------|-------------------------|
| $ax + b$ | $\frac{A}{ax+b}$ |
| $(ax+b)^n$ | $\frac{A_1}{ax+b} + \frac{A_2}{(ax+b)^2} + \cdots$ |
| $ax^2+bx+c$ irreducible | $\frac{Ax+B}{ax^2+bx+c}$ |
