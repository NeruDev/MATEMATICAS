# Guía de Estilos para Gráficos Matemáticos

> **Objetivo:** Establecer reglas consistentes para la generación de gráficos con Python/Matplotlib que separen claramente las figuras geométricas del texto explicativo, maximizando la claridad didáctica.

---

## 1. Principio Fundamental: Separación Figura-Texto

### Regla Principal
> **NUNCA colocar texto explicativo largo dentro del área de la figura geométrica.**

Las figuras deben contener únicamente:
- Etiquetas mínimas (letras: A, B, C; símbolos: α, β, θ)
- Marcadores de puntos
- Elementos geométricos (líneas, arcos, polígonos)

Todo el texto explicativo debe ir en un **panel separado**.

---

## 2. Estructura de Layout con GridSpec

### 2.1 Layout Horizontal (Figura + Info)
Ideal para figuras con muchas propiedades o fórmulas.

```python
fig = plt.figure(figsize=(12, 7), layout='constrained')
gs = fig.add_gridspec(1, 2, width_ratios=[1.3, 1], wspace=0.08)

ax_fig = fig.add_subplot(gs[0])   # Panel izquierdo: figura
ax_info = fig.add_subplot(gs[1])  # Panel derecho: información
```

### 2.2 Layout Vertical (Figuras arriba + Info abajo)
Ideal para comparaciones múltiples (criterios de congruencia, semejanza).

```python
fig = plt.figure(figsize=(13, 8), layout='constrained')
gs = fig.add_gridspec(2, 1, height_ratios=[2.5, 1], hspace=0.1)

ax_figs = fig.add_subplot(gs[0])  # Panel superior: figuras
ax_info = fig.add_subplot(gs[1])  # Panel inferior: información
```

### 2.3 Layout Mixto (Grid de figuras + Info)
Para múltiples subplots con leyenda compartida.

```python
fig = plt.figure(figsize=(13, 7), layout='constrained')
gs = fig.add_gridspec(2, 3, height_ratios=[2.5, 1], hspace=0.12, wspace=0.15)

ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[0, 2])
ax_info = fig.add_subplot(gs[1, :])  # Span completo inferior
```

---

## 3. Elemento Didáctico Principal: Caja de Fórmula Destacada

### Especificación
Toda figura didáctica debe incluir una **caja de fórmula principal** que sea el elemento visual más destacado del panel informativo.

### Implementación

```python
# Caja de fórmula destacada (OBLIGATORIA en todo gráfico didáctico)
ax_info.add_patch(plt.Rectangle(
    (0.05, 0.78), 0.9, 0.18,  # posición y tamaño
    facecolor='#fffbeb',       # fondo amarillo claro
    edgecolor=colors['tertiary'],  # borde del color de acento
    linewidth=2,
    transform=ax_info.transAxes
))

# Título de la caja
ax_info.text(0.5, 0.90, 'FÓRMULA PRINCIPAL', 
            fontsize=9, fontweight='bold',
            ha='center', va='center', 
            color=colors['tertiary'])

# Fórmula (LaTeX)
ax_info.text(0.5, 0.82, r'$\theta = \alpha + \beta$', 
            fontsize=22,  # Grande y legible
            ha='center', va='center', 
            color=colors['tertiary'], 
            fontweight='bold')
```

### Colores recomendados para cajas de fórmula
| Tipo | Fondo | Borde |
|------|-------|-------|
| Fórmula principal | `#fffbeb` (amarillo claro) | `colors['tertiary']` |
| Fórmula secundaria | `#f0f9ff` (azul claro) | `#93c5fd` |
| Demostración | `#f9fafb` (gris muy claro) | `#d1d5db` |

---

## 4. Secciones del Panel Informativo

### Estructura Jerárquica Recomendada

```
┌─────────────────────────────────┐
│     FÓRMULA PRINCIPAL           │  ← Caja destacada (obligatoria)
│         θ = α + β               │
├─────────────────────────────────┤
│   Leyenda de Símbolos           │  ← Correspondencia símbolo-significado
│   α = ángulo en A               │
│   β = ángulo en B               │
├─────────────────────────────────┤
│   Propiedad / Teorema           │  ← Enunciado textual
│   (descripción breve)           │
├─────────────────────────────────┤
│   Demostración (opcional)       │  ← En caja separada
│   (pasos o justificación)       │
└─────────────────────────────────┘
```

### Separadores entre secciones

```python
# Línea separadora horizontal
ax_info.axhline(y=0.36, xmin=0.05, xmax=0.95, color='#e5e7eb', lw=1)

# Línea separadora vertical (para layouts de columnas)
ax_info.axvline(x=0.50, ymin=0.10, ymax=0.90, color='#e5e7eb', lw=1)
```

---

## 5. Etiquetas en la Figura Geométrica

### Reglas de Posicionamiento

| Elemento | Posición | Offset típico |
|----------|----------|---------------|
| Vértices (A, B, C) | Fuera de la figura | `(-0.4, -0.35)` del punto |
| Ángulos (α, β, θ) | Cerca del arco, fuera | `(0.7, 0.4)` del vértice |
| Lados (a, b, c) | Punto medio, fuera | Perpendicular al lado |

### Implementación

```python
# Vértices - solo letra, sin descripciones
vertices_config = [
    (A, 'A', (-0.4, -0.35)),
    (B, 'B', (0.3, -0.35)), 
    (C, 'C', (-0.35, 0.25)),
]
for p, label, offset in vertices_config:
    ax.plot(p[0], p[1], 'o', color='#374151', markersize=7)
    ax.text(p[0]+offset[0], p[1]+offset[1], label, 
            fontsize=12, fontweight='bold')

# Ángulos - solo símbolo griego
ax.text(A[0]+0.7, A[1]+0.4, 'α', 
        fontsize=14, color=colors['secondary'], fontweight='bold')
```

### Lo que NO debe ir en la figura
❌ Descripciones largas ("ángulo interior no adyacente")  
❌ Fórmulas completas ("θ = α + β")  
❌ Explicaciones ("El ángulo exterior es igual a...")  
❌ Múltiples líneas de texto  

### Lo que SÍ puede ir en la figura
✅ Letras individuales (A, B, C, D)  
✅ Símbolos griegos (α, β, γ, θ)  
✅ Números de medida cuando son esenciales (90°, 45°)  
✅ Símbolos de relación (~, ≅) entre figuras  

---

## 6. Paleta de Colores Estándar

### Colores del sistema (`get_colors()`)

```python
colors = {
    'primary': '#3b82f6',    # Azul - figuras principales
    'secondary': '#10b981',  # Verde - elementos secundarios
    'accent': '#f59e0b',     # Naranja - destacados
    'tertiary': '#8b5cf6',   # Púrpura - fórmulas y énfasis
    'text': '#374151',       # Gris oscuro - texto
}
```

### Uso de colores por contexto

| Contexto | Color | Código |
|----------|-------|--------|
| Figura principal | primary | `#3b82f6` |
| Ángulos interiores | secondary/accent | `#10b981`/`#f59e0b` |
| Elemento destacado | tertiary | `#8b5cf6` |
| Texto normal | text | `#374151` |
| Texto secundario | - | `#6b7280` |
| Líneas separadoras | - | `#e5e7eb` |
| Fondo de fórmula | - | `#fffbeb` |

---

## 7. Tipografía

### Tamaños recomendados

| Elemento | Tamaño | Peso |
|----------|--------|------|
| Título general (suptitle) | 14 | bold |
| Título de sección | 10-11 | bold |
| Fórmula principal | 20-22 | bold |
| Texto de leyenda | 9 | normal |
| Etiquetas en figura | 12-14 | bold |
| Símbolos griegos | 13-16 | bold |

### LaTeX para fórmulas
Siempre usar `r'$...$'` para fórmulas matemáticas:

```python
ax.text(0.5, 0.5, r'$\theta = \alpha + \beta$', fontsize=20)
ax.text(0.5, 0.3, r'$A = \frac{b \cdot h}{2}$', fontsize=18)
```

---

## 8. Configuración Base de la Figura

### Setup obligatorio

```python
def generate() -> plt.Figure:
    """Docstring descriptivo."""
    setup_style()  # Aplicar estilo global
    colors = get_colors()  # Obtener paleta
    
    fig = plt.figure(figsize=(W, H), layout='constrained')
    # ...
```

### Ejes de la figura geométrica

```python
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)
ax.set_aspect('equal')  # IMPORTANTE para geometría
ax.axis('off')          # Sin ejes cartesianos
```

### Ejes del panel informativo

```python
ax_info.axis('off')
ax_info.set_xlim(0, 1)  # Coordenadas normalizadas
ax_info.set_ylim(0, 1)
```

---

## 9. Checklist de Revisión

Antes de finalizar un gráfico, verificar:

- [ ] **Separación clara:** figura y texto en paneles distintos
- [ ] **Caja de fórmula:** presente y destacada
- [ ] **Etiquetas mínimas:** solo símbolos en la figura
- [ ] **Leyenda completa:** todos los símbolos explicados
- [ ] **Colores consistentes:** usando la paleta estándar
- [ ] **Aspecto igual:** `ax.set_aspect('equal')` en figuras geométricas
- [ ] **Sin superposición:** verificar que nada se encime
- [ ] **Layout constrained:** `layout='constrained'` en la figura

---

## 10. Plantilla Base

```python
"""
Gráfico: [Nombre del Gráfico]
==============================
Topic: FUN-XX [Tema]
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import matplotlib.pyplot as plt
import numpy as np
from templates import setup_style, get_colors, get_output_dir_for_topic, save_figure

METADATA = {
    "topic_id": "FUN-XX",
    "name": "nombre_del_grafico",
    "description": "Descripción breve",
    "used_in": ["theory/archivo.md"],
    "section": "X.X",
}

def generate() -> plt.Figure:
    """Genera el gráfico de [descripción].
    
    Sigue las guías de estilo de graphics_style_guide.md
    """
    setup_style()
    colors = get_colors()
    
    # Layout con GridSpec
    fig = plt.figure(figsize=(12, 7), layout='constrained')
    gs = fig.add_gridspec(1, 2, width_ratios=[1.3, 1], wspace=0.08)
    
    ax = fig.add_subplot(gs[0])
    ax_info = fig.add_subplot(gs[1])
    
    # === PANEL FIGURA ===
    # ... dibujar figura ...
    ax.set_aspect('equal')
    ax.axis('off')
    
    # === PANEL INFORMACIÓN ===
    ax_info.axis('off')
    ax_info.set_xlim(0, 1)
    ax_info.set_ylim(0, 1)
    
    # Caja de fórmula (OBLIGATORIA)
    ax_info.add_patch(plt.Rectangle((0.05, 0.80), 0.9, 0.16,
                      facecolor='#fffbeb', edgecolor=colors['tertiary'], lw=2,
                      transform=ax_info.transAxes))
    ax_info.text(0.5, 0.90, 'FÓRMULA', fontsize=9, fontweight='bold',
                ha='center', color=colors['tertiary'])
    ax_info.text(0.5, 0.84, r'$fórmula$', fontsize=20, ha='center',
                color=colors['tertiary'], fontweight='bold')
    
    # Leyenda
    ax_info.axhline(y=0.76, xmin=0.05, xmax=0.95, color='#e5e7eb', lw=1)
    ax_info.text(0.5, 0.72, 'Leyenda', fontsize=10, fontweight='bold', ha='center')
    # ... items de leyenda ...
    
    # Título
    fig.suptitle('Título del Gráfico', fontsize=14, fontweight='bold')
    
    return fig

def get_output_dir():
    return get_output_dir_for_topic(METADATA["topic_id"])

if __name__ == "__main__":
    fig = generate()
    paths = save_figure(fig, get_output_dir(), METADATA["name"])
    print(f"✅ Generado: {paths}")
```

---

## Historial de Cambios

| Fecha | Cambio |
|-------|--------|
| 2026-01-03 | Creación inicial del documento |
| 2026-01-03 | Añadida sección de caja de fórmula destacada |

