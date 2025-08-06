# Step 1: Importando as bibliotecas necessárias
from selenium import webdriver
import time
import pandas as pd
from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bot.scripts.model_requests import get_llm_response 
from selenium.webdriver.common.action_chains import ActionChains

def busca_notificacao(driver, BOLINHA_NOTIFICA):
    try: 
        #busca de todas notificações
        bolinha = driver.find_elements(By.CLASS_NAME, BOLINHA_NOTIFICA)

        #local da notificação mais recente
        clica_bolinha = bolinha[-1]
        clic_action = webdriver.common.action_chains.ActionChains(driver)

        #mover mouse para o lado, já que o botão de notificação fica do lado quando aparece o dropdown de opções
        clic_action.move_to_element_with_offset(clica_bolinha, 0, -20)

        #clique e confirmação da ação
        clic_action.click()
        clic_action.perform()
        print("Notificação encontrada e clicada")
        time.sleep(3)
        return True        
    except Exception as e:
        print("sem notificação")

def capturar_contato(driver):
    #pegar telefone
    time.sleep(1)
    telefone = driver.find_element(By.XPATH, '//*[@id="main"]/header/div[2]/div/div/div/div/span')
    #Não funciona com grupos!
    time.sleep(1)
    return telefone.text

def capturar_mensagem(driver):
    try:
        # Aguarda até que exista pelo menos uma mensagem recebida
        WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.message-in"))
        )

        mensagens_cliente = driver.find_elements(By.CSS_SELECTOR, "div.message-in")

        if not mensagens_cliente:
            return None

        ultima_mensagem = mensagens_cliente[-1]
        # Busca o texto dentro do último balão de mensagem recebida
        texto_elemento = ultima_mensagem.find_element(By.CSS_SELECTOR, "span.selectable-text")
        return texto_elemento.text
    except Exception as e:
        print("sem notificação")
        return None

def enviar_mensagem(response, driver):
    """
    Envia a mensagem, dividindo-a em partes para evitar erros com textos longos
    e localizando o campo de texto a cada envio para evitar o erro 'Stale Element Reference'.
    """
    
    action = ActionChains(driver)
    # Remove caracteres que não são suportados pelo WebDriver
    response_limpa = remover_caracteres_invalidos(response)
    
    # Divide a mensagem em partes de 500 caracteres
    partes = [response_limpa[i:i+500] for i in range(0, len(response_limpa), 500)]

    for i, parte in enumerate(partes):
        try:
            # Espera até que o campo de texto esteja visível e clicável
            campo_resposta = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div/div[3]/div[1]/p'
                ))
            )
            
            # Clica para garantir o foco e envia a parte da mensagem
            campo_resposta.click()
            time.sleep(0.2)  # Uma pequena pausa para garantir o foco
            campo_resposta.send_keys(parte)
            campo_resposta.send_keys(Keys.ENTER)
            
            # Espera um pouco para o WhatsApp processar o envio antes da próxima parte
            time.sleep(1)
        except Exception as e:
            print(f"[ERRO] Falha ao enviar parte {i+1}: {e}")
    action.send_keys(Keys.ENTER)
    action.send_keys(Keys.ESCAPE).perform()
    

def obter_resposta(id_mensagem, df):
    #Retorna a mensagem correspondente ao ID fornecido.
    #Filtra a linha correspondente ao ID e pega a coluna 'Mensagem'
    resposta = df[df['ID'] == id_mensagem]['Mensagem']
    return resposta.iloc[0] if not resposta.empty else "Desculpe, não encontrei essa mensagem."

def obter_resposta_llm(mensagem , model_name='pizzaria_gemma:latest', conversation_history=[]):
    #Retorna a mensagem gerada pelo modelo LLM com base na mensagem fornecida.
    return get_llm_response(mensagem, model_name=model_name, conversation_history=conversation_history)

def salvar_contato(numero, dir_path):
    arquivo = f"{dir_path}/bot/resources/ctt.csv"

    # Ler o CSV
    df = pd.read_csv(arquivo, sep=";")
    
    # Verificar se o número já está cadastrado
    if numero in df["Numero"].values:
        print("Numero já cadastrado!")
        return
    
    # Gerar um novo ID (incremental)
    novo_id = df["ID"].max() + 1 if not df.empty else 1
    
    # Criar um novo DataFrame com o contato
    novo_contato = pd.DataFrame([[novo_id, numero]], columns=["ID", "Numero"])
    
    # Adicionar ao arquivo CSV
    novo_contato.to_csv(arquivo, mode="a", header=False, index=False)
    
    print(f"Numero {numero} salvo com sucesso!")

def enviar_mensagem_numero(numero, mensagem, driver):
    # Buscar contato na barra de pesquisa
    search_box = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div/div/div/p')
    search_box.click()
    
    search_box.send_keys(numero)  # Digita o número do contato
    time.sleep(2)  # Aguarda carregar os resultados
    search_box.send_keys(Keys.ENTER)  # Entra na conversa
        
    # Aguardar a conversa abrir
    time.sleep(2)
    
    enviar_mensagem(mensagem)
    print(f"Mensagem enviada para {numero} com sucesso!")
    
    # Aguarda até que o botão "cancelar pesquisa" esteja presente
    try:
        cancel_search = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/span/button/span'))
        )
        cancel_search.click()
    except Exception as e:
        print(f"Botão de cancelar pesquisa não encontrado: {e}")

def processar_agendamentos(dir_path):
    arquivo = f"{dir_path}/bot/resources/agendamentos.xlsx"

    # Ler o Excel e depois converter a coluna de data corretamente
    df = pd.read_excel(arquivo)
    df["data"] = pd.to_datetime(df["data"])

    data_atual = datetime.now().strftime("%m/%d/%Y")

    for i, row in df.iterrows():
        contato = row["contato"]
        data_agendada = row["data"].strftime("%m/%d/%Y")
        mensagem = row["mensagem"]
        enviada = row["enviada"]

        if data_agendada == data_atual and not enviada:
            enviar_mensagem_numero(contato, mensagem)
            print(f"[INFO] Mensagem agendada para {contato} para hoje: ({data_agendada})")
            df.at[i, "enviada"] = True

    df.to_excel(arquivo, index=False)

def remover_caracteres_invalidos(texto: str) -> str:
    # Remove caracteres fora do Basic Multilingual Plane (BMP)
    return ''.join(c for c in texto if ord(c) <= 0xFFFF)
