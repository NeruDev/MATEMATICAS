<!--
::METADATA::
type: index
topic_id: repo-readme
file_id: README
status: stable
audience: student
last_updated: 2026-01-03
-->

> 🌐 **Navegación:** [🗺️ Wiki Index - Mapa del Repositorio](WIKI_INDEX.md) | [📖 Glosario](glossary.md) | [📚 Biblioteca](00-META/bibliografia-general.md)

---

# Repositorio de Matemáticas Universitarias

## 🌱 Jardín Digital Interconectado

Este repositorio ha sido transformado en un **Jardín Digital** estilo Wikipedia, donde:

- 🔗 **Términos enlazados:** La primera mención de cada término del glosario en cada archivo está automáticamente vinculada a su definición
- 🗺️ **Índice Wiki:** Un [mapa de navegación centralizado](WIKI_INDEX.md) para ver todo el contenido organizado
- 📚 **Bibliografía validada:** Todo el contenido ha sido [verificado contra bibliografía estándar universitaria](00-META/bibliografia-general.md)

### Para humanos:
1. Explora desde el [Wiki Index](WIKI_INDEX.md) para encontrar tu tema
2. Consulta el [Glosario](glossary.md) para definiciones de términos
3. Revisa la [Biblioteca Central](00-META/bibliografia-general.md) para referencias bibliográficas

### Para IA (Copilot):
1. Lee siempre [00-META/ia-contract.md](00-META/ia-contract.md) primero
2. Respeta la nomenclatura: `[PREFIJO]-[XX]-[Contenido].md`
3. Usa el `manifest.json` de cada tema para ubicar recursos
4. Los términos del glosario están auto-vinculados en el contenido

## Módulos disponibles

| Módulo | Prefijo | Descripción | Subtemas | Estado | Bibliografía |
|--------|---------|-------------|:--------:|:------:|--------------|
| [01-Fundamentos](01-Fundamentos/00-Index.md) | `FUN` | Aritmética, álgebra, geometría, trigonometría | 6 | ✅ | Baldor, Sullivan, Swokowski |
| [02-Álgebra Lineal](02-Algebra-Lineal/00-Index.md) | `AL` | Matrices, espacios vectoriales, eigenvalores | 6 | ✅ | Grossman, Lay, Strang |
| [03-Cálculo Diferencial](03-Calculo-Diferencial/00-Index.md) | `CD` | Límites, derivadas, aplicaciones | 4 | ✅ | Stewart, Larson, Thomas |
| [04-Cálculo Integral](04-Calculo-Integral/00-Index.md) | `CI` | Integrales, técnicas, aplicaciones | 5 | ✅ | Stewart, Larson, Thomas |
| [05-Cálculo Vectorial](05-Calculo-Vectorial/00-Index.md) | `CV` | Vectores, funciones varias variables | 5 | ✅ | Stewart, Marsden, Thomas |
| [06-Ecuaciones Diferenciales](06-Ecuaciones-Diferenciales/00-Index.md) | `ED` | EDO, sistemas, Laplace, series | 5 | ✅ | Zill, Boyce, Nagle |
| [07-Métodos Numéricos](07-Metodos-Numericos/00-Index.md) | `MN` | Raíces, interpolación, integración | 4 | ✅ | Burden, Chapra, Mathews |

## Skill tree (Mapa de dependencias)

```mermaid
flowchart TD
  subgraph Fundamentos
    F1[Funciones]
    F2[Aritmética]
    F3[Álgebra]
    F4[Geometría]
    F5[Trigonometría]
    F6[Geometría Analítica]
  end
  
  subgraph "Álgebra Lineal"
    AL1[Matrices]
    AL2[Determinantes]
    AL3[Sistemas Lineales]
    AL4[Espacios Vectoriales]
    AL5[Transformaciones Lineales]
    AL6[Valores Propios]
  end
  
  subgraph Cálculo
    CD[Cálculo Diferencial]
    CI[Cálculo Integral]
    CV[Cálculo Vectorial]
  end
  
  subgraph Avanzado
    ED[Ecuaciones Diferenciales]
    MN[Métodos Numéricos]
  end
  
  F1 --> CD
  F3 --> AL1
  F5 --> CD
  AL1 --> AL2 --> AL3 --> AL4 --> AL5 --> AL6
  CD --> CI --> CV
  AL6 --> ED
  CI --> ED
  CI --> MN
  ED --> MN
```

## Referencias rápidas

| Recurso | Descripción |
|---------|-------------|
| [🗺️ Wiki Index](WIKI_INDEX.md) | Mapa de navegación centralizado |
| [📚 Biblioteca Central](00-META/bibliografia-general.md) | Referencias bibliográficas validadas |
| [📖 Glosario](glossary.md) | ~130 términos con analogías (auto-vinculado) |
| [Guía de estudio](00-META/notation-cheatsheet.md) | Símbolos y convenciones |
| [Contrato IA](00-META/ia-contract.md) | Directivas para asistentes IA |
| [Validador](00-META/tools/validate_repo.py) | Verificar integridad |
| [Auto-vinculador](00-META/tools/link_knowledge_base.py) | Script de enlaces automáticos |

---

*Última actualización: 2026-01-03* — **Auditoría bibliográfica completa:** 35 subtemas validados contra bibliografía estándar universitaria.
