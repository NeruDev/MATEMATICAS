<!--
::METADATA::
type: reference
topic_id: meta-tests
file_id: repo-tests
status: stable
audience: maintainer
last_updated: 2025-12-30
-->

# Tests de Verificación del Repositorio

## Validación Automatizada

El repositorio cuenta con un script de validación consolidado:

```powershell
# Desde la raíz del repositorio
python 00-META/tools/validate_repo.py

# Modo verbose (todos los detalles)
python 00-META/tools/validate_repo.py --verbose

# Salida en JSON (para automatización)
python 00-META/tools/validate_repo.py --json
```

### Validaciones incluidas

| Validador | Qué verifica |
|-----------|--------------|
| **MetadataValidator** | Bloques `::METADATA::` en archivos .md |
| **ManifestValidator** | Campos obligatorios en `manifest.json` |
| **NomenclatureValidator** | Nombres de archivo según estándar `[PREFIJO]-[XX]-[Contenido].md` |
| **TableSyntaxValidator** | Uso correcto de `\vert` en tablas con matemáticas |
| **ReferenceValidator** | Archivos referenciados en manifests existan |

### Opciones de validación selectiva

```powershell
python 00-META/tools/validate_repo.py --no-metadata      # Omitir metadatos
python 00-META/tools/validate_repo.py --no-manifests     # Omitir manifests
python 00-META/tools/validate_repo.py --no-nomenclature  # Omitir nomenclatura
python 00-META/tools/validate_repo.py --no-tables        # Omitir sintaxis tablas
python 00-META/tools/validate_repo.py --no-references    # Omitir referencias
```

### Transformación de frontmatter legacy

```powershell
# Ver qué archivos necesitan transformación
python 00-META/tools/validate_repo.py --transform --dry-run

# Aplicar transformación
python 00-META/tools/validate_repo.py --transform
```

---

## Tests Manuales (Checklist)

### Test 1: Integridad Estructural

**Pregunta:** ¿Cada subtema tiene los componentes requeridos?

| Componente | Obligatorio | Archivo |
|------------|:-----------:|---------|
| Metadatos | ✅ | `manifest.json` |
| Entrada | ✅ | `PREFIJO-XX-*-Intro.md` |
| Fórmulas | ✅ | `PREFIJO-XX-Resumen-Formulas.md` |
| Teoría | ✅ | `theory/PREFIJO-XX-Teoria-*.md` |
| Métodos | ✅ | `methods/PREFIJO-XX-Metodos-*.md` |
| Problemas | ✅ | `problems/PREFIJO-XX-Problemas.md` |
| Respuestas | ✅ | `solutions/PREFIJO-XX-Respuestas.md` |
| Soluciones | ⚪ | `solutions/prob-XX/solucion-metodo.md` |
| Aplicaciones | ⚪ | `applications/` |
| Media | ⚪ | `media/` |

✅ = Obligatorio | ⚪ = Opcional

---

### Test 2: Separación Semántica

| Verificación | Correcto |
|--------------|:--------:|
| ¿Hay soluciones dentro de `problems/`? | ❌ No debe |
| ¿Hay procedimientos dentro de `theory/`? | ❌ No debe |
| ¿Hay teoría dentro de `methods/`? | ❌ No debe |
| ¿Hay archivos README.md en subtemas? | ❌ No debe |

---

### Test 3: Metadatos

Todo archivo `.md` debe tener al inicio:

```markdown
<!--
::METADATA::
type: [theory | method | problem | solution | reference | index | cheatsheet]
status: [draft | review | stable | active]
-->
```

Para archivos completos, incluir también:
- `topic_id`: ID del tema en manifest
- `file_id`: Nombre del archivo sin extensión
- `audience`: student | ai_context | exam_review
- `last_updated`: YYYY-MM-DD

---

### Test 4: manifest.json

Campos obligatorios:

```json
{
  "id": "modulo-subtema",
  "topic": "Nombre del Tema",
  "type": "learning_module",
  "status": "active",
  "tags": ["etiqueta1", "etiqueta2"],
  "resource_map": {
    "entry_point": "PREFIJO-XX-*-Intro.md"
  },
  "ai_contract": {
    "allowed_tasks": ["explain_concept", "generate_problems", "verify_solution"]
  }
}
```

---

## Resultados Esperados

```
======================================================================
REPORTE DE VALIDACIÓN DEL REPOSITORIO
======================================================================
❌ Errores: 0
⚠️ Advertencias: 0
ℹ️ Información: 0
======================================================================
✅ VALIDACIÓN EXITOSA - Todo en orden
======================================================================
```
  fi
done

# Test 2 — ¿Todos los .md empiezan con frontmatter?
total_md=$(find . -name "*.md" -not -path "./.git/*" | wc -l)
md_with_fm=$(grep -rl --include="*.md" "^---" . | wc -l)
echo "Total MD: $total_md, Con frontmatter: $md_with_fm"

# Test 3 — ¿Existen diagnósticos?
for d in */*/; do
  if [ -d "$d" ] && [ -f "$d/manifest.json" ]; then
    if [ -d "${d}diagnostic" ]; then
      echo "OK: ${d}diagnostic/"
    else
      echo "MISSING: ${d}diagnostic/"
    fi
  fi
done
```

### Automatizado - Python (Validación completa)

```bash
# Ejecutar el validador Python
python3 00-META/tools/validate_repo.py

# Salida 0 = OK, Salida 1 = Errores encontrados
```

El script `validate_repo.py` verifica:
- Que todos los archivos `.md` tengan frontmatter YAML
- Que todos los `manifest.json` contengan `tags` y `ai_contract`

---

## Qué hacer si un test falla

1. **Identificar** el archivo o directorio con el problema
2. **Corregir** siguiendo las plantillas en `00-META/`
3. **Verificar** ejecutando los tests nuevamente
4. **Documentar** el cambio realizado

---

<!--
IA: Si generas contenido que no pasa estos tests,
el contenido debe ser rechazado y corregido.
-->
