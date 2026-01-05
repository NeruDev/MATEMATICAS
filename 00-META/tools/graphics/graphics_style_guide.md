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

## 11. Gráficos 3D para Cálculo Vectorial

### 11.1 Principios para Visualización 3D

Los gráficos 3D requieren consideraciones especiales para mantener la claridad didáctica:

> **Regla fundamental 3D:** Priorizar la comprensión sobre la complejidad visual. Usar múltiples vistas cuando una sola perspectiva no sea suficiente.

### 11.2 Configuración de Ejes 3D

```python
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(14, 8), layout='constrained')

# Opción 1: Un solo gráfico 3D con panel de info
gs = fig.add_gridspec(1, 2, width_ratios=[1.5, 1], wspace=0.1)
ax_3d = fig.add_subplot(gs[0], projection='3d')
ax_info = fig.add_subplot(gs[1])

# Opción 2: Múltiples vistas 3D
gs = fig.add_gridspec(2, 2, height_ratios=[1.2, 1])
ax_main = fig.add_subplot(gs[0, 0], projection='3d')  # Vista principal
ax_top = fig.add_subplot(gs[0, 1], projection='3d')   # Vista superior
ax_info = fig.add_subplot(gs[1, :])                   # Panel de info
```

### 11.3 Configuración Estándar de Ejes 3D

```python
# Configuración base para claridad
ax_3d.set_xlabel('X', fontsize=11, labelpad=10)
ax_3d.set_ylabel('Y', fontsize=11, labelpad=10)
ax_3d.set_zlabel('Z', fontsize=11, labelpad=10)

# Ángulo de vista óptimo (ajustar según el objeto)
ax_3d.view_init(elev=25, azim=45)  # Elevación y azimut

# Escala igual en todos los ejes (IMPORTANTE para geometría)
ax_3d.set_box_aspect([1, 1, 1])

# Rejilla y fondo
ax_3d.xaxis.pane.fill = False
ax_3d.yaxis.pane.fill = False
ax_3d.zaxis.pane.fill = False
ax_3d.xaxis.pane.set_edgecolor('#e5e7eb')
ax_3d.yaxis.pane.set_edgecolor('#e5e7eb')
ax_3d.zaxis.pane.set_edgecolor('#e5e7eb')
```

### 11.4 Tipos de Gráficos 3D

#### Superficies (`plot_surface`)
Para funciones $z = f(x, y)$: superficies, paraboloides, planos tangentes.

```python
# Crear malla
x = np.linspace(-3, 3, 50)
y = np.linspace(-3, 3, 50)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# Superficie con colores
surf = ax_3d.plot_surface(X, Y, Z, 
                          cmap='viridis',      # Mapa de colores
                          alpha=0.8,            # Transparencia
                          edgecolor='none',     # Sin bordes de malla
                          antialiased=True)

# Barra de color (opcional)
fig.colorbar(surf, ax=ax_3d, shrink=0.5, aspect=10, label='z')
```

#### Superficies con Wireframe
Para mostrar estructura sin llenar.

```python
ax_3d.plot_wireframe(X, Y, Z, 
                     color=colors['primary'],
                     linewidth=0.5, 
                     alpha=0.7,
                     rstride=3, cstride=3)  # Densidad del wireframe
```

#### Curvas en el Espacio (`plot`)
Para funciones vectoriales $\mathbf{r}(t) = \langle x(t), y(t), z(t) \rangle$.

```python
t = np.linspace(0, 2*np.pi, 100)
x = np.cos(t)
y = np.sin(t)
z = t / (2*np.pi)

ax_3d.plot(x, y, z, 
           color=colors['primary'], 
           linewidth=2.5,
           label='Hélice')
```

#### Vectores 3D (`quiver`)
Para campos vectoriales, gradientes, normales.

```python
# Un solo vector
ax_3d.quiver(x0, y0, z0,    # Punto inicial
             dx, dy, dz,     # Componentes
             color=colors['secondary'],
             arrow_length_ratio=0.1,
             linewidth=2)

# Campo vectorial (grid de vectores)
ax_3d.quiver(X, Y, Z, U, V, W,
             length=0.3,
             normalize=True,
             color=colors['primary'],
             alpha=0.6)
```

#### Curvas de Nivel en 3D (`contour3D`, `contourf`)
Para visualizar curvas de nivel sobre la superficie.

```python
# Curvas de nivel proyectadas en z=0
ax_3d.contour(X, Y, Z, zdir='z', offset=z_min, 
              cmap='coolwarm', levels=10, alpha=0.7)

# Curvas de nivel en la propia superficie
ax_3d.contour3D(X, Y, Z, 50, cmap='viridis')
```

### 11.5 Paleta de Colores para 3D

| Tipo de Objeto | Colormap/Color | Uso |
|----------------|----------------|-----|
| Superficies principales | `viridis`, `plasma` | Funciones z=f(x,y) |
| Planos tangentes | `#3b82f6` (primary) + alpha | Aproximaciones lineales |
| Vectores normales | `#dc2626` (rojo) | Gradientes, normales |
| Curvas paramétricas | `colors['primary']` | Trayectorias |
| Campos vectoriales | `coolwarm` o flechas sólidas | Gradiente, flujo |
| Regiones/dominios | `#10b981` (secondary) + alpha | Áreas de integración |

### 11.6 Transparencia y Capas

La transparencia es **esencial** en 3D para mostrar relaciones:

```python
# Superficie semi-transparente (para ver vectores a través)
ax_3d.plot_surface(X, Y, Z, alpha=0.5, cmap='viridis')

# Plano tangente transparente
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
verts = [list(zip(plane_x, plane_y, plane_z))]
ax_3d.add_collection3d(Poly3DCollection(verts, 
                       alpha=0.3, 
                       facecolor=colors['secondary'],
                       edgecolor=colors['secondary']))
```

### 11.7 Vistas Múltiples Recomendadas

Para conceptos complejos, usar múltiples perspectivas:

```python
# Vista isométrica (general)
ax1.view_init(elev=30, azim=45)

# Vista superior (proyección xy)
ax2.view_init(elev=90, azim=0)

# Vista frontal (proyección xz)
ax3.view_init(elev=0, azim=0)

# Vista lateral (proyección yz)
ax4.view_init(elev=0, azim=90)
```

### 11.8 Gráficos Específicos de Cálculo Vectorial

#### Vectores en el Espacio (CV-01)
```python
# Sistema de coordenadas 3D con vectores canónicos
origin = np.array([0, 0, 0])
ax_3d.quiver(*origin, 1, 0, 0, color='#dc2626', label='i')
ax_3d.quiver(*origin, 0, 1, 0, color='#10b981', label='j')
ax_3d.quiver(*origin, 0, 0, 1, color='#3b82f6', label='k')

# Vector genérico como combinación lineal
v = [2, 3, 1]
ax_3d.quiver(*origin, *v, color=colors['accent'], linewidth=2)
```

#### Superficies y Curvas de Nivel (CV-04)
```python
# Superficie con curvas de nivel proyectadas
Z = X**2 + Y**2  # Paraboloide
ax_3d.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7)
ax_3d.contour(X, Y, Z, zdir='z', offset=0, cmap='viridis', levels=8)
```

#### Plano Tangente y Gradiente (CV-04)
```python
# Superficie
ax_3d.plot_surface(X, Y, Z, alpha=0.5, cmap='coolwarm')

# Punto de tangencia
ax_3d.scatter([x0], [y0], [z0], color='red', s=100, zorder=5)

# Plano tangente (como superficie pequeña)
T = z0 + fx*(X_plane - x0) + fy*(Y_plane - y0)
ax_3d.plot_surface(X_plane, Y_plane, T, alpha=0.6, color=colors['secondary'])

# Vector gradiente
ax_3d.quiver(x0, y0, z0, -fx, -fy, 1, color='#dc2626', 
             arrow_length_ratio=0.15, linewidth=2.5,
             label=r'$\nabla f$')
```

#### Integrales de Línea y Superficie (CV-05)
```python
# Curva cerrada sobre superficie
theta = np.linspace(0, 2*np.pi, 100)
x_curve = np.cos(theta)
y_curve = np.sin(theta)
z_curve = f(x_curve, y_curve)
ax_3d.plot(x_curve, y_curve, z_curve, color=colors['accent'], linewidth=3)

# Región de integración (sombreada)
ax_3d.plot_surface(X_region, Y_region, Z_region, 
                   alpha=0.4, color=colors['secondary'])
```

### 11.9 Animaciones y Rotación Interactiva

Para notebooks o presentaciones, considerar:

```python
# Rotación automática (para GIFs/videos)
for angle in range(0, 360, 5):
    ax_3d.view_init(elev=30, azim=angle)
    plt.savefig(f'frame_{angle:03d}.png')
```

### 11.10 Layout Completo para Gráficos 3D

```python
def generate() -> plt.Figure:
    """Gráfico 3D con panel informativo."""
    setup_style()
    colors = get_colors()
    
    fig = plt.figure(figsize=(14, 8), layout='constrained')
    gs = fig.add_gridspec(1, 2, width_ratios=[1.4, 1], wspace=0.08)
    
    ax_3d = fig.add_subplot(gs[0], projection='3d')
    ax_info = fig.add_subplot(gs[1])
    
    # === PANEL 3D ===
    # ... dibujar superficie/vectores/curvas ...
    
    ax_3d.set_xlabel('X')
    ax_3d.set_ylabel('Y')
    ax_3d.set_zlabel('Z')
    ax_3d.view_init(elev=25, azim=45)
    ax_3d.set_box_aspect([1, 1, 1])
    
    # === PANEL INFORMACIÓN ===
    ax_info.axis('off')
    ax_info.set_xlim(0, 1)
    ax_info.set_ylim(0, 1)
    
    # Caja de fórmula (OBLIGATORIA)
    ax_info.add_patch(plt.Rectangle((0.05, 0.80), 0.9, 0.16,
                      facecolor='#fffbeb', edgecolor=colors['tertiary'], lw=2))
    ax_info.text(0.5, 0.90, 'FÓRMULA', fontsize=9, fontweight='bold',
                ha='center', color=colors['tertiary'])
    ax_info.text(0.5, 0.84, r'$\nabla f = \langle f_x, f_y, f_z \rangle$',
                fontsize=18, ha='center', color=colors['tertiary'], fontweight='bold')
    
    fig.suptitle('Título del Gráfico 3D', fontsize=14, fontweight='bold')
    
    return fig
```

### 11.11 Checklist para Gráficos 3D

- [ ] **Ángulo de vista:** elegido para máxima claridad
- [ ] **Transparencia:** superficies con alpha < 1 cuando hay superposición
- [ ] **Escala igual:** `set_box_aspect([1,1,1])` para geometría
- [ ] **Etiquetas de ejes:** X, Y, Z visibles y legibles
- [ ] **Leyenda:** colores/símbolos explicados en panel info
- [ ] **Múltiples vistas:** si una vista no es suficiente
- [ ] **Colormaps:** usar mapas perceptualmente uniformes (viridis, plasma)
- [ ] **Flechas:** `arrow_length_ratio` apropiado para quiver

---

## 12. Gráficos Específicos por Tema de Cálculo Vectorial

### CV-01: Vectores en el Espacio
| Gráfico | Elementos | Vista recomendada |
|---------|-----------|-------------------|
| Sistema coordenado 3D | Ejes, vectores i,j,k | Isométrica (30°, 45°) |
| Vector posición | Punto P, vector OP, componentes | Isométrica |
| Producto cruz | u, v, u×v, paralelogramo | Múltiples vistas |
| Recta en el espacio | Punto, vector director, recta | Isométrica |
| Plano en el espacio | Vector normal, plano, punto | Vista que muestre normal |

### CV-03: Funciones Vectoriales
| Gráfico | Elementos | Vista recomendada |
|---------|-----------|-------------------|
| Curva en el espacio | r(t), puntos, tangentes | Isométrica rotable |
| Vectores TNB | Curva, T, N, B en punto | Múltiples vistas |
| Curvatura | Círculo osculador, curva | Vista del plano osculador |
| Hélice | Curva, cilindro de referencia | Isométrica |

### CV-04: Funciones de Varias Variables
| Gráfico | Elementos | Vista recomendada |
|---------|-----------|-------------------|
| Superficie z=f(x,y) | Superficie coloreada por altura | Isométrica |
| Curvas de nivel | Superficie + proyección | Vista superior + 3D |
| Plano tangente | Superficie, punto, plano | Isométrica |
| Gradiente | Superficie, ∇f, curvas de nivel | Vista superior + 3D |
| Derivada direccional | Curva en dirección u, pendiente | Lateral |

### CV-05: Integración Múltiple
| Gráfico | Elementos | Vista recomendada |
|---------|-----------|-------------------|
| Región de integración | Dominio D, límites | Vista superior |
| Sólido de integración | Volumen, superficies límite | Isométrica |
| Cambio de coordenadas | Cartesiano vs polar/cilíndrico | Lado a lado |
| Integral de superficie | Superficie, elemento dS | Isométrica |

---

## Historial de Cambios

| Fecha | Cambio |
|-------|--------|
| 2026-01-03 | Creación inicial del documento |
| 2026-01-03 | Añadida sección de caja de fórmula destacada |
| 2026-01-04 | Añadidas secciones 11-12: Directivas para gráficos 3D (Cálculo Vectorial) |

