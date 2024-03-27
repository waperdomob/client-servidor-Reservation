# client-servidor-Reservation

Este es un sistema de reserva simple desarrollado en Python utilizando sockets. Permite a los clientes conectarse a un servidor y realizar reservas y cancelaciones de recursos.

## Funcionamiento
El sistema consta de dos componentes principales: el servidor y el cliente.

## Servidor
El servidor mantiene una lista de recursos disponibles (en este ejemplo, habitaciones de hotel). Cuando se inicia, crea un socket y espera conexiones entrantes de clientes.

Cuando un cliente se conecta, el servidor crea un nuevo hilo para manejar las solicitudes del cliente. El cliente puede enviar los siguientes comandos:

- **RESERVAR <recurso>** : Si el recurso está disponible, se elimina de la lista y se notifica al cliente.
- **CANCELAR <recurso>**: Si el recurso estaba reservado, se agrega de nuevo a la lista y se notifica al cliente.
- **LISTAR**: Se envía al cliente la lista de recursos disponibles.

El servidor mantiene actualizada la lista de recursos disponibles en todo momento.

## Cliente
El cliente se conecta al servidor y puede enviar comandos para realizar reservas, cancelaciones o listar los recursos disponibles.

Cuando el cliente envía un comando, el servidor responde con un mensaje indicando el resultado de la operación.

# Instrucciones de ejecución

Sigue estos pasos para ejecutar la aplicación:

## Iniciar el servidor:

Abre una terminal o línea de comandos.  
Navega hasta el directorio donde se encuentra el archivo servidor.py.  
Ejecuta el siguiente comando: python servidor.py  
El servidor se iniciará y mostrará un mensaje indicando que está escuchando en el host y puerto correspondientes.  
## Iniciar el cliente:

Abre otra terminal o línea de comandos.  
Navega hasta el directorio donde se encuentra el archivo cliente.py.  
Ejecuta el siguiente comando: python cliente.py  
El cliente se conectará al servidor y mostrará un mensaje indicando que se ha conectado correctamente.  

## Enviar comandos desde el cliente:

En la terminal del cliente, ingresa uno de los siguientes comandos:  
RESERVAR Habitación 1: Realiza una reserva de un recurso disponible.  
CANCELAR Habitación 1: Cancela una reserva existente.  
LISTAR: Muestra la lista de recursos disponibles.  
SALIR: Cierra la conexión con el servidor y termina el cliente.  
El servidor responderá con un mensaje indicando el resultado de la operación.  

Puedes ejecutar múltiples instancias del cliente y realizar reservas y cancelaciones simultáneamente. El servidor mantendrá actualizada la lista de recursos disponibles.