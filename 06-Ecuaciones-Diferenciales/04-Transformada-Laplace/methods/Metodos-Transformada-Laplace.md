<!--
content_type: methods
topic: Transformada de Laplace
---
-->

# Métodos: Transformada de Laplace

---

## Método 1: Calcular Transformada Directamente

### Pasos

1. **Identificar** la función $f(t)$

2. **Buscar en tabla** de transformadas básicas

3. **Aplicar propiedades** si es necesario:
   - Linealidad: $\mathcal{L}\{af + bg\} = aF + bG$
   - Traslación en $s$: $\mathcal{L}\{e^{at}f\} = F(s-a)$

### Ejemplo

**Encontrar:** $\mathcal{L}\{3t^2 - 5e^{-2t} + 4\sin 3t\}$

**Paso 1-2:** De la tabla:
- $\mathcal{L}\{t^2\} = \frac{2!}{s^3} = \frac{2}{s^3}$
- $\mathcal{L}\{e^{-2t}\} = \frac{1}{s+2}$
- $\mathcal{L}\{\sin 3t\} = \frac{3}{s^2+9}$

**Paso 3:** Por linealidad:
$$\mathcal{L} = 3 \cdot \frac{2}{s^3} - 5 \cdot \frac{1}{s+2} + 4 \cdot \frac{3}{s^2+9}$$

$$= \frac{6}{s^3} - \frac{5}{s+2} + \frac{12}{s^2+9}$$

---

## Método 2: Transformada con Primera Traslación

**Para:** $\mathcal{L}\{e^{at}f(t)\}$

### Pasos

1. **Encontrar** $\mathcal{L}\{f(t)\} = F(s)$

2. **Reemplazar** $s$ por $s - a$ en $F(s)$

3. **Resultado:** $\mathcal{L}\{e^{at}f(t)\} = F(s-a)$

### Ejemplo

**Encontrar:** $\mathcal{L}\{e^{2t}\cos 5t\}$

**Paso 1:** $\mathcal{L}\{\cos 5t\} = \frac{s}{s^2 + 25}$

**Paso 2-3:** Reemplazar $s \to s-2$:

$$\mathcal{L}\{e^{2t}\cos 5t\} = \frac{s-2}{(s-2)^2 + 25}$$

---

## Método 3: Transformada Inversa por Fracciones Parciales

### Pasos

1. **Verificar** que el grado del numerador < grado del denominador

2. **Factorizar** el denominador

3. **Escribir** la descomposición en fracciones parciales

4. **Encontrar** los coeficientes

5. **Invertir** cada fracción usando la tabla

### Tipos de Factores

| Factor en $Q(s)$ | Forma de fracciones parciales |
|------------------|-------------------------------|
| $(s-a)$ | $\frac{A}{s-a}$ |
| $(s-a)^n$ | $\frac{A_1}{s-a} + \frac{A_2}{(s-a)^2} + \cdots + \frac{A_n}{(s-a)^n}$ |
| $(s^2+bs+c)$ | $\frac{As+B}{s^2+bs+c}$ |

### Ejemplo Paso a Paso

**Encontrar:** $\mathcal{L}^{-1}\left\{\frac{2s+1}{(s-1)(s+2)^2}\right\}$

**Paso 1:** Grado 1 < Grado 3 ✓

**Paso 2:** Ya factorizado

**Paso 3:**
$$\frac{2s+1}{(s-1)(s+2)^2} = \frac{A}{s-1} + \frac{B}{s+2} + \frac{C}{(s+2)^2}$$

**Paso 4:**
$2s+1 = A(s+2)^2 + B(s-1)(s+2) + C(s-1)$

$s = 1$: $3 = 9A \Rightarrow A = \frac{1}{3}$

$s = -2$: $-3 = -3C \Rightarrow C = 1$

$s = 0$: $1 = 4A - 2B - C = \frac{4}{3} - 2B - 1$

$2B = \frac{1}{3} \Rightarrow B = \frac{1}{6}$

**Paso 5:**
$$\mathcal{L}^{-1} = \frac{1}{3}e^t + \frac{1}{6}e^{-2t} + te^{-2t}$$

---

## Método 4: Resolver PVI con Laplace

**Ecuación:** $ay'' + by' + cy = f(t)$, $y(0) = y_0$, $y'(0) = y_0'$

### Pasos

1. **Aplicar $\mathcal{L}$** a toda la ecuación

2. **Sustituir** usando propiedades de derivadas:
   - $\mathcal{L}\{y'\} = sY - y_0$
   - $\mathcal{L}\{y''\} = s^2Y - sy_0 - y_0'$

3. **Despejar** $Y(s)$

4. **Simplificar** y aplicar fracciones parciales

5. **Aplicar** $\mathcal{L}^{-1}$ para obtener $y(t)$

### Ejemplo Paso a Paso

**Resolver:** $y'' + 3y' + 2y = e^{-t}$, $y(0) = 0$, $y'(0) = 1$

**Paso 1:** $\mathcal{L}\{y''\} + 3\mathcal{L}\{y'\} + 2\mathcal{L}\{y\} = \mathcal{L}\{e^{-t}\}$

**Paso 2:**
$[s^2Y - 0 - 1] + 3[sY - 0] + 2Y = \frac{1}{s+1}$

$s^2Y + 3sY + 2Y - 1 = \frac{1}{s+1}$

**Paso 3:**
$Y(s^2 + 3s + 2) = \frac{1}{s+1} + 1 = \frac{s+2}{s+1}$

$Y = \frac{s+2}{(s+1)(s^2+3s+2)} = \frac{s+2}{(s+1)(s+1)(s+2)} = \frac{1}{(s+1)^2}$

**Paso 4:** Ya simplificado

**Paso 5:**
$\mathcal{L}^{-1}\left\{\frac{1}{(s+1)^2}\right\} = te^{-t}$

**Solución:** $y(t) = te^{-t}$

---

## Método 5: Manejar Funciones Escalón

**Para:** $f(t) = g(t)u(t-a)$

### Pasos

1. **Escribir** $g(t)$ en términos de $(t-a)$:
   - Sea $g(t) = h(t-a)$ donde $h(\tau) = g(\tau + a)$

2. **Aplicar** segunda traslación:
   $$\mathcal{L}\{h(t-a)u(t-a)\} = e^{-as}H(s)$$

3. **Simplificar**

### Ejemplo

**Encontrar:** $\mathcal{L}\{t^2 u(t-2)\}$

**Paso 1:** $t^2 = [(t-2) + 2]^2 = (t-2)^2 + 4(t-2) + 4$

Sea $h(\tau) = \tau^2 + 4\tau + 4$

**Paso 2:**
$\mathcal{L}\{h(t-2)u(t-2)\} = e^{-2s}\mathcal{L}\{t^2 + 4t + 4\}$

$= e^{-2s}\left(\frac{2}{s^3} + \frac{4}{s^2} + \frac{4}{s}\right)$

---

## Método 6: Inversión con Completar el Cuadrado

**Para:** $F(s) = \frac{As + B}{s^2 + bs + c}$

### Pasos

1. **Completar el cuadrado** en el denominador:
   $$s^2 + bs + c = (s + \frac{b}{2})^2 + (c - \frac{b^2}{4})$$

2. **Ajustar el numerador** para que tenga la forma $(s + \frac{b}{2})$ + constante

3. **Separar** en dos fracciones

4. **Identificar** formas estándar (coseno y seno amortiguados)

### Ejemplo

**Encontrar:** $\mathcal{L}^{-1}\left\{\frac{2s + 3}{s^2 + 4s + 13}\right\}$

**Paso 1:**
$s^2 + 4s + 13 = (s+2)^2 + 9$

**Paso 2:**
$2s + 3 = 2(s+2) + (3-4) = 2(s+2) - 1$

**Paso 3:**
$$\frac{2(s+2) - 1}{(s+2)^2 + 9} = \frac{2(s+2)}{(s+2)^2 + 9} - \frac{1}{(s+2)^2 + 9}$$

**Paso 4:**
$= 2e^{-2t}\cos 3t - \frac{1}{3}e^{-2t}\sin 3t$

**Solución:** $y(t) = e^{-2t}\left(2\cos 3t - \frac{1}{3}\sin 3t\right)$

---

## Método 7: Usar Convolución para Inversa

**Para:** $F(s) = G(s) \cdot H(s)$

### Pasos

1. **Identificar** $G(s)$ y $H(s)$

2. **Encontrar** $g(t) = \mathcal{L}^{-1}\{G\}$ y $h(t) = \mathcal{L}^{-1}\{H\}$

3. **Calcular** la convolución:
   $$f(t) = (g * h)(t) = \int_0^t g(\tau)h(t-\tau)\,d\tau$$

### Ejemplo

**Encontrar:** $\mathcal{L}^{-1}\left\{\frac{1}{s(s^2+1)}\right\}$

**Paso 1:** $G(s) = \frac{1}{s}$, $H(s) = \frac{1}{s^2+1}$

**Paso 2:** $g(t) = 1$, $h(t) = \sin t$

**Paso 3:**
$$f(t) = \int_0^t 1 \cdot \sin(t-\tau)\,d\tau = [-\cos(t-\tau)]_0^t = 1 - \cos t$$

---

## Resumen: Diagrama de Decisión

```
┌─────────────────────────────────────────────┐
│        ¿Qué tipo de problema?               │
└─────────────────────────────────────────────┘
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
   Calcular 𝓛   Calcular 𝓛⁻¹   Resolver PVI
        │           │           │
        ▼           ▼           ▼
   ¿e^(at)f?    ¿Racional?     Aplicar 𝓛
        │           │           │
   SÍ → Traslación  SÍ → Fracc. Sustituir
   NO → Tabla       parciales   derivadas
                    │           │
              ¿Cuadrático       Despejar Y(s)
              irreducible?      │
                    │           Fracciones
              SÍ → Completar    parciales
              cuadrado          │
                    │           Aplicar 𝓛⁻¹
              Identificar
              cos/sin amortiguado
```
