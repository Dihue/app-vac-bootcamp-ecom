### Entorno

1.  Tener una carpeta a parte en donde almacenar los distintos entornos

2.  Dentro de esa carpeta ejercutar el comando para la creación de un
    entorno

    > python -m venv {nombre_entorno}

    Si todo salió bien, se crean los archivos necesarios del entorno

3.  Usando un archivo vacío .py, realizar la selección del intérprete
    que se encuentra en la carpeta del entorno (python.exe)

    Esto genera que VSC tome automáticamente el entorno virtual que se
    acaba de crear y lo active (evita el hacerlo de forma manual)

    **Buena práctica para el manejo de librerías**

4.  Instalación de dependencias dentro del entorno con el siguiente
    comando:

    > pip install {nombre_dependencia} -> ej: django

5.  Creación del proyecto mediante el siguiente script:

    > django-admin startproject {nombre_del_proyecto}

6.  Para poner en marcha el proyecto, se debe usar:

    > python manage.py runserver

    Estando en el directorio correcto, que es dentro de la carpeta
    que contiene al archivo manage.py

7.  Recomendación de organización del proyecto:
    Crear una carpeta con el nombre **requirements** en donde se
    guardarán las dependencias del proyecto con sus respectivas
    versiones, para ello usamos el siguiente comando estando dentro
    de la carpeta creada

    > pip freeze > {nombre_del_archivo.txt}

    En caso, de realizar una clonación del proyecto o tener un problema
    con la carpeta del entorno del proyecto, podemos realizar el
    siguiente comando, estando dentro de la carpeta **requirements**
    para instalar todas las dependencias necesarias para poner en
    marcha la aplicación:

    > pip install -r {nombre_del_archivo.txt}

8.  Crear el archivo **views.py** para el manejo de las vistas

9.  Cambiar la configuración de los **TEMPLATES** en el archivo
    settings.py para definir de dónde debe tomar los archivos .html