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

# Método: Encontrar el Dominio de una Función

## Cuándo usar este método

<!--
Identificación del tipo de problema.
-->

Usa este método cuando necesites determinar el conjunto de valores de $x$ para los cuales una función está definida. Aplica especialmente cuando la función contiene:
- Denominadores (fracciones)
- Raíces cuadradas (o de índice par)
- Logaritmos
- Combinaciones de los anteriores

## Pasos del método

1. **Identificar restricciones por denominadores:**
   - Encontrar todos los denominadores
   - Igualar cada denominador a cero
   - Excluir esos valores del dominio

2. **Identificar restricciones por raíces pares:**
   - Encontrar expresiones bajo raíces de índice par
   - Establecer que la expresión debe ser $\geq 0$
   - Resolver la desigualdad

3. **Identificar restricciones por logaritmos:**
   - Encontrar argumentos de logaritmos
   - Establecer que el argumento debe ser $> 0$
   - Resolver la desigualdad

4. **Combinar todas las restricciones:**
   - Intersectar todos los conjuntos de valores válidos
   - Expresar el dominio en notación de intervalos o conjuntos

## Limitaciones

<!--
Casos donde este método falla o no aplica.
-->

- Para funciones definidas por partes, aplicar el método a cada parte
- Funciones trigonométricas pueden requerir análisis adicional
- Funciones implícitas requieren otros métodos

---

<!--
IA: Al resolver problemas de dominio, sigue EXACTAMENTE estos pasos.
-->
