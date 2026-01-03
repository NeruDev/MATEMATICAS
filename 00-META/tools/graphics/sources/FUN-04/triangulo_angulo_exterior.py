"""
Gráfico: Ángulo Exterior del Triángulo
======================================

Topic: FUN-04 Geometría
Usado en: theory/FUN-04-Teoria-Geometria.md, problems/FUN-04-Problemas.md (Prob-21)
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import matplotlib.pyplot as plt
import numpy as np
from templates import setup_style, get_colors, get_output_dir_for_topic, save_figure

METADATA = {
    "topic_id": "FUN-04",
    "name": "triangulo_angulo_exterior",
    "description": "Ángulo exterior del triángulo = suma de ángulos interiores no adyacentes",
    "used_in": ["theory/FUN-04-Teoria-Geometria.md", "problems/FUN-04-Problemas.md"],
    "section": "4.3",
}

def generate() -> plt.Figure:
    """Genera el gráfico del ángulo exterior del triángulo."""
    setup_style()
    colors = get_colors()
    
    fig, ax = plt.subplots(figsize=(11, 7))
    
    # Triángulo ABC
    A = np.array([0, 0])
    B = np.array([5, 0])
    C = np.array([1.5, 3])
    
    # Extensión del lado BC más allá de C
    D = C + 2.5 * (C - B) / np.linalg.norm(C - B)
    
    # Triángulo
    triangle = plt.Polygon([A, B, C], fill=True, facecolor=colors['primary'],
                          alpha=0.15, edgecolor=colors['primary'], linewidth=2.5)
    ax.add_patch(triangle)
    
    # Extensión del lado
    ax.plot([B[0], D[0]], [B[1], D[1]], '--', color='#374151', lw=2)
    
    # Vértices
    for p, label, offset in [(A, 'A', (-0.3, -0.25)), (B, 'B', (0.2, -0.25)), 
                              (C, 'C', (-0.25, 0.2)), (D, 'D', (0.15, 0.1))]:
        ax.plot(p[0], p[1], 'o', color='#374151', markersize=7)
        ax.text(p[0]+offset[0], p[1]+offset[1], label, fontsize=12, fontweight='bold')
    
    # Ángulo en A (α)
    vA1 = B - A
    vA2 = C - A
    aA1 = np.arctan2(vA1[1], vA1[0])
    aA2 = np.arctan2(vA2[1], vA2[0])
    arc_A = np.linspace(aA1, aA2, 30)
    ax.plot(A[0] + 0.5*np.cos(arc_A), A[1] + 0.5*np.sin(arc_A), 
           color=colors['secondary'], lw=2.5)
    ax.text(A[0]+0.65, A[1]+0.35, 'α', fontsize=14, color=colors['secondary'], fontweight='bold')
    
    # Ángulo en B (β)
    vB1 = A - B
    vB2 = C - B
    aB1 = np.arctan2(vB1[1], vB1[0])
    aB2 = np.arctan2(vB2[1], vB2[0])
    arc_B = np.linspace(aB1, aB2, 30)
    ax.plot(B[0] + 0.5*np.cos(arc_B), B[1] + 0.5*np.sin(arc_B), 
           color=colors['accent'], lw=2.5)
    ax.text(B[0]-0.55, B[1]+0.5, 'β', fontsize=14, color=colors['accent'], fontweight='bold')
    
    # Ángulo interior en C (γ) - más pequeño
    vC1 = A - C
    vC2 = B - C
    aC1 = np.arctan2(vC1[1], vC1[0])
    aC2 = np.arctan2(vC2[1], vC2[0])
    if aC1 < aC2:
        arc_C = np.linspace(aC1, aC2, 30)
    else:
        arc_C = np.linspace(aC2, aC1, 30)
    ax.plot(C[0] + 0.35*np.cos(arc_C), C[1] + 0.35*np.sin(arc_C), 
           color='#6b7280', lw=2)
    ax.text(C[0]+0.15, C[1]-0.55, 'γ', fontsize=12, color='#6b7280')
    
    # ÁNGULO EXTERIOR en C (θ) - destacado
    vC_ext = D - C
    aC_ext = np.arctan2(vC_ext[1], vC_ext[0])
    # El ángulo exterior va desde AC hasta CD
    if aC_ext < aC1:
        aC_ext += 2*np.pi
    arc_ext = np.linspace(aC1, aC_ext, 40)
    ax.fill(np.concatenate([[C[0]], C[0] + 0.7*np.cos(arc_ext), [C[0]]]),
            np.concatenate([[C[1]], C[1] + 0.7*np.sin(arc_ext), [C[1]]]),
            color=colors['tertiary'], alpha=0.25)
    ax.plot(C[0] + 0.7*np.cos(arc_ext), C[1] + 0.7*np.sin(arc_ext), 
           color=colors['tertiary'], lw=3)
    ax.text(C[0]-0.3, C[1]+0.9, 'θ', fontsize=16, color=colors['tertiary'], fontweight='bold')
    ax.text(C[0]-0.8, C[1]+1.3, '(exterior)', fontsize=10, color=colors['tertiary'], style='italic')
    
    # Cuadro de propiedad
    props = [
        'PROPIEDAD:',
        '',
        'El ángulo exterior de un triángulo',
        'es igual a la suma de los dos',
        'ángulos interiores no adyacentes.',
        '',
        'θ = α + β',
    ]
    
    y_start = 3.5
    for i, line in enumerate(props):
        weight = 'bold' if i == 0 or i == 6 else 'normal'
        color = colors['tertiary'] if i == 6 else '#374151'
        fontsize = 13 if i == 6 else 10
        ax.text(4, y_start - i*0.35, line, fontsize=fontsize, fontweight=weight, color=color)
    
    # Demostración visual
    ax.text(4, 0.8, 'Demostración:', fontsize=10, fontweight='bold', color='#6b7280')
    ax.text(4, 0.4, 'α + β + γ = 180° (suma interior)', fontsize=9, color='#6b7280')
    ax.text(4, 0.1, 'θ + γ = 180° (ángulos suplementarios)', fontsize=9, color='#6b7280')
    ax.text(4, -0.2, '∴ θ = α + β', fontsize=10, color=colors['tertiary'], fontweight='bold')
    
    ax.set_xlim(-0.8, 7.5)
    ax.set_ylim(-0.8, 4.5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    ax.set_title('Ángulo Exterior del Triángulo', fontsize=14, fontweight='bold', y=1.02)
    
    plt.tight_layout()
    return fig

def get_output_dir():
    return get_output_dir_for_topic(METADATA["topic_id"])

if __name__ == "__main__":
    fig = generate()
    paths = save_figure(fig, get_output_dir(), METADATA["name"])
    print(f"✅ Generado: {paths}")
