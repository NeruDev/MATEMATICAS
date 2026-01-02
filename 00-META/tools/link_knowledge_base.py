#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                     LINK KNOWLEDGE BASE - Jardín Digital                     ║
║══════════════════════════════════════════════════════════════════════════════║
║  Transforma un repositorio Markdown en un "Jardín Digital" interconectado   ║
║  estilo Wikipedia mediante:                                                  ║
║    1. Auto-hipervinculación desde un glosario activo                        ║
║    2. Generación de un índice wiki centralizado                             ║
╚══════════════════════════════════════════════════════════════════════════════╝

Autor: DevOps Knowledge Management Script
Versión: 1.0.0
Python: 3.8+
"""

import re
import os
from pathlib import Path
from typing import Dict, List, Tuple, Set, Optional
from dataclasses import dataclass
from collections import defaultdict

# ═══════════════════════════════════════════════════════════════════════════════
# CONFIGURACIÓN
# ═══════════════════════════════════════════════════════════════════════════════

# ⚠️ MODO SEGURO: True = solo muestra cambios, False = aplica cambios
DRY_RUN = True

# Ruta raíz del repositorio (se auto-detecta o puedes especificarla)
REPO_ROOT = Path(__file__).resolve().parent.parent.parent

# Archivos especiales en la raíz
GLOSSARY_FILE = "glossary.md"
README_FILE = "README.md"
WIKI_INDEX_FILE = "WIKI_INDEX.md"

# Carpetas a escanear para contenido
CONTENT_FOLDERS = [
    "01-Fundamentos",
    "02-Algebra-Lineal",
    "03-Calculo-Diferencial",
    "04-Calculo-Integral",
    "05-Calculo-Vectorial",
    "06-Ecuaciones-Diferenciales",
    "07-Metodos-Numericos",
]

# Subcarpetas que contienen contenido enlazable
CONTENT_SUBFOLDERS = ["theory", "problems", "methods", "applications", "solutions", "diagnostic"]

# Archivos/carpetas a ignorar
IGNORE_PATTERNS = [
    "00-META",
    "_directives.md",
    "manifest.json",
    ".git",
    "__pycache__",
    "node_modules",
]

# Emojis para tipos de contenido
CONTENT_EMOJIS = {
    "theory": "📘",
    "problems": "📝",
    "methods": "🧪",
    "applications": "🔬",
    "solutions": "✅",
    "diagnostic": "🩺",
    "index": "📑",
    "intro": "🎯",
    "resumen": "📋",
    "default": "📄",
}

# Términos mínimos para vincular (evita vincular palabras muy cortas)
MIN_TERM_LENGTH = 3

# ═══════════════════════════════════════════════════════════════════════════════
# ESTRUCTURAS DE DATOS
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class GlossaryTerm:
    """Representa un término del glosario."""
    term: str           # Texto exacto del término
    anchor: str         # Ancla para el enlace (#término)
    section: str        # Sección padre (h2)
    level: int          # Nivel del encabezado (2 o 3)


@dataclass
class FileInfo:
    """Información sobre un archivo Markdown."""
    path: Path          # Ruta completa
    relative_path: Path # Ruta relativa a la raíz
    title: str          # Título H1 o nombre del archivo
    folder_type: str    # theory, problems, etc.
    module: str         # Módulo padre (01-Fundamentos, etc.)
    submodule: str      # Submódulo (02-Aritmetica, etc.)


@dataclass
class LinkChange:
    """Representa un cambio de enlace a realizar."""
    file_path: Path
    original_text: str
    linked_text: str
    term: str
    line_number: int


# ═══════════════════════════════════════════════════════════════════════════════
# CLASE PRINCIPAL
# ═══════════════════════════════════════════════════════════════════════════════

class KnowledgeBaseLinker:
    """Motor principal para transformar el repositorio en jardín digital."""

    def __init__(self, repo_root: Path, dry_run: bool = True):
        self.repo_root = repo_root
        self.dry_run = dry_run
        self.glossary_terms: List[GlossaryTerm] = []
        self.content_files: List[FileInfo] = []
        self.changes: List[LinkChange] = []
        self.stats = defaultdict(int)

    # ─────────────────────────────────────────────────────────────────────────
    # TAREA 1: Extracción de términos del glosario
    # ─────────────────────────────────────────────────────────────────────────

    def extract_glossary_terms(self) -> List[GlossaryTerm]:
        """Extrae todos los términos (h2/h3) del glosario."""
        glossary_path = self.repo_root / GLOSSARY_FILE
        
        if not glossary_path.exists():
            print(f"⚠️  Advertencia: No se encontró {GLOSSARY_FILE}")
            return []

        terms = []
        current_section = ""
        
        content = glossary_path.read_text(encoding="utf-8")
        
        # Patrón para detectar encabezados h2 y h3
        header_pattern = re.compile(r'^(#{2,3})\s+(.+)$', re.MULTILINE)
        
        for match in header_pattern.finditer(content):
            level = len(match.group(1))
            title = match.group(2).strip()
            
            # Actualizar sección actual si es h2
            if level == 2:
                current_section = title
            
            # Crear ancla estilo GitHub (minúsculas, espacios a guiones)
            anchor = self._create_github_anchor(title)
            
            term = GlossaryTerm(
                term=title,
                anchor=anchor,
                section=current_section,
                level=level
            )
            terms.append(term)
            
            # También extraer términos en negrita de tablas (términos principales)
            # Buscar patrones como | **Término** |
            
        # Extraer términos de tablas (en negrita)
        table_term_pattern = re.compile(r'\|\s*\*\*([^*|]+)\*\*\s*\|')
        for match in table_term_pattern.finditer(content):
            term_text = match.group(1).strip()
            if len(term_text) >= MIN_TERM_LENGTH:
                # Crear ancla usando la convención de GitHub para tablas
                anchor = self._create_github_anchor(term_text)
                
                # Evitar duplicados
                if not any(t.term.lower() == term_text.lower() for t in terms):
                    terms.append(GlossaryTerm(
                        term=term_text,
                        anchor=anchor,
                        section=current_section,
                        level=4  # Nivel especial para términos de tabla
                    ))

        self.glossary_terms = terms
        print(f"📚 Extraídos {len(terms)} términos del glosario")
        return terms

    def _create_github_anchor(self, text: str) -> str:
        """Crea un ancla estilo GitHub a partir de texto."""
        # Convertir a minúsculas
        anchor = text.lower()
        # Remover caracteres especiales excepto espacios y guiones
        anchor = re.sub(r'[^\w\s-]', '', anchor, flags=re.UNICODE)
        # Reemplazar espacios por guiones
        anchor = re.sub(r'\s+', '-', anchor)
        # Remover guiones múltiples
        anchor = re.sub(r'-+', '-', anchor)
        # Remover guiones al inicio y final
        anchor = anchor.strip('-')
        return anchor

    # ─────────────────────────────────────────────────────────────────────────
    # TAREA 1: Escaneo y modificación de archivos
    # ─────────────────────────────────────────────────────────────────────────

    def scan_content_files(self) -> List[FileInfo]:
        """Escanea todos los archivos .md en las carpetas de contenido."""
        files = []
        
        for folder in CONTENT_FOLDERS:
            folder_path = self.repo_root / folder
            if not folder_path.exists():
                continue
                
            # Buscar recursivamente archivos .md
            for md_file in folder_path.rglob("*.md"):
                # Verificar si debe ignorarse
                if self._should_ignore(md_file):
                    continue
                
                file_info = self._extract_file_info(md_file)
                if file_info:
                    files.append(file_info)

        self.content_files = files
        print(f"📁 Encontrados {len(files)} archivos de contenido")
        return files

    def _should_ignore(self, path: Path) -> bool:
        """Verifica si un archivo debe ignorarse."""
        path_str = str(path)
        for pattern in IGNORE_PATTERNS:
            if pattern in path_str:
                return True
        return False

    def _extract_file_info(self, file_path: Path) -> Optional[FileInfo]:
        """Extrae información de un archivo Markdown."""
        try:
            content = file_path.read_text(encoding="utf-8")
            relative_path = file_path.relative_to(self.repo_root)
            
            # Extraer título H1
            title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            title = title_match.group(1).strip() if title_match else file_path.stem
            
            # Determinar tipo de carpeta
            parts = relative_path.parts
            folder_type = "default"
            module = parts[0] if len(parts) > 0 else ""
            submodule = parts[1] if len(parts) > 1 else ""
            
            for subfolder in CONTENT_SUBFOLDERS:
                if subfolder in parts:
                    folder_type = subfolder
                    break
            
            # Detectar tipos especiales por nombre de archivo
            filename_lower = file_path.stem.lower()
            if "index" in filename_lower:
                folder_type = "index"
            elif "intro" in filename_lower:
                folder_type = "intro"
            elif "resumen" in filename_lower:
                folder_type = "resumen"

            return FileInfo(
                path=file_path,
                relative_path=relative_path,
                title=title,
                folder_type=folder_type,
                module=module,
                submodule=submodule
            )
        except Exception as e:
            print(f"⚠️  Error leyendo {file_path}: {e}")
            return None

    def process_file_links(self, file_info: FileInfo) -> List[LinkChange]:
        """Procesa un archivo para agregar enlaces al glosario."""
        changes = []
        
        try:
            content = file_info.path.read_text(encoding="utf-8")
            original_content = content
            
            # Términos ya enlazados en este archivo
            linked_terms: Set[str] = set()
            
            # Ordenar términos por longitud (más largos primero para evitar conflictos)
            sorted_terms = sorted(
                self.glossary_terms, 
                key=lambda t: len(t.term), 
                reverse=True
            )
            
            for term in sorted_terms:
                if len(term.term) < MIN_TERM_LENGTH:
                    continue
                    
                term_lower = term.term.lower()
                
                # Saltar si ya se enlazó este término
                if term_lower in linked_terms:
                    continue
                
                # Buscar la primera aparición del término
                new_content, was_changed, line_num = self._link_first_occurrence(
                    content, 
                    term, 
                    file_info.relative_path
                )
                
                if was_changed:
                    # Calcular ruta relativa al glosario
                    rel_path = self._calculate_relative_path(
                        file_info.path, 
                        self.repo_root / GLOSSARY_FILE
                    )
                    
                    changes.append(LinkChange(
                        file_path=file_info.path,
                        original_text=term.term,
                        linked_text=f"[{term.term}]({rel_path}#{term.anchor})",
                        term=term.term,
                        line_number=line_num
                    ))
                    
                    content = new_content
                    linked_terms.add(term_lower)
                    self.stats["links_added"] += 1

            # Guardar cambios si no es dry run
            if content != original_content:
                self.stats["files_modified"] += 1
                if not self.dry_run:
                    file_info.path.write_text(content, encoding="utf-8")
                    
        except Exception as e:
            print(f"⚠️  Error procesando {file_info.path}: {e}")
            
        return changes

    def _link_first_occurrence(
        self, 
        content: str, 
        term: GlossaryTerm,
        file_relative_path: Path
    ) -> Tuple[str, bool, int]:
        """
        Encuentra y enlaza la primera aparición de un término.
        Respeta bloques de código, enlaces existentes y encabezados.
        """
        # Calcular ruta relativa al glosario
        depth = len(file_relative_path.parts) - 1
        rel_path = "../" * depth + GLOSSARY_FILE
        
        # Escapar el término para regex
        escaped_term = re.escape(term.term)
        
        # Patrón para encontrar el término como palabra completa
        # Ignora mayúsculas/minúsculas pero captura el texto original
        pattern = re.compile(
            rf'(?<![#\[\w])({escaped_term})(?![\]\w])',
            re.IGNORECASE
        )
        
        lines = content.split('\n')
        in_code_block = False
        
        for i, line in enumerate(lines):
            # Detectar bloques de código
            if line.strip().startswith('```'):
                in_code_block = not in_code_block
                continue
            
            if in_code_block:
                continue
            
            # Ignorar encabezados
            if line.strip().startswith('#'):
                continue
            
            # Ignorar líneas que ya tienen enlaces
            if re.search(rf'\[{escaped_term}\]', line, re.IGNORECASE):
                continue
            
            # Ignorar líneas dentro de tablas de definición del glosario
            if '|' in line and '**' in line:
                continue
                
            # Ignorar líneas de código inline
            if self._is_in_inline_code(line, term.term):
                continue
            
            # Buscar el término
            match = pattern.search(line)
            if match:
                original_text = match.group(1)
                link = f"[{original_text}]({rel_path}#{term.anchor})"
                
                # Reemplazar solo esta primera ocurrencia
                new_line = line[:match.start()] + link + line[match.end():]
                lines[i] = new_line
                
                return '\n'.join(lines), True, i + 1
        
        return content, False, 0

    def _is_in_inline_code(self, line: str, term: str) -> bool:
        """Verifica si el término está dentro de código inline."""
        # Buscar todas las secciones de código inline
        code_sections = re.findall(r'`[^`]+`', line)
        for section in code_sections:
            if term.lower() in section.lower():
                return True
        return False

    def _calculate_relative_path(self, from_file: Path, to_file: Path) -> str:
        """Calcula la ruta relativa entre dos archivos."""
        try:
            rel_path = os.path.relpath(to_file, from_file.parent)
            # Normalizar separadores para Markdown (usar /)
            return rel_path.replace('\\', '/')
        except ValueError:
            # En caso de diferentes unidades en Windows
            return to_file.as_posix()

    # ─────────────────────────────────────────────────────────────────────────
    # TAREA 2: Generación del Wiki Index
    # ─────────────────────────────────────────────────────────────────────────

    def generate_wiki_index(self) -> str:
        """Genera el contenido del archivo WIKI_INDEX.md."""
        lines = []
        
        # Cabecera
        lines.append("# 🌐 Wiki Index - Jardín Digital de Matemáticas")
        lines.append("")
        lines.append("> *Mapa de navegación centralizado del repositorio*")
        lines.append("")
        lines.append("---")
        lines.append("")
        
        # Navegación principal
        lines.append("## 🏠 Navegación Principal")
        lines.append("")
        lines.append(f"- 📖 [README Principal]({README_FILE})")
        lines.append(f"- 📚 [Glosario de Términos]({GLOSSARY_FILE})")
        lines.append("")
        lines.append("---")
        lines.append("")
        
        # Árbol de contenido
        lines.append("## 📂 Árbol de Contenido")
        lines.append("")
        
        # Organizar archivos por módulo y submódulo
        content_tree = self._build_content_tree()
        
        for module, submodules in content_tree.items():
            # Nombre limpio del módulo
            module_name = self._clean_module_name(module)
            module_emoji = self._get_module_emoji(module)
            
            lines.append(f"### {module_emoji} {module_name}")
            lines.append("")
            
            for submodule, categories in submodules.items():
                if submodule:
                    submodule_name = self._clean_module_name(submodule)
                    lines.append(f"#### {submodule_name}")
                    lines.append("")
                
                for category, files in categories.items():
                    if files:
                        emoji = CONTENT_EMOJIS.get(category, CONTENT_EMOJIS["default"])
                        category_name = category.replace("-", " ").title()
                        
                        lines.append(f"**{emoji} {category_name}**")
                        lines.append("")
                        
                        for file_info in files:
                            rel_path = file_info.relative_path.as_posix()
                            lines.append(f"  - [{file_info.title}]({rel_path})")
                        
                        lines.append("")
            
            lines.append("---")
            lines.append("")
        
        # Estadísticas
        lines.append("## 📊 Estadísticas del Repositorio")
        lines.append("")
        lines.append(f"- **Total de archivos**: {len(self.content_files)}")
        lines.append(f"- **Módulos principales**: {len(CONTENT_FOLDERS)}")
        lines.append(f"- **Términos en glosario**: {len(self.glossary_terms)}")
        lines.append("")
        lines.append("---")
        lines.append("")
        lines.append("*Índice generado automáticamente por `link_knowledge_base.py`*")
        
        return '\n'.join(lines)

    def _build_content_tree(self) -> Dict:
        """Construye el árbol jerárquico de contenido."""
        tree = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
        
        for file_info in self.content_files:
            tree[file_info.module][file_info.submodule][file_info.folder_type].append(file_info)
        
        # Ordenar archivos dentro de cada categoría
        for module in tree:
            for submodule in tree[module]:
                for category in tree[module][submodule]:
                    tree[module][submodule][category].sort(
                        key=lambda f: f.relative_path.name
                    )
        
        return tree

    def _clean_module_name(self, name: str) -> str:
        """Limpia el nombre de un módulo para mostrar."""
        # Remover prefijo numérico (01-, 02-, etc.)
        clean = re.sub(r'^\d{2}-', '', name)
        # Reemplazar guiones por espacios
        clean = clean.replace('-', ' ')
        return clean

    def _get_module_emoji(self, module: str) -> str:
        """Obtiene un emoji apropiado para el módulo."""
        module_emojis = {
            "fundamentos": "🔢",
            "algebra": "🔤",
            "calculo": "📈",
            "diferencial": "📉",
            "integral": "∫",
            "vectorial": "➡️",
            "ecuaciones": "⚙️",
            "numericos": "🖥️",
            "lineal": "📐",
        }
        
        module_lower = module.lower()
        for key, emoji in module_emojis.items():
            if key in module_lower:
                return emoji
        return "📁"

    # ─────────────────────────────────────────────────────────────────────────
    # Ejecución principal
    # ─────────────────────────────────────────────────────────────────────────

    def run(self):
        """Ejecuta el proceso completo de transformación."""
        print("=" * 70)
        print("🌱 LINK KNOWLEDGE BASE - Jardín Digital")
        print("=" * 70)
        print(f"📍 Repositorio: {self.repo_root}")
        print(f"🔒 Modo: {'DRY RUN (simulación)' if self.dry_run else '⚠️  ESCRITURA REAL'}")
        print("=" * 70)
        print()
        
        # Paso 1: Extraer términos del glosario
        print("📚 PASO 1: Extrayendo términos del glosario...")
        self.extract_glossary_terms()
        print()
        
        # Paso 2: Escanear archivos de contenido
        print("📁 PASO 2: Escaneando archivos de contenido...")
        self.scan_content_files()
        print()
        
        # Paso 3: Procesar enlaces
        print("🔗 PASO 3: Procesando enlaces automáticos...")
        for file_info in self.content_files:
            changes = self.process_file_links(file_info)
            self.changes.extend(changes)
        print()
        
        # Paso 4: Generar Wiki Index
        print("📑 PASO 4: Generando Wiki Index...")
        wiki_content = self.generate_wiki_index()
        wiki_path = self.repo_root / WIKI_INDEX_FILE
        
        if self.dry_run:
            print(f"   [DRY RUN] Se crearía: {wiki_path}")
            print("-" * 50)
            print("Vista previa del WIKI_INDEX.md (primeras 50 líneas):")
            print("-" * 50)
            preview_lines = wiki_content.split('\n')[:50]
            for line in preview_lines:
                print(f"   {line}")
            print("   ...")
        else:
            wiki_path.write_text(wiki_content, encoding="utf-8")
            print(f"   ✅ Creado: {wiki_path}")
        print()
        
        # Resumen de cambios
        self._print_summary()

    def _print_summary(self):
        """Imprime el resumen de cambios realizados."""
        print("=" * 70)
        print("📊 RESUMEN DE CAMBIOS")
        print("=" * 70)
        print(f"   📚 Términos del glosario: {len(self.glossary_terms)}")
        print(f"   📁 Archivos escaneados: {len(self.content_files)}")
        print(f"   🔗 Enlaces añadidos: {self.stats['links_added']}")
        print(f"   📝 Archivos modificados: {self.stats['files_modified']}")
        print()
        
        if self.changes:
            print("-" * 70)
            print("📋 DETALLE DE ENLACES AÑADIDOS:")
            print("-" * 70)
            
            # Agrupar por archivo
            changes_by_file = defaultdict(list)
            for change in self.changes:
                changes_by_file[change.file_path].append(change)
            
            for file_path, file_changes in changes_by_file.items():
                rel_path = file_path.relative_to(self.repo_root)
                print(f"\n   📄 {rel_path}")
                for change in file_changes[:5]:  # Mostrar máximo 5 por archivo
                    print(f"      L{change.line_number}: '{change.term}' → enlazado")
                if len(file_changes) > 5:
                    print(f"      ... y {len(file_changes) - 5} más")
        
        print()
        print("=" * 70)
        
        if self.dry_run:
            print("🔒 MODO DRY RUN: No se realizaron cambios reales.")
            print("   Para aplicar los cambios, cambia DRY_RUN = False")
            print("   o ejecuta con: python link_knowledge_base.py --apply")
        else:
            print("✅ Cambios aplicados exitosamente.")
        
        print("=" * 70)


# ═══════════════════════════════════════════════════════════════════════════════
# PUNTO DE ENTRADA
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    """Función principal."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Transforma el repositorio en un Jardín Digital interconectado"
    )
    parser.add_argument(
        "--apply", 
        action="store_true",
        help="Aplicar cambios reales (sin esta opción, solo simula)"
    )
    parser.add_argument(
        "--repo", 
        type=str,
        default=None,
        help="Ruta al repositorio (por defecto, detecta automáticamente)"
    )
    parser.add_argument(
        "--only-index",
        action="store_true",
        help="Solo generar el WIKI_INDEX.md sin procesar enlaces"
    )
    parser.add_argument(
        "--only-links",
        action="store_true",
        help="Solo procesar enlaces sin generar el índice"
    )
    
    args = parser.parse_args()
    
    # Determinar modo de ejecución
    dry_run = DRY_RUN and not args.apply
    
    # Determinar ruta del repositorio
    if args.repo:
        repo_root = Path(args.repo).resolve()
    else:
        repo_root = REPO_ROOT
    
    # Verificar que existe el repositorio
    if not repo_root.exists():
        print(f"❌ Error: No se encontró el repositorio en {repo_root}")
        return 1
    
    # Crear y ejecutar el linker
    linker = KnowledgeBaseLinker(repo_root, dry_run=dry_run)
    
    if args.only_index:
        print("📑 Modo: Solo generación de índice")
        linker.extract_glossary_terms()
        linker.scan_content_files()
        wiki_content = linker.generate_wiki_index()
        wiki_path = repo_root / WIKI_INDEX_FILE
        if not dry_run:
            wiki_path.write_text(wiki_content, encoding="utf-8")
            print(f"✅ Creado: {wiki_path}")
        else:
            print(f"[DRY RUN] Se crearía: {wiki_path}")
            print(wiki_content[:2000])
    elif args.only_links:
        print("🔗 Modo: Solo procesamiento de enlaces")
        linker.extract_glossary_terms()
        linker.scan_content_files()
        for file_info in linker.content_files:
            linker.process_file_links(file_info)
        linker._print_summary()
    else:
        linker.run()
    
    return 0


if __name__ == "__main__":
    exit(main())
