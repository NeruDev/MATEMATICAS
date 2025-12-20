<!--
HUMANO:
Resumen de aplicaciones de la integral.

IA:
Fórmulas clave con diagramas conceptuales.

---
content_type: summary
format: formula_sheet
---
-->

# Resumen: Aplicaciones de la Integral

---

## Área entre Curvas

### Integración Vertical
$$A = \int_a^b |f(x) - g(x)| \, dx$$

### Integración Horizontal
$$A = \int_c^d |f(y) - g(y)| \, dy$$

---

## Volúmenes de Revolución

### Método del Disco (eje horizontal)
$$V = \pi\int_a^b [f(x)]^2 \, dx$$

### Método del Disco (eje vertical)
$$V = \pi\int_c^d [g(y)]^2 \, dy$$

### Método de la Arandela
$$V = \pi\int_a^b \left([R(x)]^2 - [r(x)]^2\right) dx$$

### Método de la Capa Cilíndrica
$$V = 2\pi\int_a^b x \cdot f(x) \, dx$$

---

## Longitud de Arco

### Forma Cartesiana
$$L = \int_a^b \sqrt{1 + \left(\frac{dy}{dx}\right)^2} \, dx$$

### Forma Paramétrica
$$L = \int_\alpha^\beta \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} \, dt$$

---

## Área de Superficie de Revolución

### Rotación alrededor del eje $x$
$$S = 2\pi\int_a^b f(x)\sqrt{1 + [f'(x)]^2} \, dx$$

### Rotación alrededor del eje $y$
$$S = 2\pi\int_c^d g(y)\sqrt{1 + [g'(y)]^2} \, dy$$

---

## Trabajo

### Fuerza Variable
$$W = \int_a^b F(x) \, dx$$

### Ley de Hooke (resortes)
$$W = \int_0^x kx \, dx = \frac{1}{2}kx^2$$

### Bombeo de fluidos
$$W = \int_a^b \rho g A(y) \cdot d(y) \, dy$$

---

## Valor Promedio

$$f_{\text{prom}} = \frac{1}{b-a}\int_a^b f(x) \, dx$$

**Teorema del Valor Medio Integral:**
Existe $c \in (a,b)$ tal que $f(c) = f_{\text{prom}}$
