<!--
HUMANO:
Aquí se explica CÓMO se aplica un concepto.
Un archivo = un método.

IA:
Este archivo define un PROCEDIMIENTO CANÓNICO.
Úsalo como referencia para 'method-solution'.

---
content_type: method
expected_output:
  default: markdown
method_scope: canonical
---
-->

# Método: Evaluación de Límites por Factorización

## Cuándo usar este método

<!--
Identificación del tipo de problema.
-->

Usa este método cuando:
- La sustitución directa produce la forma indeterminada $\frac{0}{0}$
- El numerador y/o denominador son polinomios
- Sospechas que hay un factor común que se puede cancelar

**Forma típica del problema:**
$$\lim_{x \to a} \frac{P(x)}{Q(x)} = \frac{0}{0}$$

donde $P(x)$ y $Q(x)$ son polinomios.

## Pasos del método

1. **Intentar sustitución directa:**
   - Sustituir $x = a$ en la expresión
   - Si obtienes $\frac{0}{0}$, continuar con el paso 2

2. **Factorizar numerador y denominador:**
   - Buscar factores de la forma $(x - a)$ (ya que ambos se anulan en $x = a$)
   - Usar técnicas de factorización: factor común, diferencia de cuadrados, trinomio, etc.

3. **Cancelar factores comunes:**
   - Simplificar la fracción eliminando $(x - a)$ del numerador y denominador
   - Esto es válido porque $x \neq a$ (solo nos acercamos a $a$)

4. **Evaluar el límite simplificado:**
   - Sustituir $x = a$ en la expresión simplificada
   - El resultado es el valor del límite

## Limitaciones

<!--
Casos donde este método falla o no aplica.
-->

- **No aplica** si la forma indeterminada es diferente de $\frac{0}{0}$ (como $\frac{\infty}{\infty}$)
- **No aplica** si no hay factores comunes después de factorizar
- **Requiere** habilidad en técnicas de factorización
- Para expresiones con raíces, considerar racionalización
- Para funciones trigonométricas, usar identidades específicas

---

<!--
IA: Al resolver límites con forma 0/0, intenta este método primero.
-->
