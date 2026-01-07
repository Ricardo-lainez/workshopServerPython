# 🌐 Servicio Web con Python, Flask y MongoDB

Sistema de gestión de estudiantes ESPE desarrollado con Python (Flask) en el backend, MongoDB como base de datos, y Bootstrap para el frontend.

## 📋 Características

- ✅ API REST completa (CRUD)
- ✅ Interfaz web responsiva con Bootstrap 5
- ✅ Tabla interactiva con DataTables
- ✅ Operaciones en tiempo real
- ✅ Validación de formularios
- ✅ Alertas con SweetAlert2
- ✅ Base de datos MongoDB

## 🛠️ Tecnologías Utilizadas

### Backend
- **Flask** - Framework web de Python
- **Flask-CORS** - Manejo de CORS
- **PyMongo** - Driver de MongoDB para Python

### Frontend
- **HTML5/CSS3**
- **JavaScript**
- **Bootstrap 5** - Framework CSS
- **DataTables** - Tabla interactiva
- **SweetAlert2** - Alertas personalizadas
- **Bootstrap Icons** - Iconos

### Base de Datos
- **MongoDB** - Base de datos NoSQL

## 📦 Estructura del Proyecto

```
webServicePython/
│
├── app.py                 # Aplicación Flask principal
├── requirements.txt       # Dependencias Python
├── insert_data.py        # Script para insertar datos de ejemplo
├── README.md             # Este archivo
│
└── templates/
    └── index.html        # Página web principal
```

## 🚀 Instalación y Configuración

### Prerrequisitos

1. **Python 3.8 o superior**
   - Verifica: `python --version`
   - Descarga: https://www.python.org/downloads/

2. **MongoDB**
   - Descarga e instala: https://www.mongodb.com/try/download/community
   - O usa MongoDB Atlas (cloud): https://www.mongodb.com/cloud/atlas

### Paso 1: Instalar MongoDB (si no lo tienes)

#### Opción A: MongoDB Local
1. Descarga MongoDB Community Server
2. Instala con configuración por defecto
3. Inicia el servicio:
   ```bash
   # Windows (PowerShell como administrador)
   net start MongoDB
   ```

#### Opción B: MongoDB Atlas (Cloud)
1. Crea una cuenta en https://www.mongodb.com/cloud/atlas
2. Crea un cluster gratuito
3. Obtén la cadena de conexión
4. Modifica `app.py` y `insert_data.py` con tu URI:
   ```python
   MONGO_URI = "mongodb+srv://usuario:password@cluster.mongodb.net/"
   ```

### Paso 2: Crear Entorno Virtual (Recomendado)

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows PowerShell:
.\venv\Scripts\Activate.ps1

# Windows CMD:
venv\Scripts\activate.bat
```

### Paso 3: Instalar Dependencias

```bash
pip install -r requirements.txt
```

### Paso 4: Insertar Datos de Ejemplo

```bash
python insert_data.py
```

Este script creará la base de datos `espe_db` y la colección `estudiantes` con 10 registros de ejemplo.

### Paso 5: Ejecutar la Aplicación

```bash
python app.py
```

La aplicación estará disponible en: **http://localhost:5000**

## 🎯 Uso de la Aplicación

### Interfaz Web

1. Abre tu navegador y visita: `http://localhost:5000`
2. Verás una tabla con todos los estudiantes
3. Funcionalidades disponibles:
   - **Agregar** nuevo estudiante (botón verde)
   - **Editar** estudiante existente (botón amarillo)
   - **Eliminar** estudiante (botón rojo)
   - **Actualizar** lista (botón de recargar)
   - **Buscar** y **ordenar** en la tabla

### API REST

#### Obtener todos los estudiantes
```bash
GET http://localhost:5000/api/estudiantes
```

#### Obtener un estudiante por ID
```bash
GET http://localhost:5000/api/estudiantes/{id}
```

#### Crear nuevo estudiante
```bash
POST http://localhost:5000/api/estudiantes
Content-Type: application/json

{
  "cedula": "1730345678",
  "nombre": "Pedro",
  "apellido": "García",
  "email": "pedro.garcia@espe.edu.ec",
  "carrera": "Ingeniería en Software",
  "semestre": 5,
  "promedio": 8.5
}
```

#### Actualizar estudiante
```bash
PUT http://localhost:5000/api/estudiantes/{id}
Content-Type: application/json

{
  "promedio": 9.0
}
```

#### Eliminar estudiante
```bash
DELETE http://localhost:5000/api/estudiantes/{id}
```

## 🔧 Configuración Personalizada

### Cambiar Puerto del Servidor

En [app.py](app.py#L133):
```python
app.run(debug=True, host='0.0.0.0', port=5000)  # Cambia el puerto aquí
```

### Cambiar Base de Datos

En [app.py](app.py#L8-L10):
```python
MONGO_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "tu_base_datos"
COLLECTION_NAME = "tu_coleccion"
```

## 🐛 Solución de Problemas

### Error: "No se pudo conectar a MongoDB"
- Verifica que MongoDB esté ejecutándose:
  ```bash
  # Windows
  net start MongoDB
  ```

### Error: "ModuleNotFoundError: No module named 'flask'"
- Instala las dependencias:
  ```bash
  pip install -r requirements.txt
  ```

### Error: "Address already in use"
- El puerto 5000 está ocupado. Cámbialo en `app.py`

### La página no carga datos
- Verifica que el backend esté ejecutándose
- Abre la consola del navegador (F12) para ver errores
- Verifica que MongoDB tenga datos (ejecuta `insert_data.py`)

## 📚 Recursos Adicionales

- [Documentación Flask](https://flask.palletsprojects.com/)
- [Documentación PyMongo](https://pymongo.readthedocs.io/)
- [Documentación Bootstrap](https://getbootstrap.com/)
- [Documentación MongoDB](https://docs.mongodb.com/)

## 👨‍💻 Autor

Desarrollado para el curso de Programación Web Avanzada - ESPE

## 📝 Licencia

Este proyecto es de código abierto y está disponible para fines educativos.

---

**¡Listo para desarrollar! 🚀**
