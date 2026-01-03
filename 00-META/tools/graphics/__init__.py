"""
Sistema de Generación de Gráficos Matemáticos
=============================================

Este paquete proporciona herramientas para generar gráficos matemáticos
en formato SVG y PNG para el Repositorio de Matemáticas Universitarias.

Uso básico:
    from graphics import generate_all, generate_topic
    
    # Generar todos los gráficos
    generate_all()
    
    # Generar solo un tema específico
    generate_topic("FUN-04")

Estructura:
    - templates/: Estilos y funciones reutilizables
    - sources/: Código fuente de cada gráfico por tema
    - config.yaml: Configuración global
"""

__version__ = "1.0.0"
__author__ = "Repositorio Matemáticas"

from pathlib import Path

PACKAGE_DIR = Path(__file__).parent
CONFIG_PATH = PACKAGE_DIR / "config.yaml"
SOURCES_DIR = PACKAGE_DIR / "sources"
TEMPLATES_DIR = PACKAGE_DIR / "templates"
