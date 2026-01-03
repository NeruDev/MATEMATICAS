# Sistema de Generación de Gráficos Matemáticos

> Herramientas para generar figuras SVG y PNG de alta calidad para el repositorio.

## 🚀 Inicio Rápido

```bash
# Instalar dependencias
pip install -r requirements.txt

# Generar todos los gráficos
python generate_graphics.py

# Generar solo un tema
python generate_graphics.py --topic FUN-04

# Listar gráficos disponibles
python generate_graphics.py --list

# Validar sin generar
python generate_graphics.py --check
```

## 📁 Estructura

```
graphics/
├── __init__.py                     # Paquete principal
├── generate_graphics.py            # Motor de generación
├── config.yaml                     # Configuración global
├── requirements.txt                # Dependencias Python
├── templates/                      # Estilos reutilizables
│   ├── __init__.py
│   ├── style_common.py             # Funciones base
│   └── style_2d.py                 # Gráficos 2D (geometría)
└── sources/                        # Código fuente de gráficos
    └── {TOPIC}/                    # Organizados por tema
        └── nombre_grafico.py
```

## 📐 Crear un Nuevo Gráfico

### 1. Crear archivo en `sources/{TOPIC}/`

```python
"""
Gráfico: Descripción del gráfico
===============================

Topic: FUN-04 Geometría
Usado en: theory/FUN-04-Teoria-Geometria.md
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import matplotlib.pyplot as plt
from templates import setup_style, get_colors, get_output_dir_for_topic, save_figure

# Metadatos obligatorios
METADATA = {
    "topic_id": "FUN-04",           # Debe existir en config.yaml
    "name": "nombre_grafico",        # Sin espacios, lowercase
    "description": "Descripción",    # Para el manifest
    "used_in": ["theory/archivo.md"],# Archivos que lo usan
    "section": "4.3",                # Sección del tema
}

def generate() -> plt.Figure:
    """Genera el gráfico. OBLIGATORIO."""
    setup_style()
    colors = get_colors()
    
    fig, ax = plt.subplots(figsize=(8, 6))
    # ... código del gráfico ...
    
    ax.axis('off')
    return fig

def get_output_dir():
    """Retorna directorio de salida."""
    return get_output_dir_for_topic(METADATA["topic_id"])

if __name__ == "__main__":
    fig = generate()
    paths = save_figure(fig, get_output_dir(), METADATA["name"])
    print(f"✅ Generado: {paths}")
```

### 2. Generar el gráfico

```bash
python generate_graphics.py --file nombre_grafico
```

### 3. Referenciar en Markdown

```markdown
![Descripción del gráfico](media/generated/nombre_grafico.png)

*Figura X.Y.Z: Leyenda explicativa*
```

## 🎨 Paleta de Colores

La paleta está definida en `config.yaml` y es consistente en todo el repositorio:

| Color | Uso | Código |
|-------|-----|--------|
| `primary` | Figuras principales | `#2563eb` (azul) |
| `secondary` | Elementos destacados | `#dc2626` (rojo) |
| `accent` | Elementos auxiliares | `#059669` (verde) |
| `tertiary` | Tercer nivel | `#7c3aed` (púrpura) |
| `text` | Texto y etiquetas | `#1f2937` (gris oscuro) |

```python
from templates import get_colors
colors = get_colors()
ax.plot(x, y, color=colors['primary'])
```

## 📦 Salida

Los gráficos se generan en:
```
{MODULO}/{SUBTEMA}/media/generated/
├── nombre.svg      # Para sitio web estático (escalable)
├── nombre.png      # Para Markdown/GitHub (150 DPI)
└── manifest.json   # Registro de gráficos generados
```

## ⚙️ Configuración

Editar `config.yaml` para:

- Añadir nuevos `topics` (módulos/subtemas)
- Cambiar la paleta de colores
- Ajustar DPI de salida
- Modificar tamaños de figura

## 🔧 Funciones Disponibles

### style_common.py

| Función | Descripción |
|---------|-------------|
| `setup_style()` | Configura matplotlib |
| `get_colors()` | Obtiene paleta de colores |
| `save_figure()` | Guarda en SVG + PNG |
| `get_output_dir_for_topic()` | Ruta de salida por tema |
| `annotate_point()` | Añade etiqueta a punto |
| `draw_polygon()` | Dibuja polígono |

### style_2d.py

| Función | Descripción |
|---------|-------------|
| `create_triangle_figure()` | Crea triángulo base |
| `draw_altitude()` | Dibuja altura |
| `draw_median()` | Dibuja mediana |
| `draw_circle()` | Dibuja circunferencia |
| `draw_angle_arc()` | Dibuja arco de ángulo |
| `draw_parallel_lines_with_transversal()` | Paralelas con transversal |

## 📋 Topics Configurados

| Topic ID | Módulo | Subtema |
|----------|--------|---------|
| `FUN-04` | 01-Fundamentos | 04-Geometria |
| `FUN-05` | 01-Fundamentos | 05-Trigonometria |
| `CV-02` | 05-Calculo-Vectorial | 02-Curvas-planas-parametricas-y-polares |

Para añadir más, editar la sección `topics` en `config.yaml`.

---

*Sistema desarrollado para el Repositorio de Matemáticas Universitarias*
