<h1 align="center"> Web Scraper Multihilo con Selenium y Proxies ️‍♀️</h1>

<p align="center">Automatiza la compra de productos en PCComponentes usando múltiples hilos, Selenium y proxies. ¡Maximiza la velocidad y evita bloqueos!</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9-blue?style=for-the-badge&logo=python&logoColor=yellow" alt="Python 3.9">
  <img src="https://img.shields.io/badge/Selenium-4.10.0-green?style=for-the-badge&logo=selenium&logoColor=white" alt="Selenium 4.10.0">
  <img src="https://img.shields.io/badge/Telegram-Bot-blue?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram Bot">
</p>

## ⚡️ Características Principales

*   **Multihilo:** Ejecuta múltiples hilos para aumentar la velocidad de scraping.
*   **Selenium WebDriver:** Automatiza la interacción con la página web.
*   **Gestión de Proxies:** Evita bloqueos utilizando proxies.
*   **Notificaciones en Tiempo Real:** Recibe alertas de stock y estado de la compra por Telegram.
*   **Compra Automática:** Proceso de compra automatizado una vez detectado el stock.
*   **Gestión de Sesiones:** Detección y reintento automático de inicio de sesión.
*   **Múltiples Ventanas:** Soporte para múltiples ventanas del navegador.

## ⚙️ Estructura del Proyecto

Web Scraper Project/
├── main.py        # Script principal
├── bucle1.py      # Bucle del scraper 1
├── scrap1.py      # Configuración del driver 1
├── ...            # Archivos similares para bucles y scrapers 2-10
├── enlace.py      # Enlaces objetivo
└── requirements.txt # Dependencias

## ️ Instalación

1.  **Clonar el repositorio:**

    ```bash
    git clone [https://github.com/hmonra/Proxy-Scraping.git](https://github.com/hmonra/Proxy-Scraping.git)
    ```

2.  **Entorno virtual (opcional):**

    ```bash
    python -m venv env
    source env/bin/activate  # Linux/macOS
    env\Scripts\activate     # Windows
    ```

3.  **Instalar dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Chromedriver:** Asegúrate de tener Chromedriver en tu PATH o especificado en el código.

## ▶️ Uso

1.  **Configurar credenciales:** Edita `scrap10.py` con tus credenciales de PCComponentes.
2.  **Ejecutar el script:**

    ```bash
    python main.py
    ```

3.  **Monitoreo:** El scraper buscará el producto y, si hay stock, intentará la compra automática.

##  Notificaciones por Telegram

*   **Alertas en tiempo real:** Productos encontrados, intentos de compra, problemas de conexión, etc.
*   **Configuración:** Crea tu propio bot de Telegram y reemplaza `bot_token` y `bot_chatID` en el código.

##  Dependencias

*   `selenium`
*   `webdriver-manager`
*   `pyautogui`

## ⚠️ Advertencia

*   Este proyecto es solo para fines educativos.
*   El scraping puede violar términos de servicio. ¡Úsalo con responsabilidad!

##  Contribuciones

¡Contribuciones son bienvenidas! Siéntete libre de hacer un fork y enviar pull requests.

##  Licencia

MIT License. Consulta el archivo `LICENSE` para detalles.

##  Contacto

Desarrollado por [@hmonra](https://github.com/hmonra). ¡No dudes en contactarme con preguntas o sugerencias!

<p align="center"> ¡Dale una ⭐ al repo si te ha sido útil! </p>
