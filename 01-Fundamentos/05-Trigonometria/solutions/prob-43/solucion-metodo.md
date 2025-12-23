<!--
::METADATA::
type: solution
topic_id: fun-05-trigonometria
file_id: prob-43-solucion
problem_ref: Prob-43
status: stable
audience: student
-->

# Solución: Demostración tan θ + cot θ = sec θ csc θ

## Problema
Demuestra: $\tan\theta + \cot\theta = \sec\theta\csc\theta$

---

## Método 1: Convertir todo a seno y coseno

### Paso 1: Expresar el lado izquierdo en términos de sin y cos
$$\tan\theta + \cot\theta = \frac{\sin\theta}{\cos\theta} + \frac{\cos\theta}{\sin\theta}$$

### Paso 2: Encontrar denominador común
$$= \frac{\sin\theta \cdot \sin\theta + \cos\theta \cdot \cos\theta}{\cos\theta \cdot \sin\theta}$$

$$= \frac{\sin^2\theta + \cos^2\theta}{\cos\theta \sin\theta}$$

### Paso 3: Aplicar identidad pitagórica
$$= \frac{1}{\cos\theta \sin\theta}$$

### Paso 4: Separar la fracción
$$= \frac{1}{\cos\theta} \cdot \frac{1}{\sin\theta}$$

### Paso 5: Reconocer las funciones recíprocas
$$= \sec\theta \cdot \csc\theta$$

---

## Método 2: Partir del lado derecho

### Paso 1: Expresar sec θ csc θ en términos de sin y cos
$$\sec\theta\csc\theta = \frac{1}{\cos\theta} \cdot \frac{1}{\sin\theta} = \frac{1}{\sin\theta\cos\theta}$$

### Paso 2: Multiplicar numerador y denominador por (sin²θ + cos²θ) = 1
$$= \frac{\sin^2\theta + \cos^2\theta}{\sin\theta\cos\theta}$$

### Paso 3: Separar la fracción
$$= \frac{\sin^2\theta}{\sin\theta\cos\theta} + \frac{\cos^2\theta}{\sin\theta\cos\theta}$$

### Paso 4: Simplificar cada término
$$= \frac{\sin\theta}{\cos\theta} + \frac{\cos\theta}{\sin\theta}$$

### Paso 5: Reconocer las funciones
$$= \tan\theta + \cot\theta$$

---

## Conclusión
$$\boxed{\tan\theta + \cot\theta = \sec\theta\csc\theta \quad \blacksquare}$$

---

## Verificación: θ = 45°

**Lado izquierdo:**
$$\tan 45° + \cot 45° = 1 + 1 = 2$$

**Lado derecho:**
$$\sec 45° \cdot \csc 45° = \sqrt{2} \cdot \sqrt{2} = 2$$

$$2 = 2 \checkmark$$

---

## Verificación: θ = 30°

**Lado izquierdo:**
$$\tan 30° + \cot 30° = \frac{\sqrt{3}}{3} + \sqrt{3} = \frac{\sqrt{3} + 3\sqrt{3}}{3} = \frac{4\sqrt{3}}{3}$$

**Lado derecho:**
$$\sec 30° \cdot \csc 30° = \frac{2\sqrt{3}}{3} \cdot 2 = \frac{4\sqrt{3}}{3}$$

$$\frac{4\sqrt{3}}{3} = \frac{4\sqrt{3}}{3} \checkmark$$

---

## Restricciones
La identidad es válida para todo $\theta$ tal que:
- $\sin\theta \neq 0$ (es decir, $\theta \neq n\pi$)
- $\cos\theta \neq 0$ (es decir, $\theta \neq \frac{\pi}{2} + n\pi$)

Esto excluye los ángulos: $0°, 90°, 180°, 270°, ...$
