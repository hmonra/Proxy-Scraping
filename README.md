🚀 Web Scraper Multihilo con Selenium y Proxies 🕵️‍♀️

📌 Descripción

Este proyecto es un Web Scraper diseñado para automatizar la compra de productos en la web de PCComponentes. Utiliza múltiples hilos, Selenium WebDriver y proxies para maximizar la velocidad y evitar bloqueos por parte del sitio web.

⚡️ Características

✅ Uso de Selenium para interacción web automatizada.✅ Gestión automática de cookies y sesiones.✅ Soporte para múltiples ventanas del navegador.✅ Envío de notificaciones a Telegram en tiempo real.✅ Detección automática de cierre de sesión y reintento de login.✅ Sistema de compra automatizada en caso de encontrar stock.

🏗️ Estructura del Proyecto

📦 Web Scraper Project
│
├── 📄 main.py           # Script principal que ejecuta los bucles del scraper (1 para cada proxy)
├── 📄 bucle1.py         # Bucle del scraper 1
├── 📄 scrap1.py         # Configuración del driver y opciones del navegador 1
├── 📄 bucle2.py         # Bucle del scraper 2
├── 📄 scrap2.py         # Configuración del driver y opciones del navegador 2
├── 📄 bucle3.py         # Bucle del scraper 3
├── 📄 scrap3.py         # Configuración del driver y opciones del navegador 3
├── 📄 bucle4.py         # Bucle del scraper 4
├── 📄 scrap4.py         # Configuración del driver y opciones del navegador 4
├── 📄 bucle5.py         # Bucle del scraper 5
├── 📄 scrap5.py         # Configuración del driver y opciones del navegador 5
├── 📄 bucle6.py         # Bucle del scraper 6
├── 📄 scrap6.py         # Configuración del driver y opciones del navegador 6
├── 📄 bucle7.py         # Bucle del scraper 7
├── 📄 scrap7.py         # Configuración del driver y opciones del navegador 7
├── 📄 bucle8.py         # Bucle del scraper 8
├── 📄 scrap8.py         # Configuración del driver y opciones del navegador 8
├── 📄 bucle9.py         # Bucle del scraper 9
├── 📄 scrap9.py         # Configuración del driver y opciones del navegador 9
├── 📄 bucle10.py        # Bucle del scraper 10
├── 📄 scrap10.py        # Configuración del driver y opciones del navegador 10
├── 📄 enlace.py         # Contiene los enlaces objetivo
├── 📄 requirements.txt  # Dependencias del proyecto
├── 📄 README.md         # Este archivo 😎

🔧 Instalación

1️⃣ Clona este repositorio:

git clone https://github.com/hmonra/Proxy-Scraping.git

2️⃣ Crea un entorno virtual (opcional pero recomendado):

python -m venv env
source env/bin/activate  # Linux/MacOS
env\Scripts\activate     # Windows

3️⃣ Instala las dependencias:

pip install -r requirements.txt

4️⃣ Asegúrate de tener el chromedriver en tu PATH o especificado en el código.

▶️ Uso

1️⃣ Configura tus credenciales de PCComponentes en scrap10.py.2️⃣ Ejecuta el script principal:

python main.py

3️⃣ El scraper comenzará a escanear el stock del producto deseado y, en caso de encontrarlo, iniciará el proceso de compra automática.

📲 Notificaciones por Telegram

✅ El bot está configurado para enviarte actualizaciones en tiempo real sobre:

Productos encontrados.

Intentos de compra exitosos o fallidos.

Problemas de conexión o cierre de sesión.

💬 Configura tu propio bot de Telegram y reemplaza el bot_token y bot_chatID en el código.

📜 Archivo requirements.txt

selenium
webdriver-manager
pyautogui

🚨 Advertencia

⚠️ Este proyecto está diseñado solo con fines educativos. El scraping de sitios web puede violar sus términos de servicio, ¡úsalo con responsabilidad!

🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar este scraper, no dudes en hacer un fork del proyecto y enviar un pull request.

📈 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

📧 Contacto

✨ Desarrollado por @hmonra.📬 Si tienes alguna pregunta o sugerencia, ¡no dudes en contactarme!

🌟 ¡Dale una ⭐ al repo si te ha sido útil!

