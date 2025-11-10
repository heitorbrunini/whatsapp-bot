from PyQt5.QtCore import QThread, pyqtSignal
from selenium import webdriver
import time
import pandas as pd
import os
import requests

from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from bot.scripts.application_bot import enviar_mensagem, capturar_contato, capturar_mensagem, busca_notificacao, obter_resposta_llm

class BotWorker(QThread):
    nova_mensagem_log = pyqtSignal(str)
    novo_pedido = pyqtSignal(str, str)
    
    def __init__(self):
        super().__init__()
        self.running = True
        self.driver = None
        self._iniciou_navegador = False

    def run(self):
        conversas = {}
        ultima_mensagem_enviada = {}
        ultima_mensagem_recebida = {}
        self.iniciar_navegador()
        self.nova_mensagem_log.emit("[BOT] Executando ciclo de verificação...")
        while True:
            if not self.running:
                time.sleep(1)
                continue
            try:
                if busca_notificacao(self.driver, self.BOLINHA_NOTIFICA):
                    telefone = capturar_contato(driver=self.driver)
                    mensagem = capturar_mensagem(driver=self.driver)

                    if telefone not in conversas:
                        conversas[telefone] = []
                        ultima_mensagem_enviada[telefone] = ""
                        ultima_mensagem_recebida[telefone] = ""

                    if mensagem == ultima_mensagem_recebida[telefone]:
                        time.sleep(2)
                        continue

                    self.nova_mensagem_log.emit(f"[LOG] Telefone: {telefone}")
                    self.nova_mensagem_log.emit(f"[LOG] Mensagem: {mensagem}")

                    resposta = obter_resposta_llm(mensagem, model_name='pizzaria_gemma:latest', conversation_history=conversas[telefone])
                    
                    print(f"[LOG] Resposta: {resposta}")
                    if resposta.startswith("GERAR_JSON"):
                        # Se a resposta for um comando para gerar JSON exporta um arquivo
                        json_data = resposta.split("GERAR_JSON:")[1].strip()
                        with open(f"{os.getcwd()}/bot/resources/response.json", "w") as json_file:
                            json_file.write(json_data)
                            
                        #TODO: Chamar a api aqui para enviar o JSON
                        self.nova_mensagem_log.emit("[INFO] Arquivo JSON gerado com sucesso!")
                        self.novo_pedido.emit("004", "Lasanha 4 Queijos, Guaraná 1L")
                        enviar_mensagem("Pedido registrado com sucesso! Em breve entraremos em contato com o status.",driver=self.driver)
                    else:                
                        self.nova_mensagem_log.emit(f"[LOG] Resposta: {resposta}")
                        enviar_mensagem(resposta, driver=self.driver)

                    ultima_mensagem_recebida[telefone] = mensagem
                    ultima_mensagem_enviada[telefone] = resposta      

                    time.sleep(5)
                else:
                    self.nova_mensagem_log.emit("[LOG] Aguardando novas notificações...")
                    time.sleep(5)

            except Exception as e:
                self.nova_mensagem_log.emit("[LOG] carregamento...")
                print(f"Ocorreu um erro: {e.args[0]}")
                time.sleep(5)
    
        
    def close_driver(self): 
        if self.driver:
            self.driver.quit()
            self.nova_mensagem_log.emit("[INFO] Navegador fechado.")
        
    def iniciar_navegador(self):
        # Configuração do agente e token da API
        if not self._iniciou_navegador:
            agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
            token_api = "Ezm597rhhnUH0zcnBhk772z1MZqhqgNC"

            api = requests.get(f"https://editacodigo.com.br/index/api-whatsapp/{token_api}", headers=agent).text
            api = api.split('.n.')
            self.BOLINHA_NOTIFICA = api[3].strip()
            self.CONT_CX_MSG = api[5].strip()
            self.MSG_CLIENTE = api[6].strip()

            # WebDriver
            self.dir_path = os.getcwd()
            edge_options = Options()
            edge_options.add_argument(f"user-data-dir={self.dir_path}/profile/zap")

            driver_path = os.path.join(self.dir_path, "msedgedriver.exe")
            service = Service(driver_path)

            self.driver = webdriver.Edge(service=service, options=edge_options)
            self.driver.get("https://web.whatsapp.com/")
            time.sleep(4)
            
            self._iniciou_navegador = True
            self.nova_mensagem_log.emit("[INFO] Navegador iniciado.")

            # Carregamento do CSV
            self.df = pd.read_csv(f"{self.dir_path}/bot/resources/msg.csv", sep=";", header=None, names=["ID", "Mensagem"])
            self.df["ID"] = self.df["ID"].astype(int)
    
    def start_bot_loop(self):
        self.running = True
        self.nova_mensagem_log.emit("[BOT] Bot ativado.")

    def stop_bot_loop(self):
        self.running = False
        self.nova_mensagem_log.emit("[BOT] Bot pausado.")
