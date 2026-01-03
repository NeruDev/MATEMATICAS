#!/usr/bin/env python3
"""
Motor Principal de Generación de Gráficos
=========================================

Este script genera todos los gráficos matemáticos del repositorio
a partir de los módulos Python en la carpeta sources/.

Uso:
    python generate_graphics.py                    # Genera todos
    python generate_graphics.py --topic FUN-04     # Solo geometría
    python generate_graphics.py --file triangulo   # Archivo específico
    python generate_graphics.py --check            # Verifica sin generar
    python generate_graphics.py --list             # Lista gráficos disponibles
    python generate_graphics.py --clean            # Limpia gráficos huérfanos

Estructura esperada de cada módulo de gráfico:
    
    METADATA = {
        "topic_id": "FUN-04",
        "name": "nombre_grafico",
        "description": "Descripción del gráfico",
        "used_in": ["theory/archivo.md"],
        "section": "4.3"
    }
    
    def generate() -> plt.Figure:
        # ... código para crear el gráfico ...
        return fig

Autor: Sistema de Generación Automática
Versión: 1.0.0
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
import traceback
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# Asegurar que el paquete esté en el path
PACKAGE_DIR = Path(__file__).parent
sys.path.insert(0, str(PACKAGE_DIR))

from templates.style_common import (
    get_output_dir_for_topic,
    get_repo_root,
    load_config,
    save_figure,
    update_manifest,
)

# ============================================================
# Constantes
# ============================================================

SOURCES_DIR = PACKAGE_DIR / "sources"
VERSION = "1.0.0"


# ============================================================
# Funciones de Descubrimiento
# ============================================================

def discover_graphics(
    topic: Optional[str] = None,
    file_pattern: Optional[str] = None
) -> List[Path]:
    """
    Descubre todos los archivos de gráficos disponibles.
    
    Args:
        topic: Filtrar por topic_id (ej: "FUN-04").
        file_pattern: Filtrar por patrón en nombre de archivo.
        
    Returns:
        Lista de rutas a archivos Python de gráficos.
    """
    graphics = []
    
    if not SOURCES_DIR.exists():
        print(f"⚠️  Directorio de fuentes no encontrado: {SOURCES_DIR}")
        return graphics
    
    for topic_dir in sorted(SOURCES_DIR.iterdir()):
        if not topic_dir.is_dir():
            continue
        
        # Filtrar por topic si se especifica
        if topic and topic_dir.name != topic:
            continue
        
        for py_file in sorted(topic_dir.glob("*.py")):
            # Ignorar archivos especiales
            if py_file.name.startswith("_"):
                continue
            
            # Filtrar por patrón si se especifica
            if file_pattern and file_pattern.lower() not in py_file.stem.lower():
                continue
            
            graphics.append(py_file)
    
    return graphics


def load_graphic_module(filepath: Path) -> Any:
    """
    Carga dinámicamente un módulo Python de gráfico.
    
    Args:
        filepath: Ruta al archivo .py
        
    Returns:
        Módulo Python cargado.
        
    Raises:
        ImportError: Si el módulo no puede cargarse.
        AttributeError: Si el módulo no tiene la estructura esperada.
    """
    spec = importlib.util.spec_from_file_location(filepath.stem, filepath)
    if spec is None or spec.loader is None:
        raise ImportError(f"No se pudo crear spec para {filepath}")
    
    module = importlib.util.module_from_spec(spec)
    
    # Añadir el directorio del módulo al path temporalmente
    module_dir = str(filepath.parent)
    if module_dir not in sys.path:
        sys.path.insert(0, module_dir)
    
    try:
        spec.loader.exec_module(module)
    finally:
        if module_dir in sys.path:
            sys.path.remove(module_dir)
    
    # Verificar estructura mínima
    if not hasattr(module, 'METADATA'):
        raise AttributeError(f"Módulo {filepath.name} no tiene METADATA")
    if not hasattr(module, 'generate'):
        raise AttributeError(f"Módulo {filepath.name} no tiene función generate()")
    
    return module


def validate_metadata(metadata: Dict) -> List[str]:
    """
    Valida que los metadatos del gráfico estén completos.
    
    Returns:
        Lista de errores (vacía si todo está bien).
    """
    required = ['topic_id', 'name', 'description']
    errors = []
    
    for field in required:
        if field not in metadata:
            errors.append(f"Falta campo requerido: {field}")
    
    if 'topic_id' in metadata:
        config = load_config()
        if metadata['topic_id'] not in config['topics']:
            errors.append(f"topic_id '{metadata['topic_id']}' no está en config.yaml")
    
    return errors


# ============================================================
# Funciones de Generación
# ============================================================

def generate_single_graphic(
    filepath: Path,
    dry_run: bool = False,
    verbose: bool = True
) -> Tuple[bool, Optional[Dict]]:
    """
    Genera un único gráfico.
    
    Args:
        filepath: Ruta al archivo Python del gráfico.
        dry_run: Si True, solo valida sin generar.
        verbose: Si True, muestra mensajes detallados.
        
    Returns:
        Tupla (éxito, info_gráfico o None si falló).
    """
    topic = filepath.parent.name
    name = filepath.stem
    
    try:
        # Cargar módulo
        module = load_graphic_module(filepath)
        metadata = module.METADATA
        
        # Validar metadatos
        errors = validate_metadata(metadata)
        if errors:
            if verbose:
                print(f"  ❌ {topic}/{name}: Errores de validación:")
                for err in errors:
                    print(f"      - {err}")
            return False, None
        
        if dry_run:
            if verbose:
                print(f"  ✅ {topic}/{name}: Validación correcta")
            return True, metadata
        
        # Generar figura
        fig = module.generate()
        
        # Obtener directorio de salida
        output_dir = get_output_dir_for_topic(metadata['topic_id'])
        
        # Guardar figura
        paths = save_figure(fig, output_dir, metadata['name'])
        
        # Crear info para manifest
        graphic_info = {
            'name': metadata['name'],
            'description': metadata.get('description', ''),
            'used_in': metadata.get('used_in', []),
            'section': metadata.get('section', ''),
            'source_file': f"sources/{topic}/{name}.py",
            'files': {fmt: p.name for fmt, p in paths.items()},
            'generated_at': datetime.now().isoformat()
        }
        
        # Actualizar manifest
        update_manifest(output_dir, graphic_info)
        
        if verbose:
            files_str = ", ".join(paths.keys())
            print(f"  ✅ {topic}/{metadata['name']} → [{files_str}]")
        
        return True, graphic_info
        
    except Exception as e:
        if verbose:
            print(f"  ❌ {topic}/{name}: {type(e).__name__}: {e}")
            if '--debug' in sys.argv:
                traceback.print_exc()
        return False, None


def generate_all_graphics(
    topic: Optional[str] = None,
    file_pattern: Optional[str] = None,
    dry_run: bool = False
) -> Dict[str, List[Dict]]:
    """
    Genera todos los gráficos que coincidan con los filtros.
    
    Returns:
        Diccionario {topic: [lista de info de gráficos generados]}
    """
    graphics = discover_graphics(topic, file_pattern)
    
    if not graphics:
        print("⚠️  No se encontraron gráficos para generar.")
        return {}
    
    action = "Validando" if dry_run else "Generando"
    print(f"\n🎨 {action} {len(graphics)} gráfico(s)...\n")
    
    results_by_topic: Dict[str, List[Dict]] = {}
    success_count = 0
    fail_count = 0
    
    for graphic_path in graphics:
        topic_name = graphic_path.parent.name
        
        success, info = generate_single_graphic(
            graphic_path, 
            dry_run=dry_run,
            verbose=True
        )
        
        if success:
            success_count += 1
            if info:
                if topic_name not in results_by_topic:
                    results_by_topic[topic_name] = []
                results_by_topic[topic_name].append(info)
        else:
            fail_count += 1
    
    # Resumen
    print(f"\n{'─' * 40}")
    if dry_run:
        print(f"📋 Validación completada: {success_count} válidos, {fail_count} con errores")
    else:
        print(f"🎉 Generación completada: {success_count} exitosos, {fail_count} fallidos")
    
    return results_by_topic


# ============================================================
# Comandos Auxiliares
# ============================================================

def list_graphics(topic: Optional[str] = None) -> None:
    """Lista todos los gráficos disponibles."""
    graphics = discover_graphics(topic)
    
    if not graphics:
        print("⚠️  No se encontraron gráficos.")
        return
    
    print(f"\n📊 Gráficos disponibles: {len(graphics)}\n")
    
    current_topic = None
    for g in graphics:
        if g.parent.name != current_topic:
            current_topic = g.parent.name
            print(f"\n  📁 {current_topic}/")
        
        # Intentar cargar metadatos para mostrar descripción
        try:
            module = load_graphic_module(g)
            desc = module.METADATA.get('description', '')[:50]
            if desc:
                print(f"     • {g.stem}: {desc}")
            else:
                print(f"     • {g.stem}")
        except Exception:
            print(f"     • {g.stem} (error al cargar)")


def show_info() -> None:
    """Muestra información del sistema."""
    config = load_config()
    repo_root = get_repo_root()
    
    print(f"""
╔══════════════════════════════════════════════════════════╗
║     Sistema de Generación de Gráficos Matemáticos        ║
║                    Versión {VERSION}                           ║
╚══════════════════════════════════════════════════════════╝

📂 Rutas:
   • Repositorio: {repo_root}
   • Fuentes: {SOURCES_DIR}
   • Config: {PACKAGE_DIR / 'config.yaml'}

🎨 Formatos de salida:
   • SVG: {'✅ Habilitado' if config['output']['svg']['enabled'] else '❌ Deshabilitado'}
   • PNG: {'✅ Habilitado' if config['output']['png']['enabled'] else '❌ Deshabilitado'} ({config['output']['png']['dpi']} DPI)

📚 Topics configurados:
""")
    for topic_id, topic_config in config['topics'].items():
        print(f"   • {topic_id}: {topic_config['name']}")


# ============================================================
# CLI Principal
# ============================================================

def main():
    """Punto de entrada principal del CLI."""
    parser = argparse.ArgumentParser(
        description="Genera gráficos matemáticos para el repositorio.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  python generate_graphics.py                    # Genera todos los gráficos
  python generate_graphics.py --topic FUN-04     # Solo gráficos de Geometría
  python generate_graphics.py --file triangulo   # Solo gráficos con 'triangulo' en el nombre
  python generate_graphics.py --check            # Valida sin generar
  python generate_graphics.py --list             # Lista gráficos disponibles
        """
    )
    
    parser.add_argument(
        '--topic', '-t',
        help="Filtrar por topic_id (ej: FUN-04)"
    )
    parser.add_argument(
        '--file', '-f',
        help="Filtrar por patrón en nombre de archivo"
    )
    parser.add_argument(
        '--check', '-c',
        action='store_true',
        help="Solo validar, no generar"
    )
    parser.add_argument(
        '--list', '-l',
        action='store_true',
        help="Listar gráficos disponibles"
    )
    parser.add_argument(
        '--info', '-i',
        action='store_true',
        help="Mostrar información del sistema"
    )
    parser.add_argument(
        '--debug',
        action='store_true',
        help="Mostrar trazas de error completas"
    )
    parser.add_argument(
        '--version', '-v',
        action='version',
        version=f'%(prog)s {VERSION}'
    )
    
    args = parser.parse_args()
    
    # Comandos de información
    if args.info:
        show_info()
        return
    
    if args.list:
        list_graphics(args.topic)
        return
    
    # Generación
    generate_all_graphics(
        topic=args.topic,
        file_pattern=args.file,
        dry_run=args.check
    )


if __name__ == "__main__":
    main()
