"""
Gráfico: Criterios de Semejanza de Triángulos
=============================================

Topic: FUN-04 Geometría
Usado en: theory/FUN-04-Teoria-Geometria.md (sección 4.8)
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import matplotlib.pyplot as plt
import numpy as np
from templates import setup_style, get_colors, get_output_dir_for_topic, save_figure

METADATA = {
    "topic_id": "FUN-04",
    "name": "semejanza_criterios",
    "description": "Criterios de semejanza: AA, LAL, LLL",
    "used_in": ["theory/FUN-04-Teoria-Geometria.md"],
    "section": "4.8",
}

def draw_similar_triangles(ax, tri1, tri2, marks_config, colors_dict, title, desc):
    """Dibuja dos triángulos semejantes con marcas."""
    
    # Triángulo 1 (más pequeño)
    t1 = plt.Polygon(tri1, fill=True, facecolor=colors_dict['primary'],
                     alpha=0.15, edgecolor=colors_dict['primary'], linewidth=2)
    ax.add_patch(t1)
    
    # Triángulo 2 (más grande)
    t2 = plt.Polygon(tri2, fill=True, facecolor=colors_dict['secondary'],
                     alpha=0.15, edgecolor=colors_dict['secondary'], linewidth=2)
    ax.add_patch(t2)
    
    # Vértices
    labels1 = ['A', 'B', 'C']
    labels2 = ["A'", "B'", "C'"]
    
    for v, label in zip(tri1, labels1):
        ax.plot(v[0], v[1], 'o', color=colors_dict['primary'], markersize=5)
        ax.text(v[0]-0.15, v[1]+0.1, label, fontsize=9, color=colors_dict['primary'])
    
    for v, label in zip(tri2, labels2):
        ax.plot(v[0], v[1], 'o', color=colors_dict['secondary'], markersize=5)
        ax.text(v[0]+0.1, v[1]+0.1, label, fontsize=9, color=colors_dict['secondary'])
    
    # Marcas de ángulos iguales
    for i, highlight in enumerate(marks_config.get('angles', [])):
        if highlight:
            for tri, color in [(tri1, colors_dict['primary']), (tri2, colors_dict['secondary'])]:
                vertex = np.array(tri[i])
                p1 = np.array(tri[(i-1) % 3])
                p2 = np.array(tri[(i+1) % 3])
                
                v1 = p1 - vertex
                v2 = p2 - vertex
                a1 = np.arctan2(v1[1], v1[0])
                a2 = np.arctan2(v2[1], v2[0])
                if a2 < a1:
                    a2 += 2 * np.pi
                
                arc = np.linspace(a1, a2, 20)
                r = 0.15 if tri == tri1 else 0.2
                ax.plot(vertex[0] + r*np.cos(arc), vertex[1] + r*np.sin(arc),
                       color=colors_dict['accent'], lw=1.5)
    
    # Símbolo de semejanza
    ax.text(1.8, 1.0, '~', fontsize=24, ha='center', va='center', 
            color=colors_dict['tertiary'], fontweight='bold')
    
    ax.set_title(title, fontsize=11, fontweight='bold', pad=8)
    ax.text(1.8, -0.3, desc, ha='center', fontsize=9, color='#6b7280', style='italic')

def generate() -> plt.Figure:
    """Genera el gráfico de criterios de semejanza."""
    setup_style()
    colors = get_colors()
    
    fig, axes = plt.subplots(1, 3, figsize=(14, 5))
    
    # Triángulos base
    tri1_base = [(0, 0), (1.2, 0), (0.4, 0.9)]
    tri2_base = [(2, 0), (4, 0), (2.7, 1.5)]
    
    # === AA (Ángulo-Ángulo) ===
    config_aa = {'angles': [True, True, False]}
    draw_similar_triangles(axes[0], tri1_base, tri2_base, config_aa, colors,
                          'AA (Ángulo-Ángulo)', '2 ángulos iguales')
    
    # === LAL (Lado-Ángulo-Lado) ===
    config_lal = {'angles': [True, False, False]}
    draw_similar_triangles(axes[1], tri1_base, tri2_base, config_lal, colors,
                          'LAL (Lado-Ángulo-Lado)', '2 lados proporcionales y\nángulo comprendido igual')
    # Añadir marcas proporcionales en lados
    axes[1].text(0.2, 0.45, 'k', fontsize=9, color=colors['accent'])
    axes[1].text(0.8, 0.45, 'k', fontsize=9, color=colors['accent'])
    axes[1].text(2.35, 0.75, '2k', fontsize=9, color=colors['accent'])
    axes[1].text(3.35, 0.75, '2k', fontsize=9, color=colors['accent'])
    
    # === LLL (Lado-Lado-Lado) ===
    config_lll = {'angles': [False, False, False]}
    draw_similar_triangles(axes[2], tri1_base, tri2_base, config_lll, colors,
                          'LLL (Lado-Lado-Lado)', '3 lados proporcionales')
    # Marcas de proporcionalidad
    for i, (p1, p2) in enumerate([(tri1_base[0], tri1_base[1]), 
                                   (tri1_base[1], tri1_base[2]),
                                   (tri1_base[2], tri1_base[0])]):
        mid = ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)
        axes[2].text(mid[0], mid[1]+0.05, f'{i+1}', fontsize=8, color=colors['primary'],
                    ha='center', fontweight='bold')
    for i, (p1, p2) in enumerate([(tri2_base[0], tri2_base[1]), 
                                   (tri2_base[1], tri2_base[2]),
                                   (tri2_base[2], tri2_base[0])]):
        mid = ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)
        axes[2].text(mid[0], mid[1]+0.05, f'{2*(i+1)}', fontsize=8, color=colors['secondary'],
                    ha='center', fontweight='bold')
    
    for ax in axes:
        ax.set_xlim(-0.5, 4.5)
        ax.set_ylim(-0.6, 2)
        ax.set_aspect('equal')
        ax.axis('off')
    
    fig.suptitle('Criterios de Semejanza de Triángulos', fontsize=14, 
                 fontweight='bold', y=0.98)
    plt.tight_layout()
    return fig

def get_output_dir():
    return get_output_dir_for_topic(METADATA["topic_id"])

if __name__ == "__main__":
    fig = generate()
    paths = save_figure(fig, get_output_dir(), METADATA["name"])
    print(f"✅ Generado: {paths}")
