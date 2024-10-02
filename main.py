from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# Defina o caminho onde deseja salvar o arquivo
download_directory = os.path.join(os.getcwd(), 'downloads') 

# Configurar opções do Chrome para download automático
chrome_options = Options()
prefs = {
    "download.default_directory": download_directory,  # Definir diretório de download
    "download.prompt_for_download": False,  # Desabilitar prompt de download
    "directory_upgrade": True,  # Para evitar avisos de permissão ao baixar
    "safebrowsing.enabled": True  # Para evitar avisos de segurança ao baixar
}
chrome_options.add_experimental_option("prefs", prefs)

# Inicializar o serviço e o WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Acessar a URL desejada
url = 'https://sistemaswebb3-listados.b3.com.br/indexPage/day/ibov?language=pt-br'
driver.get(url)

# Aguarde um tempo para garantir que a página carregue completamente
time.sleep(5)

# Localizar o botão de download
download_button = driver.find_elements(By.TAG_NAME, 'a')[5]

# Clicar no botão de download
download_button.click()

# Espera um tempo para garantir o download
time.sleep(10) 

driver.quit()

print(f"Arquivo salvo em: {download_directory}")
