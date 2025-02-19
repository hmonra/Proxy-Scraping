# Librerias
import subprocess
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from datetime import datetime
from selenium.common.exceptions import TimeoutException, WebDriverException
from enlace import enlace_principal
from scrap1 import driver
from scrap1 import summary_item
from scrap1 import hora_inicial


# Para enviar mensaje de aviso por telegram
def telegram_bot_sendtext(bot_message):
    bot_token = 'BOT_TOKEN' # AÑADIR TOKEN DEL BOT
    bot_chatID = 'CHAT_ID' # AÑADIR ID DEL CHAT
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    driver.get(send_text)


def comprar():
    nombre_producto = WebDriverWait(driver, 30) \
        .until(EC.element_to_be_clickable((By.CLASS_NAME, 'enlace-disimulado')))
    nombre_producto = nombre_producto.text
    print(nombre_producto)

    print("Paso a pestaña summary...")
    driver.switch_to.window(driver.window_handles[1])
    # Botón pagar y finalizar
    print("Pulsando botón de pagar y finalizar...")
    WebDriverWait(driver, 60) \
        .until(
        EC.visibility_of and EC.element_to_be_clickable((By.CLASS_NAME, 'sc-iqHYmW.cfUOyE.sc-jacqCo.cJDOwR'))).click()
    print("Pulsado botón de pagar y finalizar...")
    payment_time = datetime.now().time()
    time.sleep(60)
    if driver.current_url == 'https://www.pccomponentes.com/cart/':
        telegram_bot_sendtext("*BOT 1 - ❌ Intento de compra realizado, sin stock ❌* ``` ```" + nombre_producto)
        print("Compra no realizada, el stock ha volado... :(")
    else:
        if driver.current_url == 'https://www.pccomponentes.com/cart/summary':
            telegram_bot_sendtext("*BOT 1 - ❌ Intento de compra realizado ❌* ``` ```" + nombre_producto)
            print("Compra no realizada, algo ha fallado... :(")
        else:
            telegram_bot_sendtext("*BOT 1 - ✅ Compra realizada ✅* ``` ```" + nombre_producto)
            print("Compra finalizada :D    ", payment_time)


def login():
    # Borrando cookies
    driver.delete_all_cookies()
    print("Borrando todas las cookies...")
    # Accediendo a web para login
    print("Accediendo a página para hacer login...")
    driver.get('https://www.pccomponentes.com/login')
    time.sleep(1)
    if driver.current_url == 'https://www.pccomponentes.com/login':
        # Se hace login
        print("Introduciendo credenciales...")
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#username'))).send_keys('USUARIO') # AÑADIR USUARIO
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#password'))).send_keys('CONTRASEÑA') # AÑADIR CONTRASEÑA
        time.sleep(1)
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.CLASS_NAME, 'sc-iqHYmW.kaLStl'))).click()
        print("Login en PCC OK...")
        time.sleep(1)
        cuadro_verificacion = WebDriverWait(driver, 5) \
            .until(EC.visibility_of_element_located and EC.element_to_be_clickable((By.ID, 'login-form')))
        cuadro_verificacion = cuadro_verificacion.text
        # print(cuadro_verificacion)
        if "El e-mail o la contraseña no son correctos." in cuadro_verificacion:
            print("Problema con verificación de login, reintentando...")
            login()
        else:
            print("Login confirmado...")

    else:
        print("Falso positivo, la cuenta sigue logueada...")


def summary():
    print("Login para precargar página summary...")
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
    login()
    time.sleep(2)
    print("Añado un producto para poder acceder al enlace summary...")
    driver.get(summary_item)
    time.sleep(1)
    print(summary_item)
    print("Cambio pestaña y accedo a enlace summary...")
    driver.switch_to.window(driver.window_handles[1])
    driver.get('https://www.pccomponentes.com/cart/summary')
    time.sleep(2)
    # Botón entiendo y acepto las condiciones
    print("Cargada página summary...")
    print("Dejo pulsado botón de acepto las condiciones...")
    WebDriverWait(driver, 60) \
        .until(EC.visibility_of and EC.element_to_be_clickable((By.CLASS_NAME, 'sc-fWPcWZ.dGKYTO'))).click()
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[0])
    print("Vacío el carrito...")
    WebDriverWait(driver, 60) \
        .until(EC.visibility_of and EC.element_to_be_clickable((By.ID, 'GTM-carrito-vaciarcarrito'))).click()
    time.sleep(1)


def bucle10():
    while True:
        try:
            driver.switch_to.window(driver.window_handles[0])
            driver.get('https://www.pccomponentes.com/premium')
            if driver.current_url == 'https://www.pccomponentes.com/premium':
                cuadro_login = WebDriverWait(driver, 15) \
                    .until(EC.visibility_of_element_located and EC.element_to_be_clickable(
                    (By.CLASS_NAME, 'c-user-menu.js-user-menu')))
                cuadro_login = cuadro_login.text
                if "USUARIO@" not in cuadro_login: # CAMBIAR POR USUARIO AÑADIENDO UNA '@' AL FINAL
                    print("Detectado cierre automático de sesión, volviendo a loguear...")
                    login()
                else:
                    print("--Sesión OK--")
        except TimeoutException or WebDriverException:
            print("")
            print("Url Time out..")
            print("URL: https://www.pccomponentes.com/premium")
            driver.delete_all_cookies()
            print("Borrando todas las cookies...")
            print("Volviendo a escanear...")
            print("")
            driver.switch_to.window(driver.window_handles[0])
            driver.refresh()
            continue
        except WebDriverException:
            print("")
            print("Url Time out..")
            print("URL: https://www.pccomponentes.com/premium")
            driver.delete_all_cookies()
            print("Borrando todas las cookies...")
            print("Volviendo a escanear...")
            print("")
            driver.switch_to.window(driver.window_handles[0])
            driver.refresh()
            continue

        try:
            driver.switch_to.window(driver.window_handles[1])
            if driver.current_url == 'https://www.pccomponentes.com/cart/summary':
                print("--Página summary OK--")
            else:
                print("--Perdida página summary, creando de nuevo--")
                summary()
            driver.switch_to.window(driver.window_handles[2])
            current_time = datetime.now().time()
            driver.get(enlace_principal)
            cuadro_cesta = WebDriverWait(driver, 15) \
                .until(EC.element_to_be_clickable((By.CLASS_NAME, 'h3.m-b-1')))
            cuadro_cesta = cuadro_cesta.text
            print(cuadro_cesta)
            if "0" not in cuadro_cesta:
                print("#########                  #########")
                print("######### STOCK ENCONTRADO #########")
                print("####", cuadro_cesta, "######")
                print("#########                  #########")
                comprar()
                summary()
            else:
                print("INSTANCIA 1 - 🔴 Ninguna gráfica en stock...      Hora:", current_time)
                print("Script corriendo desde: ", hora_inicial)
                driver.minimize_window()
                # subprocess.call("bucle9.py", shell=True)
                subprocess.call("bucle10.py", shell=True)
        except TimeoutException:
            print("")
            print("Url Time out..")
            print("URL: https://www.pccomponentes.com/lista-de-deseos/carrito/DfmMgileJWohRk")
            driver.delete_all_cookies()
            print("Borrando todas las cookies...")
            print("Volviendo a escanear...")
            print("")
            driver.switch_to.window(driver.window_handles[0])
            driver.back()
            driver.refresh()
            continue
        except WebDriverException:
            print("")
            print("Url Time out..")
            print("URL: https://www.pccomponentes.com/lista-de-deseos/carrito/DfmMgileJWohRk")
            driver.delete_all_cookies()
            print("Borrando todas las cookies...")
            print("Volviendo a escanear...")
            print("")
            driver.switch_to.window(driver.window_handles[0])
            driver.back()
            driver.refresh()
            continue