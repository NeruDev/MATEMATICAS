<!--
::METADATA::
type: reference
topic_id: trigonometria
file_id: _directives
status: stable
audience: ai_context
-->

# Directivas de Trigonometría (05)

## Clasificación del Contenido

| Carpeta/Archivo | Archivo Principal | Descripción |
|-----------------|-------------------|-------------|
| `theory/` | `FUN-05-Teoria-Trigonometria.md` | Teoría de trigonometría |
| `methods/` | `FUN-05-Metodos-Trigonometria.md` | Procedimientos paso a paso |
| `problems/` | `FUN-05-Problemas.md` | Enunciados de problemas |
| `solutions/` | `FUN-05-Respuestas.md`, `FUN-05-Soluciones-Desarrolladas.md` | Soluciones desarrolladas |
| `FUN-05-Trigonometria-Intro.md` | — | Entrada principal del tema |
| `FUN-05-Resumen-Formulas.md` | — | Resumen de fórmulas |
| `manifest.json` | — | Metadatos y configuración |

---

## Contenido por Carpetas

### 📁 theory/
**Propósito:** Fundamentos teóricos de trigonometría plana.
**Contenido:**
- Ángulos: grados, radianes, conversiones
- Razones trigonométricas en triángulos rectángulos
- Círculo unitario y coordenadas
- Gráficas de funciones trigonométricas
- Identidades fundamentales, de suma/resta, múltiplos
- Ecuaciones trigonométricas
- Funciones inversas
- Leyes de senos y cosenos

### 📁 methods/
**Propósito:** Procedimientos sistemáticos para resolver problemas trigonométricos.
**Contenido:**
- Conversión grados ↔ radianes
- Encontrar razones en triángulos rectángulos
- Evaluar funciones usando círculo unitario
- Graficar funciones transformadas
- Demostrar identidades
- Resolver ecuaciones trigonométricas
- Usar fórmulas de suma/resta
- Aplicar leyes de senos y cosenos
- Evaluar funciones inversas
- Resolver problemas de aplicación

### 📁 problems/
**Propósito:** Ejercicios organizados por subtema con niveles de dificultad.
**Estructura:**
- 5.1 Ángulos y medidas (10 problemas)
- 5.2 Razones en triángulo rectángulo (10 problemas)
- 5.3 Círculo unitario (10 problemas)
- 5.4 Gráficas (10 problemas)
- 5.5 Identidades fundamentales (10 problemas)
- 5.6 Identidades de suma/resta/múltiplos (10 problemas)
- 5.7 Ecuaciones trigonométricas (10 problemas)
- 5.8 Funciones inversas (10 problemas)
- 5.9 Ley de senos y cosenos (10 problemas)
- 5.10 Aplicaciones (10 problemas)
- Problemas de síntesis (5 problemas)

**Niveles:** ⭐ básico, ⭐⭐ intermedio, ⭐⭐⭐ avanzado, ⭐⭐⭐⭐ desafío

### 📁 solutions/
**Propósito:** Soluciones detalladas y contextualizadas.
**Formato requerido:**
1. **Contexto:** Identificar concepto o identidad aplicable
2. **Desarrollo:** Solución paso a paso
3. **Verificación:** Comprobación del resultado

### 📁 applications/
**Propósito:** Aplicaciones de trigonometría al mundo real.
**Temas sugeridos:**
- Navegación y rumbos
- Física: ondas, oscilaciones
- Ingeniería: señales AC
- Topografía y agrimensura

### 📁 diagnostic/
**Propósito:** Evaluación de conocimientos previos.
**Contenido:**
- Pre-test de trigonometría básica
- Identificación de conceptos a reforzar

### 📁 media/
**Propósito:** Recursos visuales y multimedia.
**Subcarpetas:**
- `images/`: Círculo unitario, gráficas, triángulos
- `geogebra/`: Applets interactivos
- `videos.md`: Enlaces a videos explicativos

## Convenciones de Notación

### Funciones Trigonométricas
- Seno: $\sin\theta$ (no sen)
- Coseno: $\cos\theta$
- Tangente: $\tan\theta$
- Cotangente: $\cot\theta$
- Secante: $\sec\theta$
- Cosecante: $\csc\theta$

### Funciones Inversas
- Arcoseno: $\arcsin x$ o $\sin^{-1}x$
- Arcocoseno: $\arccos x$ o $\cos^{-1}x$
- Arcotangente: $\arctan x$ o $\tan^{-1}x$
- Arcocotangente: $\text{arccot}\, x$ o $\cot^{-1}x$
- Arcosecante: $\text{arcsec}\, x$ o $\sec^{-1}x$
- Arcocosecante: $\text{arccsc}\, x$ o $\csc^{-1}x$

---

## Formato de Tablas (OBLIGATORIO)

⚠️ **Regla crítica:** El número de columnas en encabezados, separadores y datos DEBE coincidir.

### Verificación antes de guardar:

```markdown
| Col1 | Col2 | Col3 | Col4 |    ← 4 encabezados
|------|:----:|:----:|:----:|    ← 4 separadores
| a    | b    | c    | d    |    ← 4 datos por fila
```

### Errores comunes a evitar:

❌ **Encabezados incompletos:**
```markdown
| Función | Rango |              ← Solo 2 encabezados
|---------|:-----:|:-----:|:-----:| ← 4 separadores (¡NO COINCIDE!)
| Arc... | $...$ | $...$ | $...$ | ← 4 columnas de datos
```

✅ **Correcto:**
```markdown
| Función | Notación | Dominio | Rango |  ← 4 encabezados
|---------|:--------:|:-------:|:-----:|  ← 4 separadores
| Arc... | $...$ | $...$ | $...$ |        ← 4 columnas de datos
```

### Ángulos
- Ángulos en variables griegas: $\alpha$, $\beta$, $\theta$, $\phi$
- Grados con símbolo: 45°, 90°
- Radianes sin unidad o con "rad": $\frac{\pi}{4}$, $2\pi$ rad

### Unidades
- Ángulos: grados (°) o radianes
- Longitudes: según contexto (m, cm, km)
- Tiempo: segundos (s), minutos, horas

## Subtemas del Manifest

| Código | Subtema | Descripción |
|--------|---------|-------------|
| 5.1 | Ángulos y medidas | Grados, radianes, coterminales, arco, sector |
| 5.2 | Razones en triángulo rectángulo | SOH-CAH-TOA, valores notables |
| 5.3 | Círculo unitario | Coordenadas, signos por cuadrante, ángulos de referencia |
| 5.4 | Gráficas | Seno, coseno, tangente; transformaciones |
| 5.5 | Identidades fundamentales | Pitagóricas, recíprocas, cociente |
| 5.6 | Identidades de suma/resta | Suma, resta, doble ángulo, medio ángulo |
| 5.7 | Ecuaciones trigonométricas | Soluciones en intervalo y generales |
| 5.8 | Funciones inversas | Dominio, rango, evaluación |
| 5.9 | Ley de senos y cosenos | Triángulos oblicuángulos, caso ambiguo |
| 5.10 | Aplicaciones | Altura/distancia, navegación, modelado |

## Identidades de Referencia Rápida

### Pitagóricas
$$\sin^2\theta + \cos^2\theta = 1$$
$$1 + \tan^2\theta = \sec^2\theta$$
$$1 + \cot^2\theta = \csc^2\theta$$

### Ángulo Doble
$$\sin(2\theta) = 2\sin\theta\cos\theta$$
$$\cos(2\theta) = \cos^2\theta - \sin^2\theta$$

### Suma y Resta
$$\sin(\alpha \pm \beta) = \sin\alpha\cos\beta \pm \cos\alpha\sin\beta$$
$$\cos(\alpha \pm \beta) = \cos\alpha\cos\beta \mp \sin\alpha\sin\beta$$
