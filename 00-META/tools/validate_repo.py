#!/usr/bin/env python3
"""
================================================================================
VALIDADOR DE REPOSITORIO DE MATEMÁTICAS
================================================================================
Script consolidado para verificar la integridad y coherencia del repositorio.
Incluye validación de:
- Metadatos ::METADATA:: en archivos .md
- Estructura de manifest.json
- Nomenclatura estándar de archivos
- Coherencia de referencias
- Sintaxis de tablas con contenido matemático

Autor: Sistema automatizado
Versión: 2.0
Última actualización: 2025-01-30
================================================================================
"""

import os
import json
import re
import sys
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Dict, Set, Tuple, Optional
from enum import Enum
from datetime import datetime


# ==============================================================================
# CONFIGURACIÓN Y CONSTANTES
# ==============================================================================

class Severity(Enum):
    """Niveles de severidad para los problemas encontrados."""
    ERROR = "❌"
    WARNING = "⚠️"
    INFO = "ℹ️"


# Prefijos válidos por módulo
PREFIXES = {
    "01-Fundamentos": "FUN",
    "02-Algebra-Lineal": "AL",
    "03-Calculo-Diferencial": "CD",
    "04-Calculo-Integral": "CI",
    "05-Calculo-Vectorial": "CV",
    "06-Ecuaciones-Diferenciales": "ED",
    "07-Metodos-Numericos": "MN",
}

# Sufijos válidos por tipo de contenido
VALID_SUFFIXES = [
    "-Intro", "-Resumen-Formulas", "-Teoria", "-Metodos", "-Metodo-",
    "-Problemas", "-Problema-", "-Respuestas", "-Solucion-", "-Aplicacion-",
    "-Aplicaciones-", "-Diagnostico", "-Index", "-Formulas"
]

# Tipos válidos de ::METADATA::
VALID_METADATA_TYPES = [
    "theory", "method", "problem", "solution", "reference", 
    "index", "cheatsheet", "cheat-sheet", "problem_set", "problem-set",
    "answer-key", "methods", "application"
]

# Tipos válidos de manifest.json
VALID_MANIFEST_TYPES = ["learning_module", "reference_library"]

# Campos obligatorios en manifest.json
REQUIRED_MANIFEST_FIELDS = ["id", "topic", "type", "status", "tags"]


# ==============================================================================
# EXCEPCIONES AL ESTÁNDAR
# ==============================================================================

class NomenclatureExceptions:
    """Define todas las excepciones documentadas al estándar de nomenclatura."""
    
    # Carpetas completamente exentas del sistema de prefijos
    EXEMPT_FOLDERS = {
        "01-Fundamentos/01-Simbologia-Matematica/theory": 
            "Biblioteca de referencia sin secuencia de aprendizaje",
        "00-META": 
            "Carpeta de metadatos del repositorio",
        "00-META/tools":
            "Herramientas de validación y scripts",
    }
    
    # Patrones de archivos exentos (dentro de cualquier carpeta)
    EXEMPT_FILE_PATTERNS = [
        r"^_directives\.md$",           # Archivos de directivas
        r"^manifest\.json$",            # Manifiestos
        r"^README\.md$",                # README en raíz
        r"^solucion-.*\.md$",           # Soluciones dentro de prob-XX/
        r"^AUDITORIA.*\.md$",           # Archivos de auditoría
        r"^glossary\.md$",              # Glosario
        r"^00-Index\.md$",              # Índices de módulo
    ]
    
    # Carpetas donde los archivos internos están exentos
    EXEMPT_INTERNAL_FOLDERS = [
        "prob-",                        # Carpetas de soluciones prob-XX/
        "media",                        # Recursos multimedia
        "assets",                       # Recursos adicionales
    ]
    
    # Archivos específicos exentos (rutas relativas desde raíz)
    EXEMPT_SPECIFIC_FILES = {
        "README.md": "Archivo principal del repositorio",
        "glossary.md": "Glosario global",
        "AUDITORIA_ESTADO_REPO.md": "Documento de auditoría",
    }
    
    @classmethod
    def is_exempt(cls, filepath: str, root: str) -> Tuple[bool, str]:
        """
        Verifica si un archivo está exento del estándar de nomenclatura.
        
        Returns:
            Tuple[bool, str]: (está_exento, razón)
        """
        rel_path = os.path.relpath(filepath, root)
        filename = os.path.basename(filepath)
        parent_dir = os.path.dirname(rel_path)
        
        # Verificar archivo específico exento
        if rel_path.replace("\\", "/") in cls.EXEMPT_SPECIFIC_FILES:
            return True, cls.EXEMPT_SPECIFIC_FILES[rel_path.replace("\\", "/")]
        
        # Verificar carpeta exenta
        for exempt_folder, reason in cls.EXEMPT_FOLDERS.items():
            if parent_dir.replace("\\", "/").startswith(exempt_folder):
                return True, reason
        
        # Verificar patrón de archivo exento
        for pattern in cls.EXEMPT_FILE_PATTERNS:
            if re.match(pattern, filename):
                return True, f"Patrón exento: {pattern}"
        
        # Verificar si está dentro de carpeta interna exenta
        for exempt_internal in cls.EXEMPT_INTERNAL_FOLDERS:
            if exempt_internal in parent_dir:
                return True, f"Dentro de carpeta exenta: {exempt_internal}"
        
        return False, ""


# ==============================================================================
# ESTRUCTURAS DE DATOS
# ==============================================================================

@dataclass
class ValidationIssue:
    """Representa un problema encontrado durante la validación."""
    filepath: str
    severity: Severity
    category: str
    message: str
    suggestion: str = ""
    
    def __str__(self) -> str:
        s = f"{self.severity.value} [{self.category}] {self.filepath}\n   {self.message}"
        if self.suggestion:
            s += f"\n   💡 {self.suggestion}"
        return s


@dataclass
class ValidationReport:
    """Reporte completo de validación."""
    root: str
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    issues: List[ValidationIssue] = field(default_factory=list)
    stats: Dict[str, int] = field(default_factory=dict)
    
    def add_issue(self, issue: ValidationIssue):
        self.issues.append(issue)
    
    @property
    def errors(self) -> List[ValidationIssue]:
        return [i for i in self.issues if i.severity == Severity.ERROR]
    
    @property
    def warnings(self) -> List[ValidationIssue]:
        return [i for i in self.issues if i.severity == Severity.WARNING]
    
    @property
    def infos(self) -> List[ValidationIssue]:
        return [i for i in self.issues if i.severity == Severity.INFO]


# ==============================================================================
# VALIDADORES
# ==============================================================================

class MetadataValidator:
    """Valida los bloques ::METADATA:: en archivos .md"""
    
    METADATA_PATTERN = re.compile(
        r'<!--[\s\S]*?::METADATA::[\s\S]*?-->',
        re.MULTILINE
    )
    
    # Frontmatter dentro de comentario HTML (busca cualquier campo type o content_type)
    FRONTMATTER_PATTERN = re.compile(
        r'<!--[\s\S]*?---\s*\n[\s\S]*?(content_type|type):\s*\w+[\s\S]*?---[\s\S]*?-->',
        re.MULTILINE
    )
    
    LEGACY_FRONTMATTER = re.compile(
        r'^---\s*\n[\s\S]*?\n---',
        re.MULTILINE
    )
    
    @classmethod
    def has_valid_metadata(cls, content: str) -> Tuple[bool, str]:
        """
        Verifica si el contenido tiene metadatos válidos.
        
        Returns:
            Tuple[bool, str]: (tiene_metadatos, tipo_encontrado)
        """
        # Buscar ::METADATA:: (formato nuevo)
        if cls.METADATA_PATTERN.search(content[:3000]):
            return True, "::METADATA::"
        
        # Buscar frontmatter en comentario HTML (formato intermedio)
        if cls.FRONTMATTER_PATTERN.search(content[:3000]):
            return True, "frontmatter_html"
        
        # Buscar frontmatter legacy (fuera de comentario)
        if cls.LEGACY_FRONTMATTER.match(content):
            return True, "frontmatter_legacy"
        
        return False, "none"
    
    @classmethod
    def extract_metadata(cls, content: str) -> Dict[str, str]:
        """Extrae los campos del bloque ::METADATA::"""
        metadata = {}
        match = cls.METADATA_PATTERN.search(content[:3000])
        if match:
            block = match.group()
            # Extraer campos tipo: valor
            for line in block.split('\n'):
                if ':' in line and not line.strip().startswith('<!--') and not line.strip().startswith('::'):
                    parts = line.split(':', 1)
                    if len(parts) == 2:
                        key = parts[0].strip()
                        value = parts[1].strip()
                        if key and value:
                            metadata[key] = value
        return metadata
    
    @classmethod
    def validate_file(cls, filepath: str, report: ValidationReport):
        """Valida un archivo .md específico."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            report.add_issue(ValidationIssue(
                filepath=filepath,
                severity=Severity.ERROR,
                category="FILE_READ",
                message=f"No se pudo leer el archivo: {e}"
            ))
            return
        
        has_meta, meta_type = cls.has_valid_metadata(content)
        
        if not has_meta:
            report.add_issue(ValidationIssue(
                filepath=filepath,
                severity=Severity.WARNING,
                category="METADATA",
                message="Archivo sin metadatos (::METADATA:: o frontmatter)",
                suggestion="Agregar bloque ::METADATA:: al inicio del archivo"
            ))
        elif meta_type == "frontmatter_legacy":
            report.add_issue(ValidationIssue(
                filepath=filepath,
                severity=Severity.INFO,
                category="METADATA",
                message="Usa frontmatter legacy (fuera de comentario HTML)",
                suggestion="Migrar a formato ::METADATA:: dentro de comentario HTML"
            ))
        
        # Validar campos si tiene ::METADATA::
        if meta_type == "::METADATA::":
            metadata = cls.extract_metadata(content)
            if 'type' not in metadata:
                report.add_issue(ValidationIssue(
                    filepath=filepath,
                    severity=Severity.WARNING,
                    category="METADATA",
                    message="Campo 'type' faltante en ::METADATA::"
                ))
            elif metadata.get('type') not in VALID_METADATA_TYPES:
                report.add_issue(ValidationIssue(
                    filepath=filepath,
                    severity=Severity.INFO,
                    category="METADATA",
                    message=f"Tipo '{metadata.get('type')}' no está en la lista estándar",
                    suggestion=f"Tipos válidos: {', '.join(VALID_METADATA_TYPES)}"
                ))


class ManifestValidator:
    """Valida archivos manifest.json"""
    
    @classmethod
    def validate_manifest(cls, filepath: str, report: ValidationReport):
        """Valida un archivo manifest.json específico."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            report.add_issue(ValidationIssue(
                filepath=filepath,
                severity=Severity.ERROR,
                category="MANIFEST",
                message=f"JSON inválido: {e}"
            ))
            return
        except Exception as e:
            report.add_issue(ValidationIssue(
                filepath=filepath,
                severity=Severity.ERROR,
                category="MANIFEST",
                message=f"Error leyendo archivo: {e}"
            ))
            return
        
        # Verificar campos obligatorios
        for fld in REQUIRED_MANIFEST_FIELDS:
            if fld not in data:
                report.add_issue(ValidationIssue(
                    filepath=filepath,
                    severity=Severity.ERROR,
                    category="MANIFEST",
                    message=f"Campo obligatorio faltante: '{fld}'"
                ))
        
        # Verificar tipo válido
        if 'type' in data and data['type'] not in VALID_MANIFEST_TYPES:
            report.add_issue(ValidationIssue(
                filepath=filepath,
                severity=Severity.WARNING,
                category="MANIFEST",
                message=f"Tipo '{data['type']}' no reconocido",
                suggestion=f"Tipos válidos: {', '.join(VALID_MANIFEST_TYPES)}"
            ))
        
        # Verificar resource_map si es learning_module
        if data.get('type') == 'learning_module':
            if 'resource_map' not in data:
                report.add_issue(ValidationIssue(
                    filepath=filepath,
                    severity=Severity.WARNING,
                    category="MANIFEST",
                    message="learning_module sin resource_map"
                ))
            else:
                rmap = data['resource_map']
                if 'entry_point' not in rmap:
                    report.add_issue(ValidationIssue(
                        filepath=filepath,
                        severity=Severity.WARNING,
                        category="MANIFEST",
                        message="resource_map sin entry_point"
                    ))
        
        # Verificar ai_contract (estándar actual)
        if 'ai_contract' not in data:
            report.add_issue(ValidationIssue(
                filepath=filepath,
                severity=Severity.INFO,
                category="MANIFEST",
                message="Sin configuración de IA (ai_contract)"
            ))


class NomenclatureValidator:
    """Valida la nomenclatura de archivos según el estándar."""
    
    # Patrón para archivos con prefijo semántico
    PREFIX_PATTERN = re.compile(
        r'^(FUN|AL|CD|CI|CV|ED|MN|REF)-(\d{2})-(.+)\.md$'
    )
    
    @classmethod
    def get_expected_prefix(cls, filepath: str, root: str) -> Optional[str]:
        """Determina el prefijo esperado basado en la ubicación del archivo."""
        rel_path = os.path.relpath(filepath, root)
        parts = rel_path.replace("\\", "/").split("/")
        
        if len(parts) >= 2:
            module = parts[0]
            return PREFIXES.get(module)
        return None
    
    @classmethod
    def validate_filename(cls, filepath: str, root: str, report: ValidationReport):
        """Valida el nombre de un archivo según el estándar."""
        # Verificar excepciones primero
        is_exempt, reason = NomenclatureExceptions.is_exempt(filepath, root)
        if is_exempt:
            return  # Archivo exento, no validar
        
        filename = os.path.basename(filepath)
        rel_path = os.path.relpath(filepath, root)
        
        # Solo validar archivos .md en módulos de contenido
        if not filename.endswith('.md'):
            return
        
        # Verificar si debería tener prefijo
        expected_prefix = cls.get_expected_prefix(filepath, root)
        if not expected_prefix:
            return  # No está en un módulo que requiera prefijo
        
        match = cls.PREFIX_PATTERN.match(filename)
        
        if not match:
            report.add_issue(ValidationIssue(
                filepath=filepath,
                severity=Severity.WARNING,
                category="NOMENCLATURE",
                message=f"Nombre no sigue el patrón [PREFIJO]-[XX]-[Contenido].md",
                suggestion=f"Usar prefijo '{expected_prefix}' para este módulo"
            ))
            return
        
        file_prefix = match.group(1)
        
        # Verificar que el prefijo coincida con el módulo
        if file_prefix != expected_prefix:
            report.add_issue(ValidationIssue(
                filepath=filepath,
                severity=Severity.ERROR,
                category="NOMENCLATURE",
                message=f"Prefijo '{file_prefix}' no coincide con módulo (esperado: '{expected_prefix}')",
                suggestion=f"Renombrar usando prefijo '{expected_prefix}'"
            ))


class TableSyntaxValidator:
    """Valida la sintaxis de tablas Markdown con contenido matemático."""
    
    # Patrón correcto: \vert, \lvert, \rvert o \| (norma)
    CORRECT_PATTERN = re.compile(r'\\[lr]?vert|\\\\?\|')
    
    # Patrón de norma: \|...\| (barra doble escapada para normas)
    NORM_PATTERN = re.compile(r'\\\|[^|]+\\\|')
    
    @classmethod
    def validate_file(cls, filepath: str, report: ValidationReport):
        """Valida las tablas de un archivo .md"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            return  # Error de lectura ya reportado por otro validador
        
        # Buscar líneas que parecen ser tablas con matemáticas
        lines = content.split('\n')
        in_table = False
        
        for i, line in enumerate(lines, 1):
            stripped = line.strip()
            
            # Detectar si estamos en una tabla
            if stripped.startswith('|') and stripped.endswith('|'):
                in_table = True
                
                # Ignorar si usa \| para normas (sintaxis correcta)
                if cls.NORM_PATTERN.search(line):
                    continue
                
                # Ignorar contenido dentro de backticks (código inline)
                line_without_code = re.sub(r'`[^`]+`', '', line)
                
                # Buscar $ | $ dentro de la línea (potencial problema)
                if '$|' in line_without_code or '|$' in line_without_code:
                    # Verificar si usa \vert
                    if not cls.CORRECT_PATTERN.search(line_without_code):
                        # Verificar que realmente sea un valor absoluto problemático
                        if re.search(r'\$[^$]*\|[^$]*\$', line_without_code):
                            report.add_issue(ValidationIssue(
                                filepath=f"{filepath}:{i}",
                                severity=Severity.WARNING,
                                category="TABLE_SYNTAX",
                                message="Posible uso de | como valor absoluto en tabla",
                                suggestion="Usar $\\vert x \\vert$ en lugar de $|x|$"
                            ))
            elif in_table and not stripped.startswith('|'):
                in_table = False


class ReferenceValidator:
    """Valida coherencia de referencias entre archivos."""
    
    @classmethod
    def validate_manifest_references(cls, manifest_path: str, root: str, report: ValidationReport):
        """Verifica que los archivos referenciados en manifest.json existan."""
        try:
            with open(manifest_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception:
            return  # Error ya reportado
        
        manifest_dir = os.path.dirname(manifest_path)
        
        if 'resource_map' not in data:
            return
        
        rmap = data['resource_map']
        
        # Verificar archivos referenciados
        for key, value in rmap.items():
            if isinstance(value, str) and value.endswith('.md'):
                full_path = os.path.join(manifest_dir, value)
                if not os.path.exists(full_path):
                    report.add_issue(ValidationIssue(
                        filepath=manifest_path,
                        severity=Severity.ERROR,
                        category="REFERENCE",
                        message=f"Archivo referenciado no existe: {value}",
                        suggestion=f"Crear el archivo o actualizar resource_map"
                    ))
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, str) and item.endswith('.md'):
                        full_path = os.path.join(manifest_dir, item)
                        if not os.path.exists(full_path):
                            report.add_issue(ValidationIssue(
                                filepath=manifest_path,
                                severity=Severity.WARNING,
                                category="REFERENCE",
                                message=f"Archivo en lista no existe: {item}"
                            ))


# ==============================================================================
# UTILIDADES
# ==============================================================================

class FrontmatterTransformer:
    """Transforma frontmatter legacy a formato de comentario HTML."""
    
    @staticmethod
    def transform_file(filepath: str) -> Tuple[bool, str]:
        """
        Transforma un archivo MD para ocultar frontmatter en comentario HTML.
        
        Returns:
            Tuple[bool, str]: (transformado, mensaje)
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            return False, f"Error leyendo: {e}"
        
        # Caso 1: Comentario HTML seguido de frontmatter separado
        pattern1 = re.compile(r'^(<!--[\s\S]*?-->)\s*\n+(---\n[\s\S]*?\n---)\s*\n+')
        match1 = pattern1.match(content)
        
        if match1:
            comment = match1.group(1)
            frontmatter = match1.group(2)
            rest = content[match1.end():]
            
            comment_body = comment[4:-3].strip()
            new_content = f"<!--\n{comment_body}\n\n{frontmatter}\n-->\n\n{rest}"
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True, "Frontmatter movido dentro de comentario HTML"
        
        # Caso 2: Solo frontmatter sin comentario previo
        pattern2 = re.compile(r'^(---\n[\s\S]*?\n---)\s*\n+')
        match2 = pattern2.match(content)
        
        if match2:
            frontmatter = match2.group(1)
            rest = content[match2.end():]
            new_content = f"<!--\n{frontmatter}\n-->\n\n{rest}"
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True, "Frontmatter envuelto en comentario HTML"
        
        return False, "Sin cambios necesarios"


# ==============================================================================
# MOTOR PRINCIPAL
# ==============================================================================

class RepoValidator:
    """Motor principal de validación del repositorio."""
    
    def __init__(self, root: str = '.'):
        self.root = os.path.abspath(root)
        self.report = ValidationReport(root=self.root)
    
    def discover_files(self) -> Tuple[List[str], List[str]]:
        """Descubre todos los archivos .md y manifest.json"""
        md_files = []
        manifest_files = []
        
        for dirpath, dirs, files in os.walk(self.root):
            # Ignorar directorios ocultos
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            
            for f in files:
                full_path = os.path.join(dirpath, f)
                if f.endswith('.md'):
                    md_files.append(full_path)
                elif f == 'manifest.json':
                    manifest_files.append(full_path)
        
        return md_files, manifest_files
    
    def validate(self, 
                 check_metadata: bool = True,
                 check_manifests: bool = True,
                 check_nomenclature: bool = True,
                 check_tables: bool = True,
                 check_references: bool = True) -> ValidationReport:
        """Ejecuta todas las validaciones seleccionadas."""
        
        md_files, manifest_files = self.discover_files()
        
        self.report.stats['md_files'] = len(md_files)
        self.report.stats['manifest_files'] = len(manifest_files)
        
        # Validar archivos .md
        for filepath in md_files:
            if check_metadata:
                MetadataValidator.validate_file(filepath, self.report)
            if check_nomenclature:
                NomenclatureValidator.validate_filename(filepath, self.root, self.report)
            if check_tables:
                TableSyntaxValidator.validate_file(filepath, self.report)
        
        # Validar manifest.json
        for filepath in manifest_files:
            if check_manifests:
                ManifestValidator.validate_manifest(filepath, self.report)
            if check_references:
                ReferenceValidator.validate_manifest_references(filepath, self.root, self.report)
        
        return self.report
    
    def transform_frontmatter(self, dry_run: bool = True) -> Dict[str, str]:
        """Transforma frontmatter legacy en todos los archivos."""
        results = {}
        md_files, _ = self.discover_files()
        
        for filepath in md_files:
            if dry_run:
                # Solo verificar sin modificar
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    if re.match(r'^---\n', content):
                        results[filepath] = "Necesita transformación"
                except Exception as e:
                    results[filepath] = f"Error: {e}"
            else:
                success, msg = FrontmatterTransformer.transform_file(filepath)
                if success:
                    results[filepath] = msg
        
        return results


# ==============================================================================
# INTERFAZ DE LÍNEA DE COMANDOS
# ==============================================================================

def print_report(report: ValidationReport, verbose: bool = False):
    """Imprime el reporte de validación de forma formateada."""
    
    print("=" * 70)
    print("REPORTE DE VALIDACIÓN DEL REPOSITORIO")
    print("=" * 70)
    print(f"📁 Ruta: {report.root}")
    print(f"🕐 Timestamp: {report.timestamp}")
    print(f"📄 Archivos MD: {report.stats.get('md_files', 0)}")
    print(f"📋 Manifests: {report.stats.get('manifest_files', 0)}")
    print("-" * 70)
    
    # Resumen
    print(f"\n{Severity.ERROR.value} Errores: {len(report.errors)}")
    print(f"{Severity.WARNING.value} Advertencias: {len(report.warnings)}")
    print(f"{Severity.INFO.value} Información: {len(report.infos)}")
    
    # Detalles de errores (siempre mostrar)
    if report.errors:
        print("\n" + "=" * 70)
        print("ERRORES (requieren corrección)")
        print("=" * 70)
        for issue in report.errors:
            print(f"\n{issue}")
    
    # Detalles de advertencias (mostrar las primeras o todas si verbose)
    if report.warnings:
        print("\n" + "-" * 70)
        print("ADVERTENCIAS")
        print("-" * 70)
        warnings_to_show = report.warnings if verbose else report.warnings[:10]
        for issue in warnings_to_show:
            print(f"\n{issue}")
        if not verbose and len(report.warnings) > 10:
            print(f"\n... y {len(report.warnings) - 10} advertencias más (usar --verbose)")
    
    # Información (solo si verbose)
    if verbose and report.infos:
        print("\n" + "-" * 70)
        print("INFORMACIÓN")
        print("-" * 70)
        for issue in report.infos:
            print(f"\n{issue}")
    
    # Resultado final
    print("\n" + "=" * 70)
    if report.errors:
        print("❌ VALIDACIÓN FALLIDA - Hay errores que deben corregirse")
    elif report.warnings:
        print("⚠️ VALIDACIÓN CON ADVERTENCIAS - Revisar los problemas reportados")
    else:
        print("✅ VALIDACIÓN EXITOSA - Todo en orden")
    print("=" * 70)


def main():
    """Punto de entrada principal."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Validador del repositorio de matemáticas',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  python validate_repo.py                    # Validar directorio actual
  python validate_repo.py /ruta/repo         # Validar ruta específica
  python validate_repo.py --verbose          # Mostrar todos los detalles
  python validate_repo.py --transform        # Transformar frontmatter
  python validate_repo.py --no-tables        # Omitir validación de tablas
        """
    )
    
    parser.add_argument('root', nargs='?', default='.',
                        help='Directorio raíz del repositorio (default: actual)')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Mostrar todos los detalles')
    parser.add_argument('--transform', action='store_true',
                        help='Transformar frontmatter legacy a formato HTML')
    parser.add_argument('--dry-run', action='store_true',
                        help='Solo mostrar qué se transformaría (con --transform)')
    parser.add_argument('--no-metadata', action='store_true',
                        help='Omitir validación de metadatos')
    parser.add_argument('--no-manifests', action='store_true',
                        help='Omitir validación de manifests')
    parser.add_argument('--no-nomenclature', action='store_true',
                        help='Omitir validación de nomenclatura')
    parser.add_argument('--no-tables', action='store_true',
                        help='Omitir validación de sintaxis de tablas')
    parser.add_argument('--no-references', action='store_true',
                        help='Omitir validación de referencias')
    parser.add_argument('--json', action='store_true',
                        help='Salida en formato JSON')
    
    args = parser.parse_args()
    
    validator = RepoValidator(args.root)
    
    # Modo transformación
    if args.transform:
        print("Transformando frontmatter...")
        results = validator.transform_frontmatter(dry_run=args.dry_run)
        for path, msg in results.items():
            print(f"{'🔍' if args.dry_run else '✓'} {path}: {msg}")
        print(f"\nArchivos {'que necesitan' if args.dry_run else ''} transformación: {len(results)}")
        return
    
    # Modo validación
    report = validator.validate(
        check_metadata=not args.no_metadata,
        check_manifests=not args.no_manifests,
        check_nomenclature=not args.no_nomenclature,
        check_tables=not args.no_tables,
        check_references=not args.no_references
    )
    
    if args.json:
        # Salida JSON
        output = {
            'root': report.root,
            'timestamp': report.timestamp,
            'stats': report.stats,
            'summary': {
                'errors': len(report.errors),
                'warnings': len(report.warnings),
                'info': len(report.infos)
            },
            'issues': [
                {
                    'filepath': i.filepath,
                    'severity': i.severity.name,
                    'category': i.category,
                    'message': i.message,
                    'suggestion': i.suggestion
                }
                for i in report.issues
            ]
        }
        print(json.dumps(output, indent=2, ensure_ascii=False))
    else:
        print_report(report, verbose=args.verbose)
    
    # Código de salida
    sys.exit(1 if report.errors else 0)


if __name__ == '__main__':
    main()

