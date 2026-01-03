"""
Gráfico: Sector y Segmento Circular
===================================

Topic: FUN-04 Geometría
Usado en: theory/FUN-04-Teoria-Geometria.md, problems/FUN-04-Problemas.md
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import matplotlib.pyplot as plt
import numpy as np
from templates import setup_style, get_colors, get_output_dir_for_topic, save_figure

METADATA = {
    "topic_id": "FUN-04",
    "name": "sector_segmento_circular",
    "description": "Sector circular y segmento circular con fórmulas",
    "used_in": ["theory/FUN-04-Teoria-Geometria.md", "problems/FUN-04-Problemas.md"],
    "section": "4.6",
}

def generate() -> plt.Figure:
    """Genera el gráfico de sector y segmento circular."""
    setup_style()
    colors = get_colors()
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    r = 2.0
    theta1 = np.radians(20)
    theta2 = np.radians(100)
    
    # === SECTOR CIRCULAR ===
    # Circunferencia completa (línea tenue)
    theta_full = np.linspace(0, 2*np.pi, 100)
    ax1.plot(r*np.cos(theta_full), r*np.sin(theta_full), color='#d1d5db', lw=1.5)
    
    # Sector (relleno)
    theta_sector = np.linspace(theta1, theta2, 50)
    sector_x = np.concatenate([[0], r*np.cos(theta_sector), [0]])
    sector_y = np.concatenate([[0], r*np.sin(theta_sector), [0]])
    ax1.fill(sector_x, sector_y, color=colors['primary'], alpha=0.4)
    ax1.plot(r*np.cos(theta_sector), r*np.sin(theta_sector), color=colors['primary'], lw=3)
    
    # Radios
    ax1.plot([0, r*np.cos(theta1)], [0, r*np.sin(theta1)], color=colors['secondary'], lw=2.5)
    ax1.plot([0, r*np.cos(theta2)], [0, r*np.sin(theta2)], color=colors['secondary'], lw=2.5)
    
    # Centro
    ax1.plot(0, 0, 'o', color='#374151', markersize=6)
    ax1.text(0.15, -0.25, 'O', fontsize=11, fontweight='bold')
    
    # Arco del ángulo central
    arc_angle = np.linspace(theta1, theta2, 30)
    ax1.plot(0.4*np.cos(arc_angle), 0.4*np.sin(arc_angle), color=colors['accent'], lw=2)
    ax1.text(0.35, 0.55, 'θ', fontsize=14, color=colors['accent'], fontweight='bold')
    
    # Etiquetas
    ax1.text(r*np.cos((theta1+theta2)/2)*1.15, r*np.sin((theta1+theta2)/2)*1.15, 
            'arco', fontsize=10, color=colors['primary'], fontweight='bold', ha='center')
    ax1.text(r*np.cos(theta1)*0.6, r*np.sin(theta1)*0.6 - 0.15, 
            'r', fontsize=12, color=colors['secondary'], fontweight='bold')
    
    ax1.set_title('SECTOR CIRCULAR', fontsize=12, fontweight='bold', pad=10)
    
    # Fórmulas
    ax1.text(0, -2.8, 'Área del sector:', fontsize=10, fontweight='bold', 
            color='#374151', ha='center')
    ax1.text(0, -3.2, r'$A = \frac{\theta}{360°} \cdot \pi r^2$', fontsize=12, 
            ha='center', color='#1f2937')
    ax1.text(0, -3.7, 'Longitud del arco:', fontsize=10, fontweight='bold', 
            color='#374151', ha='center')
    ax1.text(0, -4.1, r'$L = \frac{\theta}{360°} \cdot 2\pi r$', fontsize=12, 
            ha='center', color='#1f2937')
    
    ax1.set_xlim(-2.8, 2.8)
    ax1.set_ylim(-4.5, 2.8)
    ax1.set_aspect('equal')
    ax1.axis('off')
    
    # === SEGMENTO CIRCULAR ===
    # Circunferencia completa
    ax2.plot(r*np.cos(theta_full), r*np.sin(theta_full), color='#d1d5db', lw=1.5)
    
    # Segmento (región entre cuerda y arco)
    A = np.array([r*np.cos(theta1), r*np.sin(theta1)])
    B = np.array([r*np.cos(theta2), r*np.sin(theta2)])
    
    # Relleno del segmento
    segment_x = np.concatenate([r*np.cos(theta_sector), [A[0]]])
    segment_y = np.concatenate([r*np.sin(theta_sector), [A[1]]])
    ax2.fill(segment_x, segment_y, color=colors['tertiary'], alpha=0.4)
    
    # Arco
    ax2.plot(r*np.cos(theta_sector), r*np.sin(theta_sector), color=colors['tertiary'], lw=3)
    
    # Cuerda
    ax2.plot([A[0], B[0]], [A[1], B[1]], color=colors['secondary'], lw=2.5, 
            label='Cuerda')
    
    # Centro
    ax2.plot(0, 0, 'o', color='#374151', markersize=6)
    ax2.text(0.15, -0.25, 'O', fontsize=11, fontweight='bold')
    
    # Radios (punteados)
    ax2.plot([0, A[0]], [0, A[1]], '--', color='#9ca3af', lw=1.5)
    ax2.plot([0, B[0]], [0, B[1]], '--', color='#9ca3af', lw=1.5)
    
    # Puntos A y B
    ax2.plot(A[0], A[1], 'o', color=colors['secondary'], markersize=7)
    ax2.plot(B[0], B[1], 'o', color=colors['secondary'], markersize=7)
    ax2.text(A[0]+0.15, A[1]-0.2, 'A', fontsize=11, fontweight='bold')
    ax2.text(B[0]-0.1, B[1]+0.2, 'B', fontsize=11, fontweight='bold')
    
    # Etiquetas
    mid_chord = (A + B) / 2
    ax2.text(mid_chord[0]-0.3, mid_chord[1]-0.3, 'cuerda', fontsize=10, 
            color=colors['secondary'], fontweight='bold')
    ax2.text(0.3, 1.8, 'segmento', fontsize=10, color=colors['tertiary'], 
            fontweight='bold')
    
    ax2.set_title('SEGMENTO CIRCULAR', fontsize=12, fontweight='bold', pad=10)
    
    # Fórmulas
    ax2.text(0, -2.8, 'Área del segmento:', fontsize=10, fontweight='bold', 
            color='#374151', ha='center')
    ax2.text(0, -3.2, r'$A_{seg} = A_{sector} - A_{triángulo}$', fontsize=11, 
            ha='center', color='#1f2937')
    ax2.text(0, -3.7, r'$A_{seg} = \frac{r^2}{2}(\theta - \sin\theta)$', fontsize=11, 
            ha='center', color=colors['tertiary'])
    ax2.text(0, -4.1, '(θ en radianes)', fontsize=9, ha='center', 
            color='#6b7280', style='italic')
    
    ax2.set_xlim(-2.8, 2.8)
    ax2.set_ylim(-4.5, 2.8)
    ax2.set_aspect('equal')
    ax2.axis('off')
    
    fig.suptitle('Sector y Segmento Circular', fontsize=14, fontweight='bold', y=0.98)
    plt.tight_layout()
    return fig

def get_output_dir():
    return get_output_dir_for_topic(METADATA["topic_id"])

if __name__ == "__main__":
    fig = generate()
    paths = save_figure(fig, get_output_dir(), METADATA["name"])
    print(f"✅ Generado: {paths}")
