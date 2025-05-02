# El Taller Interior - Blog con Django

Bienvenido al repositorio de "El Taller Interior", un proyecto de blog enfocado en la motivación y el desarrollo personal, construido íntegramente con Python y el framework Django.
Este proyecto fue desarrollado como parte del curso de Python en Coderhouse y sirve como demostración práctica de la implementación de un sitio web dinámico con funcionalidades esenciales y avanzadas.

## ✨ Funcionalidades Principales

* **Gestión de Artículos (Pages):** CRUD completo (Crear, Leer, Actualizar, Borrar) para los artículos del blog.
    * Uso de editor de texto enriquecido (CKEditor) para el contenido.
    * Soporte para carga de imágenes destacadas por artículo.
    * Permisos: Solo usuarios logueados pueden crear, y solo el autor puede editar/borrar sus propios artículos.
* **Sistema de Autenticación:** Registro de nuevos usuarios, Inicio de Sesión (Login), Cierre de Sesión (Logout) y recuperación de contraseña.
* **Perfiles de Usuario:**
    * Cada usuario tiene un perfil asociado.
    * Visualización de datos del perfil (nombre, apellido, email, biografía, avatar).
    * Edición de datos del perfil, incluyendo la carga/cambio de imagen de avatar.
    * Funcionalidad para cambiar la contraseña.
* **Mensajería Privada:** Sistema básico para que los usuarios registrados puedan enviarse mensajes privados entre sí.
    * Bandeja de entrada listando conversaciones.
    * Vista detallada de conversación.
    * Formulario para enviar mensajes.
* **Navegación y Estructura:**
    * Uso de Herencia de Plantillas (`base.html`) para una estructura consistente.
    * Barra de navegación dinámica (cambia según el estado de autenticación).
    * Páginas estáticas (Inicio, Acerca de Mí).
* **Interfaz de Administración Django:** Modelos registrados para gestión interna.
* **Desarrollo:**
    * Uso del patrón MVT (Modelo-Vista-Template).
    * Implementación con Vistas Basadas en Clases (CBVs) y Vistas Basadas en Funciones (FBVs).
    * Uso de Mixins (`LoginRequiredMixin`, `UserPassesTestMixin`) y Decoradores (`@login_required`) para control de acceso.

## 🛠️ Tecnologías Utilizadas

* **Backend:** Python 3.x, Django 5.x
* **Base de Datos:** SQLite (por defecto en desarrollo)
* **Frontend:** HTML5, CSS3 (estilos básicos inline/en `<style>`), Templates Django
* **Librerías Python Clave:**
    * `Pillow` (manejo de imágenes)
    * `django-ckeditor` (editor de texto enriquecido)
* **Control de Versiones:** Git y GitHub

## 🚀 Configuración e Instalación

Sigue estos pasos para poner en marcha el proyecto en tu entorno local:

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/pitydroid/PY_proj3

2.  **Crear y activar un entorno virtual (Recomendado):**
    ```bash
    # Crear el entorno (puedes usar 'python3' si 'python' no funciona)
    python -m venv venv

    # Activar en Windows (CMD/PowerShell)
    venv\Scripts\activate

    # Activar en Linux/macOS
    source venv/bin/activate
    ```
    *Verás `(venv)` al principio de la línea de comandos si se activó correctamente.*

3.  **Instalar las dependencias:**
    * Asegúrate de que el entorno virtual esté activado.
    * Instala todos los paquetes necesarios desde el archivo `requirements.txt`:
      ```bash
      pip install -r requirements.txt
      ```

4.  **(Opcional pero Recomendado) Crear Avatar por Defecto:**
    * Crea una carpeta llamada `media` en la raíz del proyecto (junto a `manage.py`).
    * Dentro de `media`, crea otra carpeta llamada `avatars`.
    * Coloca una imagen llamada `default.png` dentro de `media/avatars/`. Esta será usada si un usuario no sube su propio avatar.

5.  **Aplicar las migraciones:**
    * Este comando creará la base de datos (`db.sqlite3` si no existe) y las tablas necesarias.
      ```bash
      python manage.py migrate
      ```

6.  **(Opcional pero necesario para Admin) Crear un superusuario:**
    ```bash
    python manage.py createsuperuser
    ```
    * Sigue las instrucciones para crear tu cuenta de administrador (username, email, password).

7.  **Iniciar el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```

