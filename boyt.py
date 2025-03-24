# Step 1: Importando as bibliotecas necessárias
from selenium import webdriver
import time
import pandas as pd

from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys

import os

# Step 2: Configurando o WebDriver
# diretório atual do terminal
dir_path = os.getcwd()
print ("path: " + dir_path)
edge_options2 = Options()
edge_options2.add_argument(f"user-data-dir={dir_path}/profile/zap")

# Caminho correto do Edge WebDriver
driver_path = os.path.join(dir_path, "msedgedriver.exe")

# Criando o serviço com o caminho do driver
service = Service(driver_path)
driver = webdriver.Edge(service=service, options=edge_options2)

#Lendo o arquivo de respostas
df = pd.read_csv('msg.csv', sep=';', header=None, names=['ID', 'Mensagem'])
# Converter a coluna ID para int (caso venha como string)
df['ID'] = df['ID'].astype(int)

# Step 3: Acessando o WhatsApp Web
driver.get("https://web.whatsapp.com/")

# Step 4: Mantendo o navegador aberto por 30 segundos
time.sleep(30)

def busca_notificação():
    try: 
        #busca de todas notificações
        bolinha = driver.find_elements(By.CLASS_NAME, "x7h3shv")

        #local da notificação mais recente
        clica_bolinha = bolinha[-1]
        clic_action = webdriver.common.action_chains.ActionChains(driver)

        #mover mouse para o lado, já que o botão de notificação fica do lado quando aparece o dropdown de opções
        clic_action.move_to_element_with_offset(clica_bolinha, 0, -20)

        time.sleep(3)
    except Exception as e:
        print("sem notificação")

def capturar_contato():
    #pegar telefone
    time.sleep(1)
    telefone = driver.find_element(By.XPATH, '//*[@id="main"]/header/div[2]/div/div/div/span')
    #Não funciona com grupos!
    time.sleep(1)
    return telefone.text

def capturar_mensagem():
    #pegar mensagem
    mensagem = driver.find_elements(By.CLASS_NAME, '_akbu')
    # todas_mensagens = [e.text for e in mensagem]
    return mensagem[-1].text

def enviar_mensagem(response):
    #buscando campo de resposta
    campo_resposta = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p')
    campo_resposta.click()
    time.sleep(1)

    #digitando e enviando a resposta
    campo_resposta.send_keys(response, Keys.ENTER)
    time.sleep(1)

    #voltar para a tela de conversa
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

def obter_resposta(id_mensagem):
    #Retorna a mensagem correspondente ao ID fornecido.
    
    #Filtra a linha correspondente ao ID e pega a coluna 'Mensagem'
    resposta = df[df['ID'] == id_mensagem]['Mensagem']
    return resposta.iloc[0] if not resposta.empty else "Desculpe, não encontrei essa mensagem."


while True:
    try:
        busca_notificação()
        print("telefone: "+ capturar_contato())
        print("mensagem: "+ capturar_mensagem())
        enviar_mensagem("Olá, tudo bem? sou um bot desenvolvido em Python!")
        time.sleep(5)
    except KeyboardInterrupt as e:
        print("Fim do programa")
        driver.quit()
        exit()