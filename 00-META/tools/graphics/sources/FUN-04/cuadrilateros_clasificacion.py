"""
Gráfico: Clasificación Jerárquica de Cuadriláteros
===================================================

Topic: FUN-04 Geometría
Usado en: theory/FUN-04-Teoria-Geometria.md (Sección 4.4)

Reemplaza el diagrama ASCII de clasificación de cuadriláteros:
```
Cuadriláteros
├── Paralelogramos (lados opuestos paralelos)
│   ├── Rectángulo (4 ángulos rectos)
│   ├── Rombo (4 lados iguales)
│   └── Cuadrado (rectángulo + rombo)
└── No paralelogramos
    ├── Trapecio (un par de lados paralelos)
    └── Trapezoide (ningún lado paralelo)
```
"""

import sys
from pathlib import Path

# Añadir el directorio de templates al path
sys.path.insert(0, str(Path(__file__).parent.parent))

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

from templates import (
    setup_style,
    get_colors,
    get_output_dir_for_topic,
    save_figure,
)

# ============================================================
# Metadatos del Gráfico
# ============================================================

METADATA = {
    "topic_id": "FUN-04",
    "name": "cuadrilateros_clasificacion",
    "description": "Diagrama jerárquico de clasificación de cuadriláteros",
    "used_in": ["theory/FUN-04-Teoria-Geometria.md"],
    "section": "4.4 Cuadriláteros",
    "replaces_ascii": True,
}

# ============================================================
# Función de Generación
# ============================================================

def generate() -> plt.Figure:
    """
    Genera el diagrama de clasificación de cuadriláteros.
    
    Returns:
        Figura de matplotlib con el diagrama.
    """
    setup_style()
    colors = get_colors()
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Configuración del diagrama
    box_width = 2.8
    box_height = 0.7
    v_spacing = 1.8
    y_start = 6
    
    # Definir estructura jerárquica
    # (nombre, x_position, nivel, color_key)
    boxes = [
        # Nivel 0 - Raíz
        ("Cuadriláteros", 0, 0, 'primary'),
        
        # Nivel 1 - Primera división
        ("Paralelogramos", -3.5, 1, 'primary'),
        ("No Paralelogramos", 3.5, 1, 'tertiary'),
        
        # Nivel 2 - Tipos específicos
        ("Rectángulo", -5.5, 2, 'accent'),
        ("Rombo", -2, 2, 'accent'),
        ("Trapecio", 2.5, 2, 'secondary'),
        ("Trapezoide", 5.5, 2, 'secondary'),
        
        # Nivel 3 - Caso especial
        ("Cuadrado", -3.75, 3, 'accent'),
    ]
    
    # Subnotas para cada caja
    subnotes = {
        "Paralelogramos": "(lados opuestos paralelos)",
        "Rectángulo": "(4 ángulos rectos)",
        "Rombo": "(4 lados iguales)",
        "Cuadrado": "(rectángulo + rombo)",
        "Trapecio": "(1 par paralelo)",
        "Trapezoide": "(ningún paralelo)",
    }
    
    # Diccionario de posiciones
    positions = {}
    
    # Dibujar cajas
    for name, x, level, color_key in boxes:
        y = y_start - level * v_spacing
        
        # Seleccionar colores
        if color_key == 'primary':
            face_color = colors['primary']
            alpha = 0.15
        elif color_key == 'accent':
            face_color = colors['accent']
            alpha = 0.2
        elif color_key == 'secondary':
            face_color = colors['secondary']
            alpha = 0.15
        else:
            face_color = colors['tertiary']
            alpha = 0.15
        
        # Dibujar caja con esquinas redondeadas
        rect = patches.FancyBboxPatch(
            (x - box_width/2, y - box_height/2),
            box_width, box_height,
            boxstyle="round,pad=0.05,rounding_size=0.2",
            facecolor=face_color,
            edgecolor=colors['text'],
            alpha=alpha,
            linewidth=2
        )
        ax.add_patch(rect)
        
        # Borde más oscuro
        rect_border = patches.FancyBboxPatch(
            (x - box_width/2, y - box_height/2),
            box_width, box_height,
            boxstyle="round,pad=0.05,rounding_size=0.2",
            facecolor='none',
            edgecolor=face_color,
            linewidth=2,
            alpha=0.8
        )
        ax.add_patch(rect_border)
        
        # Texto principal
        ax.text(x, y + 0.08, name, 
                ha='center', va='center',
                fontsize=11, fontweight='bold',
                color=colors['text'])
        
        # Subnota si existe
        if name in subnotes:
            ax.text(x, y - 0.22, subnotes[name],
                    ha='center', va='center',
                    fontsize=8, style='italic',
                    color=colors['text'], alpha=0.7)
        
        positions[name] = (x, y)
    
    # Definir conexiones
    connections = [
        ("Cuadriláteros", "Paralelogramos"),
        ("Cuadriláteros", "No Paralelogramos"),
        ("Paralelogramos", "Rectángulo"),
        ("Paralelogramos", "Rombo"),
        ("No Paralelogramos", "Trapecio"),
        ("No Paralelogramos", "Trapezoide"),
        ("Rectángulo", "Cuadrado"),
        ("Rombo", "Cuadrado"),
    ]
    
    # Dibujar conexiones
    for parent, child in connections:
        px, py = positions[parent]
        cx, cy = positions[child]
        
        # Punto de salida (abajo del padre)
        start_y = py - box_height/2
        # Punto de llegada (arriba del hijo)
        end_y = cy + box_height/2
        
        # Punto medio para curva
        mid_y = (start_y + end_y) / 2
        
        # Dibujar línea con curva suave
        ax.plot([px, px], [start_y, mid_y], 
                color=colors['text'], linewidth=1.5, alpha=0.5)
        ax.plot([px, cx], [mid_y, mid_y], 
                color=colors['text'], linewidth=1.5, alpha=0.5)
        ax.plot([cx, cx], [mid_y, end_y], 
                color=colors['text'], linewidth=1.5, alpha=0.5)
    
    # Dibujar pequeños ejemplos de figuras
    example_size = 0.4
    examples = {
        "Rectángulo": 'rectangle',
        "Rombo": 'rhombus', 
        "Cuadrado": 'square',
        "Trapecio": 'trapezoid',
        "Trapezoide": 'trapezium',
    }
    
    for name, shape in examples.items():
        x, y = positions[name]
        x_offset = box_width/2 + 0.5
        draw_mini_shape(ax, (x + x_offset, y), shape, example_size, colors)
    
    # Configurar ejes
    ax.set_xlim(-9, 9)
    ax.set_ylim(-1, 7.5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Título
    ax.set_title('Clasificación de Cuadriláteros', 
                fontsize=16, fontweight='bold', pad=20)
    
    return fig


def draw_mini_shape(ax, center, shape_type, size, colors):
    """Dibuja una mini figura de ejemplo."""
    cx, cy = center
    s = size
    
    if shape_type == 'square':
        verts = [(cx-s, cy-s), (cx+s, cy-s), (cx+s, cy+s), (cx-s, cy+s)]
    elif shape_type == 'rectangle':
        verts = [(cx-s*1.3, cy-s*0.7), (cx+s*1.3, cy-s*0.7), 
                (cx+s*1.3, cy+s*0.7), (cx-s*1.3, cy+s*0.7)]
    elif shape_type == 'rhombus':
        verts = [(cx, cy-s), (cx+s*0.8, cy), (cx, cy+s), (cx-s*0.8, cy)]
    elif shape_type == 'trapezoid':
        verts = [(cx-s, cy-s*0.6), (cx+s, cy-s*0.6),
                (cx+s*0.6, cy+s*0.6), (cx-s*0.6, cy+s*0.6)]
    else:  # trapezium
        verts = [(cx-s, cy-s*0.6), (cx+s*0.8, cy-s*0.4),
                (cx+s*0.4, cy+s*0.5), (cx-s*0.6, cy+s*0.3)]
    
    polygon = patches.Polygon(
        verts,
        closed=True,
        facecolor=colors['primary'],
        edgecolor=colors['text'],
        alpha=0.3,
        linewidth=1
    )
    ax.add_patch(polygon)


def get_output_dir():
    """Retorna el directorio de salida para este gráfico."""
    return get_output_dir_for_topic(METADATA["topic_id"])


# ============================================================
# Ejecución Directa
# ============================================================

if __name__ == "__main__":
    print(f"Generando: {METADATA['name']}")
    fig = generate()
    output_dir = get_output_dir()
    paths = save_figure(fig, output_dir, METADATA["name"])
    print(f"✅ Guardado en: {output_dir}")
    for fmt, path in paths.items():
        print(f"   • {fmt}: {path.name}")
