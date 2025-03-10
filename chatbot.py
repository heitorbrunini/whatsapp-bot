from selenium import webdriver
import time
import os
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import requests



token_api = "m4LTg1VWn0rcmn6TR0mkVbYpIUpVY7MO"

dir_path = os.getcwd()
print ("path: " + dir_path)
edge_options2 = Options()
edge_options2.add_argument(f"user-data-dir={dir_path}/PYTHON/whatsapp-bot/profile/zap")

# Caminho correto do Edge WebDriver
driver_path = os.path.join(dir_path, "PYTHON", "whatsapp-bot", "msedgedriver.exe")
print(driver_path)

# Criando o serviço com o caminho do driver
service = Service(driver_path)
driver = webdriver.Edge(service=service, options=edge_options2)

# Acessando o WhatsApp Web
driver.get("https://web.whatsapp.com/")

agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
classname =  "x1rg5ohu x173ssrc x1xaadd7 x682dto x1e01kqd x12j7j87 x9bpaai x1pg5gke x1s688f xo5v014 x1u28eo4 x2b8uid x16dsc37 x18ba5f9 x1sbl2l xy9co9w x5r174s x7h3shv"
### uso da API


#x1rg5ohu x173ssrc x1xaadd7 x682dto x1e01kqd x12j7j87 x9bpaai x1pg5gke x1s688f xo5v014 x1u28eo4 x2b8uid x16dsc37 x18ba5f9 x1sbl2l xy9co9w x5r174s x7h3shv
time.sleep(60)

def bot():

    #busca de todas notificações
    bolinha = driver.find_elements(By.CLASS_NAME, "x7h3shv")

    #local da notificação mais recente
    clica_bolinha = bolinha[-1]

    clic_action = webdriver.common.action_chains.ActionChains(driver)

    #mover mouse para o lado, já que o botão de notificação fica do lado quando aparece o dropdown de opções
    clic_action.move_to_element_with_offset(clica_bolinha, 0, -20)

    #clique e confirmação da ação
    clic_action.click()
    clic_action.perform()

    '''
    api = requests.get(f"https://editacodigo.com.br/index/api-whatsapp/{token_api}", headers=agent)
    api = api.text

    api = api.split('.n.')
    bolinha_notificacao = api[3].strip()
    contcaixa_msg = api[5].strip()
    msg_cliente = api[6].strip()

    print (f"bolinha: {bolinha_notificacao}")
    '''

    print(bolinha)
    time.sleep(120)

bot()