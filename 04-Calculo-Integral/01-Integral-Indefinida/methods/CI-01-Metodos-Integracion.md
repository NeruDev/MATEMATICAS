<!--
::METADATA::
type: method
topic_id: 01-integral-indefinida
file_id: CI-01-Metodos-Integracion
status: stable
audience: student
-->

# Métodos de Integración Directa

> **Objetivo:** Dominar las técnicas fundamentales de integración con explicaciones paso a paso, cálculos intermedios detallados y ejemplos clásicos.

---

## Método 1: Regla de la Potencia

### Cuándo Usar
- Integrando de la forma $x^n$ donde $n \neq -1$

### Fórmula
$$\int x^n \, dx = \frac{x^{n+1}}{n+1} + C$$

### Algoritmo de Resolución

| Paso | Acción | Verificación |
|------|--------|--------------|
| 1 | Identificar el exponente $n$ | ¿Es $n \neq -1$? |
| 2 | Sumar 1 al exponente | Nuevo exponente: $n+1$ |
| 3 | Dividir por el nuevo exponente | Factor: $\frac{1}{n+1}$ |
| 4 | Agregar la constante $C$ | Siempre al final |

### Ejemplo Detallado

**Problema:** Calcular $\int x^4 \, dx$

**Paso 1:** Identificamos $n = 4$ (claramente $4 \neq -1$ ✓)

**Paso 2:** Sumamos 1 al exponente:
$$n + 1 = 4 + 1 = 5$$

**Paso 3:** Dividimos por el nuevo exponente:
$$\frac{x^5}{5}$$

**Paso 4:** Agregamos la [constante de integración](../../../glossary.md#constante-de-integración):
$$\int x^4 \, dx = \frac{x^5}{5} + C$$

**Verificación:** Derivamos el resultado: $\frac{d}{dx}\left(\frac{x^5}{5}\right) = \frac{5x^4}{5} = x^4$ ✓

---

## Método 2: Potencias Fraccionarias y Negativas

### Cuándo Usar
- Radicales: $\sqrt{x}$, $\sqrt[n]{x^m}$
- Potencias en denominador: $\frac{1}{x^n}$

### Algoritmo de Resolución

| Paso | Acción | Conversión |
|------|--------|------------|
| 1 | Reescribir radicales como potencias fraccionarias | $\sqrt[n]{x^m} = x^{m/n}$ |
| 2 | Reescribir denominadores como potencias negativas | $\frac{1}{x^n} = x^{-n}$ |
| 3 | Aplicar la regla de la potencia | $\frac{x^{n+1}}{n+1} + C$ |
| 4 | Simplificar el resultado | Opcional: regresar a forma radical |

### Ejemplo 1: Radicales

**Problema:** Calcular $\int \sqrt[3]{x^2} \, dx$

**Paso 1:** Convertimos el radical a exponente fraccionario:
$$\sqrt[3]{x^2} = x^{2/3}$$

**Paso 2:** Aplicamos la regla de la potencia con $n = \frac{2}{3}$:
$$n + 1 = \frac{2}{3} + 1 = \frac{2}{3} + \frac{3}{3} = \frac{5}{3}$$

**Paso 3:** Formamos la fracción:
$$\frac{x^{5/3}}{5/3}$$

**Paso 4:** Simplificamos (dividir por fracción = multiplicar por recíproco):
$$\frac{x^{5/3}}{5/3} = x^{5/3} \cdot \frac{3}{5} = \frac{3x^{5/3}}{5}$$

**Resultado final:**
$$\int \sqrt[3]{x^2} \, dx = \frac{3x^{5/3}}{5} + C = \frac{3\sqrt[3]{x^5}}{5} + C$$

### Ejemplo 2: Potencias Negativas

**Problema:** Calcular $\int \frac{1}{x^4} \, dx$

**Paso 1:** Convertimos a potencia negativa:
$$\frac{1}{x^4} = x^{-4}$$

**Paso 2:** Aplicamos regla con $n = -4$:
$$n + 1 = -4 + 1 = -3$$

**Paso 3:** Formamos la fracción:
$$\frac{x^{-3}}{-3} = -\frac{x^{-3}}{3}$$

**Paso 4:** Reescribimos en forma estándar:
$$-\frac{x^{-3}}{3} = -\frac{1}{3x^3}$$

**Resultado final:**
$$\int \frac{1}{x^4} \, dx = -\frac{1}{3x^3} + C$$

---

## Método 3: Integral de $1/x$

### Cuándo Usar
- Exclusivamente cuando $n = -1$ (la regla de potencia falla aquí)
- Integrando de la forma $\frac{k}{x}$

### Fórmula
$$\int \frac{1}{x} \, dx = \ln\lvert x \rvert + C$$

### ¿Por qué valor absoluto?
La [función](../../../glossary.md#función) $\ln x$ solo está definida para $x > 0$, pero $\frac{1}{x}$ existe para todo $x \neq 0$. El valor absoluto permite que la [antiderivada](../../../glossary.md#antiderivada) funcione también para $x < 0$.

### Algoritmo de Resolución

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Verificar la forma $\frac{k}{x}$ | Extraer constante $k$ |
| 2 | Aplicar $\int \frac{1}{x}dx = \ln\lvert x\rvert$ | Usar valor absoluto |
| 3 | Multiplicar por la constante | $k \cdot \ln\lvert x\rvert$ |
| 4 | Agregar $+ C$ | Constante de integración |

### Ejemplo Detallado

**Problema:** Calcular $\int \frac{3}{x} \, dx$

**Paso 1:** Identificamos la constante $k = 3$:
$$\int \frac{3}{x} \, dx = 3 \int \frac{1}{x} \, dx$$

**Paso 2:** Aplicamos la fórmula del logaritmo:
$$= 3 \cdot \ln\lvert x \rvert$$

**Paso 3:** Agregamos la constante:
$$\int \frac{3}{x} \, dx = 3\ln\lvert x \rvert + C$$

**Verificación:** $\frac{d}{dx}(3\ln|x|) = 3 \cdot \frac{1}{x} = \frac{3}{x}$ ✓

---

## Método 4: Exponenciales

### Cuándo Usar
- Funciones $e^x$ ([base](../../../glossary.md#base) natural)
- Funciones $a^x$ (base cualquier positivo $a \neq 1$)

### Fórmulas
$$\int e^x \, dx = e^x + C$$
$$\int a^x \, dx = \frac{a^x}{\ln a} + C \quad (a > 0, a \neq 1)$$

### Algoritmo de Resolución

| Caso | Fórmula | Factor de ajuste |
|------|---------|------------------|
| Base $e$ | $\int e^x dx = e^x + C$ | Ninguno |
| Base $a$ | $\int a^x dx = \frac{a^x}{\ln a} + C$ | Dividir por $\ln a$ |

### Ejemplo Detallado

**Problema:** Calcular $\int 5^x \, dx$

**Paso 1:** Identificamos la base $a = 5$

**Paso 2:** Calculamos $\ln 5 \approx 1.609$ (valor exacto: $\ln 5$)

**Paso 3:** Aplicamos la fórmula:
$$\int 5^x \, dx = \frac{5^x}{\ln 5} + C$$

**Verificación:** Derivamos usando la regla $(a^x)' = a^x \ln a$:
$$\frac{d}{dx}\left(\frac{5^x}{\ln 5}\right) = \frac{5^x \cdot \ln 5}{\ln 5} = 5^x \checkmark$$

---

## Método 5: Funciones Trigonométricas Básicas

### Cuándo Usar
- Funciones trigonométricas elementales

### Tabla de Fórmulas con Verificación

| Integral | Resultado | Verificación ([derivada](../../../glossary.md#derivada)) |
|----------|-----------|------------------------|
| $\int \sin x \, dx$ | $-\cos x + C$ | $(-\cos x)' = \sin x$ ✓ |
| $\int \cos x \, dx$ | $\sin x + C$ | $(\sin x)' = \cos x$ ✓ |
| $\int \sec^2 x \, dx$ | $\tan x + C$ | $(\tan x)' = \sec^2 x$ ✓ |
| $\int \csc^2 x \, dx$ | $-\cot x + C$ | $(-\cot x)' = \csc^2 x$ ✓ |

### Algoritmo de Resolución

| Paso | Acción |
|------|--------|
| 1 | Identificar la función trigonométrica |
| 2 | Extraer constantes multiplicativas |
| 3 | Consultar la tabla de antiderivadas |
| 4 | Multiplicar por las constantes y agregar $C$ |

### Ejemplo Detallado

**Problema:** Calcular $\int (3\sin x + 2\cos x) \, dx$

**Paso 1:** Separamos en suma de integrales:
$$\int (3\sin x + 2\cos x) \, dx = \int 3\sin x \, dx + \int 2\cos x \, dx$$

**Paso 2:** Extraemos las constantes:
$$= 3\int \sin x \, dx + 2\int \cos x \, dx$$

**Paso 3:** Aplicamos las fórmulas de la tabla:
$$= 3(-\cos x) + 2(\sin x) + C$$

**Paso 4:** Simplificamos:
$$\int (3\sin x + 2\cos x) \, dx = -3\cos x + 2\sin x + C$$

---

## Método 6: Productos Trigonométricos Especiales

### Cuándo Usar
- Producto $\sec x \tan x$ (derivada de secante)
- Producto $\csc x \cot x$ (derivada de cosecante con signo)

### Fórmulas
$$\int \sec x \tan x \, dx = \sec x + C$$
$$\int \csc x \cot x \, dx = -\csc x + C$$

### Memoria Visual

| Producto | Antiderivada | Regla mnemotécnica |
|----------|--------------|-------------------|
| $\sec x \tan x$ | $\sec x$ | "sec con tan da sec" |
| $\csc x \cot x$ | $-\csc x$ | "csc con cot da -csc" |

### Ejemplo Detallado

**Problema:** Calcular $\int 4\sec x \tan x \, dx$

**Paso 1:** Extraemos la constante:
$$\int 4\sec x \tan x \, dx = 4\int \sec x \tan x \, dx$$

**Paso 2:** Reconocemos el patrón $\sec x \tan x$

**Paso 3:** Aplicamos la fórmula:
$$= 4 \cdot \sec x + C$$

**Resultado:**
$$\int 4\sec x \tan x \, dx = 4\sec x + C$$

---

## Método 7: Integrales que Producen Arcoseno

### Cuándo Usar
- Forma $\frac{1}{\sqrt{a^2 - x^2}}$ donde $|x| < a$

### Fórmula
$$\int \frac{1}{\sqrt{a^2 - x^2}} \, dx = \arcsin\frac{x}{a} + C$$

### Algoritmo de Resolución

| Paso | Acción | Pregunta clave |
|------|--------|----------------|
| 1 | Identificar la forma $\sqrt{a^2 - x^2}$ | ¿Hay resta bajo raíz? |
| 2 | Determinar el valor de $a$ | $a^2 = $ constante |
| 3 | Aplicar la fórmula | Argumento: $\frac{x}{a}$ |

### Ejemplo Detallado

**Problema:** Calcular $\int \frac{1}{\sqrt{9 - x^2}} \, dx$

**Paso 1:** Identificamos la forma $\sqrt{a^2 - x^2}$:
$$\sqrt{9 - x^2} = \sqrt{3^2 - x^2}$$

**Paso 2:** Determinamos $a = 3$

**Paso 3:** Aplicamos la fórmula:
$$\int \frac{1}{\sqrt{9 - x^2}} \, dx = \arcsin\frac{x}{3} + C$$

**Verificación:** 
$$\frac{d}{dx}\left(\arcsin\frac{x}{3}\right) = \frac{1}{\sqrt{1 - (x/3)^2}} \cdot \frac{1}{3} = \frac{1}{3\sqrt{1 - x^2/9}} = \frac{1}{\sqrt{9 - x^2}} \checkmark$$

---

## Método 8: Integrales que Producen Arcotangente

### Cuándo Usar
- Forma $\frac{1}{a^2 + x^2}$ (suma de cuadrados en denominador)

### Fórmula
$$\int \frac{1}{a^2 + x^2} \, dx = \frac{1}{a}\arctan\frac{x}{a} + C$$

### Algoritmo de Resolución

| Paso | Acción | Cálculo |
|------|--------|---------|
| 1 | Identificar $a^2 + x^2$ | Constante + variable² |
| 2 | Obtener $a = \sqrt{\text{constante}}$ | $a$ debe ser positivo |
| 3 | Factor: $\frac{1}{a}$ | Coeficiente exterior |
| 4 | Argumento: $\frac{x}{a}$ | Dentro del arctan |

### Ejemplo Detallado

**Problema:** Calcular $\int \frac{1}{4 + x^2} \, dx$

**Paso 1:** Identificamos la forma $a^2 + x^2$:
$$4 + x^2 = 2^2 + x^2$$

**Paso 2:** Determinamos $a = 2$

**Paso 3:** Calculamos el factor $\frac{1}{a} = \frac{1}{2}$

**Paso 4:** Aplicamos la fórmula:
$$\int \frac{1}{4 + x^2} \, dx = \frac{1}{2}\arctan\frac{x}{2} + C$$

**Verificación:**
$$\frac{d}{dx}\left(\frac{1}{2}\arctan\frac{x}{2}\right) = \frac{1}{2} \cdot \frac{1}{1 + (x/2)^2} \cdot \frac{1}{2} = \frac{1}{4 + x^2} \checkmark$$

---

## Método 9: Combinación Lineal

### Cuándo Usar
- Suma o diferencia de funciones integrables
- Multiplicación por constantes

### Propiedades Fundamentales
$$\int [f(x) + g(x)] \, dx = \int f(x) \, dx + \int g(x) \, dx$$
$$\int k \cdot f(x) \, dx = k \int f(x) \, dx$$

### Algoritmo de Resolución

| Paso | Acción | Resultado |
|------|--------|-----------|
| 1 | Separar la integral en suma/diferencia | Una integral por término |
| 2 | Extraer constantes de cada integral | Constante fuera del símbolo |
| 3 | Integrar cada término por separado | Aplicar métodos básicos |
| 4 | Combinar resultados | Una sola constante $C$ al final |

### Ejemplo Detallado

**Problema:** Calcular $\int (x^3 - 4x + e^x) \, dx$

**Paso 1:** Separamos en tres integrales:
$$= \int x^3 \, dx - \int 4x \, dx + \int e^x \, dx$$

**Paso 2:** Extraemos constantes:
$$= \int x^3 \, dx - 4\int x \, dx + \int e^x \, dx$$

**Paso 3:** Integramos cada término:
- $\int x^3 \, dx = \frac{x^4}{4}$
- $\int x \, dx = \frac{x^2}{2}$
- $\int e^x \, dx = e^x$

**Paso 4:** Combinamos:
$$= \frac{x^4}{4} - 4 \cdot \frac{x^2}{2} + e^x + C = \frac{x^4}{4} - 2x^2 + e^x + C$$

---

## Método 10: Simplificación Algebraica Previa

### Cuándo Usar
- Cuando el integrando se puede simplificar algebraicamente
- Fracciones que se pueden dividir
- Expresiones que se pueden expandir

### Algoritmo de Resolución

| Paso | Acción | Técnicas comunes |
|------|--------|------------------|
| 1 | Analizar si se puede simplificar | ¿División? ¿Expansión? ¿[Factorización](../../../glossary.md#factorización)? |
| 2 | Realizar la simplificación algebraica | Manipulación de fracciones |
| 3 | Separar en términos integrables | Suma de funciones simples |
| 4 | Aplicar métodos básicos | Reglas anteriores |

### Ejemplo 1: División de Polinomios

**Problema:** Calcular $\int \frac{x^3 + 2x^2 - x}{x} \, dx$

**Paso 1:** Dividimos cada término por $x$:
$$\frac{x^3 + 2x^2 - x}{x} = \frac{x^3}{x} + \frac{2x^2}{x} - \frac{x}{x} = x^2 + 2x - 1$$

**Paso 2:** Integramos el resultado simplificado:
$$\int (x^2 + 2x - 1) \, dx = \frac{x^3}{3} + x^2 - x + C$$

### Ejemplo 2: Expansión de Productos

**Problema:** Calcular $\int (x + 1)^2 \, dx$

**Paso 1:** Expandimos el cuadrado:
$$(x + 1)^2 = x^2 + 2x + 1$$

**Paso 2:** Integramos término a término:
$$\int (x^2 + 2x + 1) \, dx = \frac{x^3}{3} + x^2 + x + C$$

### Ejemplo 3: Racionalización

**Problema:** Calcular $\int \frac{1}{\sqrt{x}(1 + \sqrt{x})} \, dx$

**Paso 1:** Sustituimos $u = \sqrt{x}$, entonces $x = u^2$ y $dx = 2u \, du$:
$$\int \frac{1}{u(1 + u)} \cdot 2u \, du = 2\int \frac{1}{1 + u} \, du$$

**Paso 2:** Integramos:
$$= 2\ln|1 + u| + C = 2\ln|1 + \sqrt{x}| + C$$

### Ejemplo
$$\int \frac{x^3 + 2x}{x} \, dx = \int (x^2 + 2) \, dx = \frac{x^3}{3} + 2x + C$$

$$\int (x + 1)^2 \, dx = \int (x^2 + 2x + 1) \, dx = \frac{x^3}{3} + x^2 + x + C$$
