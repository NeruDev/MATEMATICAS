<!--
::METADATA::
type: method
topic_id: 01-integral-indefinida
file_id: CI-01-Metodos-Integracion
status: stable
audience: student
-->

# Métodos de Integración Directa

---

## Método 1: Regla de la Potencia

### Cuándo Usar
- Integrando de la forma $x^n$ donde $n \neq -1$

### Fórmula
$$\int x^n \, dx = \frac{x^{n+1}}{n+1} + C$$

### Ejemplo
$$\int x^4 \, dx = \frac{x^5}{5} + C$$

---

## Método 2: Potencias Fraccionarias y Negativas

### Cuándo Usar
- Radicales o potencias en denominador

### Pasos
1. Convertir a forma $x^n$
2. Aplicar regla de la potencia

### Ejemplo
$$\int \sqrt[3]{x^2} \, dx = \int x^{2/3} \, dx = \frac{x^{5/3}}{5/3} + C = \frac{3x^{5/3}}{5} + C$$

$$\int \frac{1}{x^4} \, dx = \int x^{-4} \, dx = \frac{x^{-3}}{-3} + C = -\frac{1}{3x^3} + C$$

---

## Método 3: Integral de $1/x$

### Cuándo Usar
- Cuando $n = -1$ (excepción de regla de potencia)

### Fórmula
$$\int \frac{1}{x} \, dx = \ln\lvert x \rvert + C$$

### Ejemplo
$$\int \frac{3}{x} \, dx = 3\ln\lvert x \rvert + C$$

---

## Método 4: Exponenciales

### Cuándo Usar
- Funciones $e^x$ o $a^x$

### Fórmulas
$$\int e^x \, dx = e^x + C$$
$$\int a^x \, dx = \frac{a^x}{\ln a} + C$$

### Ejemplo
$$\int 5^x \, dx = \frac{5^x}{\ln 5} + C$$

---

## Método 5: Funciones Trigonométricas Básicas

### Cuándo Usar
- Seno, coseno, secante cuadrada, cosecante cuadrada

### Fórmulas
| Integrando | Resultado |
|------------|-----------|
| $\sin x$ | $-\cos x + C$ |
| $\cos x$ | $\sin x + C$ |
| $\sec^2 x$ | $\tan x + C$ |
| $\csc^2 x$ | $-\cot x + C$ |

### Ejemplo
$$\int (3\sin x + 2\cos x) \, dx = -3\cos x + 2\sin x + C$$

---

## Método 6: Productos Trigonométricos Especiales

### Cuándo Usar
- $\sec x \tan x$ o $\csc x \cot x$

### Fórmulas
$$\int \sec x \tan x \, dx = \sec x + C$$
$$\int \csc x \cot x \, dx = -\csc x + C$$

### Ejemplo
$$\int 4\sec x \tan x \, dx = 4\sec x + C$$

---

## Método 7: Integrales que Producen Arcoseno

### Cuándo Usar
- Forma $\frac{1}{\sqrt{a^2 - x^2}}$

### Fórmula
$$\int \frac{1}{\sqrt{a^2 - x^2}} \, dx = \arcsin\frac{x}{a} + C$$

### Ejemplo
$$\int \frac{1}{\sqrt{9 - x^2}} \, dx = \arcsin\frac{x}{3} + C$$

---

## Método 8: Integrales que Producen Arcotangente

### Cuándo Usar
- Forma $\frac{1}{a^2 + x^2}$

### Fórmula
$$\int \frac{1}{a^2 + x^2} \, dx = \frac{1}{a}\arctan\frac{x}{a} + C$$

### Ejemplo
$$\int \frac{1}{4 + x^2} \, dx = \frac{1}{2}\arctan\frac{x}{2} + C$$

---

## Método 9: Combinación Lineal

### Cuándo Usar
- Suma o diferencia de funciones integrables

### Pasos
1. Separar la integral en suma/diferencia
2. Integrar cada término individualmente
3. Combinar resultados

### Ejemplo
$$\int (x^3 - 4x + e^x) \, dx = \frac{x^4}{4} - 2x^2 + e^x + C$$

---

## Método 10: Simplificación Algebraica Previa

### Cuándo Usar
- Cuando se puede simplificar antes de integrar

### Pasos
1. Expandir, factorizar o dividir
2. Aplicar métodos básicos

### Ejemplo
$$\int \frac{x^3 + 2x}{x} \, dx = \int (x^2 + 2) \, dx = \frac{x^3}{3} + 2x + C$$

$$\int (x + 1)^2 \, dx = \int (x^2 + 2x + 1) \, dx = \frac{x^3}{3} + x^2 + x + C$$
