# Mi Blog con Django

Este es un proyecto simple de Blog desarrollado con Django como parte de un ejercicio de aprendizaje. Demuestra el uso del patrón MVT, herencia de plantillas, modelos, formularios y una función de búsqueda básica.

## Requisitos Previos

* Python 3.x
* pip (gestor de paquetes de Python)
* Git (opcional, para clonar)

## Configuración e Instalación

1.  **Clonar el repositorio (si está en GitHub):**
    ```bash
    git clone <URL_DEL_REPOSITORIO_GITHUB>
    cd nombre-del-directorio-clonado
    ```
    O simplemente descarga y descomprime el código fuente.

2.  **Crear y activar un entorno virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Linux/macOS
    # venv\Scripts\activate    # En Windows
    ```

3.  **Instalar las dependencias:**
    ```bash
    pip install Django
    # Si tienes un archivo requirements.txt, usa: pip install -r requirements.txt
    ```

4.  **Aplicar las migraciones:**
    ```bash
    python manage.py migrate
    ```

5.  **(Opcional) Crear un superusuario para acceder al admin:**
    ```bash
    python manage.py createsuperuser
    ```
    Sigue las instrucciones para crear el usuario.

6.  **Iniciar el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```

    El sitio estará disponible en `http://127.0.0.1:8000/`. La interfaz de administración estará en `http://127.0.0.1:8000/admin/`.

## Orden de Prueba y Funcionalidades

Puedes probar las funcionalidades en el siguiente orden:

1.  **Accede a la página de inicio:** Ve a `http://127.0.0.1:8000/` (o `http://127.0.0.1:8000/blog/`). Verás la bienvenida y la sección de últimos posts (inicialmente vacía).
2.  **Añadir un Autor:** Navega a "Añadir Autor" (`/blog/add_author/`) y completa el formulario. Necesitarás autores antes de poder crear posts.
3.  **Añadir una Categoría:** Navega a "Añadir Categoría" (`/blog/add_category/`) y crea una o más categorías.
4.  **Añadir un Post:** Navega a "Añadir Post" (`/blog/add_post/`). Selecciona un autor y (opcionalmente) una categoría de los desplegables y escribe el contenido del post.
5.  **Ver Posts en Inicio:** Vuelve a la página de inicio. Ahora deberías ver los posts que has creado.
6.  **Buscar Posts:** Utiliza el enlace "Buscar" (`/blog/search/`) o el formulario en la barra de navegación. Introduce un término que esté en el título de alguno de tus posts y pulsa buscar. Se mostrarán los resultados coincidentes.
7.  **(Opcional) Explorar el Admin:** Accede a `/admin/`, inicia sesión con tu superusuario y explora cómo puedes ver, añadir, editar y eliminar Autores, Categorías y Posts directamente desde la interfaz administrativa.

## Estructura

* **`myblogproject/`**: Directorio principal del proyecto Django.
    * `settings.py`: Configuración del proyecto.
    * `urls.py`: URLs a nivel de proyecto.
* **`blog/`**: Aplicación Django que contiene la lógica del blog.
    * `models.py`: Define las clases `Author`, `Category` y `Post` (base de datos).
    * `forms.py`: Define los formularios `AuthorForm`, `CategoryForm`, `PostForm` y `SearchForm`.
    * `views.py`: Contiene la lógica para manejar las peticiones web (controladores MVT).
    * `urls.py`: URLs específicas de la aplicación `blog`.
    * `templates/blog/`: Contiene las plantillas HTML.
        * `base.html`: Plantilla base con la estructura común y herencia.
        * Otras plantillas (`home.html`, `add_*.html`, `search_results.html`): Extienden `base.html`.
    * `admin.py`: Configuración para mostrar los modelos en la interfaz de admin.
* **`manage.py`**: Utilidad de línea de comandos de Django.
* **`README.md`**: Este archivo.