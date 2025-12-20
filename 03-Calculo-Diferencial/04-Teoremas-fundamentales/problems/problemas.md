<!--
HUMANO:
Problemas de teoremas fundamentales.

IA:
Clasificados por subtema, dificultad indicada con ★.

---
content_type: problems
format: unlabeled_list
---
-->

# Problemas de Teoremas Fundamentales

---

## 4.1 Teorema de Rolle

### Nivel Básico ★

1. Verificar que $f(x) = x^2 - 4x + 3$ cumple las hipótesis de Rolle en $[1, 3]$ y encontrar $c$.

2. ¿La función $f(x) = \lvert x \rvert$ cumple el teorema de Rolle en $[-1, 1]$? Justificar.

3. Verificar Rolle para $f(x) = \sin x$ en $[0, \pi]$ y hallar $c$.

4. Mostrar que $f(x) = x^3 - 3x$ cumple Rolle en $[-\sqrt{3}, \sqrt{3}]$.

### Nivel Intermedio ★★

5. Usar Rolle para probar que $x^3 + x - 1 = 0$ tiene exactamente una raíz real.

6. Demostrar que entre dos raíces consecutivas de $\cos x$ hay una raíz de $\sin x$.

7. Probar que $e^x = 1 + x$ tiene exactamente una solución.

8. Si $f(a) = f(b) = 0$, probar que $f(x) + f'(x) = 0$ tiene al menos una solución en $(a, b)$.

### Nivel Avanzado ★★★

9. Sea $f$ diferenciable con $f(0) = 0$ y $f(1) = 1$. Probar que la ecuación $f'(x) = 2x$ tiene solución en $(0, 1)$.

10. Probar que si $f$ es diferenciable y tiene $n$ raíces distintas, entonces $f'$ tiene al menos $n-1$ raíces.

---

## 4.2 Teorema del Valor Medio

### Nivel Básico ★

11. Encontrar $c$ que satisface el TVM para $f(x) = x^2$ en $[0, 2]$.

12. Verificar el TVM para $f(x) = \sqrt{x}$ en $[1, 4]$.

13. Encontrar $c$ para $f(x) = x^3 - x$ en $[0, 2]$.

14. Aplicar TVM a $f(x) = \ln x$ en $[1, e]$.

### Nivel Intermedio ★★

15. Probar que $\lvert \cos a - \cos b \rvert \leq \lvert a - b \rvert$ para todo $a, b$.

16. Demostrar que $\sqrt{1 + x} < 1 + \frac{x}{2}$ para $x > 0$.

17. Un auto recorre 120 km en 1 hora. Probar que en algún momento su velocidad fue exactamente 120 km/h.

18. Si $f'(x) > 0$ en $(a, b)$, probar que $f$ es estrictamente creciente.

19. Probar que $\tan x > x$ para $x \in (0, \frac{\pi}{2})$.

### Nivel Avanzado ★★★

20. Sea $f$ continua en $[0, 1]$, diferenciable en $(0, 1)$, con $f(0) = 0$ y $f(1) = 1$. Probar que existen $c_1, c_2 \in (0, 1)$ distintos con $f'(c_1) \cdot f'(c_2) = 1$.

21. Probar: $\frac{a - b}{\cos^2 b} \leq \tan a - \tan b \leq \frac{a - b}{\cos^2 a}$ para $0 < b < a < \frac{\pi}{2}$.

22. Si $f''(x) > 0$ en $[a, b]$, probar que $f\left(\frac{a+b}{2}\right) < \frac{f(a) + f(b)}{2}$.

---

## 4.3 TVM Generalizado de Cauchy

### Nivel Intermedio ★★

23. Verificar el TVM de Cauchy para $f(x) = x^2$ y $g(x) = x^3$ en $[1, 2]$.

24. Aplicar TVM de Cauchy a $f(x) = \sin x$ y $g(x) = \cos x$ en $[0, \frac{\pi}{4}]$.

25. Si $f(t) = t^2$ y $g(t) = t^3$ representan posición en dos coordenadas, interpretar geométricamente el TVM de Cauchy.

### Nivel Avanzado ★★★

26. Usar TVM de Cauchy para probar la regla de L'Hôpital para el caso $\frac{0}{0}$.

27. Sean $f$ y $g$ diferenciables con $g'(x) \neq 0$. Probar que existe $\theta \in (0, 1)$ tal que:
$$\frac{f(a+h) - f(a)}{g(a+h) - g(a)} = \frac{f'(a + \theta h)}{g'(a + \theta h)}$$

---

## 4.4 Regla de L'Hôpital (Forma $\frac{0}{0}$)

### Nivel Básico ★

28. $\displaystyle\lim_{x \to 0} \frac{\sin x}{x}$

29. $\displaystyle\lim_{x \to 0} \frac{e^x - 1}{x}$

30. $\displaystyle\lim_{x \to 0} \frac{1 - \cos x}{x^2}$

31. $\displaystyle\lim_{x \to 1} \frac{\ln x}{x - 1}$

32. $\displaystyle\lim_{x \to 0} \frac{\tan x - x}{x^3}$

### Nivel Intermedio ★★

33. $\displaystyle\lim_{x \to 0} \frac{x - \sin x}{x^3}$

34. $\displaystyle\lim_{x \to 0} \frac{e^x - e^{-x} - 2x}{x - \sin x}$

35. $\displaystyle\lim_{x \to 0} \frac{\arctan x - x}{x^3}$

36. $\displaystyle\lim_{x \to a} \frac{x^n - a^n}{x - a}$ (demostrar que es $na^{n-1}$)

37. $\displaystyle\lim_{x \to 0} \frac{\sqrt{1+x} - \sqrt{1-x}}{x}$

### Nivel Avanzado ★★★

38. $\displaystyle\lim_{x \to 0} \frac{e^{x^2} - \cos x}{x^2}$

39. $\displaystyle\lim_{x \to 0} \frac{\tan x - \sin x}{x^3}$

40. $\displaystyle\lim_{x \to 0} \frac{x\cos x - \sin x}{x^2 \sin x}$

---

## 4.5 Regla de L'Hôpital (Forma $\frac{\infty}{\infty}$)

### Nivel Básico ★

41. $\displaystyle\lim_{x \to \infty} \frac{x}{e^x}$

42. $\displaystyle\lim_{x \to \infty} \frac{\ln x}{x}$

43. $\displaystyle\lim_{x \to \infty} \frac{x^2}{e^x}$

44. $\displaystyle\lim_{x \to 0^+} \frac{\ln x}{\cot x}$

### Nivel Intermedio ★★

45. $\displaystyle\lim_{x \to \infty} \frac{x^n}{e^x}$ para $n \in \mathbb{N}$

46. $\displaystyle\lim_{x \to \infty} \frac{\ln(\ln x)}{\ln x}$

47. $\displaystyle\lim_{x \to \infty} \frac{e^x + e^{-x}}{e^x - e^{-x}}$

---

## 4.6 Otras Formas Indeterminadas

### Forma $0 \cdot \infty$ ★★

48. $\displaystyle\lim_{x \to 0^+} x \ln x$

49. $\displaystyle\lim_{x \to \infty} x e^{-x}$

50. $\displaystyle\lim_{x \to 0^+} x^2 \cot x$

51. $\displaystyle\lim_{x \to \frac{\pi}{2}^-} (\sec x - \tan x) \cdot \cos x$

### Forma $\infty - \infty$ ★★

52. $\displaystyle\lim_{x \to 0} \left(\frac{1}{\sin x} - \frac{1}{x}\right)$

53. $\displaystyle\lim_{x \to \infty} (x - \sqrt{x^2 + x})$

54. $\displaystyle\lim_{x \to 0} \left(\frac{1}{x} - \frac{1}{e^x - 1}\right)$

55. $\displaystyle\lim_{x \to 0^+} \left(\frac{1}{\ln(1+x)} - \frac{1}{x}\right)$

### Forma $0^0$ ★★★

56. $\displaystyle\lim_{x \to 0^+} x^x$

57. $\displaystyle\lim_{x \to 0^+} (\sin x)^x$

58. $\displaystyle\lim_{x \to 0^+} x^{\sin x}$

### Forma $1^\infty$ ★★★

59. $\displaystyle\lim_{x \to 0} (1 + x)^{1/x}$

60. $\displaystyle\lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x$

61. $\displaystyle\lim_{x \to 0} (\cos x)^{1/x^2}$

62. $\displaystyle\lim_{x \to 0} \left(\frac{\sin x}{x}\right)^{1/x^2}$

### Forma $\infty^0$ ★★★

63. $\displaystyle\lim_{x \to \infty} x^{1/x}$

64. $\displaystyle\lim_{x \to \infty} (e^x + x)^{1/x}$

65. $\displaystyle\lim_{x \to 0^+} (\cot x)^{\sin x}$

---

## 4.7 Teorema de Taylor y Series

### Polinomios de Taylor ★

66. Encontrar el polinomio de Taylor de grado 3 de $e^x$ alrededor de $x = 0$.

67. Encontrar $P_4(x)$ de $\cos x$ alrededor de $x = 0$.

68. Encontrar $P_3(x)$ de $\ln(1 + x)$ alrededor de $x = 0$.

69. Encontrar $P_2(x)$ de $\sqrt{1 + x}$ alrededor de $x = 0$.

### Taylor en $a \neq 0$ ★★

70. Encontrar $P_3(x)$ de $\ln x$ alrededor de $x = 1$.

71. Encontrar $P_2(x)$ de $\sin x$ alrededor de $x = \frac{\pi}{6}$.

72. Encontrar $P_3(x)$ de $e^x$ alrededor de $x = 1$.

### Estimación de Error ★★

73. Usar $P_2(x)$ de $e^x$ para aproximar $e^{0.1}$ y estimar el error.

74. ¿Cuántos términos de la serie de $\sin x$ se necesitan para aproximar $\sin(0.1)$ con error menor que $10^{-6}$?

75. Aproximar $\sqrt{1.1}$ usando Taylor de grado 2 y estimar el error.

### Límites usando Taylor ★★★

76. $\displaystyle\lim_{x \to 0} \frac{e^x - 1 - x - \frac{x^2}{2}}{x^3}$

77. $\displaystyle\lim_{x \to 0} \frac{\sin x - x + \frac{x^3}{6}}{x^5}$

78. $\displaystyle\lim_{x \to 0} \frac{\cos x - 1 + \frac{x^2}{2}}{x^4}$

79. $\displaystyle\lim_{x \to 0} \frac{e^{\sin x} - e^x}{x^3}$

80. $\displaystyle\lim_{x \to 0} \frac{\ln(1 + \sin x) - \sin x}{x^3}$
