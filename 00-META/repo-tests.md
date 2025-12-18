<!--
HUMANO:
Tests de verificación para asegurar que el repositorio
mantiene su integridad estructural.

IA:
Usa estos tests para validar contenido antes de agregarlo.

---
content_type: meta
expected_output:
  default: markdown
audience: maintainer
---
-->

# Tests de Verificación del Repositorio

## Test 1: Integridad Estructural

**Pregunta:** ¿Cada tema tiene todos los componentes requeridos?

### Checklist por tema:
- [ ] `README.md` - Visión general del tema
- [ ] `theory/` - Directorio de teoría
- [ ] `methods/` - Directorio de métodos
- [ ] `problems/` - Directorio de problemas
- [ ] `solutions/` - Directorio de soluciones
- [ ] `media/` - Directorio de recursos multimedia
- [ ] `manifest.json` - Metadatos del tema

**Resultado esperado:** Todos los elementos presentes.

---

## Test 2: Separación Semántica

**Pregunta:** ¿El contenido está en el lugar correcto?

### Verificaciones:

| Verificación | Correcto | Error |
|--------------|----------|-------|
| ¿Hay soluciones dentro de `problems/`? | No | Sí |
| ¿Hay procedimientos dentro de `theory/`? | No | Sí |
| ¿Hay teoría dentro de `methods/`? | No | Sí |
| ¿Hay enunciados dentro de `solutions/`? | No | Sí |

**Resultado esperado:** Todas las verificaciones en "Correcto".

---

## Test 3: Contrato IA

**Pregunta:** ¿Los archivos cumplen con el contrato de IA?

### Checklist:
- [ ] Cada archivo tiene `content_type` en frontmatter
- [ ] Las soluciones respetan `assigned_method`
- [ ] Los comentarios para IA están presentes
- [ ] El Markdown es válido y limpio

**Resultado esperado:** Todos los elementos marcados.

---

## Test 4: Legibilidad

**Pregunta:** ¿El contenido es comprensible?

### Para humanos:
- [ ] ¿Un estudiante puede entender el tema leyendo solo README + theory?
- [ ] ¿Los métodos son claros y paso a paso?
- [ ] ¿Los problemas tienen enunciados completos?

### Para IA:
- [ ] ¿La IA puede generar un problema nuevo sin salir del tema?
- [ ] ¿La IA puede identificar el método correcto para un problema?
- [ ] ¿Los metadatos son suficientes para clasificar el contenido?

**Resultado esperado:** Todas las preguntas con respuesta "Sí".

---

## Cómo ejecutar los tests

### Manual:
1. Navegar al tema a verificar
2. Revisar cada checklist
3. Documentar cualquier fallo

### Automatizado - Shell (Test rápido)

```bash
# Test 1 — ¿Todos los temas tienen manifest.json?
for d in */; do
  if [ -f "$d/manifest.json" ]; then
    echo "OK: $d/manifest.json"
  else
    echo "MISSING: $d/manifest.json"
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
