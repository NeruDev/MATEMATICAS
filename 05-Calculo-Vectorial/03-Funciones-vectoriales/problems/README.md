# Problemas — Funciones vectoriales

---

## Nivel Básico

### Límites y continuidad
1) Calcula $\lim_{t \to 0} \mathbf{r}(t)$ donde $\mathbf{r}(t) = \langle t^2, \sin t, e^t \rangle$.

2) Determina si $\mathbf{r}(t) = \langle \frac{\sin t}{t}, t^2, \cos t \rangle$ es continua en $t = 0$.

3) Halla $\lim_{t \to 1} \langle \ln t, t^3 - 1, \sqrt{t} \rangle$.

### Derivadas
4) Encuentra $\mathbf{r}'(t)$ si $\mathbf{r}(t) = \langle 3t, t^2, \ln(1+t) \rangle$.

5) Calcula la velocidad y rapidez en $t = 2$ para $\mathbf{r}(t) = \langle t^2, 4t, t^3 \rangle$.

6) Si $\mathbf{r}(t) = \langle \cos 2t, \sin 2t, 3t \rangle$, encuentra $\mathbf{r}'(t)$ y $\mathbf{r}''(t)$.

### Integrales
7) Calcula $\int \langle 2t, e^t, \cos t \rangle \, dt$.

8) Evalúa $\int_0^1 \langle 3t^2, 2t, 1 \rangle \, dt$.

9) Si $\mathbf{v}(t) = \langle 1, 2t, 3t^2 \rangle$ y $\mathbf{r}(0) = \langle 0, 0, 0 \rangle$, encuentra $\mathbf{r}(t)$.

---

## Nivel Intermedio

### Longitud de arco
10) Encuentra la longitud de la curva $\mathbf{r}(t) = \langle \cos t, \sin t, t \rangle$ para $t \in [0, \pi]$.

11) Calcula la longitud de $\mathbf{r}(t) = \langle t, t^2, \frac{2}{3}t^3 \rangle$ en $[0, 1]$.

12) Halla la longitud de la hélice $\mathbf{r}(t) = \langle 3\cos t, 3\sin t, 4t \rangle$ en $[0, 2\pi]$.

### Vector tangente unitario
13) Encuentra $\mathbf{T}(t)$ para $\mathbf{r}(t) = \langle t, t^2, 0 \rangle$.

14) Calcula $\mathbf{T}$ en $t = 0$ para $\mathbf{r}(t) = \langle e^t, e^{-t}, \sqrt{2}t \rangle$.

15) Si $\mathbf{r}(t) = \langle \sin t, \cos t, t \rangle$, halla $\mathbf{T}(\pi/2)$.

### Curvatura
16) Calcula la curvatura de $\mathbf{r}(t) = \langle t, t^2, 0 \rangle$ en $t = 1$.

17) Encuentra $\kappa$ para la circunferencia $\mathbf{r}(t) = \langle 5\cos t, 5\sin t, 0 \rangle$.

18) Determina la curvatura de $\mathbf{r}(t) = \langle t, \ln(\cos t), 0 \rangle$ en $t = 0$.

---

## Nivel Avanzado

### Marco TNB completo
19) Para $\mathbf{r}(t) = \langle t, \cos t, \sin t \rangle$, encuentra $\mathbf{T}$, $\mathbf{N}$, $\mathbf{B}$ en $t = 0$.

20) Calcula el marco TNB de la hélice $\mathbf{r}(t) = \langle 2\cos t, 2\sin t, t \rangle$ en $t = \pi/2$.

21) Encuentra $\mathbf{T}$, $\mathbf{N}$, $\mathbf{B}$ para $\mathbf{r}(t) = \langle e^t\cos t, e^t\sin t, e^t \rangle$ en $t = 0$.

### Curvatura y torsión
22) Calcula la curvatura y torsión de $\mathbf{r}(t) = \langle t, t^2, t^3 \rangle$ en $t = 0$.

23) Demuestra que la torsión de la hélice $\mathbf{r}(t) = \langle a\cos t, a\sin t, bt \rangle$ es constante.

24) Encuentra $\kappa$ y $\tau$ para $\mathbf{r}(t) = \langle \cosh t, \sinh t, t \rangle$ en $t = 0$.

### Aplicaciones físicas
25) Una partícula se mueve según $\mathbf{r}(t) = \langle t^2, 2t, \ln(t+1) \rangle$. Encuentra velocidad, rapidez y aceleración en $t = 1$.

26) Si la posición es $\mathbf{r}(t) = \langle \sin t, 1 - \cos t, t \rangle$, determina las componentes tangencial y normal de la aceleración.

27) Un proyectil sigue $\mathbf{r}(t) = \langle 10t, 20t - 5t^2, 0 \rangle$. Encuentra la altura máxima y el alcance horizontal.

### Problemas de síntesis
28) Encuentra la ecuación del plano osculador de $\mathbf{r}(t) = \langle t, t^2, t^3 \rangle$ en $t = 1$.

29) Determina el círculo osculador de $\mathbf{r}(t) = \langle \cos t, \sin t, 0 \rangle$ en $t = 0$.

30) Para $\mathbf{r}(t) = \langle 3t - t^3, 3t^2, 3t + t^3 \rangle$, calcula $\kappa$ y demuestra que $\mathbf{r}$ describe una curva plana identificando el plano.

---

## Problemas de Aplicación

31) **Diseño de montaña rusa**: Una sección de vía sigue $\mathbf{r}(t) = \langle 10\cos t, 10\sin t, 5t \rangle$ para $t \in [0, 4\pi]$. Calcula la longitud total de vía necesaria.

32) **Trayectoria de satélite**: Un satélite orbita según $\mathbf{r}(t) = \langle 7000\cos(0.001t), 7000\sin(0.001t), 500\sin(0.002t) \rangle$ (km). Encuentra la rapidez y la curvatura de la órbita.

33) **Animación 3D**: Para crear una curva suave, un diseñador usa $\mathbf{r}(t) = \langle t, t^2, t^3 \rangle$. Parametriza la curva por longitud de arco en $[0,1]$.
