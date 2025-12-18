#!/usr/bin/env python3
"""
Transforma archivos MD para ocultar el frontmatter YAML dentro de comentarios HTML.
Patrón actual:
    <!--
    HUMANO: ...
    IA: ...
    -->

    ---
    content_type: ...
    ---

    # Título

Se convierte en:
    <!--
    HUMANO: ...
    IA: ...

    ---
    content_type: ...
    ---
    -->

    # Título
"""
import os
import re
import sys


def transform_file(path):
    """Transforma un archivo MD para ocultar frontmatter en comentario."""
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Patrón: comentario HTML seguido de frontmatter YAML separado
    # Captura: comentario completo, frontmatter, resto del contenido
    pattern = r'^(<!--[\s\S]*?-->)\s*\n+(---\n[\s\S]*?\n---)\s*\n+'
    
    match = re.match(pattern, content)
    if match:
        comment = match.group(1)
        frontmatter = match.group(2)
        rest = content[match.end():]
        
        # Quitar el cierre del comentario y agregar frontmatter dentro
        comment_body = comment[4:-3].rstrip()  # Quita <!-- y -->
        new_content = f"<!--\n{comment_body.strip()}\n\n{frontmatter}\n-->\n\n{rest}"
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    
    # Caso alternativo: solo frontmatter sin comentario previo
    pattern_only_fm = r'^(---\n[\s\S]*?\n---)\s*\n+'
    match_fm = re.match(pattern_only_fm, content)
    if match_fm:
        frontmatter = match_fm.group(1)
        rest = content[match_fm.end():]
        new_content = f"<!--\n{frontmatter}\n-->\n\n{rest}"
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    
    return False


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else '.'
    transformed = 0
    skipped = 0
    
    for dp, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for f in files:
            if f.endswith('.md'):
                path = os.path.join(dp, f)
                if transform_file(path):
                    print(f"✓ {path}")
                    transformed += 1
                else:
                    print(f"⊘ {path} (sin cambios)")
                    skipped += 1
    
    print(f"\nTransformados: {transformed}, Sin cambios: {skipped}")


if __name__ == '__main__':
    main()
