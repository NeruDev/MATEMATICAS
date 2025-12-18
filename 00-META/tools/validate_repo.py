#!/usr/bin/env python3
"""
Validador de estructura del repositorio de matemáticas.
Verifica que los archivos MD tengan frontmatter y que los manifest.json estén correctos.
"""
import os
import json
import sys


def has_frontmatter(path):
    """Verifica si un archivo MD tiene frontmatter YAML."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Remover comentarios HTML al inicio
            lines = content.split('\n')
            in_comment = False
            for i, line in enumerate(lines):
                stripped = line.strip()
                # Manejar comentarios HTML
                if '<!--' in stripped and '-->' in stripped:
                    continue  # Comentario de una línea
                if '<!--' in stripped:
                    in_comment = True
                    continue
                if '-->' in stripped:
                    in_comment = False
                    continue
                if in_comment:
                    continue
                # Si encontramos contenido no vacío que no es comentario
                if stripped:
                    # Debe ser el inicio del frontmatter
                    return stripped == '---'
            return False
    except Exception as e:
        print(f"Error leyendo {path}: {e}")
        return False


def validate_manifests(root='.'):
    """Valida que los manifest.json tengan los campos requeridos."""
    problems = []
    for dirpath, dirs, files in os.walk(root):
        # Ignorar directorios ocultos
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        if 'manifest.json' in files:
            p = os.path.join(dirpath, 'manifest.json')
            try:
                with open(p, 'r', encoding='utf-8') as fh:
                    data = json.load(fh)
                if 'tags' not in data:
                    problems.append((p, "missing tags"))
                if 'ai_contract' not in data:
                    problems.append((p, "missing ai_contract"))
            except json.JSONDecodeError as e:
                problems.append((p, f"JSON inválido: {e}"))
            except Exception as e:
                problems.append((p, str(e)))
    return problems


def main():
    root = '.'
    if len(sys.argv) > 1:
        root = sys.argv[1]
    
    print(f"Validando repositorio en: {os.path.abspath(root)}")
    print("-" * 50)
    
    # Encontrar todos los archivos MD
    md_files = []
    for dp, dirs, fs in os.walk(root):
        # Ignorar directorios ocultos
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for f in fs:
            if f.endswith('.md'):
                md_files.append(os.path.join(dp, f))
    
    # Verificar frontmatter
    fm_issues = [f for f in md_files if not has_frontmatter(f)]
    
    # Verificar manifests
    m_problems = validate_manifests(root)
    
    # Reportar resultados
    print(f"\nArchivos MD encontrados: {len(md_files)}")
    print(f"MD sin frontmatter: {len(fm_issues)}")
    for p in fm_issues[:10]:
        print(f"  - {p}")
    if len(fm_issues) > 10:
        print(f"  ... y {len(fm_issues) - 10} más")
    
    print(f"\nProblemas en manifest.json: {len(m_problems)}")
    for p, err in m_problems:
        print(f"  - {p}: {err}")
    
    print("-" * 50)
    if fm_issues or m_problems:
        print("❌ Validación FALLIDA")
        sys.exit(2)
    else:
        print("✅ Todas las validaciones pasaron")
        sys.exit(0)


if __name__ == '__main__':
    main()
