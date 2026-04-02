# JapaLearn

JapaLearn es una aplicación web desarrollada con Django para apoyar el aprendizaje del japonés mediante el registro de frases personales.

Permite escribir una frase en español, traducirla al japonés usando Google Cloud Translation API y guardarla en una biblioteca personal organizada por categorías y notas, dentro de un sistema de usuarios con datos separados.

---

## Características

- Traducción de frases de español a japonés
- Guardado de frases en base de datos
- Organización por categorías
- Notas personales por frase
- Registro e inicio de sesión de usuarios
- Separación de datos por usuario
- Consulta de frases guardadas
- Búsqueda por texto
- Filtro por categoría
- Orden ascendente y descendente por fecha
- Edición de frases existentes
- Eliminación de registros

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

### 2. Crear y activar entorno virtual

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
PGPASSWORD=tu_password
PGHOST=localhost
PGPORT=5432
```

### Django

```env
SECRET_KEY=tu_secret_key
DEBUG=True
```

### Google Cloud Translation API

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

http://127.0.0.1:8000/

---

## Flujo de uso

1. Escribir una frase en español
2. Traducirla al japonés
3. Iniciar sesión o registrarse para guardarla
4. Asignar categoría y nota
5. Consultar, buscar, filtrar, editar o eliminar frases guardadas

---

## Estructura del proyecto
```
JapaLearn/
├── japalearn/
├── phrases/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── services.py
│   └── admin.py
├── manage.py
├── requirements.txt
└── readme.MD
```
---

## Estado del proyecto

Proyecto funcional en su primera versión pública, con autenticación, traducción, gestión de frases y organización por usuario.

---

## Autor

Desarrollado por Miguel Varas Sánchez

GitHub: https://github.com/MiguelitoBFMV/JapaLearn
