# PROYECTO PORTAFOLIO CON DJANGO 馃悕馃捇

### Este proyecto muestra una galer铆a con una colecci贸n de portafolios creados por el usario principal, el cual tiene la opci贸n de crear nuevos portafolios, siempre y cuando el usuario previamente haya inicado sesion.

### Se agreg贸 validaci贸n en cada campo solicitado al momento de registrar un nuevo portafolio.

### Este proyecto web permite la creaci贸n de varios usuarios, donde cada uno puede a帽adir m谩s portafolios a la galer铆a principal.  

### En la galer铆a de portafolios se muestra cada portafolio con los siguientes campos: T铆tulo, descripci贸n, Foto, Url, tags y tambien el nombre del usario que cre贸 el portafolio.

### Link del repositorio:
  https://github.com/e-orosco/U4Portafolio 



# veamos el proyecto  馃捇

### Pasos para poder correr el proyecto:
### Clonar el repositorio en tu terminal.
    git clone git@github.com:e-orosco/U4Portafolio.git


### Dentro de nuestra carpeta creamos nuestro entorno virtual
    python3.10 -m venv e-env

### Entramos al entorno virtual
    source e-env/bin/activate 

### Instalamos los requerimientos
    pip install -r requirements.txt

### Us茅 mysql como base de datos con la siguiente configuraciones:
DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'portafolio',
        'USER':'usurario',
        'PASSWORD':'contrase帽aDelUsuario',
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

### Link de proyecto desplegado en railway:
https://portafoliopersonal-production.up.railway.app/

    
