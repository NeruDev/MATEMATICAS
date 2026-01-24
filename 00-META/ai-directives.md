<!--
::METADATA::
type: reference
topic_id: meta-ai-directives
file_id: ai-directives
status: stable
audience: ai_context
last_updated: 2026-01-02
-->

# Directivas Técnicas para IA — Repositorio de Matemáticas

> **Nota:** Este archivo complementa a `ia-contract.md` con reglas técnicas específicas.
> Para la guía principal, consultar [ia-contract.md](ia-contract.md).

---

## 1. Notación de Valor Absoluto en Tablas Markdown

**Problema:** El símbolo `|` para valor absoluto (`$|x|$`) interfiere con los separadores de columnas de las tablas Markdown.

**Directiva:** En tablas Markdown, usar notación LaTeX explícita:

| Incorrecto | Correcto |
|------------|----------|
| `$|x|$` | `$\lvert x \rvert$` |
| `$|a| < |b|$` | `$\lvert a \rvert < \lvert b \rvert$` |
| `$||v||$` | `$\lVert v \rVert$` |

**Nota:** Fuera de tablas, ambas notaciones son aceptables.

---

## 2. Formato de Soluciones

**Directiva:** Toda solución debe incluir contexto antes del desarrollo:

```markdown
**[Prob-XX])** *Contexto: [Concepto/método aplicable]*

[Desarrollo paso a paso]

**Verificación:** [Comprobación del resultado]
```

---

## 3. Símbolos Problemáticos en Tablas

| Símbolo | Uso | Alternativa LaTeX |
|---------|-----|-------------------|
| Valor absoluto | $\lvert x \rvert$ | `$\lvert x \rvert$` |
| Norma | $\lVert v \rVert$ | `$\lVert v \rVert$` |
| Evaluado en | $f(x)\big\vert_a^b$ | `$\big\vert$` |
| Tal que (conjuntos) | $\{x \mid x > 0\}$ | `$\mid$` |
| Divisibilidad | $a \mid b$ | `$\mid$` |

---

## 4. Formato LaTeX

- **Inline:** `$...$` — una línea
- **Display:** `$$...$$` — ecuaciones centradas
- **NO usar:** `\begin{equation}` en Markdown (no renderiza)
- **Alineación múltiple:** Usar `$$\begin{aligned}...\end{aligned}$$`

---

## 5. Idioma y Estilo

| Aspecto | Especificación |
|---------|----------------|
| Idioma | Español |
| Nivel | Universitario |
| Estilo | Didáctico, progresivo |
| Prioridad | Claridad sobre brevedad |
| Ejemplos | Incluir siempre que ayuden |

---

## 6. Sintaxis de Enlaces (OBLIGATORIO)

> **⚠️ DIRECTIVA CRÍTICA:** Todos los enlaces internos DEBEN seguir esta sintaxis para garantizar navegación funcional en VS Code y GitHub.

### 6.1 Formato Correcto de Enlaces

```markdown
[Texto visible](ruta/relativa/archivo.md)
[Texto visible](ruta/relativa/archivo.md#ancla)
```

### 6.2 Ejemplos por Tipo de Enlace

| Tipo | Sintaxis Correcta | Ejemplo |
|------|-------------------|---------|
| **Glosario** | `[término](../glossary.md#ancla)` | `[función](../glossary.md#funcion)` |
| **Índice principal** | `[texto](../WIKI_INDEX.md)` | `[← Volver](../WIKI_INDEX.md)` |
| **Archivo en misma carpeta** | `[texto](./archivo.md)` | `[Intro](./AL-01-Matrices-Intro.md)` |
| **Archivo en subcarpeta** | `[texto](./subcarpeta/archivo.md)` | `[Teoría](./theory/AL-01-Teoria-Matrices.md)` |
| **Archivo en carpeta padre** | `[texto](../carpeta/archivo.md)` | `[Índice](../00-Index.md)` |
| **Otro módulo** | `[texto](../Modulo/carpeta/archivo.md)` | `[Álgebra](../02-Algebra-Lineal/00-Index.md)` |

### 6.3 Errores Comunes (NO HACER)

| ❌ Incorrecto | ✅ Correcto | Problema |
|---------------|-------------|----------|
| `](../glossary.md)#term)` | `](../glossary.md#term)` | Paréntesis fuera del ancla |
| `](..](../glossary.md)` | `](../glossary.md)` | Doble bracket |
| `[texto](README.md)` | `[texto](*-Intro.md)` | No existen README en subtemas |
| `[texto](archivo)` | `[texto](archivo.md)` | Falta extensión .md |

### 6.4 Navegación Estándar (Header)

Todo archivo de contenido debe incluir este header de navegación:

```markdown
> 🏠 **Navegación:** [← Volver al Índice Principal](../WIKI_INDEX.md) | [📚 Glosario](../glossary.md)
```

Ajustar la ruta relativa según la profundidad del archivo:
- Nivel 1 (`01-Fundamentos/00-Index.md`): `../WIKI_INDEX.md`
- Nivel 2 (`01-Fundamentos/02-Aritmetica/FUN-02-Intro.md`): `../../WIKI_INDEX.md`
- Nivel 3 (`01-Fundamentos/02-Aritmetica/theory/FUN-02-Teoria.md`): `../../../WIKI_INDEX.md`

### 6.5 Validación de Enlaces

Antes de finalizar cualquier contenido nuevo:
1. Verificar que todas las rutas relativas existen
2. Probar enlaces en VS Code Markdown Preview
3. Ejecutar script de validación si está disponible

---

## 7. Gestión de Archivos Grandes (Git LFS)

**Directiva:** Las imágenes y archivos binarios NO deben ser tratados como texto plano en Git. 

1. **Extensiones LFS:** Asegurar que archivos `.png`, `.svg`, `.jpg`, `.webp`, `.gif`, `.bmp` se gestionen mediante Git LFS.
2. **Nuevos Formatos:** Si se requiere añadir un nuevo tipo de archivo pesado (ej: `.mp4`, `.zip`), solicitar el rastreo con `git lfs track "*.ext"`.
3. **Ubicación:** Las imágenes deben residir preferiblemente en carpetas `media/` o `media/generated/`.

---

## 8. Exclusión de Entornos (gitignore)

**Directiva:** El repositorio mantiene una política estricta de exclusión para evitar "contaminación" de dependencias locales.

1. **Entornos Virtuales:** Carpetas como `.venv/`, `venv/`, `env/` están excluidas globalmente.
2. **Caché:** Archivos `__pycache__/` y artefactos de compilación Python están ignorados.
3. **No forzar:** Nunca usar `git add -f` para añadir archivos ignorados por el `.gitignore`.

---

## 9. Referencias Cruzadas al Glosario

Para términos del glosario, usar formato: `[término](../glossary.md#ancla)`

**Anclas válidas:** El ancla debe coincidir con el ID del término en `glossary.md` (en minúsculas, guiones en lugar de espacios).

Ejemplos:
- `[función](../glossary.md#funcion)`
- `[valor absoluto](../glossary.md#valor-absoluto)`
- `[regla de la cadena](../glossary.md#regla-de-la-cadena)`

---

## 8. Creación de Gráficos con Python/Matplotlib

> **⚠️ DIRECTIVA CRÍTICA:** Todos los gráficos matemáticos DEBEN seguir la guía de estilos en [`00-META/tools/graphics/graphics_style_guide.md`](tools/graphics/graphics_style_guide.md).

### 8.1 Principio Fundamental

**SEPARACIÓN FIGURA-TEXTO:** Nunca colocar texto explicativo largo dentro del área de la figura geométrica.

| En la figura | En panel separado |
|--------------|-------------------|
| Letras (A, B, C) | Fórmulas completas |
| Símbolos (α, β, θ) | Leyendas explicativas |
| Medidas esenciales (90°) | Propiedades y teoremas |
| Símbolos de relación (~, ≅) | Demostraciones |

### 8.2 Estructura Obligatoria con GridSpec

```python
fig = plt.figure(figsize=(12, 7), layout='constrained')
gs = fig.add_gridspec(1, 2, width_ratios=[1.3, 1], wspace=0.08)

ax_fig = fig.add_subplot(gs[0])   # Panel: figura geométrica
ax_info = fig.add_subplot(gs[1])  # Panel: información
```

**Layouts disponibles:**
- **Horizontal** (1×2): Figura izquierda + Info derecha
- **Vertical** (2×1): Figura(s) arriba + Info abajo
- **Mixto** (2×N): Grid de figuras + Info en fila inferior

### 8.3 Elemento Didáctico Obligatorio: Caja de Fórmula

Todo gráfico DEBE incluir una caja de fórmula principal destacada:

```python
# Caja de fórmula (OBLIGATORIA)
ax_info.add_patch(plt.Rectangle(
    (0.05, 0.78), 0.9, 0.18,
    facecolor='#fffbeb',           # Amarillo claro
    edgecolor=colors['tertiary'],  # Borde de acento
    linewidth=2,
    transform=ax_info.transAxes
))
ax_info.text(0.5, 0.90, 'FÓRMULA PRINCIPAL', 
            fontsize=9, fontweight='bold', ha='center')
ax_info.text(0.5, 0.82, r'$fórmula$', 
            fontsize=22, ha='center', fontweight='bold')
```

### 8.4 Estructura del Panel Informativo

```
┌─────────────────────────────────┐
│     FÓRMULA PRINCIPAL           │  ← Caja destacada (obligatoria)
├─────────────────────────────────┤
│   Leyenda de Símbolos           │  ← Correspondencia símbolo-significado
├─────────────────────────────────┤
│   Propiedad / Teorema           │  ← Enunciado textual
├─────────────────────────────────┤
│   Demostración (opcional)       │  ← En caja separada
└─────────────────────────────────┘
```

### 8.5 Paleta de Colores Estándar

| Contexto | Color | Código |
|----------|-------|--------|
| Figura principal | primary | `#3b82f6` |
| Elementos secundarios | secondary | `#10b981` |
| Destacados | accent | `#f59e0b` |
| Fórmulas/énfasis | tertiary | `#8b5cf6` |
| Texto | text | `#374151` |
| Fondo fórmula | - | `#fffbeb` |
| Separadores | - | `#e5e7eb` |

### 8.6 Checklist de Gráficos

Antes de finalizar cualquier gráfico:

- [ ] ¿Usa `layout='constrained'` en la figura?
- [ ] ¿Tiene GridSpec con paneles separados?
- [ ] ¿Incluye caja de fórmula destacada?
- [ ] ¿Las etiquetas en la figura son mínimas (solo símbolos)?
- [ ] ¿La leyenda explica todos los símbolos usados?
- [ ] ¿Usa `ax.set_aspect('equal')` para figuras geométricas?
- [ ] ¿No hay texto superpuesto?

### 8.7 Ubicación de Archivos

| Tipo | Ubicación |
|------|-----------|
| Scripts fuente | `00-META/tools/graphics/sources/FUN-XX/` |
| Imágenes generadas | `01-Fundamentos/XX-Tema/media/generated/` |
| Guía de estilos | `00-META/tools/graphics/graphics_style_guide.md` |
| Templates | `00-META/tools/graphics/templates.py` |

### 8.8 Referencia en Markdown

```markdown
![Título Descriptivo](../media/generated/nombre_grafico.png)

*Figura X.Y.Z: Descripción de lo que muestra el gráfico*
```
