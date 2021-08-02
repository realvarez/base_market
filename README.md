# base_market

Este proyecto es un proyecto simple de back end en lo que sería un negocio en flask

Para ejecutarlo se debe existir una base de datos postgress y se debe crear un archivo que contendrá la configuración de la base de datos, este debe llevar por nombre "db-secret" y su contenido debe ser

[secrets] <br>
host= <br> 
port= <br>
user= <br>
password= <br>
dbname= <br>

Para crear la base de datos necesaria se debe ejecutar:<br>

1. Inicialización del proyecto <br>
   `flask init`  <br>
2. Creación de las migraciones <br>
   `flask db migrate` <br>
3. Ejecución de cambios en DB <br>
   `flask db upgrade`
   
