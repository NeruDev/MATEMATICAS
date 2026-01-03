"""
Plantillas de Estilo para Gráficos Matemáticos
==============================================

Este módulo contiene:
- Configuración global de matplotlib
- Paleta de colores estándar
- Funciones de utilidad para guardar figuras
- Decoradores y helpers comunes

Uso:
    from templates.style_common import setup_style, get_colors, save_figure
    
    setup_style()
    colors = get_colors()
    fig, ax = plt.subplots()
    # ... crear gráfico ...
    save_figure(fig, output_dir, "nombre_grafico")
"""

from __future__ import annotations

import json
import warnings
from datetime import datetime
from pathlib import Path
from typing import TYPE_CHECKING, Dict, List, Optional, Tuple, Union

# Configurar backend sin GUI antes de importar pyplot
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
import yaml

if TYPE_CHECKING:
    from matplotlib.figure import Figure

# ============================================================
# Configuración Global
# ============================================================

_CONFIG: Optional[Dict] = None
_PACKAGE_DIR = Path(__file__).parent.parent


def load_config() -> Dict:
    """
    Carga la configuración desde config.yaml.
    
    Returns:
        Diccionario con la configuración global.
        
    Raises:
        FileNotFoundError: Si no existe config.yaml
    """
    global _CONFIG
    
    if _CONFIG is not None:
        return _CONFIG
    
    config_path = _PACKAGE_DIR / "config.yaml"
    
    if not config_path.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo de configuración: {config_path}\n"
            "Asegúrate de que config.yaml existe en el directorio graphics/"
        )
    
    with open(config_path, 'r', encoding='utf-8') as f:
        _CONFIG = yaml.safe_load(f)
    
    return _CONFIG


def get_repo_root() -> Path:
    """
    Obtiene la ruta raíz del repositorio.
    
    Returns:
        Path absoluto a la raíz del repositorio.
    """
    # Subir desde 00-META/tools/graphics/ hasta la raíz
    return _PACKAGE_DIR.parent.parent.parent.resolve()


# ============================================================
# Estilos de Matplotlib
# ============================================================

def setup_style(dark_mode: bool = False) -> None:
    """
    Configura el estilo global de matplotlib para el repositorio.
    
    Esta función debe llamarse al inicio de cada script de gráfico
    para asegurar consistencia visual.
    
    Args:
        dark_mode: Si True, usa esquema de colores oscuro (experimental).
    """
    config = load_config()
    style = config['style']
    colors = style['colors']
    
    # Colores de fondo según el modo
    bg_color = '#1f2937' if dark_mode else colors['background']
    text_color = colors['background'] if dark_mode else colors['text']
    
    plt.rcParams.update({
        # Tipografía
        'font.family': style['font_family'],
        'font.size': style['font_size'],
        'axes.titlesize': style['title_size'],
        'axes.labelsize': style['font_size'],
        
        # Líneas y bordes
        'axes.linewidth': 1.5,
        'lines.linewidth': style['line_widths']['default'],
        
        # Cuadrícula
        'axes.grid': False,  # Desactivada por defecto para geometría
        'grid.alpha': 0.3,
        'grid.color': colors['grid'],
        
        # Colores de fondo
        'figure.facecolor': bg_color,
        'axes.facecolor': bg_color,
        'savefig.facecolor': bg_color,
        'savefig.edgecolor': 'none',
        
        # Texto
        'text.color': text_color,
        'axes.labelcolor': text_color,
        'xtick.color': text_color,
        'ytick.color': text_color,
        
        # LaTeX
        'text.usetex': False,  # Usar mathtext en lugar de LaTeX externo
        'mathtext.fontset': 'dejavusans',
        
        # Otros
        'figure.dpi': style['figure']['dpi'],
        'savefig.dpi': config['output']['png']['dpi'],
        'savefig.bbox': 'tight',
        'savefig.pad_inches': 0.1,
    })


def get_colors() -> Dict[str, str]:
    """
    Obtiene la paleta de colores estándar.
    
    Returns:
        Diccionario con nombres de colores y sus valores hex.
        
    Example:
        >>> colors = get_colors()
        >>> ax.plot(x, y, color=colors['primary'])
    """
    config = load_config()
    return config['style']['colors'].copy()


def get_line_widths() -> Dict[str, float]:
    """
    Obtiene los grosores de línea estándar.
    
    Returns:
        Diccionario con tipos de línea y sus grosores.
    """
    config = load_config()
    return config['style']['line_widths'].copy()


def get_figure_size(size_type: str = 'default') -> Tuple[float, float]:
    """
    Obtiene el tamaño de figura estándar.
    
    Args:
        size_type: 'default', 'square', o 'wide'
        
    Returns:
        Tupla (ancho, alto) en pulgadas.
    """
    config = load_config()
    sizes = config['style']['figure']
    
    size_key = f"{size_type}_size"
    if size_key not in sizes:
        size_key = "default_size"
    
    return tuple(sizes[size_key])


# ============================================================
# Guardado de Figuras
# ============================================================

def save_figure(
    fig: Figure,
    output_dir: Path,
    name: str,
    formats: Tuple[str, ...] = ('svg', 'png'),
    close_fig: bool = True,
    metadata: Optional[Dict] = None
) -> Dict[str, Path]:
    """
    Guarda la figura en los formatos especificados.
    
    Args:
        fig: Figura de matplotlib a guardar.
        output_dir: Directorio de salida.
        name: Nombre base del archivo (sin extensión).
        formats: Formatos de salida ('svg', 'png').
        close_fig: Si True, cierra la figura después de guardar.
        metadata: Metadatos adicionales para el manifest.
        
    Returns:
        Diccionario con formato -> ruta del archivo generado.
        
    Example:
        >>> paths = save_figure(fig, Path("media/generated"), "triangulo")
        >>> print(paths['svg'])  # media/generated/triangulo.svg
    """
    config = load_config()
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    paths = {}
    
    for fmt in formats:
        # Verificar si el formato está habilitado
        if fmt in config['output'] and not config['output'][fmt].get('enabled', True):
            continue
            
        filepath = output_dir / f"{name}.{fmt}"
        
        # Configuración específica por formato
        save_kwargs = {
            'format': fmt,
            'bbox_inches': 'tight',
            'pad_inches': 0.1,
        }
        
        if fmt == 'png':
            save_kwargs['dpi'] = config['output']['png']['dpi']
        elif fmt == 'svg':
            # SVG no necesita DPI pero configuramos metadata
            save_kwargs['metadata'] = {
                'Creator': 'Repositorio Matemáticas Universitarias',
                'Date': datetime.now().isoformat(),
            }
        
        fig.savefig(filepath, **save_kwargs)
        paths[fmt] = filepath
    
    if close_fig:
        plt.close(fig)
    
    return paths


def get_output_dir_for_topic(topic_id: str) -> Path:
    """
    Obtiene el directorio de salida para un tema específico.
    
    Args:
        topic_id: Identificador del tema (ej: "FUN-04")
        
    Returns:
        Path al directorio media/generated/ del tema.
        
    Raises:
        ValueError: Si el topic_id no está en la configuración.
    """
    config = load_config()
    
    if topic_id not in config['topics']:
        raise ValueError(
            f"Topic '{topic_id}' no encontrado en config.yaml. "
            f"Topics disponibles: {list(config['topics'].keys())}"
        )
    
    topic_config = config['topics'][topic_id]
    repo_root = get_repo_root()
    
    output_dir = (
        repo_root 
        / topic_config['module'] 
        / topic_config['subtopic'] 
        / 'media' 
        / config['output']['svg']['target']
    )
    
    return output_dir


# ============================================================
# Utilidades de Dibujo
# ============================================================

def add_right_angle_marker(
    ax: plt.Axes,
    vertex: Tuple[float, float],
    direction1: Tuple[float, float],
    direction2: Tuple[float, float],
    size: float = 0.3,
    color: Optional[str] = None
) -> None:
    """
    Dibuja un marcador de ángulo recto en el vértice especificado.
    
    Args:
        ax: Axes de matplotlib.
        vertex: Coordenadas del vértice.
        direction1: Vector dirección hacia el primer lado.
        direction2: Vector dirección hacia el segundo lado.
        size: Tamaño del marcador.
        color: Color del marcador (usa secondary por defecto).
    """
    if color is None:
        color = get_colors()['secondary']
    
    # Normalizar direcciones
    d1 = np.array(direction1)
    d2 = np.array(direction2)
    d1 = d1 / np.linalg.norm(d1) * size
    d2 = d2 / np.linalg.norm(d2) * size
    
    v = np.array(vertex)
    
    # Puntos del cuadrado
    p1 = v + d1
    p2 = v + d1 + d2
    p3 = v + d2
    
    # Dibujar las dos líneas del ángulo recto
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=color, linewidth=1)
    ax.plot([p2[0], p3[0]], [p2[1], p3[1]], color=color, linewidth=1)


def annotate_point(
    ax: plt.Axes,
    point: Tuple[float, float],
    label: str,
    offset: Tuple[float, float] = (0.3, 0.3),
    fontsize: Optional[int] = None,
    fontweight: str = 'bold',
    color: Optional[str] = None
) -> None:
    """
    Añade una etiqueta a un punto.
    
    Args:
        ax: Axes de matplotlib.
        point: Coordenadas del punto.
        label: Texto de la etiqueta (puede incluir LaTeX).
        offset: Desplazamiento (x, y) de la etiqueta.
        fontsize: Tamaño de fuente (usa config por defecto).
        fontweight: Peso de la fuente.
        color: Color del texto (usa text por defecto).
    """
    config = load_config()
    
    if fontsize is None:
        fontsize = config['style']['annotation_size']
    if color is None:
        color = get_colors()['text']
    
    ax.annotate(
        label,
        point,
        xytext=offset,
        textcoords='offset points',
        fontsize=fontsize,
        fontweight=fontweight,
        color=color
    )


def draw_polygon(
    ax: plt.Axes,
    vertices: List[Tuple[float, float]],
    close: bool = True,
    fill: bool = False,
    fill_alpha: float = 0.1,
    edge_color: Optional[str] = None,
    fill_color: Optional[str] = None,
    linewidth: Optional[float] = None
) -> plt.Polygon:
    """
    Dibuja un polígono dados sus vértices.
    
    Args:
        ax: Axes de matplotlib.
        vertices: Lista de coordenadas de vértices.
        close: Si True, cierra el polígono.
        fill: Si True, rellena el polígono.
        fill_alpha: Transparencia del relleno.
        edge_color: Color del borde (usa primary por defecto).
        fill_color: Color del relleno (usa primary por defecto).
        linewidth: Grosor de línea.
        
    Returns:
        Objeto Polygon añadido al axes.
    """
    colors = get_colors()
    lw = get_line_widths()
    
    if edge_color is None:
        edge_color = colors['primary']
    if fill_color is None:
        fill_color = colors['primary']
    if linewidth is None:
        linewidth = lw['default']
    
    polygon = plt.Polygon(
        vertices,
        closed=close,
        fill=fill,
        facecolor=fill_color if fill else 'none',
        edgecolor=edge_color,
        linewidth=linewidth,
        alpha=fill_alpha if fill else 1.0
    )
    
    ax.add_patch(polygon)
    return polygon


# ============================================================
# Manifest de Gráficos
# ============================================================

def update_manifest(
    output_dir: Path,
    graphic_info: Dict,
    append: bool = True
) -> Path:
    """
    Actualiza o crea el manifest.json en el directorio de salida.
    
    Args:
        output_dir: Directorio donde está el manifest.
        graphic_info: Información del gráfico generado.
        append: Si True, añade al manifest existente.
        
    Returns:
        Path al archivo manifest.
    """
    manifest_path = output_dir / "manifest.json"
    
    if append and manifest_path.exists():
        with open(manifest_path, 'r', encoding='utf-8') as f:
            manifest = json.load(f)
    else:
        manifest = {
            "generated_at": None,
            "generator": "graphics/generate_graphics.py",
            "graphics": []
        }
    
    # Actualizar timestamp
    manifest["generated_at"] = datetime.now().isoformat()
    
    # Añadir o actualizar gráfico
    existing_names = [g['name'] for g in manifest['graphics']]
    if graphic_info['name'] in existing_names:
        idx = existing_names.index(graphic_info['name'])
        manifest['graphics'][idx] = graphic_info
    else:
        manifest['graphics'].append(graphic_info)
    
    # Guardar
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    
    return manifest_path
