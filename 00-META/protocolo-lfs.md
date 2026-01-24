# Protocolo: Migración Retroactiva de Binarios a Git LFS (v1.1)

Este protocolo tiene como objetivo reducir el tamaño del directorio .git eliminando archivos binarios del historial de commits y moviéndolos a Git Large File Storage (LFS).

⚠️ **Advertencia Crítica**
Este procedimiento reescribe el historial de Git. Los hashes de los commits cambiarán. Si el repositorio es compartido, todos los colaboradores deberán re-clonar el repositorio o realizar un hard reset a la nueva rama tras la operación.

---

## Fase 1: Identificación y Configuración
1. **Identificar extensiones:** Determinar qué extensiones de archivo están causando el aumento de peso (ej. .png, .jpg, .zip, .pdf).
2. **Inicializar LFS:**
   ```powershell
   git lfs install
   ```
3. **Configurar rastreo actual:**
   ```powershell
   git lfs track "*.png" "*.jpg" "*.jpeg" "*.gif" "*.webp" "*.ico" "*.pdf" "*.zip"
   git add .gitattributes
   ```

## Fase 2: Migración del Historial (Reescritura)
⚠️ **NOTA DE EJECUCIÓN:** Debido a que este comando es interactivo y requiere confirmaciones críticas de seguridad que pueden fallar en entornos de agentes IA o IDEs integrados, **DEBE ejecutarse manualmente en una terminal externa (PowerShell o Bash).**

1. **Ejecutar migración integral:**
   ```powershell
   git lfs migrate import --everything --include="*.png,*.jpg,*.jpeg,*.gif,*.webp,*.ico,*.pdf,*.zip"
   ```
   *   Al ejecutarlo, la terminal preguntará: `override changes in your working copy? [y/N]`. Escribir `y` y presionar Enter.

## Fase 3: Purga y Limpieza Profunda
⚠️ **NOTA DE EJECUCIÓN:** Al igual que la fase anterior, se recomienda ejecutar estos comandos en una **terminal externa** para asegurar que el proceso de recolección de basura no sea interrumpido por el tiempo de espera del agente.

1. **Expirar logs y purgar:**
   ```powershell
   # Eliminar el rastro de commits antiguos en el reflog
   git reflog expire --expire=now --all

   # Limpieza agresiva de objetos no referenciados
   git gc --prune=now --aggressive
   ```

## Fase 4: Sincronización Remota
Para que el servidor (GitHub/GitLab) refleje la reducción de espacio:

1. **Force Push:**
   ```powershell
   git push origin main --force
   ```

---

## Verificación de Éxito
El agente/usuario debe validar:
1. **Listado de LFS:** `git lfs ls-files` (Debe mostrar los archivos rastreados).
2. **Peso del historial:** `git count-objects -vH` (El `size-pack` debería haber disminuido).
3. **Integridad:** Navegar a un commit antiguo y verificar que el archivo binario sigue siendo accesible.

---
*Firmado: Protocolo de Optimización de Repositorios IA - v1.1 (Actualizado por incidencia de interactividad en CLI)*
