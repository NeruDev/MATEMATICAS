<!--
::METADATA::
type: reference
topic_id: meta-audit-meta-files
file_id: audit-meta-files
status: stable
audience: ai_context
last_updated: 2026-01-05
-->

# 📋 Auditoría de Archivos en `00-META`

> **Propósito:** Documento de referencia que describe cada archivo en `00-META`, su función, relaciones con otros documentos y estado actual. Diseñado para que cualquier IA pueda orientarse rápidamente.

---

## 1. Inventario Completo

### 1.1 Archivos Normativos (Alta Prioridad para IA)

| Archivo | Propósito | Estado | Dependencias |
|---------|-----------|:------:|--------------|
| **[ia-contract.md](ia-contract.md)** | LEY SUPREMA — Todas las reglas globales para IA | ✅ Estable | Ninguna (es la raíz normativa) |
| **[ai-directives.md](ai-directives.md)** | Reglas técnicas (LaTeX en tablas, formato de soluciones, enlaces) | ✅ Estable | Extiende `ia-contract.md` |
| **[nomenclatura-estandar.md](nomenclatura-estandar.md)** | Convenciones detalladas de nombrado de archivos | ✅ Estable | Complementa `ia-contract.md` §2 |

### 1.2 Archivos de Estructura y Navegación

| Archivo | Propósito | Estado | Dependencias |
|---------|-----------|:------:|--------------|
| **[directory-tree.md](directory-tree.md)** | Árbol de directorios actualizado del repositorio | ✅ Estable | Debe actualizarse con cambios estructurales |
| **[audit-file-list.md](audit-file-list.md)** | Lista de archivos obligatorios por módulo | ✅ Estable | Deriva de `ia-contract.md` §1 |
| **[audit-table-issues.md](audit-table-issues.md)** | Registro histórico de problemas en tablas Markdown | ⚠️ Histórico | Solo referencia |

### 1.3 Archivos de Referencia

| Archivo | Propósito | Estado | Dependencias |
|---------|-----------|:------:|--------------|
| **[bibliografia-general.md](bibliografia-general.md)** | Biblioteca central de referencias académicas | ✅ Estable | Usado por todos los módulos |
| **[notation-cheatsheet.md](notation-cheatsheet.md)** | Símbolos LaTeX y convenciones de notación | ✅ Estable | Referenciado en `ai-directives.md` |
| **[plantilla-respuestas.md](plantilla-respuestas.md)** | Template para archivos de soluciones | ✅ Estable | Usado al crear nuevos `*-Respuestas.md` |

### 1.4 Archivos para Estudiantes

| Archivo | Propósito | Estado | Dependencias |
|---------|-----------|:------:|--------------|
| **[study-guide.md](study-guide.md)** | Guía de estudio y navegación para humanos | ✅ Estable | Simplifica `ia-contract.md` para estudiantes |
| **[prompts-for-students.md](prompts-for-students.md)** | Prompts prediseñados para usar con IA | ✅ Estable | Independiente |

### 1.5 Archivos de Validación

| Archivo | Propósito | Estado | Dependencias |
|---------|-----------|:------:|--------------|
| **[repo-tests.md](repo-tests.md)** | Pruebas lógicas de integridad del repositorio | ✅ Estable | Usado por `tools/validate_repo.py` |

### 1.6 Herramientas (`tools/`)

| Archivo/Carpeta | Propósito | Lenguaje |
|-----------------|-----------|----------|
| `validate_repo.py` | Auditor consolidado de estructura | Python |
| `link_knowledge_base.py` | Auto-vinculador de términos al glosario | Python |
| `check_tables.py` | Validador de tablas Markdown | Python |
| `graphics/` | Subsistema de generación de gráficos SVG/PNG | Python + Matplotlib |

---

## 2. Jerarquía de Documentos

```
.ai-bootstrap.md (RAÍZ - PUNTO DE ENTRADA)
       │
       ├── ia-contract.md ─────────────────┬── ai-directives.md
       │       │                           │
       │       └── nomenclatura-estandar.md│
       │                                   │
       ├── directory-tree.md               │
       │                                   │
       └── audit-file-list.md              │
                                           │
                                           ▼
                              manifest.json (por subtema)
                              _directives.md (por subtema)
```

### Flujo de Lectura Recomendado para IA

1. **`.ai-bootstrap.md`** → Orientación inicial, jerarquía y perfiles
2. **`ia-contract.md`** → Reglas globales completas
3. **`manifest.json` del tema** → Reglas específicas del contexto
4. **Archivos de referencia** según necesidad

---

## 3. Matriz de Responsabilidades

| Tarea | Documento Principal | Documentos de Apoyo |
|-------|---------------------|---------------------|
| Crear un archivo nuevo | `ia-contract.md` | `nomenclatura-estandar.md`, `plantilla-respuestas.md` |
| Verificar nomenclatura | `nomenclatura-estandar.md` | `audit-file-list.md` |
| Resolver problemas de formato | `ai-directives.md` | `notation-cheatsheet.md` |
| Añadir bibliografía | `bibliografia-general.md` | — |
| Generar gráficos | `tools/graphics/` | `ai-directives.md` §8 |
| Validar integridad | `repo-tests.md` | `tools/validate_repo.py` |
| Orientar a estudiantes | `study-guide.md` | `prompts-for-students.md` |

---

## 4. Estado de Cada Archivo

### 4.1 Archivos Completos y Estables

✅ **Listos para uso:**
- `ia-contract.md` — Actualizado 2026-01-05 con jerarquía normativa
- `ai-directives.md` — Actualizado 2026-01-02
- `nomenclatura-estandar.md` — Actualizado 2026-01-02
- `directory-tree.md` — Actualizado 2026-01-05
- `audit-file-list.md` — Actualizado 2025-12-30
- `bibliografia-general.md` — Actualizado 2026-01-03
- `notation-cheatsheet.md` — Estable
- `study-guide.md` — Estable
- `plantilla-respuestas.md` — Estable
- `prompts-for-students.md` — Estable
- `repo-tests.md` — Estable

### 4.2 Archivos de Historial (Solo Referencia)

⚠️ **No modificar activamente:**
- `audit-table-issues.md` — Registro histórico de correcciones

---

## 5. Relaciones Cruzadas

### 5.1 Documentos que SE COMPLEMENTAN

| Documento A | Documento B | Relación |
|-------------|-------------|----------|
| `ia-contract.md` | `ai-directives.md` | B extiende reglas técnicas de A |
| `ia-contract.md` | `nomenclatura-estandar.md` | B detalla la sección §2 de A |
| `ia-contract.md` | `audit-file-list.md` | B enumera los archivos de la estructura §1 de A |
| `study-guide.md` | `ia-contract.md` | A es versión simplificada de B para humanos |
| `plantilla-respuestas.md` | `ia-contract.md` §4 | A implementa el formato de B |

### 5.2 Documentos INDEPENDIENTES

- `prompts-for-students.md` — No tiene dependencias
- `bibliografia-general.md` — Fuente de verdad independiente
- `notation-cheatsheet.md` — Referencia rápida autónoma

---

## 6. Preguntas Frecuentes para IA

### ¿Dónde busco las reglas para crear un archivo?

1. `ia-contract.md` → Reglas globales
2. `manifest.json` del tema destino → Reglas específicas
3. `nomenclatura-estandar.md` → Detalles de nombrado

### ¿Cómo sé qué archivos deben existir en un subtema?

Consultar `audit-file-list.md` §1.

### ¿Dónde encuentro las convenciones de LaTeX?

`ai-directives.md` §1-4 y `notation-cheatsheet.md`.

### ¿Cómo verifico que un enlace está bien formado?

`ai-directives.md` §6 y `ia-contract.md` §5.

### ¿Dónde están las referencias bibliográficas?

`bibliografia-general.md` — Única fuente de verdad.

---

## 7. Actualizaciones Requeridas

### Al añadir un nuevo módulo o subtema:

- [ ] Actualizar `directory-tree.md`
- [ ] Actualizar `audit-file-list.md`
- [ ] Verificar bibliografía en `bibliografia-general.md`

### Al cambiar reglas globales:

- [ ] Modificar `ia-contract.md`
- [ ] Verificar coherencia con `ai-directives.md`
- [ ] Actualizar `.ai-bootstrap.md` si afecta jerarquía

### Al añadir herramientas:

- [ ] Documentar en `directory-tree.md`
- [ ] Añadir instrucciones en archivo relevante (`ai-directives.md` si es para IA)

---

*Última actualización: 2026-01-05*
