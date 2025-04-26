# PROYECTO SPRINT 8 QA ENGINEER BOOTCAMP
Este proyecto busca poner en práactica lo aprendido en el Sprint 8 
del Bootcamp QA Engineer, mediante la automatizacion de pruebas para 
una aplicación web.

## Introducción
El código de este proyecto contiene pruebas para probar la funcionalidad
de la aplicación dada por TripleTen, Urban Routes, donde se realizan
los pasos necesarios para solicitar un taxi.

## Pre-requisitos
Para este proyecto, se necesita la instalación de las librerías Selenium y
Pytest.

## Estructura del proyecto
### **Archivos usados:**
`data.py:` Contiene URL y las variables que serán importadas para
la clase UrbanRoutesPage y a su vez utilizadas en las pruebas.

`utils.py:` Contiene el método retrieve_pone_code que luego será
importado y utilizado en UrbanRoutesPage.

`main.py:`
- Clase UrbanRoutesPage:
  - Aqui se encuentran los localizadores de cada elemento de la web
y los métodos que interactúan con ellos. 

- Clase TestUrbanRoutes:
  - Aquí se encuentran las pruebas para hacer la solicitud del taxi 
con sus respectivos 'assert'. A continuación una breve descripción 
de las mismas.
  
**1. test_set_route:** Define la ruta, rellenando los campos 'Desde'
y 'Hasta'

**2. test_select_comfort_fare:** Selecciona el botón de pedir taxi y 
selecciona la tarifa 'Comfort'

**3. test_phone_number:** Rellena el campo de número de teléfono,
así como su respectivo código de confirmación.

**4. test_add_credit_card:** Realiza el proceso para agregar una tarjeta
de crédito como método de pago

**5. test_message_driver:** Escribe un mensaje para el conductor

**6. test_request_blanket_and_tissues:** Selecciona la opción para
agregar una manta y pañuelos al pedido

**7. test_ice_cream_counter:** Agrega 2 helados al pedido

**8. test_final_request_taxi_button:** Solicita al sitio web la
búsqueda de un taxi

**9. test_driver_information:** Muestra la información del conductor

## Tecnologías utilizadas
`Selenium` `Pycharm` `Git` `Github` `DevTools`

## Técnicas utilizadas
  - Creación de archivos
  - Instalación e importación de librerías
  - Importación de datos entre archivos
  - Creación de clases
  - Creación de localizadores.
  - Creación y aplicación de métodos de selenium
  - Creación de pruebas
  - Creación de asserts.
  - Control de versiones con Git (Clonar, Fusionar, Actualización, Extracción).
Navegación en ramificaciones Git.

## Contacto
**Discord:** ale016489

**Link del proyecto:**  


*Muchas gracias por leer :)*

  

