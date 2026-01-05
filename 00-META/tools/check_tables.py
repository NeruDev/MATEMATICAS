#!/usr/bin/env python3
"""
Script para detectar tablas Markdown con columnas desalineadas.
Busca tablas donde el número de columnas no coincide entre:
- Fila de encabezados
- Fila de separadores (|---|---|)
- Filas de datos
"""

import os
import re
import sys
from pathlib import Path

# Force UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

def count_columns(line):
    """Cuenta el número de columnas en una línea de tabla Markdown."""
    # Eliminar espacios al inicio y final
    line = line.strip()
    
    # Si la línea empieza y termina con |, eliminarlos para contar correctamente
    if line.startswith('|'):
        line = line[1:]
    if line.endswith('|'):
        line = line[:-1]
    
    # Contar separadores | (cada uno separa una columna)
    # Pero hay que tener cuidado con | escapados o dentro de código
    columns = line.split('|')
    return len(columns)

def is_separator_row(line):
    """Verifica si una línea es una fila de separadores (|---|---|)."""
    # Patrón: debe contener principalmente guiones, dos puntos y pipes
    cleaned = line.strip()
    if not cleaned.startswith('|'):
        return False
    # Verificar que contenga el patrón de separador
    return bool(re.match(r'^\|[\s\-:]+(\|[\s\-:]+)*\|?$', cleaned))

def find_tables_with_issues(file_path):
    """Encuentra tablas con problemas de columnas en un archivo."""
    issues = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        return []
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Detectar inicio de tabla (línea que empieza con |)
        if line.startswith('|') and not is_separator_row(line):
            table_start = i
            header_line = line
            header_cols = count_columns(header_line)
            
            # Verificar si la siguiente línea es un separador
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                if is_separator_row(next_line):
                    separator_line = next_line
                    separator_cols = count_columns(separator_line)
                    
                    # Recopilar filas de datos
                    data_rows = []
                    j = i + 2
                    while j < len(lines):
                        data_line = lines[j].strip()
                        if data_line.startswith('|') and not is_separator_row(data_line):
                            data_rows.append((j + 1, data_line, count_columns(data_line)))
                            j += 1
                        elif data_line == '' or not data_line.startswith('|'):
                            break
                        else:
                            j += 1
                    
                    # Verificar inconsistencias
                    has_issue = False
                    issue_details = []
                    
                    # Comparar encabezado vs separador
                    if header_cols != separator_cols:
                        has_issue = True
                        issue_details.append(f"  - Encabezado tiene {header_cols} columnas, separador tiene {separator_cols}")
                    
                    # Comparar filas de datos vs encabezado
                    for line_num, data_line, data_cols in data_rows:
                        if data_cols != header_cols:
                            has_issue = True
                            issue_details.append(f"  - Fila {line_num}: {data_cols} columnas (encabezado: {header_cols})")
                    
                    if has_issue:
                        issue = {
                            'file': str(file_path),
                            'line': table_start + 1,
                            'header': header_line,
                            'header_cols': header_cols,
                            'separator': separator_line,
                            'separator_cols': separator_cols,
                            'data_rows': data_rows[:5],  # Primeras 5 filas de datos
                            'details': issue_details
                        }
                        issues.append(issue)
                    
                    i = j
                    continue
        i += 1
    
    return issues

def main():
    base_path = Path(r"G:\REPOSITORIOS GITHUB\MATEMATICAS GITHUB")
    folders = [
        "01-Fundamentos",
        "02-Algebra-Lineal", 
        "03-Calculo-Diferencial",
        "04-Calculo-Integral",
        "05-Calculo-Vectorial",
        "06-Ecuaciones-Diferenciales",
        "07-Metodos-Numericos"
    ]
    
    all_issues = []
    files_checked = 0
    
    for folder in folders:
        folder_path = base_path / folder
        if folder_path.exists():
            for md_file in folder_path.rglob("*.md"):
                files_checked += 1
                issues = find_tables_with_issues(md_file)
                all_issues.extend(issues)
    
    print("=" * 80)
    print("REPORTE DE TABLAS MARKDOWN CON COLUMNAS DESALINEADAS")
    print("=" * 80)
    print(f"\nArchivos analizados: {files_checked}")
    print(f"Tablas con problemas encontradas: {len(all_issues)}")
    print("\n" + "=" * 80)
    
    if all_issues:
        for idx, issue in enumerate(all_issues, 1):
            rel_path = issue['file'].replace(str(base_path) + "\\", "")
            print(f"\n{'-' * 80}")
            print(f"PROBLEMA #{idx}")
            print(f"{'-' * 80}")
            print(f"Archivo: {rel_path}")
            print(f"Linea: {issue['line']}")
            print(f"\nANALISIS DE COLUMNAS:")
            print(f"   * Encabezado: {issue['header_cols']} columnas")
            print(f"   * Separador: {issue['separator_cols']} columnas")
            
            print(f"\nCONTENIDO DE LA TABLA:")
            print(f"   Encabezado (L{issue['line']}): {issue['header'][:100]}{'...' if len(issue['header']) > 100 else ''}")
            print(f"   Separador  (L{issue['line']+1}): {issue['separator'][:100]}{'...' if len(issue['separator']) > 100 else ''}")
            
            if issue['data_rows']:
                print(f"\n   Primeras filas de datos:")
                for line_num, data_line, cols in issue['data_rows'][:3]:
                    print(f"   Fila L{line_num} ({cols} cols): {data_line[:80]}{'...' if len(data_line) > 80 else ''}")
            
            print(f"\nDETALLES DEL ERROR:")
            for detail in issue['details']:
                print(f"   {detail}")
    else:
        print("\nNo se encontraron tablas con problemas de columnas.")
    
    print(f"\n{'=' * 80}")
    print("FIN DEL REPORTE")
    print("=" * 80)

if __name__ == "__main__":
    main()
