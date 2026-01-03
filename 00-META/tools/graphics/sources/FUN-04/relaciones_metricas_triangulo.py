"""
Gráfico: Relaciones Métricas en el Triángulo Rectángulo
=======================================================

Topic: FUN-04 Geometría
Usado en: theory/FUN-04-Teoria-Geometria.md (sección 4.9)
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import matplotlib.pyplot as plt
import numpy as np
from templates import setup_style, get_colors, get_output_dir_for_topic, save_figure

METADATA = {
    "topic_id": "FUN-04",
    "name": "relaciones_metricas_triangulo",
    "description": "Relaciones métricas: proyecciones, altura sobre hipotenusa",
    "used_in": ["theory/FUN-04-Teoria-Geometria.md"],
    "section": "4.9",
}

def generate() -> plt.Figure:
    """Genera el gráfico de relaciones métricas en triángulo rectángulo."""
    setup_style()
    colors = get_colors()
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Triángulo rectángulo ABC con ángulo recto en C
    A = np.array([0, 0])
    B = np.array([8, 0])
    C = np.array([3, 0])  # Proyección de C en AB (pie de la altura)
    
    # Calcular la posición de C (vértice del ángulo recto)
    # Para un triángulo con catetos a=4, b=3 y hipotenusa c=8
    # La altura h desde C a AB
    h = 3 * 4 / 5  # h = (a*b)/c para el ejemplo
    C_vertex = np.array([3, 4])  # Punto real C
    
    # Puntos
    A = np.array([0, 0])
    B = np.array([8, 0])
    C = np.array([2.5, 4])
    H = np.array([2.5, 0])  # Pie de la altura
    
    # Triángulo principal
    ax.plot([A[0], B[0]], [A[1], B[1]], color=colors['primary'], lw=3)
    ax.plot([B[0], C[0]], [B[1], C[1]], color=colors['secondary'], lw=3, label='Cateto a')
    ax.plot([C[0], A[0]], [C[1], A[1]], color=colors['accent'], lw=3, label='Cateto b')
    
    # Altura
    ax.plot([C[0], H[0]], [C[1], H[1]], color=colors['tertiary'], lw=2.5, 
            linestyle='--', label='Altura h')
    
    # Proyecciones
    ax.plot([A[0], H[0]], [A[1], H[1]], color='#f59e0b', lw=4, alpha=0.6)
    ax.plot([H[0], B[0]], [H[1], B[1]], color='#ec4899', lw=4, alpha=0.6)
    
    # Símbolo de ángulo recto en C
    sq_size = 0.3
    ax.plot([C[0]-sq_size, C[0]-sq_size, C[0]], 
           [C[1], C[1]-sq_size, C[1]-sq_size], color='#374151', lw=1.5)
    
    # Símbolo de ángulo recto en H
    ax.plot([H[0]+0.25, H[0]+0.25, H[0]], 
           [H[1], H[1]+0.25, H[1]+0.25], color='#374151', lw=1.5)
    
    # Vértices y etiquetas
    vertices = [(A, 'A', (-0.3, -0.3)), (B, 'B', (0.2, -0.3)), 
                (C, 'C', (-0.3, 0.2)), (H, 'H', (0, -0.4))]
    for p, label, offset in vertices:
        ax.plot(p[0], p[1], 'o', color='#374151', markersize=8)
        ax.text(p[0]+offset[0], p[1]+offset[1], label, fontsize=13, fontweight='bold')
    
    # Etiquetas de segmentos
    ax.text(4, -0.6, 'c (hipotenusa)', fontsize=11, ha='center', color=colors['primary'])
    ax.text(5.8, 2.3, 'a', fontsize=13, color=colors['secondary'], fontweight='bold')
    ax.text(0.8, 2.3, 'b', fontsize=13, color=colors['accent'], fontweight='bold')
    ax.text(2.1, 2, 'h', fontsize=13, color=colors['tertiary'], fontweight='bold')
    ax.text(1.2, 0.3, 'm', fontsize=12, color='#f59e0b', fontweight='bold')
    ax.text(5.2, 0.3, 'n', fontsize=12, color='#ec4899', fontweight='bold')
    
    # Fórmulas
    formulas = [
        (r'$h^2 = m \cdot n$', 'Altura al cuadrado'),
        (r'$a^2 = n \cdot c$', 'Cateto a²'),
        (r'$b^2 = m \cdot c$', 'Cateto b²'),
        (r'$a \cdot b = c \cdot h$', 'Producto de catetos'),
    ]
    
    box_x = 9.5
    for i, (formula, desc) in enumerate(formulas):
        y = 3.5 - i * 0.9
        ax.text(box_x, y, formula, fontsize=12, color='#1f2937',
               bbox=dict(boxstyle='round', facecolor='white', edgecolor='#d1d5db'))
        ax.text(box_x, y - 0.35, desc, fontsize=9, color='#6b7280', style='italic')
    
    # Leyenda de colores
    ax.text(9.5, 0.8, 'Proyecciones:', fontsize=10, fontweight='bold', color='#374151')
    ax.plot([9.5, 10], [0.4, 0.4], color='#f59e0b', lw=3)
    ax.text(10.2, 0.4, 'm = proyección de b', fontsize=9, va='center')
    ax.plot([9.5, 10], [0, 0], color='#ec4899', lw=3)
    ax.text(10.2, 0, 'n = proyección de a', fontsize=9, va='center')
    
    ax.set_xlim(-1, 14)
    ax.set_ylim(-1.2, 5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    ax.set_title('Relaciones Métricas en el Triángulo Rectángulo', 
                 fontsize=14, fontweight='bold', y=1.02)
    
    plt.tight_layout()
    return fig

def get_output_dir():
    return get_output_dir_for_topic(METADATA["topic_id"])

if __name__ == "__main__":
    fig = generate()
    paths = save_figure(fig, get_output_dir(), METADATA["name"])
    print(f"✅ Generado: {paths}")
