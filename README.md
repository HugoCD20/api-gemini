📦 Proyecto Backend - Configuración y Ejecución
Este proyecto es un backend desarrollado en Python. A continuación, se describen los pasos para configurar el entorno virtual, instalar dependencias y ejecutar el servidor.

🚀 Requisitos
Python 3.8 o superior

Git (para clonar el repositorio)

pip (normalmente viene con Python)

🛠️ Configuración en Windows
bash
Copiar
Editar
# Entrar a la carpeta backend
cd backend

# Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual
cd venv\Scripts
activate.bat

# Volver a la carpeta backend
cd ../..

# Instalar dependencias
pip install -r requirements.txt

# Crear el archivo .env a partir del ejemplo
copy .env-example .env  # O hacerlo manualmente

# Editar .env para configurar las variables necesarias

# Ejecutar el servidor
python api.py
🐧 Configuración en Ubuntu/Linux
bash
Copiar
Editar
# Entrar a la carpeta backend
cd backend

# Crear el entorno virtual
python3 -m venv venv

# Activar el entorno virtual
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Crear el archivo .env a partir del ejemplo
cp .env-example .env

# Editar el archivo .env con tus variables de entorno

# Ejecutar el servidor
python3 api.py
📄 Notas
Asegúrate de tener todas las variables necesarias definidas en el archivo .env.

Para desactivar el entorno virtual:

En Windows: deactivate

En Linux: deactivate

