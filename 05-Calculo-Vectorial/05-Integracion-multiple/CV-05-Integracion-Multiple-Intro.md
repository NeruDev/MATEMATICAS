<!--
::METADATA::
type: index
topic_id: cv-05-integracion-multiple
file_id: CV-05-Integracion-Multiple-Intro
status: stable
audience: student
requires: [CI-03-Integral-Definida, CV-04-Varias-Variables]
-->

# Integración múltiple

## Propósito del tema

Calcular integrales dobles y triples para determinar áreas, volúmenes, masas y centroides, dominando las técnicas de cambio de variables a coordenadas polares, cilíndricas y esféricas.

## Ruta de aprendizaje

1. **Integrales dobles:** definición, iteración, regiones tipo I y II.
2. **Cambio a polares:** jacobiano, aplicaciones a regiones circulares.
3. **Integrales triples:** iteración en coordenadas cartesianas.
4. **Coordenadas cilíndricas:** conversión, jacobiano, aplicaciones.
5. **Coordenadas esféricas:** conversión, jacobiano, volúmenes de sólidos.
6. **Aplicaciones:** área, volumen, masa, centro de masa, momentos de inercia.

## Mapa de recursos

```
CV-05-Integracion-Multiple-Intro.md  ← Estás aquí
CV-05-Resumen-Formulas.md            ← Fórmulas clave para repaso rápido
theory/
  └── CV-05-Teoria-Integracion.md    ← Desarrollo completo de la teoría
methods/
  └── [métodos paso a paso]
problems/
  └── [enunciados de práctica]
solutions/
  └── [soluciones detalladas]
```

## Conexiones

- **Prerequisitos:** [integral definida](../../glossary.md#integral-definida), funciones de varias variables.
- **Usos posteriores:** integrales de línea, teoremas de Green, Stokes y Gauss.

## Vista previa de conceptos clave

| Concepto | Descripción breve |
|----------|-------------------|
| Integral doble | $\iint_R f(x,y)\, dA$ |
| Integral triple | $\iiint_E f(x,y,z)\, dV$ |
| Jacobiano | [Factor de escala](../../glossary.md#factor-de-escala) en cambio de variables |
| Coord. cilíndricas | $(r, \theta, z)$, $dV = r\,dr\,d\theta\,dz$ |
| Coord. esféricas | $(\rho, \phi, \theta)$, $dV = \rho^2\sin\phi\,d\rho\,d\phi\,d\theta$ |

---

<!--
IA: Este es el punto de entrada (entry_point) para el tema de integración múltiple.
Consulta el manifest.json para el resource_map completo.
file_id: CV-05-Integracion-Multiple-Intro
-->
