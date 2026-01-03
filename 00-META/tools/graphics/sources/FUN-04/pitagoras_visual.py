"""
Gráfico: Teorema de Pitágoras Visual
====================================

Topic: FUN-04 Geometría
Usado en: theory/FUN-04-Teoria-Geometria.md (Sección 4.9)
          methods/FUN-04-Metodos-Geometria.md (Método 4)

Ilustra el teorema de Pitágoras con cuadrados sobre los lados.
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
    "name": "pitagoras_visual",
    "description": "Representación visual del teorema de Pitágoras con cuadrados",
    "used_in": [
        "theory/FUN-04-Teoria-Geometria.md",
        "methods/FUN-04-Metodos-Geometria.md"
    ],
    "section": "4.9 Teorema de Pitágoras",
}

# ============================================================
# Función de Generación
# ============================================================

def generate() -> plt.Figure:
    """
    Genera el diagrama visual del teorema de Pitágoras.
    
    Muestra un triángulo rectángulo con cuadrados construidos
    sobre cada lado, ilustrando que a² + b² = c².
    
    Returns:
        Figura de matplotlib.
    """
    setup_style()
    colors = get_colors()
    
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # Triángulo rectángulo 3-4-5 (escalado)
    scale = 1.5
    a, b = 3 * scale, 4 * scale  # catetos
    c = 5 * scale  # hipotenusa
    
    # Vértices del triángulo
    A = np.array([0, 0])  # Ángulo recto
    B = np.array([b, 0])  # Extremo del cateto b
    C = np.array([0, a])  # Extremo del cateto a
    
    # Dibujar el triángulo
    triangle = plt.Polygon([A, B, C], 
                           fill=True, 
                           facecolor=colors['text'],
                           edgecolor=colors['text'],
                           alpha=0.1,
                           linewidth=2)
    ax.add_patch(triangle)
    
    # Bordes del triángulo
    ax.plot([A[0], B[0]], [A[1], B[1]], color=colors['text'], linewidth=2.5)
    ax.plot([B[0], C[0]], [B[1], C[1]], color=colors['text'], linewidth=2.5)
    ax.plot([C[0], A[0]], [C[1], A[1]], color=colors['text'], linewidth=2.5)
    
    # Marcar ángulo recto
    right_angle_size = 0.4
    right_angle = patches.Rectangle(
        A, right_angle_size, right_angle_size,
        fill=False, edgecolor=colors['secondary'], linewidth=2
    )
    ax.add_patch(right_angle)
    
    # === Cuadrado sobre el cateto a (vertical, a la izquierda) ===
    sq_a_vertices = [
        C,
        C + np.array([-a, 0]),
        C + np.array([-a, -a]),
        A + np.array([-a, 0]),
    ]
    # Ajustar para que esté afuera
    sq_a_vertices = [
        A + np.array([-a, 0]),
        A,
        C,
        C + np.array([-a, 0]),
    ]
    sq_a = plt.Polygon(sq_a_vertices, 
                       fill=True, facecolor=colors['accent'],
                       edgecolor=colors['accent'], alpha=0.3, linewidth=2)
    ax.add_patch(sq_a)
    
    # Etiqueta del cuadrado a²
    sq_a_center = np.array([-a/2, a/2])
    ax.text(sq_a_center[0], sq_a_center[1], '$a^2$', 
            fontsize=18, fontweight='bold', ha='center', va='center',
            color=colors['accent'])
    
    # === Cuadrado sobre el cateto b (horizontal, abajo) ===
    sq_b_vertices = [
        A,
        B,
        B + np.array([0, -b]),
        A + np.array([0, -b]),
    ]
    sq_b = plt.Polygon(sq_b_vertices, 
                       fill=True, facecolor=colors['tertiary'],
                       edgecolor=colors['tertiary'], alpha=0.3, linewidth=2)
    ax.add_patch(sq_b)
    
    # Etiqueta del cuadrado b²
    sq_b_center = np.array([b/2, -b/2])
    ax.text(sq_b_center[0], sq_b_center[1], '$b^2$', 
            fontsize=18, fontweight='bold', ha='center', va='center',
            color=colors['tertiary'])
    
    # === Cuadrado sobre la hipotenusa c ===
    # Vector de la hipotenusa (de C a B)
    hyp_vec = B - C
    hyp_unit = hyp_vec / np.linalg.norm(hyp_vec)
    # Vector perpendicular (hacia afuera del triángulo)
    perp_unit = np.array([hyp_unit[1], -hyp_unit[0]])
    
    sq_c_vertices = [
        C,
        B,
        B + perp_unit * c,
        C + perp_unit * c,
    ]
    sq_c = plt.Polygon(sq_c_vertices, 
                       fill=True, facecolor=colors['secondary'],
                       edgecolor=colors['secondary'], alpha=0.3, linewidth=2)
    ax.add_patch(sq_c)
    
    # Etiqueta del cuadrado c²
    sq_c_center = (C + B) / 2 + perp_unit * c / 2
    ax.text(sq_c_center[0], sq_c_center[1], '$c^2$', 
            fontsize=18, fontweight='bold', ha='center', va='center',
            color=colors['secondary'])
    
    # === Etiquetas de los lados ===
    # Cateto a
    ax.text(-0.5, a/2, '$a$', fontsize=16, fontweight='bold',
            ha='center', va='center', color=colors['text'])
    
    # Cateto b
    ax.text(b/2, -0.5, '$b$', fontsize=16, fontweight='bold',
            ha='center', va='center', color=colors['text'])
    
    # Hipotenusa c
    mid_hyp = (B + C) / 2
    offset_hyp = np.array([0.4, 0.3])
    ax.text(mid_hyp[0] + offset_hyp[0], mid_hyp[1] + offset_hyp[1], '$c$', 
            fontsize=16, fontweight='bold',
            ha='center', va='center', color=colors['text'])
    
    # === Fórmula principal ===
    formula_box = dict(boxstyle='round,pad=0.6', 
                      facecolor='white', 
                      edgecolor=colors['primary'],
                      linewidth=2)
    ax.text(7.5, 7, '$c^2 = a^2 + b^2$', 
            fontsize=24, fontweight='bold',
            bbox=formula_box, ha='center',
            color=colors['primary'])
    
    # Ejemplo numérico
    example_text = (
        f'Ejemplo: $3^2 + 4^2 = 5^2$\n'
        f'$9 + 16 = 25$ ✓'
    )
    ax.text(7.5, 4.5, example_text, 
            fontsize=14, ha='center', va='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    # Puntos en los vértices
    for point, label in [(A, 'A'), (B, 'B'), (C, 'C')]:
        ax.plot(point[0], point[1], 'o', color=colors['text'], markersize=8)
    
    # Configurar ejes
    ax.set_xlim(-6, 12)
    ax.set_ylim(-7, 10)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Título
    ax.set_title('Teorema de Pitágoras', 
                fontsize=18, fontweight='bold', pad=20)
    
    return fig


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
