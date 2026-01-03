"""
Módulo de Plantillas para Gráficos Matemáticos
=============================================

Exporta todas las funciones de estilo y utilidades de dibujo.
"""

from .style_common import (
    add_right_angle_marker,
    annotate_point,
    draw_polygon,
    get_colors,
    get_figure_size,
    get_line_widths,
    get_output_dir_for_topic,
    get_repo_root,
    load_config,
    save_figure,
    setup_style,
    update_manifest,
)

from .style_2d import (
    create_quadrilateral_example,
    create_triangle_figure,
    draw_altitude,
    draw_angle_arc,
    draw_circle,
    draw_median,
    draw_parallel_lines_with_transversal,
    draw_quadrilateral_hierarchy,
    draw_radius,
)

__all__ = [
    # style_common
    'load_config',
    'get_repo_root',
    'setup_style',
    'get_colors',
    'get_line_widths',
    'get_figure_size',
    'save_figure',
    'get_output_dir_for_topic',
    'add_right_angle_marker',
    'annotate_point',
    'draw_polygon',
    'update_manifest',
    # style_2d
    'create_triangle_figure',
    'draw_altitude',
    'draw_median',
    'draw_parallel_lines_with_transversal',
    'draw_angle_arc',
    'draw_circle',
    'draw_radius',
    'draw_quadrilateral_hierarchy',
    'create_quadrilateral_example',
]
