# Demo agents — subagentes de demostración

Este repositorio contiene la configuración y los agentes de demostración diseñados para el **Módulo 6** del curso **"IA generativa en el desarrollo de software"**. El objetivo es ilustrar cómo interactúan, se coordinan y restringen diferentes agentes bajo un mismo orquestador.

---

## Requisitos de Sistema

Para ejecutar estas demostraciones correctamente, necesitarás:
1. **Claude Code** (o un entorno de ejecución compatible con la especificación de agentes `.claude`).
2. **Python 3** (instalado y accesible en el sistema como `python3` para la ejecución del script de logging).
3. **Dos terminales** abiertas de forma simultánea.

---

## Instrucciones de Uso

Sigue estos pasos para observar el comportamiento de los agentes en tiempo real:

1. **Terminal 1 (Monitoreo de Logs):**
   Ve a la raíz del repositorio y ejecuta el siguiente comando para ver las entradas de log a medida que ocurren:
   ```bash
   tail -f output/agent-log.txt
   ```

2. **Terminal 2 (Ejecución):**
   Inicia la herramienta Claude Code en este mismo directorio:
   ```bash
   claude
   ```
   Una vez dentro de la sesión interactiva con Claude, ejecuta cualquiera de las demos escribiendo:
   ```text
   demo N
   ```
   *(Reemplaza `N` con un número del 1 al 8).*

---

## Estructura del Repositorio

La arquitectura del proyecto está estructurada de la siguiente manera:

```text
demo-agents/
├── README.md             # Guía del proyecto (este archivo)
├── scripts/
│   └── log.py            # Script auxiliar para formatear y almacenar logs
├── output/
│   └── .gitkeep          # Mantiene la carpeta de salida en control de versiones
└── .claude/
    ├── CLAUDE.md         # Guía de orquestación interpretada por Claude Code
    └── agents/           # Definición de agentes individuales
        ├── echo-agent.md
        ├── context-agent.md
        ├── parallel-a.md
        ├── parallel-b.md
        ├── restricted-agent.md
        ├── slow-agent.md
        ├── router-a.md
        ├── router-b.md
        └── reject-agent.md
```

---

## Tabla de Demostraciones

| Demo | Comando | Concepto Principal | Descripción |
|---|---|---|---|
| **1** | `demo 1` | Invocación Básica | Llama a `echo-agent` y devuelve el texto de entrada intacto tras registrar eventos. |
| **2** | `demo 2` | Paso de Contexto | Demuestra cómo responde `context-agent` con y sin parámetros explícitos de entorno. |
| **3** | `demo 3` | Ejecución en Paralelo | Ejecuta `parallel-a` y `parallel-b` de forma concurrente, optimizando el tiempo total. |
| **4** | `demo 4` | Ejecución Secuencial | Invoca `parallel-a` y, una vez terminado, inicia `parallel-b`. |
| **5** | `demo 5` | Restricción de Herramientas | Prueba el comportamiento de `restricted-agent` cuando se bloquean los permisos de escritura. |
| **6** | `demo 6` | Comparación de Latencias | Evalúa la diferencia de tiempo al correr dos agentes secuencialmente frente a paralelo. |
| **7** | `demo 7` | Enrutamiento Semántico | Redirige peticiones automáticamente a `router-a` (rendimiento) o `router-b` (seguridad). |
| **8** | `demo 8` | Rechazo por Ámbito (Scope) | `reject-agent` rechaza solicitudes fuera de su ámbito (como borrar archivos) pero acepta resúmenes. |

---

## Formato del Archivo de Log

El script `scripts/log.py` escribe en `output/agent-log.txt` utilizando la siguiente estructura fija:

```text
[HH:MM:SS] [nombre-del-agente  ] EVENTO — mensaje descriptivo
```

Donde:
* **`[HH:MM:SS]`**: Marca de tiempo local.
* **`[nombre-del-agente]`**: Nombre del agente alineado a la izquierda (relleno hasta 20 caracteres).
* **`EVENTO`**: Tipo de evento (`START`, `END`, `REJECT`, `FAIL`, `INFO`) alineado a la izquierda (6 caracteres).
* **`mensaje descriptivo`**: Descripción del evento realizado por el agente.

---

## Experimento Recomendado

El ejercicio más didáctico consiste en **modificar las descripciones semánticas** en los encabezados (frontmatter) de `router-a.md` y `router-b.md`.
Por ejemplo, si cambias los keywords de rendimiento y seguridad, o los haces más ambiguos, podrás ver cómo varía la decisión del orquestador al procesar la entrada de la **Demo 7**.

---

## Portar los Agentes a Antigravity

Si estás ejecutando este entorno dentro del asistente de desarrollo **Antigravity**, puedes replicar estas mismas conductas mediante los mecanismos de subagentes de Antigravity.

### 1. Definir un Subagente
Puedes usar la herramienta `define_subagent` de Antigravity para registrar dinámicamente un subagente basado en sus definiciones markdown. Por ejemplo, para registrar a `reject-agent`:

* **`name`**: `reject_agent`
* **`system_prompt`**: El contenido del cuerpo de `.claude/agents/reject-agent.md` junto a las restricciones descritas en su frontmatter.
* **`enable_write_tools`**: `true` (para permitir la herramienta Bash y ejecutar `log.py`).

### 2. Invocar un Subagente
Una vez definido, puedes llamar a dicho agente usando la herramienta `invoke_subagent` especificando el `TypeName` (ej: `reject_agent`) y el `Prompt` de la tarea.

De esta manera, el orquestador de Antigravity se encarga de instanciar y supervisar el ciclo de vida de los agentes exactamente como lo haría Claude Code.
