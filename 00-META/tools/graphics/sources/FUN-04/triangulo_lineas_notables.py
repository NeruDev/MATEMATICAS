"""
Gráfico: Líneas Notables del Triángulo
======================================

Topic: FUN-04 Geometría
Usado en: theory/FUN-04-Teoria-Geometria.md (Sección 4.3)

Muestra las cuatro líneas notables: mediana, altura, mediatriz, bisectriz.
"""

import sys
from pathlib import Path

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
    "name": "triangulo_lineas_notables",
    "description": "Las cuatro líneas notables del triángulo: mediana, altura, mediatriz, bisectriz",
    "used_in": ["theory/FUN-04-Teoria-Geometria.md"],
    "section": "4.3 Triángulos - Líneas notables",
}

# ============================================================
# Función de Generación
# ============================================================

def generate() -> plt.Figure:
    """
    Genera el diagrama con las cuatro líneas notables.
    
    Returns:
        Figura de matplotlib con 4 subplots.
    """
    setup_style()
    colors = get_colors()
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 12))
    axes = axes.flatten()
    
    # Triángulo base (mismo para todos)
    A = np.array([0, 0])
    B = np.array([6, 0])
    C = np.array([2, 4.5])
    vertices = [A, B, C]
    
    line_configs = [
        ('Mediana', colors['accent'], draw_median),
        ('Altura', colors['secondary'], draw_altura),
        ('Mediatriz', colors['tertiary'], draw_mediatriz),
        ('Bisectriz', '#f59e0b', draw_bisectriz),
    ]
    
    for ax, (title, color, draw_func) in zip(axes, line_configs):
        # Dibujar triángulo base
        triangle = plt.Polygon(vertices, fill=True,
                              facecolor=colors['primary'], alpha=0.1,
                              edgecolor=colors['primary'], linewidth=2)
        ax.add_patch(triangle)
        
        # Etiquetas de vértices
        ax.text(A[0] - 0.3, A[1] - 0.3, '$A$', fontsize=13, fontweight='bold')
        ax.text(B[0] + 0.2, B[1] - 0.3, '$B$', fontsize=13, fontweight='bold')
        ax.text(C[0] - 0.3, C[1] + 0.2, '$C$', fontsize=13, fontweight='bold')
        
        # Dibujar línea notable específica
        draw_func(ax, A, B, C, color)
        
        # Configurar subplot
        ax.set_xlim(-1.5, 7.5)
        ax.set_ylim(-1.5, 6)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title(title, fontsize=14, fontweight='bold', pad=10)
    
    plt.tight_layout()
    
    return fig


def draw_median(ax, A, B, C, color):
    """Dibuja la mediana desde C al punto medio de AB."""
    M = (A + B) / 2  # Punto medio de AB
    
    ax.plot([C[0], M[0]], [C[1], M[1]], color=color, linewidth=2.5)
    ax.plot(*M, 'o', color=color, markersize=8)
    
    # Etiqueta
    ax.text(M[0], M[1] - 0.4, '$M$', fontsize=12, ha='center', color=color)
    
    # Descripción
    ax.text(3, -0.8, 'Une vértice con punto\nmedio del lado opuesto',
            fontsize=10, ha='center', style='italic')
    ax.text(3, 5.3, 'Punto de concurrencia:\nCentroide (G)',
            fontsize=10, ha='center', color=color,
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))


def draw_altura(ax, A, B, C, color):
    """Dibuja la altura desde C perpendicular a AB."""
    # Proyección de C sobre AB
    AB = B - A
    AC = C - A
    t = np.dot(AC, AB) / np.dot(AB, AB)
    H = A + t * AB
    
    ax.plot([C[0], H[0]], [C[1], H[1]], color=color, linewidth=2.5, linestyle='--')
    ax.plot(*H, 'o', color=color, markersize=8)
    
    # Ángulo recto
    size = 0.3
    AB_unit = AB / np.linalg.norm(AB)
    perp = np.array([-AB_unit[1], AB_unit[0]])
    
    ax.plot([H[0], H[0] + size * AB_unit[0]], 
            [H[1], H[1] + size * AB_unit[1]], color=color, linewidth=1.5)
    ax.plot([H[0] + size * AB_unit[0], H[0] + size * AB_unit[0] + size * perp[0]], 
            [H[1] + size * AB_unit[1], H[1] + size * AB_unit[1] + size * perp[1]], 
            color=color, linewidth=1.5)
    
    ax.text(H[0] + 0.3, H[1] - 0.3, '$H$', fontsize=12, color=color)
    
    ax.text(3, -0.8, 'Perpendicular desde vértice\nal lado opuesto',
            fontsize=10, ha='center', style='italic')
    ax.text(3, 5.3, 'Punto de concurrencia:\nOrtocentro (H)',
            fontsize=10, ha='center', color=color,
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))


def draw_mediatriz(ax, A, B, C, color):
    """Dibuja la mediatriz de AB."""
    M = (A + B) / 2
    
    # Dirección perpendicular a AB
    AB = B - A
    perp = np.array([-AB[1], AB[0]])
    perp = perp / np.linalg.norm(perp)
    
    # Extender la mediatriz
    P1 = M - 2.5 * perp
    P2 = M + 2.5 * perp
    
    ax.plot([P1[0], P2[0]], [P1[1], P2[1]], color=color, linewidth=2.5)
    ax.plot(*M, 'o', color=color, markersize=8)
    
    # Marcas de igualdad en AM y MB
    mark_pos_1 = (A + M) / 2
    mark_pos_2 = (M + B) / 2
    mark_len = 0.15
    
    for pos in [mark_pos_1, mark_pos_2]:
        ax.plot([pos[0] - mark_len * perp[0], pos[0] + mark_len * perp[0]],
                [pos[1] - mark_len * perp[1], pos[1] + mark_len * perp[1]],
                color=color, linewidth=2)
    
    ax.text(M[0] + 0.3, M[1] - 0.3, '$M$', fontsize=12, color=color)
    
    ax.text(3, -0.8, 'Perpendicular que pasa\npor punto medio del lado',
            fontsize=10, ha='center', style='italic')
    ax.text(3, 5.3, 'Punto de concurrencia:\nCircuncentro (O)',
            fontsize=10, ha='center', color=color,
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))


def draw_bisectriz(ax, A, B, C, color):
    """Dibuja la bisectriz del ángulo en C."""
    # Vectores desde C hacia A y B
    CA = A - C
    CB = B - C
    
    # Normalizar
    CA_unit = CA / np.linalg.norm(CA)
    CB_unit = CB / np.linalg.norm(CB)
    
    # Bisectriz es la suma de los vectores unitarios
    bisector_dir = CA_unit + CB_unit
    bisector_dir = bisector_dir / np.linalg.norm(bisector_dir)
    
    # Encontrar intersección con AB
    # Parametrización: C + t * bisector_dir = A + s * (B - A)
    AB = B - A
    denom = bisector_dir[0] * AB[1] - bisector_dir[1] * AB[0]
    if abs(denom) > 1e-10:
        t = ((A[0] - C[0]) * AB[1] - (A[1] - C[1]) * AB[0]) / denom
        D = C + t * bisector_dir
    else:
        D = (A + B) / 2  # fallback
    
    ax.plot([C[0], D[0]], [C[1], D[1]], color=color, linewidth=2.5)
    ax.plot(*D, 'o', color=color, markersize=8)
    
    # Arcos para mostrar ángulos iguales
    arc_radius = 0.8
    angle_CA = np.degrees(np.arctan2(CA[1], CA[0]))
    angle_CB = np.degrees(np.arctan2(CB[1], CB[0]))
    angle_mid = np.degrees(np.arctan2(bisector_dir[1], bisector_dir[0]))
    
    arc1 = patches.Arc(C, 2*arc_radius, 2*arc_radius,
                       angle=0, theta1=min(angle_CA, angle_mid), 
                       theta2=max(angle_CA, angle_mid),
                       color=color, linewidth=1.5)
    arc2 = patches.Arc(C, 2*arc_radius, 2*arc_radius,
                       angle=0, theta1=min(angle_mid, angle_CB), 
                       theta2=max(angle_mid, angle_CB),
                       color=color, linewidth=1.5)
    ax.add_patch(arc1)
    ax.add_patch(arc2)
    
    ax.text(D[0] + 0.3, D[1] + 0.2, '$D$', fontsize=12, color=color)
    
    ax.text(3, -0.8, 'Divide el ángulo\nen dos partes iguales',
            fontsize=10, ha='center', style='italic')
    ax.text(3, 5.3, 'Punto de concurrencia:\nIncentro (I)',
            fontsize=10, ha='center', color=color,
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))


def get_output_dir():
    """Retorna el directorio de salida para este gráfico."""
    return get_output_dir_for_topic(METADATA["topic_id"])


if __name__ == "__main__":
    print(f"Generando: {METADATA['name']}")
    fig = generate()
    output_dir = get_output_dir()
    paths = save_figure(fig, output_dir, METADATA["name"])
    print(f"✅ Guardado en: {output_dir}")
    for fmt, path in paths.items():
        print(f"   • {fmt}: {path.name}")
