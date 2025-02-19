🚀 Multithreaded Web Scraper with Selenium and Proxies 🕵️‍♀️

📌 Description

This project is a Web Scraper designed to automate product purchases on the PCComponentes website. It uses multiple threads, Selenium WebDriver, and proxies to maximize speed and avoid being blocked by the website.

⚡️ Features

✅ Uses Selenium for automated web interaction.
✅ Automatic management of cookies and sessions.
✅ Support for multiple browser windows.
✅ Real-time notifications to Telegram.
✅ Automatic logout detection and login retry.
✅ Automated purchase system when stock is found.

🏗️ Project Structure

📦 Web Scraper Project
│
├── 📄 main.py           # Main script that runs the scraper loops (1 for each proxy)
├── 📄 bucle1.py         # Scraper loop 1
├── 📄 scrap1.py         # Driver and browser configuration 1
├── 📄 bucle2.py         # Scraper loop 2
├── 📄 scrap2.py         # Driver and browser configuration 2
├── 📄 bucle3.py         # Scraper loop 3
├── 📄 scrap3.py         # Driver and browser configuration 3
├── 📄 bucle4.py         # Scraper loop 4
├── 📄 scrap4.py         # Driver and browser configuration 4
├── 📄 bucle5.py         # Scraper loop 5
├── 📄 scrap5.py         # Driver and browser configuration 5
├── 📄 bucle6.py         # Scraper loop 6
├── 📄 scrap6.py         # Driver and browser configuration 6
├── 📄 bucle7.py         # Scraper loop 7
├── 📄 scrap7.py         # Driver and browser configuration 7
├── 📄 bucle8.py         # Scraper loop 8
├── 📄 scrap8.py         # Driver and browser configuration 8
├── 📄 bucle9.py         # Scraper loop 9
├── 📄 scrap9.py         # Driver and browser configuration 9
├── 📄 bucle10.py        # Scraper loop 10
├── 📄 scrap10.py        # Driver and browser configuration 10
├── 📄 enlace.py         # Contains target links
├── 📄 requirements.txt  # Project dependencies
├── 📄 README.md         # This file 😎

🔧 Installation

1️⃣ Clone this repository:

git clone https://github.com/hmonra/Proxy-Scraping.git

2️⃣ Create a virtual environment (optional but recommended):

python -m venv env
source env/bin/activate  # Linux/MacOS
env\Scripts\activate     # Windows

3️⃣ Install dependencies:

pip install -r requirements.txt

4️⃣ Make sure you have chromedriver in your PATH or specified in the code.

▶️ Usage

1️⃣ Configure your PCComponentes credentials in scrap10.py.
2️⃣ Run the main script:

python main.py

3️⃣ The scraper will start scanning for product stock and, if found, will initiate the automated purchase process.

📲 Telegram Notifications

✅ The bot is set up to send you real-time updates about:

Products found.

Successful or failed purchase attempts.

Connection problems or logouts.

💬 Set up your own Telegram bot and replace bot_token and bot_chatID in the code.

📜 requirements.txt File

selenium
webdriver-manager
pyautogui

🚨 Warning

⚠️ This project is designed for educational purposes only. Scraping websites may violate their terms of service, use it responsibly!

🤝 Contributions

Contributions are welcome! If you want to improve this scraper, feel free to fork the project and submit a pull request.

📈 License

This project is under the MIT license. See the LICENSE file for more details.

📧 Contact

✨ Developed by @hmonra.
📬 If you have any questions or suggestions, feel free to contact me!

🌟 Give the repo a ⭐ if you found it useful!

