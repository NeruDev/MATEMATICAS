# Problemas — Integración múltiple

---

## Nivel Básico

### Integrales dobles en rectangulares
1) Evalúa $\iint_R (x + y)\,dA$ donde $R = [0, 1] \times [0, 2]$.

2) Calcula $\iint_R xy^2\,dA$ sobre el rectángulo $R = [0, 2] \times [0, 1]$.

3) Evalúa $\int_0^2 \int_0^3 (2x + 3y)\,dy\,dx$.

4) Calcula $\iint_R e^{x+y}\,dA$ donde $R = [0, 1] \times [0, 1]$.

### Cambio de orden
5) Reescribe $\int_0^1 \int_0^x f(x,y)\,dy\,dx$ cambiando el orden de integración.

6) Evalúa $\int_0^1 \int_y^1 x^2\,dx\,dy$ cambiando el orden.

### Regiones no rectangulares
7) Calcula $\iint_R y\,dA$ donde $R$ es el triángulo con vértices $(0,0)$, $(1,0)$, $(0,1)$.

8) Evalúa $\iint_R x\,dA$ sobre la región delimitada por $y = x$ y $y = x^2$.

---

## Nivel Intermedio

### Integrales dobles en polares
9) Calcula $\iint_D (x^2 + y^2)\,dA$ donde $D$ es el disco $x^2 + y^2 \leq 1$.

10) Evalúa $\iint_D \frac{1}{\sqrt{x^2+y^2}}\,dA$ sobre el anillo $1 \leq x^2 + y^2 \leq 4$.

11) Calcula el área de la región dentro del cardioide $r = 1 + \cos\theta$.

12) Evalúa $\iint_D e^{-(x^2+y^2)}\,dA$ sobre todo el plano $\mathbb{R}^2$.

### Integrales triples rectangulares
13) Calcula el volumen del tetraedro limitado por $x + y + z = 1$ y los planos coordenados.

14) Evalúa $\iiint_V xyz\,dV$ donde $V = [0,1] \times [0,2] \times [0,3]$.

15) Calcula $\iiint_V (x + y + z)\,dV$ sobre el cubo $[0,1]^3$.

### Integrales triples en cilíndricas
16) Calcula el volumen del cilindro $x^2 + y^2 \leq 4$, $0 \leq z \leq 3$.

17) Evalúa $\iiint_V z\,dV$ donde $V$ es el sólido bajo $z = 4 - x^2 - y^2$ sobre el disco $x^2 + y^2 \leq 4$.

18) Calcula el volumen del cono $z = \sqrt{x^2 + y^2}$ con $0 \leq z \leq 2$.

### Integrales triples en esféricas
19) Calcula el volumen de la esfera $x^2 + y^2 + z^2 = 9$.

20) Evalúa $\iiint_V (x^2 + y^2 + z^2)\,dV$ sobre la esfera de radio $a$.

21) Calcula el volumen del hemisferio superior $x^2 + y^2 + z^2 \leq 4$, $z \geq 0$.

---

## Nivel Avanzado

### Integrales de línea
22) Calcula $\int_C \mathbf{F} \cdot d\mathbf{r}$ donde $\mathbf{F} = \langle y, x \rangle$ y $C$ es la recta de $(0,0)$ a $(1,2)$.

23) Evalúa $\int_C (x^2 + y^2)\,ds$ donde $C$ es el círculo $x^2 + y^2 = 4$.

24) Calcula el trabajo de $\mathbf{F} = \langle x, y, z \rangle$ a lo largo de la hélice $\mathbf{r}(t) = \langle \cos t, \sin t, t \rangle$, $t \in [0, 2\pi]$.

25) Determina si $\mathbf{F} = \langle 2xy, x^2 + z, y \rangle$ es conservativo. Si lo es, encuentra su potencial.

### Teorema de Green
26) Usa Green para calcular $\oint_C (x^2 - y)\,dx + (y^2 + x)\,dy$ donde $C$ es el círculo $x^2 + y^2 = 1$ (CCW).

27) Calcula el área de la elipse $\frac{x^2}{4} + y^2 = 1$ usando el teorema de Green.

28) Evalúa $\oint_C \mathbf{F} \cdot d\mathbf{r}$ donde $\mathbf{F} = \langle -y^3, x^3 \rangle$ y $C$ es el cuadrado $|x| + |y| = 1$ (CCW).

### Teorema de Gauss (Divergencia)
29) Calcula el flujo de $\mathbf{F} = \langle x, y, z \rangle$ a través de la esfera $x^2 + y^2 + z^2 = 4$.

30) Evalúa $\oiint_S \mathbf{F} \cdot d\mathbf{S}$ donde $\mathbf{F} = \langle x^2, y^2, z^2 \rangle$ y $S$ es el cubo $[0,1]^3$.

31) Usa Gauss para encontrar el flujo de $\mathbf{F} = \langle xy, yz, xz \rangle$ a través del cilindro $x^2 + y^2 \leq 1$, $0 \leq z \leq 2$ (superficie cerrada).

### Teorema de Stokes
32) Usa Stokes para calcular $\oint_C \mathbf{F} \cdot d\mathbf{r}$ donde $\mathbf{F} = \langle -y, x, 0 \rangle$ y $C$ es el círculo $x^2 + y^2 = 1$ en $z = 0$ (CCW).

33) Calcula la circulación de $\mathbf{F} = \langle y, z, x \rangle$ alrededor del triángulo con vértices $(1,0,0)$, $(0,1,0)$, $(0,0,1)$.

34) Verifica Stokes: para $\mathbf{F} = \langle z, x, y \rangle$ y el hemisferio $z = \sqrt{1-x^2-y^2}$ con borde el círculo unitario.

---

## Problemas de Aplicación

35) **Masa de lámina**: Una lámina triangular con vértices $(0,0)$, $(2,0)$, $(0,2)$ tiene densidad $\rho(x,y) = xy$. Calcula su masa.

36) **Centro de masa**: Encuentra el centroide de la región delimitada por $y = x^2$ y $y = 4$.

37) **Momento de inercia**: Calcula el momento de inercia respecto al eje $z$ de un cono sólido $z = \sqrt{x^2+y^2}$, $z \leq 1$, con densidad uniforme $\rho = 1$.

38) **Flujo de fluido**: El campo de velocidad de un fluido es $\mathbf{v} = \langle x, -y, 0 \rangle$. Calcula el flujo a través del cuadrado $[0,1] \times [0,1]$ en el plano $z = 0$ con normal $\mathbf{k}$.

39) **Trabajo**: Una partícula se mueve en el campo de fuerza $\mathbf{F} = \langle -y, x \rangle$ a lo largo de la elipse $\frac{x^2}{4} + y^2 = 1$ una vez en sentido antihorario. Calcula el trabajo realizado.
