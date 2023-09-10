# Aplicación de Web Scraping con Selenium y Almacenamiento en MongoDB
Este proyecto es una aplicación de web scraping en Python que utiliza Selenium para extraer datos de sitios web y los almacena en una base de datos MongoDB. Esta aplicación es útil para recopilar información de sitios web de forma automática y almacenarla en una base de datos para su posterior análisis.
## Requisitos
Asegúrate de tener instalados los siguientes requisitos antes de ejecutar la aplicación:
- **Python 3.x:** [Descargar Python](https://www.python.org/downloads/)
- **Selenium:** Puedes instalarlo usando pip:
 `pip install selenium`
- **WebDriver:** Debes descargar el controlador específico del navegador que vas a utilizar con Selenium y asegurarte de que esté en tu PATH. Puedes encontrar los controladores en los siguientes enlaces:
  - [ChromeDriver](https://sites.google.com/chromium.org/driver/)
  - [GeckoDriver (Firefox)](https://github.com/mozilla/geckodriver)
  - [EdgeDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
- **MongoDB Atlas:** Debes tener una cuenta en MongoDB Atlas y configurar una base de datos. Obtén la URL de conexión de tu base de datos, que se utilizará para la conexión desde la aplicación.
- **PyMongo:** Instala la biblioteca PyMongo para interactuar con MongoDB Atlas:
  `pip install pymongo`
  
## Configuración
Antes de ejecutar la aplicación, configura los siguientes parámetros:
1. **URL del sitio web a scrappear:** Abre el archivo `main.py` y establece la URL del sitio web que deseas scrappear.
2. **Credenciales de MongoDB Atlas:** En el archivo `db.py`, proporciona la URL de conexión a tu base de datos en MongoDB Atlas y cualquier otra información de autenticación necesaria.

## Uso
Para ejecutar la aplicación, simplemente ejecuta el script `main.py`:
`python main.py`
La aplicación utilizará Selenium para acceder al sitio web, realizará el web scraping y almacenará los datos en la base de datos MongoDB Atlas configurada.

## Estructura del Proyecto
El proyecto está organizado de la siguiente manera:
- **main.py:** El script principal que realiza el web scraping y la extracción de datos utilizando Selenium.
- **db.py:** Contiene la lógica para conectarse a la base de datos MongoDB Atlas y almacenar los datos.
- **requirements.txt:** Un archivo que enumera las bibliotecas de Python necesarias para este proyecto. Puedes usarlo con pip para instalar las dependencias:
  `pip install -r requirements.txt`
## Contribución
Si deseas contribuir a este proyecto, siéntete libre de abrir un problema o enviar una solicitud de extracción (pull request) en el repositorio de GitHub.

## Licencia
Este proyecto se distribuye bajo la Licencia MIT. Consulta el archivo LICENSE para obtener más detalles.

¡Disfruta de tu experiencia de web scraping y almacenamiento en MongoDB Atlas con esta aplicación! Si tienes alguna pregunta o encuentras problemas, no dudes en ponerte en contacto.
