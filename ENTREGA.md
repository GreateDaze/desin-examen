# Documento de entrega - TaskFlow MVC

## 1. Datos del proyecto

- Alumno: Ivan Cortegoso Rodriguez
- Aplicacion: TaskFlow MVC
- Tecnologia: Python + PySide6
- Patron de diseno: MVC
- Version de Python recomendada: 3.11
- Repositorio GitHub: PENDIENTE_DE_ANADIR_URL

## 2. Descripcion

TaskFlow MVC es una aplicacion de escritorio para gestionar tareas. Permite crear, editar, eliminar, completar y reabrir tareas. Cada tarea incluye titulo, descripcion, prioridad y fecha limite.

## 3. Estructura MVC

- Modelo: `app/models/task.py` y `app/models/task_model.py`
- Vista: `app/views/main_window.py`
- Controlador: `app/controllers/task_controller.py`
- Punto de entrada: `main.py`

## 4. Ejecucion local

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

## 5. Conversion a ejecutable

El proyecto genera el ejecutable directamente con PyInstaller mediante este comando:

```bash
python -m PyInstaller --onefile --windowed --name TaskFlowMVC main.py
```

## 6. Instalador

El instalador para Windows se define en `installer/TaskFlowMVC.iss` y se compila con Inno Setup:

```powershell
iscc installer/TaskFlowMVC.iss
```

El asistente incluye aceptacion de licencia y terminos.

Clave educativa de prueba para la pagina de licencia:

```text
TF-MVC-2026
```

## 7. GitHub Actions

El workflow se encuentra en `.github/workflows/build.yml`.

Se ejecuta automaticamente con:

- `push` a `main`
- `pull_request` a `main`

Genera artifacts:

- `TaskFlowMVC-windows-exe`
- `TaskFlowMVC-linux-deb`

## 8. Capturas de pantalla requeridas

Anadir capturas de:

1. Aplicacion PySide6 en ejecucion.
2. Repositorio publico en GitHub.
3. Carpeta `.github/workflows/` con el archivo `build.yml`.
4. Ejecucion del workflow con check verde.
5. Detalle de los artifacts generados.
6. Instalador ejecutandose y pantalla de licencia.

## 9. Validacion final

- Interfaz funcional en PySide6: completado.
- Arquitectura MVC: completado.
- README con instrucciones: completado.
- Workflow de GitHub Actions: completado.
- Generacion automatizada de `.exe` y `.deb`: configurada.
- Capturas del proceso: pendiente de incorporar tras subir el proyecto a GitHub.
