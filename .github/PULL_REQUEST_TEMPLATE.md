<!--
::METADATA::
type: reference
file_id: pull-request-template
status: stable
last_updated: 2025-12-30
-->

## Checklist PR — Añadiendo o modificando contenido

### Estructura
- [ ] ¿El nuevo tema sigue la estructura `theory/methods/problems/solutions/manifest.json`?
- [ ] ¿El archivo de entrada es `PREFIJO-XX-*-Intro.md` (no README.md)?
- [ ] ¿Existe `PREFIJO-XX-Resumen-Formulas.md` con las fórmulas clave?

### Metadatos
- [ ] ¿Todos los .md tienen bloque `::METADATA::` con `type` y `status`?
- [ ] ¿`manifest.json` contiene `resource_map` y `ai_contract`?

### Nomenclatura
- [ ] ¿Los archivos siguen el patrón `[PREFIJO]-[XX]-[Contenido].md`?
- [ ] ¿El prefijo corresponde al módulo? (FUN, AL, CD, CI, CV, ED, MN)

### Validación
- [ ] ¿Se ejecutó `python 00-META/tools/validate_repo.py` sin errores?

### Opcional
- [ ] ¿`media/` incluye recursos visuales (PNG/SVG < 800px)?
- [ ] ¿`diagnostic/` contiene pre-test de prerequisitos?
