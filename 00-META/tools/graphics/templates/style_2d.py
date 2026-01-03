"""
Plantillas de Estilo para Gráficos 2D
=====================================

Funciones especializadas para geometría plana:
- Triángulos con líneas notables
- Cuadriláteros y polígonos
- Circunferencias y arcos
- Ángulos y transversales

Uso:
    from templates.style_2d import (
        draw_triangle_with_labels,
        draw_circle_with_elements,
        draw_parallel_lines_with_transversal
    )
"""

from __future__ import annotations

from typing import Dict, List, Optional, Tuple

import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np

from .style_common import (
    annotate_point,
    draw_polygon,
    get_colors,
    get_figure_size,
    get_line_widths,
    setup_style,
)


# ============================================================
# Triángulos
# ============================================================

def create_triangle_figure(
    vertices: Dict[str, Tuple[float, float]],
    title: Optional[str] = None,
    show_labels: bool = True,
    figsize: Optional[Tuple[float, float]] = None,
    padding: float = 1.0
) -> Tuple[plt.Figure, plt.Axes]:
    """
    Crea una figura con un triángulo básico.
    
    Args:
        vertices: Diccionario {'A': (x, y), 'B': (x, y), 'C': (x, y)}
        title: Título opcional de la figura.
        show_labels: Si mostrar etiquetas de vértices.
        figsize: Tamaño de figura o None para usar default.
        padding: Espacio extra alrededor del triángulo.
        
    Returns:
        Tupla (Figure, Axes).
    """
    setup_style()
    colors = get_colors()
    
    if figsize is None:
        figsize = get_figure_size('square')
    
    fig, ax = plt.subplots(figsize=figsize)
    
    # Extraer puntos en orden
    points = list(vertices.values())
    labels = list(vertices.keys())
    
    # Dibujar triángulo
    draw_polygon(ax, points, close=True)
    
    # Etiquetas de vértices
    if show_labels:
        for label, point in vertices.items():
            # Calcular offset basado en posición relativa
            centroid = np.mean(points, axis=0)
            direction = np.array(point) - centroid
            offset = direction / np.linalg.norm(direction) * 15
            
            annotate_point(ax, point, f'${label}$', offset=tuple(offset))
    
    # Configurar ejes
    all_x = [p[0] for p in points]
    all_y = [p[1] for p in points]
    
    ax.set_xlim(min(all_x) - padding, max(all_x) + padding)
    ax.set_ylim(min(all_y) - padding, max(all_y) + padding)
    ax.set_aspect('equal')
    ax.axis('off')
    
    if title:
        ax.set_title(title, fontsize=14, pad=10)
    
    return fig, ax


def draw_altitude(
    ax: plt.Axes,
    vertex: Tuple[float, float],
    base_start: Tuple[float, float],
    base_end: Tuple[float, float],
    color: Optional[str] = None,
    label: Optional[str] = None,
    show_right_angle: bool = True
) -> Tuple[float, float]:
    """
    Dibuja la altura desde un vértice a la base opuesta.
    
    Args:
        ax: Axes de matplotlib.
        vertex: Vértice desde donde se traza la altura.
        base_start: Inicio de la base.
        base_end: Fin de la base.
        color: Color de la altura.
        label: Etiqueta para la altura.
        show_right_angle: Si mostrar el marcador de ángulo recto.
        
    Returns:
        Coordenadas del pie de la altura.
    """
    if color is None:
        color = get_colors()['secondary']
    
    # Calcular pie de la altura (proyección)
    v = np.array(vertex)
    a = np.array(base_start)
    b = np.array(base_end)
    
    ab = b - a
    av = v - a
    
    # Proyección de av sobre ab
    t = np.dot(av, ab) / np.dot(ab, ab)
    foot = a + t * ab
    
    # Dibujar altura
    ax.plot([vertex[0], foot[0]], [vertex[1], foot[1]], 
            color=color, linewidth=2, linestyle='--')
    
    # Marcador de ángulo recto
    if show_right_angle:
        size = 0.3
        # Vector unitario de la base
        ab_unit = ab / np.linalg.norm(ab)
        # Vector perpendicular (hacia el vértice)
        perp = np.array([-ab_unit[1], ab_unit[0]])
        if np.dot(perp, v - foot) < 0:
            perp = -perp
        
        # Dibujar cuadrado
        p1 = foot + ab_unit * size
        p2 = p1 + perp * size
        p3 = foot + perp * size
        
        ax.plot([foot[0], p1[0]], [foot[1], p1[1]], color=color, linewidth=1)
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=color, linewidth=1)
        ax.plot([p2[0], p3[0]], [p2[1], p3[1]], color=color, linewidth=1)
    
    # Etiqueta
    if label:
        mid = (np.array(vertex) + foot) / 2
        ax.annotate(label, mid + np.array([0.2, 0]), fontsize=12, color=color)
    
    return tuple(foot)


def draw_median(
    ax: plt.Axes,
    vertex: Tuple[float, float],
    opposite_start: Tuple[float, float],
    opposite_end: Tuple[float, float],
    color: Optional[str] = None,
    label: Optional[str] = None
) -> Tuple[float, float]:
    """
    Dibuja la mediana desde un vértice al punto medio del lado opuesto.
    
    Returns:
        Coordenadas del punto medio.
    """
    if color is None:
        color = get_colors()['accent']
    
    midpoint = ((opposite_start[0] + opposite_end[0]) / 2,
                (opposite_start[1] + opposite_end[1]) / 2)
    
    ax.plot([vertex[0], midpoint[0]], [vertex[1], midpoint[1]],
            color=color, linewidth=1.5, linestyle='-.')
    
    # Marcar punto medio
    ax.plot(*midpoint, 'o', color=color, markersize=5)
    
    if label:
        mid = ((vertex[0] + midpoint[0]) / 2 + 0.2,
               (vertex[1] + midpoint[1]) / 2)
        ax.annotate(label, mid, fontsize=11, color=color)
    
    return midpoint


# ============================================================
# Rectas Paralelas y Transversales
# ============================================================

def draw_parallel_lines_with_transversal(
    ax: plt.Axes,
    y_positions: Tuple[float, float],
    x_range: Tuple[float, float],
    transversal_points: Tuple[Tuple[float, float], Tuple[float, float]],
    line_color: Optional[str] = None,
    trans_color: Optional[str] = None,
    show_parallel_marks: bool = True
) -> Dict:
    """
    Dibuja dos rectas paralelas con una transversal.
    
    Args:
        ax: Axes de matplotlib.
        y_positions: Posiciones Y de las dos paralelas.
        x_range: Rango X para las paralelas (x_min, x_max).
        transversal_points: Puntos de inicio y fin de la transversal.
        line_color: Color de las paralelas.
        trans_color: Color de la transversal.
        show_parallel_marks: Si mostrar las marcas de paralelismo.
        
    Returns:
        Diccionario con puntos de intersección.
    """
    colors = get_colors()
    
    if line_color is None:
        line_color = colors['primary']
    if trans_color is None:
        trans_color = colors['secondary']
    
    y1, y2 = y_positions
    x_min, x_max = x_range
    t_start, t_end = transversal_points
    
    # Dibujar paralelas
    ax.plot([x_min, x_max], [y1, y1], color=line_color, linewidth=2)
    ax.plot([x_min, x_max], [y2, y2], color=line_color, linewidth=2)
    
    # Dibujar transversal
    ax.plot([t_start[0], t_end[0]], [t_start[1], t_end[1]], 
            color=trans_color, linewidth=2)
    
    # Calcular intersecciones
    # Transversal: y = m*x + b
    m = (t_end[1] - t_start[1]) / (t_end[0] - t_start[0])
    b = t_start[1] - m * t_start[0]
    
    x_int1 = (y1 - b) / m
    x_int2 = (y2 - b) / m
    
    intersections = {
        'line1': (x_int1, y1),
        'line2': (x_int2, y2)
    }
    
    # Marcas de paralelismo
    if show_parallel_marks:
        mark_x = (x_min + x_max) / 2
        arrow_len = 0.15
        
        for y in [y1, y2]:
            ax.annotate('', xy=(mark_x + arrow_len, y), 
                       xytext=(mark_x - arrow_len, y),
                       arrowprops=dict(arrowstyle='->', color=line_color, lw=1.5))
    
    return intersections


def draw_angle_arc(
    ax: plt.Axes,
    vertex: Tuple[float, float],
    angle_start: float,
    angle_end: float,
    radius: float = 0.5,
    color: Optional[str] = None,
    label: Optional[str] = None,
    label_radius_factor: float = 1.5
) -> None:
    """
    Dibuja un arco para representar un ángulo.
    
    Args:
        vertex: Centro del arco (vértice del ángulo).
        angle_start: Ángulo inicial en grados.
        angle_end: Ángulo final en grados.
        radius: Radio del arco.
        color: Color del arco.
        label: Etiqueta del ángulo.
        label_radius_factor: Factor para posicionar la etiqueta.
    """
    if color is None:
        color = get_colors()['tertiary']
    
    # Crear arco
    arc = patches.Arc(
        vertex, 
        2 * radius, 
        2 * radius,
        angle=0,
        theta1=angle_start,
        theta2=angle_end,
        color=color,
        linewidth=1.5
    )
    ax.add_patch(arc)
    
    # Etiqueta
    if label:
        mid_angle = np.radians((angle_start + angle_end) / 2)
        label_r = radius * label_radius_factor
        label_pos = (
            vertex[0] + label_r * np.cos(mid_angle),
            vertex[1] + label_r * np.sin(mid_angle)
        )
        ax.annotate(label, label_pos, fontsize=11, color=color, ha='center', va='center')


# ============================================================
# Circunferencias
# ============================================================

def draw_circle(
    ax: plt.Axes,
    center: Tuple[float, float],
    radius: float,
    color: Optional[str] = None,
    fill: bool = False,
    fill_alpha: float = 0.1,
    linestyle: str = '-'
) -> patches.Circle:
    """
    Dibuja una circunferencia.
    
    Returns:
        Objeto Circle de matplotlib.
    """
    if color is None:
        color = get_colors()['primary']
    
    circle = patches.Circle(
        center,
        radius,
        fill=fill,
        facecolor=color if fill else 'none',
        edgecolor=color,
        linewidth=2,
        linestyle=linestyle,
        alpha=fill_alpha if fill else 1.0
    )
    ax.add_patch(circle)
    
    return circle


def draw_radius(
    ax: plt.Axes,
    center: Tuple[float, float],
    endpoint: Tuple[float, float],
    color: Optional[str] = None,
    label: Optional[str] = None,
    label_position: str = 'mid'
) -> None:
    """
    Dibuja un radio de la circunferencia.
    
    Args:
        center: Centro de la circunferencia.
        endpoint: Punto en la circunferencia.
        color: Color del radio.
        label: Etiqueta del radio.
        label_position: 'mid' o 'end'.
    """
    if color is None:
        color = get_colors()['secondary']
    
    ax.plot([center[0], endpoint[0]], [center[1], endpoint[1]],
            color=color, linewidth=1.5)
    
    if label:
        if label_position == 'mid':
            pos = ((center[0] + endpoint[0]) / 2,
                   (center[1] + endpoint[1]) / 2)
        else:
            pos = endpoint
        ax.annotate(label, pos, fontsize=11, color=color,
                   xytext=(5, 5), textcoords='offset points')


# ============================================================
# Cuadriláteros
# ============================================================

def draw_quadrilateral_hierarchy(
    ax: plt.Axes,
    x_center: float = 0,
    y_start: float = 5,
    box_width: float = 3,
    box_height: float = 0.8,
    v_spacing: float = 1.2
) -> None:
    """
    Dibuja el diagrama jerárquico de clasificación de cuadriláteros.
    
    Este es un diagrama tipo árbol que muestra la relación entre
    los diferentes tipos de cuadriláteros.
    """
    colors = get_colors()
    
    # Definir niveles y contenido
    hierarchy = {
        0: [("Cuadriláteros", 0)],
        1: [("Paralelogramos", -2), ("No Paralelogramos", 2)],
        2: [("Rectángulo", -3), ("Rombo", -1), ("Trapecio", 1.5), ("Trapezoide", 3.5)],
        3: [("Cuadrado", -2)],
    }
    
    box_positions = {}
    
    # Dibujar cajas
    for level, items in hierarchy.items():
        y = y_start - level * v_spacing
        
        for name, x_offset in items:
            x = x_center + x_offset
            
            # Color según tipo
            if name in ["Cuadrado"]:
                facecolor = colors['accent']
                alpha = 0.2
            elif name in ["Rectángulo", "Rombo", "Paralelogramos"]:
                facecolor = colors['primary']
                alpha = 0.15
            else:
                facecolor = colors['tertiary']
                alpha = 0.1
            
            # Dibujar caja
            rect = patches.FancyBboxPatch(
                (x - box_width/2, y - box_height/2),
                box_width, box_height,
                boxstyle="round,pad=0.05",
                facecolor=facecolor,
                edgecolor=colors['text'],
                alpha=alpha,
                linewidth=1.5
            )
            ax.add_patch(rect)
            
            # Texto
            ax.text(x, y, name, ha='center', va='center', 
                   fontsize=10, fontweight='bold', color=colors['text'])
            
            box_positions[name] = (x, y)
    
    # Dibujar conexiones
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
    
    for parent, child in connections:
        if parent in box_positions and child in box_positions:
            px, py = box_positions[parent]
            cx, cy = box_positions[child]
            
            # Línea desde abajo del padre hasta arriba del hijo
            ax.plot([px, cx], [py - box_height/2, cy + box_height/2],
                   color=colors['grid'], linewidth=1.5, linestyle='-')


def create_quadrilateral_example(
    quad_type: str,
    ax: plt.Axes,
    center: Tuple[float, float] = (0, 0),
    size: float = 2
) -> None:
    """
    Dibuja un ejemplo de cuadrilátero del tipo especificado.
    
    Args:
        quad_type: 'square', 'rectangle', 'rhombus', 'parallelogram', 
                   'trapezoid', 'trapezium'
    """
    colors = get_colors()
    cx, cy = center
    s = size / 2
    
    if quad_type == 'square':
        vertices = [(cx-s, cy-s), (cx+s, cy-s), (cx+s, cy+s), (cx-s, cy+s)]
    elif quad_type == 'rectangle':
        vertices = [(cx-s*1.5, cy-s*0.8), (cx+s*1.5, cy-s*0.8), 
                   (cx+s*1.5, cy+s*0.8), (cx-s*1.5, cy+s*0.8)]
    elif quad_type == 'rhombus':
        vertices = [(cx, cy-s), (cx+s*0.8, cy), (cx, cy+s), (cx-s*0.8, cy)]
    elif quad_type == 'parallelogram':
        offset = s * 0.4
        vertices = [(cx-s+offset, cy-s*0.7), (cx+s+offset, cy-s*0.7),
                   (cx+s-offset, cy+s*0.7), (cx-s-offset, cy+s*0.7)]
    elif quad_type == 'trapezoid':
        vertices = [(cx-s, cy-s*0.7), (cx+s, cy-s*0.7),
                   (cx+s*0.6, cy+s*0.7), (cx-s*0.6, cy+s*0.7)]
    else:  # trapezium / irregular
        vertices = [(cx-s, cy-s*0.8), (cx+s*0.8, cy-s*0.5),
                   (cx+s*0.5, cy+s*0.7), (cx-s*0.7, cy+s*0.4)]
    
    draw_polygon(ax, vertices, fill=True, fill_alpha=0.2)
