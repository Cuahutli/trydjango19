# Proyecto Try Django 1.9

### Para usar este proyecto, seguimos los siguientes pasos:

1. Clonamos el repositorio

```sh
git clone https://github.com/Cuahutli/trydjango19.git
```

2. Accedemos al directorio 

```sh
cd trydjango19
```

3. Creamos un nuevo entorno virtual con `virtualenv`

```sh
# Usando la distribución por default de python en el sistema
virtualenv venv

# Usando especificamente python3 (en mi caso este es el path, variará según donde tengas tú python3 instalado)

# En Windows
virtualenv -p c:/Python3/python.exe venv

# En Linux/Mac
virvualenv -p /usr/bin/python3 venv
```

4. Activamos el entorno virtual que creamos

```sh
# En Windows
venv\Scripts\activate

# En Linux/Mac
source venv/bin/activate
```

5. Instalamos las librerias necesarias

```sh
pip install -r requirements.txt
```

6. Accedemos a la carpeta src

```sh
cd src
```

7. Creamos la BD (haciendo las migraciones)

```sh
python manage.py migrate
```

8. Creamos un super usuario (lleanamos los datos que nos piden)

```sh
python manage.py createsuperuser
```

9. Ejecutamos el proyecto

```sh
python manage.py runserver
```

10. Creamos nuestro primer post accediendo a la siguiente url

```sh
http://127.0.0.1:8000/posts/create/
```


**A Disfrutar del proyecto**




