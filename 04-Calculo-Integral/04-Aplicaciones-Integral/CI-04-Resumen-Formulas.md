<!--
::METADATA::
type: cheatsheet
topic_id: ci-04-aplicaciones-integral
file_id: CI-04-Resumen-Formulas
status: stable
audience: exam_review
requires: []
-->

# Resumen rápido — Aplicaciones de la Integral

## 1. Área entre curvas

### Integración respecto a $x$

$$A = \int_a^b |f(x) - g(x)|\,dx = \int_a^b [\text{arriba} - \text{abajo}]\,dx$$

### Integración respecto a $y$

$$A = \int_c^d |f(y) - g(y)|\,dy = \int_c^d [\text{derecha} - \text{izquierda}]\,dy$$

## 2. Volúmenes de sólidos de revolución

### Método de discos

Revolución alrededor del eje $x$:
$$V = \pi\int_a^b [R(x)]^2\,dx$$

Revolución alrededor del eje $y$:
$$V = \pi\int_c^d [R(y)]^2\,dy$$

### Método de arandelas (washers)

$$V = \pi\int_a^b \left([R_{\text{ext}}(x)]^2 - [R_{\text{int}}(x)]^2\right)\,dx$$

### Método de capas cilíndricas (shells)

Revolución alrededor del eje $y$:
$$V = 2\pi\int_a^b x \cdot f(x)\,dx$$

Revolución alrededor del eje $x$:
$$V = 2\pi\int_c^d y \cdot g(y)\,dy$$

### Guía de selección de método

| Eje de revolución | Variable de integración | Método recomendado |
|-------------------|------------------------|-------------------|
| Eje $x$ | $dx$ | Discos/Arandelas |
| Eje $x$ | $dy$ | Capas cilíndricas |
| Eje $y$ | $dy$ | Discos/Arandelas |
| Eje $y$ | $dx$ | Capas cilíndricas |

## 3. Longitud de arco

### Forma cartesiana $y = f(x)$

$$L = \int_a^b \sqrt{1 + \left(\frac{dy}{dx}\right)^2}\,dx = \int_a^b \sqrt{1 + [f'(x)]^2}\,dx$$

### Forma cartesiana $x = g(y)$

$$L = \int_c^d \sqrt{1 + \left(\frac{dx}{dy}\right)^2}\,dy = \int_c^d \sqrt{1 + [g'(y)]^2}\,dy$$

### Forma paramétrica $x = x(t)$, $y = y(t)$

$$L = \int_\alpha^\beta \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}\,dt$$

### Coordenadas polares $r = f(\theta)$

$$L = \int_\alpha^\beta \sqrt{r^2 + \left(\frac{dr}{d\theta}\right)^2}\,d\theta$$

## 4. Área de superficie de revolución

### Revolución alrededor del eje $x$

$$S = 2\pi\int_a^b y\sqrt{1 + \left(\frac{dy}{dx}\right)^2}\,dx$$

### Revolución alrededor del eje $y$

$$S = 2\pi\int_c^d x\sqrt{1 + \left(\frac{dx}{dy}\right)^2}\,dy$$

### Forma paramétrica (alrededor de $x$)

$$S = 2\pi\int_\alpha^\beta y(t)\sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}\,dt$$

## 5. Trabajo

### Trabajo general

$$W = \int_a^b F(x)\,dx$$

### Ley de Hooke (resortes)

$$F = kx \quad \Rightarrow \quad W = \int_a^b kx\,dx = \frac{1}{2}k(b^2 - a^2)$$

### Bombeo de líquidos

$$W = \int_a^b \rho g \cdot A(y) \cdot d(y)\,dy$$

donde:
- $\rho$ = densidad del líquido
- $g$ = aceleración gravitacional
- $A(y)$ = área de sección transversal
- $d(y)$ = distancia a recorrer

## 6. Valor promedio

$$f_{\text{prom}} = \frac{1}{b-a}\int_a^b f(x)\,dx$$

## 7. Centro de masa (barra unidimensional)

$$\bar{x} = \frac{\int_a^b x \cdot \rho(x)\,dx}{\int_a^b \rho(x)\,dx}$$

---

<!--
IA: Hoja de referencia rápida para aplicaciones de la integral.
Para desarrollo completo: theory/CI-04-Teoria-Aplicaciones.md
file_id: CI-04-Resumen-Formulas
-->
