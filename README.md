# Supreme-lamp

# Para crear e iniciar el contenedor en docker
docker compose up -d --build

# RECORDATORIO crear red si es que no esta creada
docker network create clbb

# IMPORTANTE para que pueda funcionar con las demas aplicaciones contenidas en el docker es necesario que el contenedor 
# este en la misma red de los otros contenedoress a los que se quieren conectar, por el ello el --network 'nombre contenedor'

# La aplicacion funciona como aplicacion web, donde se ingresa a la direccion IP del computador que este ejecutando la app
# Para abrir la página de los botones se coloca el ip del computador donde se levanta el server
ipv4:9090

# IMPORTANTE, cambiar todas las ip de las url de las funciones del index, y de la operacion get del main por el ipv4 del pc que se levanto el 
# server, manteniendo los puertos y lo que le sigue.
