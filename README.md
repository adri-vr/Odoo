# Guia de Despliegue de Odoo 17 en Render

Este documento detalla el proceso completo para desplegar un servidor Odoo 17 con un modulo personalizado utilizando Docker y PostgreSQL en la plataforma Render.

---

## 1. Preparacion de Archivos y Repositorio

Antes de configurar el servidor, es necesario preparar la estructura de archivos en el ordenador local y subirla a GitHub.

### Estructura de Carpetas
Crea una carpeta en tu ordenador con la siguiente estructura exacta. Es muy importante que la carpeta del modulo use guion bajo (`_`) y no guion medio.

```text
proyecto-odoo/
├── Dockerfile
└── extra-addons/
    └── dummy_module/
        ├── __init__.py
        └── __manifest__.py
```

## Contenido de los Archivos
Archivo: Dockerfile Crea un archivo sin extension llamado Dockerfile y pega el siguiente contenido:
```
FROM odoo:17
COPY ./extra-addons /mnt/extra-addons
EXPOSE 8069
ENV PGPORT=5432
CMD ["bash","-lc", "echo '==> Checking/initializing DB $PGDATABASE' && odoo -d $PGDATABASE -i base --without-demo=all --db_host=$PGHOST --db_port=$PGPORT --db_user=$PGUSER --db_password=$PGPASSWORD --addons-path=/usr/lib/python3/dist-packages/odoo/addons,/mnt/extra-addons --stop-after-init || true; echo '==> Starting Odoo server' && odoo --db_host=$PGHOST --db_port=$PGPORT --db_user=$PGUSER --db_password=$PGPASSWORD --addons-path=/usr/lib/python3/dist-packages/odoo/addons,/mnt/extra-addons --db-filter=$PGDATABASE --dev=all"]
```

## Archivo: extra-addons/dummy_module/manifest.py Crea este archivo dentro de las subcarpetas indicadas con el siguiente codigo:
```
{
    "name": "Dummy Module",
    "version": "1.0",
    "summary": "Modulo vacio de prueba",
    "installable": True,
}
```

## Archivo: extra-addons/dummy_module/__init.py__ Crea este archivo y dejalo vacio, pero asegúrate de que exista.

## Subida a GitHub
1. Inicia sesion en GitHub y crea un nuevo repositorio.

2. Selecciona la opcion de subir archivos existentes ("uploading an existing file").

3. Arrastra todos los archivos y carpetas creados anteriormente.

4. Confirma los cambios ("Commit changes").

## 2. Creacion de la Base de Datos (PostgreSQL)
  Odoo requiere una base de datos externa para funcionar.

1. Inicia sesion en Render.com.

2. En el panel de control (Dashboard), haz clic en "New" y selecciona "PostgreSQL".

## Rellena los datos:
Name: db-odoo

Region: Frankfurt (EU Central)

Instance Type: Free (Gratuito)

Haz clic en "Create Database".

## IMPORTANTE: Una vez creada, localiza la sección "Connections" y copia en un lugar seguro los siguientes datos (los necesitarás en el siguiente paso):

Internal Hostname, Username, Password, Database Name


## Creacion del Servicio Web (Odoo)
Este paso conecta el codigo de GitHub con la base de datos creada.

1. En el Dashboard de Render, haz clic en "New" y selecciona "Web Service".

2. Selecciona la opcion "Build and deploy from a Git repository".

3. Conecta el repositorio que creaste en el paso 1.

4. Configura los detalles del servicio:

  Name: mi-odoo-web
  
  Runtime: Docker (Es fundamental seleccionar Docker y no Python)
  
  Region: Frankfurt (Debe coincidir con la base de datos)
  
  Instance Type: Free

## Configuracion de Variables de Entorno
# Antes de finalizar, desplazate hacia abajo hasta la sección "Environment Variables". Debes añadir las siguientes 6 variables utilizando los datos copiados de la base de datos:

Clave       Valor 

PGHOST      (Pega aqui el Internal Hostname de tu base de datos)

PGPORT      5432

PGUSER      (Pega aqui el Username de tu base de datos)

PGPASSWORD  (Pega aqui el Password de tu base de datos)

PGDATABASE  (Pega aqui el Database Name de tu base de datos)

PORT        8069


5. Haz clic en "Create Web Service"

## Verificacion y Acceso
1. Espera a que Render complete el proceso de construcción (Build) y despliegue (Deploy). Puede tardar varios minutos.
2. Cuando el estado cambie a "Live", haz clic en la URL proporcionada por Render.
3. Deberias ver la pantalla de inicio de sesion de Odoo.
  Email: admin
  Password: admin
4. Para verificar el modulo personalizado:
  Ve al menu de "Aplicaciones".
  Elimina el filtro "Aplicaciones" de la barra de busqueda.
  Busca "Dummy".
  El modulo "Dummy Module" deberia aparecer listo para instalar.















