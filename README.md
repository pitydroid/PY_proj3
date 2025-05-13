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

## 📋 Requisitos Previos

* Python 3.8 o superior.
* `pip` (gestor de paquetes de Python).
* Git (opcional, para clonar el repositorio fácilmente).

## 🚀 Configuración e Instalación

Sigue estos pasos para poner en marcha el proyecto en tu entorno local:

1.  **Clonar el repositorio:**
    ```bash
    git clone <URL_DEL_REPOSITORIO_GITHUB>
    cd nombre-del-repositorio-clonado # Ej: cd El_Taller_Interior_Django
    ```
    *(Reemplaza `<URL_DEL_REPOSITORIO_GITHUB>` con la URL real de tu repo)*.
    O descarga el archivo ZIP desde GitHub y descomprímelo.

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

8.  **Acceder al sitio:**
    * Abre tu navegador web y ve a `http://127.0.0.1:8000/`.
    * La interfaz de administración estará disponible en `http://127.0.0.1:8000/admin/` (requiere login con superusuario).

## 🧪 Orden de Prueba y Funcionalidades Sugerido

Puedes probar las funcionalidades principales en este orden:

1.  **Navegación Anónima:** Accede a Inicio (`/`), Artículos (`/pages/`), Acerca de Mí (`/pages/about/`). Verifica que los enlaces de Login/Registro estén visibles y los de Usuario/Mensajes/Crear no. Intenta acceder a una página restringida (ej. `/accounts/profile/`) y verifica que te redirija al Login.
2.  **Registro:** Ve a "Registrarse" (`/accounts/signup/`). Intenta registrarte con datos inválidos y luego con datos válidos para un **Usuario 1**. Verifica el login automático y el cambio en la barra de navegación.
3.  **Login/Logout:** Cierra sesión ("Logout"). Ve a "Login" (`/accounts/login/`). Intenta login con datos incorrectos y luego con los datos correctos del **Usuario 1**. Verifica el funcionamiento.
4.  **Gestión de Perfil:**
    * Ve a "Mi Perfil" (`/accounts/profile/`). Verifica que se muestren los datos (avatar por defecto).
    * Ve a "Editar Perfil" (`/accounts/profile/edit/`). Cambia nombre, apellido, bio y **sube un avatar**. Guarda. Verifica que los cambios (incluyendo el nuevo avatar) se reflejen en la vista de perfil.
    * Ve a "Cambiar Contraseña". Prueba el flujo completo de cambio de contraseña. Cierra sesión y vuelve a entrar con la nueva contraseña.
5.  **Gestión de Artículos (Pages):**
    * Ve a "+ Crear Artículo" (`/pages/create/`). Crea un artículo nuevo, usando formato en CKEditor y **subiendo una imagen**. Guarda.
    * Verifica que aparezca en la lista de "Artículos" (`/pages/`). Comprueba que los enlaces Editar/Borrar sean visibles *solo* para este artículo.
    * Entra al detalle del artículo. Verifica que se muestre la imagen, el contenido formateado, autor, fecha, etc. y los enlaces Editar/Borrar.
    * Edita el artículo (cambia algo, cambia/quita la imagen). Guarda y verifica los cambios.
    * Borra el artículo (prueba cancelar y luego confirmar). Verifica que desaparezca de la lista.
6.  **Prueba de Permisos:** Registra un **Usuario 2**. Inicia sesión como Usuario 2. Intenta ver la lista y el detalle del artículo creado por Usuario 1. Verifica que **no** ves los enlaces Editar/Borrar. Intenta acceder a las URLs de edición/borrado directamente y verifica que se te niegue el acceso (Error 403 o redirección).
7.  **Mensajería Básica:**
    * Logueado como Usuario 1, ve a "Mensajes" (`/messages/`). Ve a la lista de usuarios (`/messages/users/`) y selecciona Usuario 2. Envía un mensaje.
    * Logueado como Usuario 2, ve a "Mensajes". Entra a la conversación con Usuario 1. Verifica que ves el mensaje. Envía una respuesta.
    * Vuelve como Usuario 1 y verifica que ves la respuesta.
8.  **(Opcional) Explorar el Admin:** Accede a `/admin/` con tu superusuario. Revisa los modelos `Pages`, `Profiles`, `Messages` y verifica que puedes ver/administrar los datos creados desde el sitio.

## 📂 Estructura del Proyecto
¡Excelente! Vamos a mejorar ese README para que refleje con precisión el proyecto final que has construido, incluyendo las nuevas funcionalidades y la temática de "El Taller Interior".

Aquí tienes una versión mejorada y más completa. Puedes copiarla y pegarla en tu archivo README.md, reemplazando el contenido anterior. Asegúrate de reemplazar los placeholders como <URL_DEL_REPOSITORIO_GITHUB> con tu URL real.

Markdown

# El Taller Interior - Blog con Django

Bienvenido/a al repositorio de "El Taller Interior", un proyecto de blog enfocado en la motivación y el desarrollo personal, construido íntegramente con Python y el framework Django.

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

## 📋 Requisitos Previos

* Python 3.8 o superior.
* `pip` (gestor de paquetes de Python).
* Git (opcional, para clonar el repositorio fácilmente).

## 🚀 Configuración e Instalación

Sigue estos pasos para poner en marcha el proyecto en tu entorno local:

1.  **Clonar el repositorio:**
    ```bash
    git clone <URL_DEL_REPOSITORIO_GITHUB>
    cd nombre-del-repositorio-clonado # Ej: cd El_Taller_Interior_Django
    ```
    *(Reemplaza `<URL_DEL_REPOSITORIO_GITHUB>` con la URL real de tu repo)*.
    O descarga el archivo ZIP desde GitHub y descomprímelo.

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

8.  **Acceder al sitio:**
    * Abre tu navegador web y ve a `http://127.0.0.1:8000/`.
    * La interfaz de administración estará disponible en `http://127.0.0.1:8000/admin/` (requiere login con superusuario).
