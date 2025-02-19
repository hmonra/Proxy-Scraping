<h1 align="center"> Multi-threaded Web Scraper with Selenium and Proxies ️‍♀️</h1>

<p align="center">Automate product purchases on PCComponentes using multiple threads, Selenium, and proxies. Maximize speed and bypass blocks!</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9-blue?style=for-the-badge&logo=python&logoColor=yellow" alt="Python 3.9">
  <img src="https://img.shields.io/badge/Selenium-4.10.0-green?style=for-the-badge&logo=selenium&logoColor=white" alt="Selenium 4.10.0">
  <img src="https://img.shields.io/badge/Telegram-Bot-blue?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram Bot">
</p>

## ⚡️ Key Features

*   **Multi-threading:** Run multiple threads to boost scraping speed.
*   **Selenium WebDriver:** Automate web page interactions.
*   **Proxy Management:** Bypass blocks using proxies.
*   **Real-time Notifications:** Get stock and purchase status alerts via Telegram.
*   **Automated Purchase:** Streamlined buying process once stock is detected.
*   **Session Handling:** Automatic login detection and retry.
*   **Multiple Windows:** Support for multiple browser windows.

## ⚙️ Project Structure

Web Scraper Project/

├── main.py        # Main script

├── bucle1.py      # Scraper loop 1

├── scrap1.py      # Driver config 1

├── ...            # Similar files for loops and scrapers 2-10

├── enlace.py      # Target links

└── requirements.txt # Dependencies

## ️ Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/hmonra/Proxy-Scraping.git](https://github.com/hmonra/Proxy-Scraping.git)
    ```

2.  **Virtual environment (optional):**

    ```bash
    python -m venv env
    source env/bin/activate  # Linux/macOS
    env\Scripts\activate     # Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Chromedriver:** Ensure Chromedriver is in your PATH or specified in the code.

## ▶️ Usage

1.  **Configure credentials:** Edit `scrap10.py` with your PCComponentes login details.
2.  **Run the script:**

    ```bash
    python main.py
    ```

3.  **Monitoring:** The scraper will search for the product and attempt automatic purchase if stock is found.

## Telegram Notifications

*   **Real-time alerts:** Products found, purchase attempts, connection issues, etc.
*   **Setup:** Create your own Telegram bot and replace `bot_token` and `bot_chatID` in the code.

## Dependencies

*   `selenium`
*   `webdriver-manager`
*   `pyautogui`

## ⚠️ Disclaimer

*   This project is for educational purposes only.
*   Scraping might violate terms of service. Use responsibly!

## Contributions

Contributions are welcome! Feel free to fork and submit pull requests.

## License

MIT License. See the `LICENSE` file for details.

## Contact

Developed by [@hmonra](https://github.com/hmonra). Don't hesitate to reach out with questions or suggestions!

<p align="center"> Give the repo a ⭐ if you found it helpful! </p>
