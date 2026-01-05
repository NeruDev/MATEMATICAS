<!--
::METADATA::
type: reference
topic_id: meta-audit
file_id: audit-table-issues
status: active
audience: ai_context
last_updated: 2026-01-05
-->

# Auditoría: Problemas de Tablas Markdown

> **Propósito:** Documentar errores de formato en tablas para corrección sistemática.
> **Estado:** ✅ **COMPLETADO** (2026-01-05)

---

## Resumen del Problema

Se detectaron **~95 tablas** con problemas de formato en el repositorio, principalmente:

1. **Encabezados incompletos:** El número de columnas en encabezados no coincide con los datos
2. **Enlaces rotos:** Patrón `](../../..](` corrupto que rompe la estructura
3. **Valor absoluto sin escapar:** `|` en expresiones LaTeX interfiere con Markdown

---

## Estado de Corrección: ✅ COMPLETADO

### A. Patrón de enlace corrupto `](../../..](` — **TODOS CORREGIDOS**

| Archivo | Estado |
|---------|--------|
| `01-Fundamentos/02-Aritmetica/methods/FUN-02-Metodos-Aritmetica.md` | ✅ |
| `01-Fundamentos/05-Trigonometria/theory/FUN-05-Teoria-Trigonometria.md` | ✅ |
| `01-Fundamentos/05-Trigonometria/methods/FUN-05-Metodos-Trigonometria.md` | ✅ |
| `01-Fundamentos/06-Geometria-Analitica/methods/FUN-06-Metodos-Geometria-Analitica.md` | ✅ |
| `02-Algebra-Lineal/01-Matrices/methods/AL-01-Metodos-Matrices.md` | ✅ |
| `02-Algebra-Lineal/02-Determinantes/methods/AL-02-Metodos-Determinantes.md` | ✅ |
| `02-Algebra-Lineal/03-Sistemas-Lineales/methods/AL-03-Metodos-Sistemas-Lineales.md` | ✅ |
| `02-Algebra-Lineal/04-Espacios-Vectoriales/methods/AL-04-Metodos-Espacios-Vectoriales.md` | ✅ |
| `02-Algebra-Lineal/05-Transformaciones-Lineales/methods/AL-05-Metodos-Transformaciones-Lineales.md` | ✅ |
| `02-Algebra-Lineal/06-Valores-Vectores-Propios/methods/AL-06-Metodos-Valores-Vectores-Propios.md` | ✅ |
| `03-Calculo-Diferencial/02-Derivadas/theory/CD-02-Teoria-Derivadas.md` | ✅ |
| `03-Calculo-Diferencial/02-Derivadas/methods/CD-02-Metodos-Derivadas.md` | ✅ |
| `03-Calculo-Diferencial/03-Aplicaciones-de-la-derivada/methods/CD-03-Metodos-Aplicaciones-Derivada.md` | ✅ |
| `04-Calculo-Integral/01-Integral-Indefinida/methods/CI-01-Metodos-Integracion.md` | ✅ |
| `04-Calculo-Integral/02-Tecnicas-Integracion/theory/CI-02-Teoria-Tecnicas-Integracion.md` | ✅ |
| `04-Calculo-Integral/02-Tecnicas-Integracion/methods/CI-02-Metodos-Tecnicas-Integracion.md` | ✅ |
| `04-Calculo-Integral/03-Integral-Definida/methods/CI-03-Metodos-Integral-Definida.md` | ✅ |
| `04-Calculo-Integral/04-Aplicaciones-Integral/methods/CI-04-Metodos-Aplicaciones-Integral.md` | ✅ |
| `04-Calculo-Integral/05-Integrales-Impropias/methods/CI-05-Metodos-Integrales-Impropias.md` | ✅ |
| `05-Calculo-Vectorial/03-Funciones-vectoriales/methods/CV-03-Metodos-Funciones-Vectoriales.md` | ✅ |
| `05-Calculo-Vectorial/04-Funciones-de-varias-variables/methods/CV-04-Metodos-Varias-Variables.md` | ✅ |
| `05-Calculo-Vectorial/05-Integracion-multiple/methods/CV-05-Metodos-Integracion-Multiple.md` | ✅ |
| `06-Ecuaciones-Diferenciales/01-EDO-Primer-Orden/methods/ED-01-Metodos-EDO-Primer-Orden.md` | ✅ |
| `06-Ecuaciones-Diferenciales/03-Sistemas-EDO/methods/ED-03-Metodos-Sistemas-EDO.md` | ✅ |
| `06-Ecuaciones-Diferenciales/04-Transformada-Laplace/methods/ED-04-Metodos-Transformada-Laplace.md` | ✅ |
| `06-Ecuaciones-Diferenciales/05-Series-Potencias/methods/ED-05-Metodos-Series-Potencias.md` | ✅ |
| `07-Metodos-Numericos/01-Raices-Ecuaciones/theory/MN-01-Teoria-Raices-Ecuaciones.md` | ✅ |
| `07-Metodos-Numericos/01-Raices-Ecuaciones/methods/MN-01-Metodos-Raices-Ecuaciones.md` | ✅ |
| `07-Metodos-Numericos/02-Interpolacion/methods/MN-02-Metodos-Interpolacion.md` | ✅ |
| `07-Metodos-Numericos/02-Interpolacion/problems/MN-02-Problemas.md` | ✅ |
| `07-Metodos-Numericos/03-Integracion-Numerica/theory/MN-03-Teoria-Integracion-Numerica.md` | ✅ |

**Total corregidos:** 31 archivos con ~62 tablas afectadas

---

## Referencia: Cómo Detectar Patrones

```bash
# Buscar el patrón corrupto
grep -rn "](../../..]\(" --include="*.md"

# Ejemplo de error:
❌ [texto](../../..](../../../glossary.md#termino)
✅ [texto](../../../glossary.md#termino)
```

### B. Valor absoluto `|` en tablas

**Usar estas alternativas LaTeX:**

| Símbolo original | Alternativa |
|------------------|-------------|
| `$\|x\|$` | `$\lvert x \rvert$` |
| `$\|\mathbf{v}\|$` | `$\lVert \mathbf{v} \rVert$` |
| `$\|x\| \geq 1$` | `$\lvert x \rvert \geq 1$` |

### C. Tablas con encabezados incompletos

**Ejemplo detectado y corregido:**
```markdown
❌ ANTES (en FUN-05-Teoria-Trigonometria.md):
| [Función](../../../glossary.md#dominio) | Rango |
|---------|:--------:|:-------:|:-----:|
| Arcoseno | $\arcsin x$ | $[-1, 1]$ | $[-\pi/2, \pi/2]$ |

✅ DESPUÉS:
| Función | Notación | Dominio | Rango |
|---------|:--------:|:-------:|:-----:|
| Arcoseno | $\arcsin x$ | $[-1, 1]$ | $[-\pi/2, \pi/2]$ |
```

---

## Directivas Agregadas

Se actualizaron los siguientes archivos con reglas para prevenir estos errores:

1. **`00-META/ia-contract.md`**
   - Sección 4.5: Formato de Tablas (OBLIGATORIO)
   - Sección 5.5: Detección y Corrección de Enlaces Rotos

2. **`01-Fundamentos/05-Trigonometria/_directives.md`**
   - Sección: Formato de Tablas (OBLIGATORIO)
   - Ejemplos de errores comunes

---

## Proceso de Corrección Sugerido

1. **Ejecutar búsqueda de patrones corruptos:**
   ```bash
   grep -rn "](../../..]\(" --include="*.md" .
   grep -rn "|\s*\$.*\\|.*\$\s*|" --include="*.md" .
   ```

2. **Validar cada tabla manualmente:**
   - Contar columnas en encabezados
   - Contar separadores `|---|`
   - Contar columnas en cada fila de datos

3. **Usar herramienta de validación:**
   ```bash
   python 00-META/tools/validate_repo.py --check-tables
   ```

---

## Estado de Correcciones

| Archivo | Estado | Fecha |
|---------|--------|-------|
| `FUN-05-Teoria-Trigonometria.md` | ✅ Corregido | 2026-01-05 |
| Otros archivos | ⏳ Pendiente | — |

---

<!--
::AI_DIRECTIVE::
Al encontrar tablas con estos errores, corregirlas usando las directivas de ia-contract.md.
Priorizar archivos de teoría y métodos sobre problemas.
-->
