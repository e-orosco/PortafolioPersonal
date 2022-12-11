# PROYECTO PORTAFOLIO CON DJANGO 🐍💻

### Este proyecto muestra una galería con una colección de portafolios creados por el usario principal, el cual tiene la opción de crear nuevos portafolios, siempre y cuando el usuario previamente haya inicado sesion.

### Se agregó validación en cada campo solicitado al momento de registrar un nuevo portafolio.

### Este proyecto web permite la creación de varios usuarios, donde cada uno puede añadir más portafolios a la galería principal.  

### En la galería de portafolios se muestra cada portafolio con los siguientes campos: Título, descripción, Foto, Url, tags y tambien el nombre del usario que creó el portafolio.

### Link del repositorio:
  https://github.com/e-orosco/U4Portafolio 



# veamos al proyecto  💻

### Pasos para poder correr el proyecto:
### Clonar el repositorio en tu terminal.
    git clone git@github.com:e-orosco/U4Portafolio.git


### Dentro de nuestra carpeta creamos nuestro entorno virtual
    python3.10 -m venv e-env

### Entramos al entorno virtual
    source e-env/bin/activate 

### Instalamos los requerimientos
    pip install -r requirements.txt

### Usé mysql como base de datos con la siguiente configuraciones:
DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'portafolio',
        'USER':'usurario',
        'PASSWORD':'contraseñaDelUsuario',
        'HOST':localhost,
        'PORT':3306,
    }
}


### Hacemos las migraciones en la terminal
    python manage.py makemigrations
    python manage.py migrate

### Finalmente ya tenemos todo listo corremos el programa
    python manage.py runserver
    
    
### Rutas principales del proyeco:
    Vista de la pagina principal ('/')
    Inicio de sesion ('/accounts/login')
    Registro ("accounts/registro_user")
    Creacion de portafolio ("portafolioNew/")

  

    
