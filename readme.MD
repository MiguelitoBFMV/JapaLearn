# JapaLearn

## 📌 Descripción

JapaLearn es una aplicación web orientada al aprendizaje del japonés, que permite registrar frases de interés de forma estructurada.

El usuario puede ingresar una frase en español, traducirla al japonés mediante una API externa, y almacenarla junto a información adicional como categorías y notas personales. Posteriormente, es posible consultar estos registros para reforzar el aprendizaje.

El proyecto está desarrollado con Django (Python) e integra servicios de traducción mediante Google Cloud Translation API.

---

## 🚀 Funcionalidades

- Traducción de frases desde español a japonés mediante API  
- Registro de frases en una base de datos  
- Clasificación de frases por categorías  
- Posibilidad de añadir notas personalizadas a cada registro  
- Consulta de frases guardadas  

---

## 🛠️ Tecnologías utilizadas

- Python  
- Django  
- PostgreSQL  
- HTML / CSS  
- Google Cloud Translation API  

---

## ⚙️ Instalación

### Requisitos previos

Antes de comenzar, asegúrate de tener instalado:

- Python 3.12 o superior  
- PostgreSQL  

> Este proyecto fue desarrollado utilizando Python 3.12.10.

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd JapaLearn
```

### 2. Crear y activar un entorno virtual

```bash
python -m venv venv
```

Activar entorno virtual:

**Windows**
```bash
venv\Scripts\activate
```

**Linux / macOS**
```bash
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

Crea un archivo `.env` en la raíz del proyecto y define las variables necesarias para la conexión a la base de datos.

Ejemplo:

```env
DB_NAME=nombre_base_de_datos
DB_USER=usuario
DB_PASSWORD=contraseña
DB_HOST=localhost
DB_PORT=5432
```

### 5. Configurar Google Cloud Translation API

Para habilitar la traducción automática:

- Crear un proyecto en Google Cloud  
- Habilitar **Google Cloud Translation API**  
- Generar y descargar las credenciales en formato JSON  
- Configurar la ruta a las credenciales en el entorno (por ejemplo, mediante variable de entorno)  

### 6. Aplicar migraciones

```bash
python manage.py migrate
```

### 7. Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

Luego abre el navegador en:

http://127.0.0.1:8000/

---

## ▶️ Uso

1. Accede a la aplicación desde el navegador  
2. Ingresa una frase en español  
3. Traduce la frase al japonés  
4. Guarda la frase junto a su categoría y notas opcionales  
5. Consulta tus frases guardadas para reforzar el aprendizaje  

---

## 🔮 Futuras mejoras

- Mejora del diseño y experiencia de usuario 
- Implementación de traducción del Japonés al Español (posibilidad)
- Sistema de autenticación de usuarios  (posibilidad)
