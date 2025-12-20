# Teoría — Funciones de varias variables

Las funciones de varias variables modelan fenómenos donde el resultado depende de múltiples factores: temperatura en el espacio, presión atmosférica, superficies económicas, etc.

---

## 4.1 Definición de función de varias variables

Una **función de varias variables** es una función $f: D \subseteq \mathbb{R}^n \to \mathbb{R}$, donde $D$ es el dominio.

### Caso de dos variables
$$f: D \subseteq \mathbb{R}^2 \to \mathbb{R}, \quad z = f(x, y)$$

**Dominio**: Conjunto de pares $(x, y)$ para los cuales $f$ está definida.

### Caso de tres variables
$$f: D \subseteq \mathbb{R}^3 \to \mathbb{R}, \quad w = f(x, y, z)$$

### Ejemplos de dominios

| Función | Dominio | Restricción |
|---------|---------|-------------|
| $f(x,y) = \sqrt{x+y}$ | $\{(x,y) : x + y \geq 0\}$ | Raíz de no negativo |
| $f(x,y) = \ln(xy)$ | $\{(x,y) : xy > 0\}$ | Logaritmo de positivo |
| $f(x,y) = \frac{1}{x^2-y^2}$ | $\{(x,y) : x \neq \pm y\}$ | Denominador no cero |
| $f(x,y,z) = \frac{1}{\sqrt{1-x^2-y^2-z^2}}$ | Esfera abierta unitaria | Interior de la esfera |

---

## 4.2 Gráficas, curvas y superficies de nivel

### Gráfica de $z = f(x, y)$
Es una **superficie en $\mathbb{R}^3$**: el conjunto de puntos $(x, y, f(x,y))$.

### Curvas de nivel
Las **curvas de nivel** son conjuntos donde $f(x, y) = k$ (constante).

$$C_k = \{(x, y) : f(x, y) = k\}$$

**Interpretación**: Son como las líneas de un mapa topográfico.

| Función | Curvas de nivel | Forma |
|---------|----------------|-------|
| $f(x,y) = x^2 + y^2$ | $x^2 + y^2 = k$ | Circunferencias concéntricas |
| $f(x,y) = x + y$ | $x + y = k$ | Rectas paralelas |
| $f(x,y) = xy$ | $xy = k$ | Hipérbolas |
| $f(x,y) = x^2 - y^2$ | $x^2 - y^2 = k$ | Hipérbolas (silla) |

### Superficies de nivel (3 variables)
Para $w = f(x, y, z)$, las **superficies de nivel** son:
$$S_k = \{(x, y, z) : f(x, y, z) = k\}$$

**Ejemplo**: $f(x,y,z) = x^2 + y^2 + z^2$. Las superficies de nivel son esferas concéntricas.

---

## 4.3 Límite y continuidad

### Límite
$$\lim_{(x,y) \to (a,b)} f(x, y) = L$$

El límite existe si $f(x,y) \to L$ cuando $(x,y) \to (a,b)$ por **cualquier camino**.

### Criterio de inexistencia
Si dos caminos diferentes dan límites distintos, el límite **no existe**.

**Caminos comunes para probar**:
- $y = 0$ (eje $x$)
- $x = 0$ (eje $y$)
- $y = x$ (diagonal)
- $y = mx$ (rectas por el origen)
- $y = x^2$ (parábola)

### Continuidad
$f$ es **continua en $(a, b)$** si:
1. $f(a, b)$ está definida.
2. $\lim_{(x,y) \to (a,b)} f(x, y)$ existe.
3. $\lim_{(x,y) \to (a,b)} f(x, y) = f(a, b)$.

**Funciones continuas**: Polinomios, racionales (donde el denominador no es cero), composiciones de continuas.

---

## 4.4 Derivadas parciales

### Definición
La **derivada parcial** de $f$ respecto a $x$ es:

$$f_x(x, y) = \frac{\partial f}{\partial x} = \lim_{h \to 0} \frac{f(x+h, y) - f(x, y)}{h}$$

Análogamente para $f_y$:

$$f_y(x, y) = \frac{\partial f}{\partial y} = \lim_{h \to 0} \frac{f(x, y+h) - f(x, y)}{h}$$

### Interpretación geométrica

| Derivada | Interpretación |
|----------|---------------|
| $f_x(a,b)$ | Pendiente de la curva $z = f(x, b)$ en $x = a$ |
| $f_y(a,b)$ | Pendiente de la curva $z = f(a, y)$ en $y = b$ |

### Notaciones equivalentes

$$\frac{\partial f}{\partial x} = f_x = \partial_x f = D_x f = D_1 f$$

### Regla práctica
Para calcular $f_x$: **deriva respecto a $x$ tratando $y$ como constante**.

---

## 4.5 Incrementos y diferenciales

### Incremento
$$\Delta f = f(x + \Delta x, y + \Delta y) - f(x, y)$$

### Diferencial total
$$df = f_x \, dx + f_y \, dy$$

Para tres variables:
$$df = f_x \, dx + f_y \, dy + f_z \, dz$$

### Aproximación lineal
Para cambios pequeños $\Delta x, \Delta y$:

$$f(x + \Delta x, y + \Delta y) \approx f(x, y) + f_x \, \Delta x + f_y \, \Delta y$$

### Plano tangente
La ecuación del **plano tangente** a $z = f(x, y)$ en $(a, b, f(a,b))$ es:

$$z - f(a,b) = f_x(a,b)(x - a) + f_y(a,b)(y - b)$$

---

## 4.6 Regla de la cadena y derivación implícita

### Caso 1: Una variable independiente
Si $z = f(x, y)$ con $x = x(t)$, $y = y(t)$:

$$\frac{dz}{dt} = \frac{\partial f}{\partial x}\frac{dx}{dt} + \frac{\partial f}{\partial y}\frac{dy}{dt} = f_x \, x'(t) + f_y \, y'(t)$$

### Caso 2: Dos variables independientes
Si $z = f(x, y)$ con $x = x(s, t)$, $y = y(s, t)$:

$$\frac{\partial z}{\partial s} = f_x \frac{\partial x}{\partial s} + f_y \frac{\partial y}{\partial s}$$

$$\frac{\partial z}{\partial t} = f_x \frac{\partial x}{\partial t} + f_y \frac{\partial y}{\partial t}$$

### Derivación implícita
Si $F(x, y) = 0$ define $y$ implícitamente como función de $x$:

$$\frac{dy}{dx} = -\frac{F_x}{F_y} \quad (\text{si } F_y \neq 0)$$

Para $F(x, y, z) = 0$:

$$\frac{\partial z}{\partial x} = -\frac{F_x}{F_z}, \quad \frac{\partial z}{\partial y} = -\frac{F_y}{F_z}$$

---

## 4.7 Derivadas de orden superior

### Segundas derivadas parciales
$$f_{xx} = \frac{\partial^2 f}{\partial x^2}, \quad f_{yy} = \frac{\partial^2 f}{\partial y^2}, \quad f_{xy} = \frac{\partial^2 f}{\partial y \partial x}, \quad f_{yx} = \frac{\partial^2 f}{\partial x \partial y}$$

### Teorema de Clairaut (Schwarz)
Si $f_{xy}$ y $f_{yx}$ son **continuas** en una región, entonces:

$$f_{xy} = f_{yx}$$

**Importancia**: El orden de derivación no importa para funciones "suaves".

### Laplaciano
$$\nabla^2 f = \Delta f = f_{xx} + f_{yy} \quad \text{(2D)}$$
$$\nabla^2 f = f_{xx} + f_{yy} + f_{zz} \quad \text{(3D)}$$

El Laplaciano aparece en ecuaciones de calor, ondas y potencial.

---

## 4.8 Derivada direccional y gradiente

### Gradiente
El **gradiente** de $f$ es el vector de derivadas parciales:

$$\nabla f = \left\langle \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y} \right\rangle = f_x \, \mathbf{i} + f_y \, \mathbf{j}$$

En 3D:
$$\nabla f = \langle f_x, f_y, f_z \rangle$$

### Propiedades del gradiente

| Propiedad | Significado |
|-----------|-------------|
| $\nabla f$ apunta en la dirección de **máximo crecimiento** | Subir la montaña más rápido |
| $\|\nabla f\|$ es la **tasa máxima de cambio** | Qué tan empinado es |
| $\nabla f$ es **perpendicular** a las curvas de nivel | Normal a la curva $f = k$ |

### Derivada direccional
La **derivada direccional** de $f$ en la dirección del vector unitario $\mathbf{u}$ es:

$$D_{\mathbf{u}}f = \nabla f \cdot \mathbf{u} = f_x \cos\theta + f_y \sin\theta$$

**Interpretación**: Tasa de cambio de $f$ en la dirección $\mathbf{u}$.

### Casos especiales

| Dirección | Resultado |
|-----------|-----------|
| $\mathbf{u}$ paralelo a $\nabla f$ | Máximo: $D_{\mathbf{u}}f = \|\nabla f\|$ |
| $\mathbf{u}$ opuesto a $\nabla f$ | Mínimo: $D_{\mathbf{u}}f = -\|\nabla f\|$ |
| $\mathbf{u}$ perpendicular a $\nabla f$ | Cero: $D_{\mathbf{u}}f = 0$ (tangente a curva de nivel) |

---

## 4.9 Extremos de funciones de dos variables

### Puntos críticos
Un **punto crítico** es donde $\nabla f = \mathbf{0}$, es decir:

$$f_x(a, b) = 0 \quad \text{y} \quad f_y(a, b) = 0$$

### Criterio de la segunda derivada (Test del Hessiano)

Calcula el **discriminante** o **Hessiano**:

$$D = f_{xx}(a,b) \cdot f_{yy}(a,b) - [f_{xy}(a,b)]^2$$

| Condición | Conclusión |
|-----------|------------|
| $D > 0$ y $f_{xx} > 0$ | **Mínimo local** |
| $D > 0$ y $f_{xx} < 0$ | **Máximo local** |
| $D < 0$ | **Punto silla** |
| $D = 0$ | **Inconcluso** (requiere más análisis) |

### Matriz Hessiana
$$H = \begin{pmatrix} f_{xx} & f_{xy} \\ f_{yx} & f_{yy} \end{pmatrix}$$

El discriminante $D = \det(H)$.

### Extremos absolutos en regiones cerradas
Para encontrar el **máximo y mínimo absoluto** de $f$ en una región cerrada $R$:

1. Encuentra todos los puntos críticos **interiores** de $R$.
2. Encuentra los extremos en la **frontera** de $R$.
3. Compara los valores de $f$ en todos los candidatos.

---

## Resumen de fórmulas clave

| Concepto | Fórmula |
|----------|---------|
| Derivada parcial | $f_x = \lim_{h \to 0} \frac{f(x+h,y) - f(x,y)}{h}$ |
| Diferencial total | $df = f_x \, dx + f_y \, dy$ |
| Plano tangente | $z - z_0 = f_x(x-x_0) + f_y(y-y_0)$ |
| Gradiente | $\nabla f = \langle f_x, f_y \rangle$ |
| Derivada direccional | $D_{\mathbf{u}}f = \nabla f \cdot \mathbf{u}$ |
| Regla de la cadena | $\frac{dz}{dt} = f_x x'(t) + f_y y'(t)$ |
| Derivación implícita | $\frac{dy}{dx} = -\frac{F_x}{F_y}$ |
| Discriminante | $D = f_{xx} f_{yy} - f_{xy}^2$ |
| Laplaciano | $\nabla^2 f = f_{xx} + f_{yy}$ |
