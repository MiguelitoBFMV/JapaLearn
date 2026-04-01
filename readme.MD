# JapaLearn

JapaLearn es una aplicación web desarrollada con Django para apoyar el aprendizaje del japonés mediante el registro de frases personales.

Permite escribir frases en español, traducirlas al japonés usando Google Cloud Translation API y guardarlas organizadas por categoría y notas, todo dentro de un sistema de usuarios con datos separados.

---

## Características principales

- Traducción de frases (ES → JP)
- Registro de frases en base de datos
- Clasificación por categorías
- Notas personales por frase
- Búsqueda y filtrado de registros
- Edición y eliminación de frases
- Registro de usuarios
- Login y logout
- Separación de datos por usuario

---

## Tecnologías utilizadas

- Python
- Django
- PostgreSQL
- HTML / CSS
- Google Cloud Translation API

---

## Requisitos

- Python 3.12 o superior
- PostgreSQL
- Git

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/MiguelitoBFMV/JapaLearn.git
cd JapaLearn
```

### 2. Crear entorno virtual

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Variables de entorno

Crea un archivo `.env` en la raíz del proyecto.

### Base de datos

```env
PGDATABASE=nombre_db
PGUSER=usuario
PGPASSWORD=password
PGHOST=localhost
PGPORT=5432
```

### Django

```env
SECRET_KEY=tu_secret_key
DEBUG=True
```

### Google Cloud API

```env
GOOGLE_APPLICATION_CREDENTIALS=ruta/a/credenciales.json
```

---

## Migraciones

```bash
python manage.py migrate
```

Crear superusuario (opcional):

```bash
python manage.py createsuperuser
```

---

## Ejecutar el proyecto

```bash
python manage.py runserver
```

Abrir en navegador:

```text
http://127.0.0.1:8000/
```

---

## Flujo de uso

1. Escribir una frase en español  
2. Traducirla al japonés  
3. Iniciar sesión o registrarse  
4. Guardar la frase con categoría y nota  
5. Consultar, filtrar, editar o eliminar tus frases  

---

## Estructura del proyecto

```text
JapaLearn/
├── japalearn/
├── phrases/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── services.py
│   └── admin.py
├── manage.py
├── requirements.txt
└── README.md
```

---

## Estado del proyecto

- Sistema de autenticación completo  
- CRUD funcional de frases  
- Integración con API de traducción  
- Separación de datos por usuario  

---

## Mejoras futuras

- Manejo de errores en la API de traducción  
- Mensajes de feedback al usuario (éxito/error)  
- Mejora de experiencia de usuario (UX/UI)  

---

## Autor

Desarrollado por **Miguel Varas Sánchez**

GitHub:
https://github.com/MiguelitoBFMV/JapaLearn
