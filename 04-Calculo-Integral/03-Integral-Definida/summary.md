# Resumen: Integral Definida

## Definición
$$\int_a^b f(x) \, dx = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*) \Delta x$$

## Propiedades Fundamentales

1. $\displaystyle\int_a^a f(x) \, dx = 0$

2. $\displaystyle\int_a^b f(x) \, dx = -\int_b^a f(x) \, dx$

3. $\displaystyle\int_a^b cf(x) \, dx = c\int_a^b f(x) \, dx$

4. $\displaystyle\int_a^b [f(x) \pm g(x)] \, dx = \int_a^b f(x) \, dx \pm \int_a^b g(x) \, dx$

5. $\displaystyle\int_a^b f(x) \, dx = \int_a^c f(x) \, dx + \int_c^b f(x) \, dx$

## Teorema Fundamental del Cálculo

**Parte 1:** Si $g(x) = \int_a^x f(t) \, dt$, entonces $g'(x) = f(x)$

**Parte 2:** $\displaystyle\int_a^b f(x) \, dx = F(b) - F(a)$, donde $F'(x) = f(x)$

## Funciones Pares e Impares

- **Par** ($f(-x) = f(x)$): $\displaystyle\int_{-a}^{a} f(x) \, dx = 2\int_0^a f(x) \, dx$

- **Impar** ($f(-x) = -f(x)$): $\displaystyle\int_{-a}^{a} f(x) \, dx = 0$
