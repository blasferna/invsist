# Django
## Inicio Rápido

1. Crear [entorno virtual](https://docs.python.org/es/3.8/library/venv.html#:~:text=Un%20entorno%20virtual%20es%20un,parte%20de%20tu%20sistema%20operativo.) para instalar librerías localmente (dentro del proyecto) y de esa manera éstas no creen conflicto con el entorno global de python.

```bash
c:\> python -m venv venv
```
O
```bash
c:\> py -3 -m venv venv
```

2. Activar el entorno virtual

```bash
c:\> cd venv\Scripts
c:\> activate

# así debe aparecer si está activado el entorno virtual
(venv) c:\venv\Scripts>

# ir a la raíz
(venv) c:\venv\Scripts> cd \

(venv) c:\>
```

3. Instalar última versión de django

```bash
(venv) c:\> pip install django
```

4. Crear un proyecto django utilizando el comando `startproject`

```bash
(venv) c:\> django-admin startproject invsist
```

5. Acceder al nuevo proyecto creado

```bash
(venv) c:\> cd invsist
```

Un proyecto django posee la siguiente estructura al crearse.

```
C:\invsist
|   manage.py   
\---invsist
        asgi.py
        settings.py
        urls.py
        wsgi.py
        __init__.py
```

6. Copiamos la carpeta venv dentro del proyecto para que la estructura quede de la siguiente manera.

```
C:\invsist
|   manage.py   
\---invsist
        asgi.py
        settings.py
        urls.py
        wsgi.py
        __init__.py
\---venv     <-- carpeta del entorno virtual dentro
``` 

## Comandos útiles
1. Crear una aplicación.

```bash
(venv) c:\invsist>python manage.py startapp inventory
```

2. Crear migraciones, cada vez que sea creado o modificado los modelos de datos.

```bash
(venv) c:\invsist>python manage.py makemigrations
```

3. Persistir migraciones en la base de datos.

```bash
(venv) c:\invsist>python manage.py migrate
```

3. Ejecutar el servidor para realizar pruebas.

```bash
(venv) c:\invsist>python manage.py runserver
```