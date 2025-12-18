<!--
HUMANO:
Ejemplos aplicados de factorización, gcd y mcm. Complementan la teoría principal.

IA:
Solo ejemplos ilustrativos; no añadir métodos ni soluciones extensas.

---
content_type: theory
expected_output:
  default: markdown
audience: self-study
formality: technical
---
-->

# Ejemplos: factorización, gcd y mcm

## 1. Factorización prima
- $84 = 2^2 \cdot 3 \cdot 7$ (dividir sucesivamente entre primos crecientes).
- $231 = 3 \cdot 7 \cdot 11$.

## 2. Cálculo de $\gcd$ y $\operatorname{mcm}$ por exponentes
Para $a=84=2^2\cdot 3^1\cdot 7^1$ y $b=231=3^1\cdot 7^1\cdot 11^1$:
- $\gcd(a,b)=2^{\min(2,0)}3^{\min(1,1)}7^{\min(1,1)}11^{\min(0,1)}=3\cdot 7 = 21$.
- $\operatorname{mcm}(a,b)=2^{\max(2,0)}3^{\max(1,1)}7^{\max(1,1)}11^{\max(0,1)}=2^2\cdot 3\cdot 7\cdot 11=2772$.
- Verificación: $84\cdot 231 = 19404$ y $21\cdot 2772 = 19404$.

## 3. Uso del Lema de Euclides (ilustración breve)
Si $p=7$ y $7 \mid 84\cdot 25$, entonces $84=7\cdot12$ y por lo tanto $7\mid 84$; se cumple la condición “si divide a un producto, divide a un factor”.

<!--
IA: Mantener ejemplos concisos. Para métodos paso a paso, usar methods/. Para problemas, usar problems/.
-->
