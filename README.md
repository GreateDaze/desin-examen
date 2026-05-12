# TaskFlow MVC

TaskFlow MVC es una aplicacion de escritorio desarrollada integramente en Python con PySide6. La aplicacion permite gestionar tareas personales con titulo, descripcion, prioridad, fecha limite y estado de finalizacion.

El proyecto sigue el patron MVC:

- `app/models/`: datos y persistencia.
- `app/views/`: interfaz grafica PySide6.
- `app/controllers/`: coordinacion entre la vista y el modelo.

## Requisitos

- Python 3.11 recomendado.
- PySide6.
- PyInstaller para generar ejecutables.

## Ejecucion local

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

En Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Generar ejecutable local

```bash
pip install -r requirements.txt
python -m PyInstaller --onefile --windowed --name TaskFlowMVC main.py
```

El ejecutable se genera en `dist/TaskFlowMVC.exe` en Windows.

## Instalador para Windows

El instalador se define en `installer/TaskFlowMVC.iss` y esta preparado para Inno Setup. Incluye:

- Asistente de instalacion.
- Aceptacion de terminos y condiciones.
- Pagina de licencia.
- Validacion de licencia con la clave educativa `TF-MVC-2026`.
- Creacion de accesos directos.

Para compilarlo en Windows con Inno Setup instalado:

```powershell
iscc installer/TaskFlowMVC.iss
```

## GitHub Actions

El workflow se encuentra en `.github/workflows/build.yml` y se ejecuta automaticamente al hacer `push` o `pull_request` sobre la rama `main`.

El workflow:

- Configura Python.
- Instala PySide6 y PyInstaller.
- Genera un ejecutable `.exe` en Windows.
- Genera un paquete `.deb` en Linux.
- Publica los resultados como artifacts descargables.

## Estructura principal

```text
.
├── app/
│   ├── controllers/
│   ├── models/
│   └── views/
├── installer/
├── packaging/
├── .github/workflows/
├── main.py
├── requirements.txt
└── README.md
```
