from selenium import webdriver
import time
import os
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service

token_api = "m4LTg1VWn0rcmn6TR0mkVbYpIUpVY7MO"

dir_path = os.getcwd()
edge_options2 = Options()
edge_options2.add_argument(f"user-data-dir={dir_path}/profile/zap")

# Caminho correto do Edge WebDriver
driver_path = os.path.join(dir_path, "PYTHON", "Chat", "msedgedriver.exe")
print(driver_path)

# Criando o serviço com o caminho do driver
service = Service(driver_path)
driver = webdriver.Edge(service=service, options=edge_options2)

# Acessando o WhatsApp Web
driver.get("https://web.whatsapp.com/")
time.sleep(120)
