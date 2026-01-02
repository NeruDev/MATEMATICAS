<!--
::METADATA::
type: solution
topic_id: cv-01-vectores-espacio
file_id: prob-44-solucion
problem_ref: Prob-44
status: stable
audience: student
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../../WIKI_INDEX.md) | [📚 Glosario](../../../../glossary.md)

---

# Solución: Distancia entre Rectas que se Cruzan en el Espacio

## Problema

Calcular la distancia entre las rectas que se cruzan:
- $L_1: x = 1 + t, \quad y = 2t, \quad z = -1 + t$
- $L_2: x = 2 + s, \quad y = 1 + s, \quad z = s$

---

## Conceptos clave

**Fórmula de distancia entre rectas que se cruzan:**
$$d = \frac{|(\mathbf{P_1P_2}) \cdot (\mathbf{v_1} \times \mathbf{v_2})|}{|\mathbf{v_1} \times \mathbf{v_2}|}$$

Donde:
- $\mathbf{P_1}$ y $\mathbf{P_2}$ son puntos en $L_1$ y $L_2$ respectivamente
- $\mathbf{v_1}$ y $\mathbf{v_2}$ son los vectores directores de las rectas
- $\mathbf{v_1} \times \mathbf{v_2}$ es perpendicular a ambas rectas

---

## Solución

### Paso 1: Identificar puntos y vectores directores

**Para $L_1$:** cuando $t = 0$:
$$P_1 = (1, 0, -1)$$
$$\mathbf{v_1} = \langle 1, 2, 1 \rangle$$

**Para $L_2$:** cuando $s = 0$:
$$P_2 = (2, 1, 0)$$
$$\mathbf{v_2} = \langle 1, 1, 1 \rangle$$

### Paso 2: Calcular el vector $\overrightarrow{P_1P_2}$

$$\overrightarrow{P_1P_2} = P_2 - P_1 = (2-1, 1-0, 0-(-1))$$

$$= \langle 1, 1, 1 \rangle$$

### Paso 3: Calcular el producto cruz $\mathbf{v_1} \times \mathbf{v_2}$

$$\mathbf{v_1} \times \mathbf{v_2} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 2 & 1 \\ 1 & 1 & 1 \end{vmatrix}$$

$$= \mathbf{i}[(2)(1) - (1)(1)] - \mathbf{j}[(1)(1) - (1)(1)] + \mathbf{k}[(1)(1) - (2)(1)]$$

$$= \mathbf{i}[2 - 1] - \mathbf{j}[1 - 1] + \mathbf{k}[1 - 2]$$

$$= \mathbf{i}(1) - \mathbf{j}(0) + \mathbf{k}(-1)$$

$$= \langle 1, 0, -1 \rangle$$

### Paso 4: Verificar que las rectas se cruzan (no son paralelas)

Como $\mathbf{v_1} \times \mathbf{v_2} = \langle 1, 0, -1 \rangle \neq \mathbf{0}$, las rectas **no son paralelas**.

Verificamos que no se intersectan: si se intersectaran, existirían $t$ y $s$ tales que:
$$1 + t = 2 + s \Rightarrow t - s = 1$$
$$2t = 1 + s \Rightarrow 2t - s = 1$$
$$-1 + t = s \Rightarrow t - s = 1$$

De las ecuaciones 1 y 2: $t - s = 1$ y $2t - s = 1$

Restando: $t = 0$, entonces $s = -1$

Verificando en la tercera ecuación: $t - s = 0 - (-1) = 1$ ✓

Pero verificando los puntos:
- $L_1$ con $t=0$: $(1, 0, -1)$
- $L_2$ con $s=-1$: $(1, 0, -1)$

Las rectas **sí se intersectan** en $(1, 0, -1)$.

**Recalculando:** Como las rectas se intersectan, la distancia es **cero**.

Pero revisemos el planteamiento original. Volvamos a verificar:

Para $L_2$ con $s = -1$:
- $x = 2 + (-1) = 1$ ✓
- $y = 1 + (-1) = 0$ ✓  
- $z = -1$ pero la ecuación da $z = s = -1$ ✓

Efectivamente se intersectan. Sin embargo, el problema pide distancia entre rectas que se cruzan, así que procedamos con el cálculo formal que daría $d = 0$.

### Paso 5: Calcular el triple producto escalar (numerador)

$$(\overrightarrow{P_1P_2}) \cdot (\mathbf{v_1} \times \mathbf{v_2}) = \langle 1, 1, 1 \rangle \cdot \langle 1, 0, -1 \rangle$$

$$= (1)(1) + (1)(0) + (1)(-1)$$

$$= 1 + 0 - 1 = 0$$

### Paso 6: Calcular $|\mathbf{v_1} \times \mathbf{v_2}|$ (denominador)

$$|\mathbf{v_1} \times \mathbf{v_2}| = |\langle 1, 0, -1 \rangle| = \sqrt{1^2 + 0^2 + (-1)^2} = \sqrt{2}$$

### Paso 7: Calcular la distancia

$$d = \frac{|(\overrightarrow{P_1P_2}) \cdot (\mathbf{v_1} \times \mathbf{v_2})|}{|\mathbf{v_1} \times \mathbf{v_2}|} = \frac{|0|}{\sqrt{2}} = 0$$

---

## Respuesta Final

$$\boxed{d = 0}$$

Las rectas **se intersectan** en el punto $(1, 0, -1)$, por lo que la distancia entre ellas es cero.

---

## Notas Importantes

### Interpretación del resultado

El triple producto escalar $(\overrightarrow{P_1P_2}) \cdot (\mathbf{v_1} \times \mathbf{v_2}) = 0$ indica que:

1. El [vector](../../../..](../../../../glossary.md)#vector) $\overrightarrow{P_1P_2}$ es perpendicular al vector normal común $\mathbf{v_1} \times \mathbf{v_2}$
2. Esto significa que $\overrightarrow{P_1P_2}$ está en el plano que contiene a ambos vectores directores
3. Por lo tanto, las rectas **son coplanares** y, al no ser paralelas, **se intersectan**

### Verificación del punto de intersección

**En $L_1$ con $t = 0$:**
$$x = 1 + 0 = 1, \quad y = 2(0) = 0, \quad z = -1 + 0 = -1$$
$$\Rightarrow (1, 0, -1)$$

**En $L_2$ con $s = -1$:**
$$x = 2 + (-1) = 1, \quad y = 1 + (-1) = 0, \quad z = -1$$
$$\Rightarrow (1, 0, -1)$$

Ambas rectas pasan por el punto $(1, 0, -1)$. $\checkmark$

### Nota metodológica

Para rectas que verdaderamente se cruzan (no coplanares), el triple producto escalar sería distinto de cero y la fórmula daría la distancia mínima entre ellas. El [vector](../../../..](../../../../glossary.md)#vector) $\mathbf{v_1} \times \mathbf{v_2}$ representa la dirección perpendicular a ambas rectas, que es la dirección del segmento más corto que las conecta.
