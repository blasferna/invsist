# invsist
Sistema de gestión de inventario (Tutorial)

## Instalación

1. Clonar el repositorio: 

```
git clone https://github.com/blasferna/invsist
```

2. Crear el entorno virtual

```
cd invsist
python -m venv venv
cd venv\Scripts
activate
```

3. Instalar dependencias

```
(venv) c:\invsist> pip install -r requirements.txt
```

4. Ejecutar migraciones

```
(venv) c:\invsist> python manage.py migrate
```

5. Crear usuario administrador

```
(venv) c:\invsist> python manage.py createsuperuser
```

6. Ejecutar servidor de pruebas

```
(venv) c:\invsist> python manage.py runserver
```


