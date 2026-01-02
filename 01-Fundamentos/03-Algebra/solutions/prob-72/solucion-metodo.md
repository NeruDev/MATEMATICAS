<!--
::METADATA::
type: solution
topic_id: fun-03-algebra
file_id: FUN-03-Prob-72-Solucion
status: stable
audience: student
problem_ref: "[Prob-72]"
methods: ["sustitucion-cuadratica", "ecuacion-bicuadratica", "factorizacion"]
-->

# Solución [Prob-72]: Ecuación bicuadrática

> **Problema:** Resuelve: $x^4 - 5x^2 + 4 = 0$

## Concepto clave

Una **ecuación bicuadrática** tiene la forma:

$$ax^4 + bx^2 + c = 0$$

Se resuelve mediante la **[sustitución](../../../../glossary.md#sustitucion)** $u = x^2$, lo que la convierte en una ecuación cuadrática en $u$.

---

## Método 1: Sustitución

### Paso 1: Realizar la sustitución

Sea $u = x^2$ (donde $u \geq 0$ porque $x^2$ nunca es negativo)

Como $x^4 = (x^2)^2 = u^2$, la ecuación se transforma:

$$u^2 - 5u + 4 = 0$$

### Paso 2: Resolver la ecuación cuadrática en $u$

Factorizamos buscando dos números que:
- Sumen $-5$ (coeficiente de $u$)
- Multipliquen $4$ (término independiente)

Esos números son $-1$ y $-4$:

$$u^2 - 5u + 4 = (u - 1)(u - 4) = 0$$

Por lo tanto:

$$u - 1 = 0 \quad \Rightarrow \quad u = 1$$

$$u - 4 = 0 \quad \Rightarrow \quad u = 4$$

### Paso 3: Deshacer la sustitución

Recordando que $u = x^2$:

**Para $u = 1$:**

$$x^2 = 1$$

$$x = \pm\sqrt{1}$$

$$x = \pm 1$$

**Para $u = 4$:**

$$x^2 = 4$$

$$x = \pm\sqrt{4}$$

$$x = \pm 2$$

### Paso 4: Escribir todas las soluciones

$$x \in \{-2, -1, 1, 2\}$$

---

## Método 2: Factorización directa

### Paso 1: Reconocer la estructura factorizable

Observamos que $x^4 - 5x^2 + 4$ es un "trinomio cuadrático" en $x^2$:

$$x^4 - 5x^2 + 4 = (x^2 - 1)(x^2 - 4)$$

Podemos verificar expandiendo:

$$(x^2 - 1)(x^2 - 4) = x^4 - 4x^2 - x^2 + 4 = x^4 - 5x^2 + 4 \quad \checkmark$$

### Paso 2: Factorizar cada factor (diferencia de cuadrados)

**Factor 1:** $x^2 - 1$

$$x^2 - 1 = x^2 - 1^2 = (x + 1)(x - 1)$$

**Factor 2:** $x^2 - 4$

$$x^2 - 4 = x^2 - 2^2 = (x + 2)(x - 2)$$

### Paso 3: Escribir la factorización completa

$$x^4 - 5x^2 + 4 = (x + 1)(x - 1)(x + 2)(x - 2)$$

### Paso 4: Encontrar las raíces

Igualando cada factor a cero:

- $x + 1 = 0 \Rightarrow x = -1$
- $x - 1 = 0 \Rightarrow x = 1$
- $x + 2 = 0 \Rightarrow x = -2$
- $x - 2 = 0 \Rightarrow x = 2$

---

## Método 3: Fórmula cuadrática (para la ecuación en $u$)

### Paso 1: Aplicar la sustitución

Con $u = x^2$:

$$u^2 - 5u + 4 = 0$$

### Paso 2: Usar la fórmula cuadrática

$$u = \frac{-(-5) \pm \sqrt{(-5)^2 - 4(1)(4)}}{2(1)}$$

$$u = \frac{5 \pm \sqrt{25 - 16}}{2}$$

$$u = \frac{5 \pm \sqrt{9}}{2}$$

$$u = \frac{5 \pm 3}{2}$$

**Solución 1:**

$$u = \frac{5 + 3}{2} = \frac{8}{2} = 4$$

**Solución 2:**

$$u = \frac{5 - 3}{2} = \frac{2}{2} = 1$$

### Paso 3: Deshacer la sustitución

Como antes, de $u = 1$ y $u = 4$ obtenemos $x = \pm 1$ y $x = \pm 2$.

---

## Verificación

### Verificación de $x = 1$

$$1^4 - 5(1)^2 + 4 = 1 - 5 + 4 = 0 \quad \checkmark$$

### Verificación de $x = -1$

$$(-1)^4 - 5(-1)^2 + 4 = 1 - 5 + 4 = 0 \quad \checkmark$$

### Verificación de $x = 2$

$$2^4 - 5(2)^2 + 4 = 16 - 20 + 4 = 0 \quad \checkmark$$

### Verificación de $x = -2$

$$(-2)^4 - 5(-2)^2 + 4 = 16 - 20 + 4 = 0 \quad \checkmark$$

---

## Representación gráfica

La [función](../../../../glossary.md#funcion) $f(x) = x^4 - 5x^2 + 4$ es un [polinomio](../../../../glossary.md#polinomio) de grado 4:

```
     y
     │       ╱    ╲       ╱
     │      ╱      ╲     ╱
   4 ┼─────●────────────●───────
     │    ╱          ╲ ╱
     │   ╱            ╳
     │  ╱            ╱ ╲
     │ ╱            ╱   ╲
   0 ┼───●────●─────●────●─────▶ x
     │  -2   -1     1    2
     │
```

Los cuatro puntos donde la curva cruza el eje $x$ son las soluciones.

---

## Diagrama del proceso de sustitución

```
     Ecuación bicuadrática           Ecuación cuadrática
     
         x⁴ - 5x² + 4 = 0    ───────▶    u² - 5u + 4 = 0
                             u = x²
                  │                           │
                  │                      Factorizar
                  │                           │
                  │                    (u-1)(u-4) = 0
                  │                           │
                  │                     u = 1  ó  u = 4
                  │                           │
                  └──────────◀────────────────┘
                             x² = u
                                  │
                    ┌─────────────┴─────────────┐
                    │                           │
               x² = 1                       x² = 4
                    │                           │
              x = ±1                       x = ±2
                    │                           │
                    └─────────────┬─────────────┘
                                  │
                        x ∈ {-2, -1, 1, 2}
```

---

## Análisis del discriminante

Para la ecuación auxiliar $u^2 - 5u + 4 = 0$:

$$\Delta = (-5)^2 - 4(1)(4) = 25 - 16 = 9 > 0$$

Como $\Delta > 0$, hay dos valores distintos de $u$. Como ambos son positivos ($u = 1$ y $u = 4$), cada uno da dos valores de $x$, para un total de **4 soluciones reales**.

### Casos posibles en ecuaciones bicuadráticas

| Valores de $u$ | Soluciones para $x$ |
|----------------|---------------------|
| Ambos $u > 0$ | 4 soluciones reales |
| Un $u > 0$, un $u = 0$ | 3 soluciones reales |
| Un $u > 0$, un $u < 0$ | 2 soluciones reales |
| Ambos $u = 0$ (raíz doble) | 1 solución: $x = 0$ |
| Un $u = 0$, un $u < 0$ | 1 solución: $x = 0$ |
| Ambos $u < 0$ | 0 soluciones reales (4 complejas) |

---

## Errores comunes a evitar

⚠️ **Error 1:** Olvidar el signo $\pm$ al deshacer la [sustitución](../../../../glossary.md#sustitucion).

Si $u = 4$, entonces $x = \pm 2$, no solo $x = 2$.

⚠️ **Error 2:** Aceptar valores negativos de $u$.

Si la ecuación en $u$ diera $u = -3$, eso significaría $x^2 = -3$, que no tiene solución real.

⚠️ **Error 3:** Olvidar verificar que $u \geq 0$ antes de continuar.

---

## Respuesta Final

$$\boxed{x = -2, \quad x = -1, \quad x = 1, \quad x = 2}$$

**Conjunto solución:** $\{-2, -1, 1, 2\}$

**[Factorización](../../../../glossary.md#factorizacion) completa:**

$$x^4 - 5x^2 + 4 = (x + 2)(x + 1)(x - 1)(x - 2)$$

> 📚 Volver a: [FUN-03-Problemas](../../problems/FUN-03-Problemas.md)
