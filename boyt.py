# Step 1: Importando as bibliotecas necessárias
from selenium import webdriver
import time
import pandas as pd
from datetime import datetime


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
time.sleep(60)
print("Tempo de espera encerrado")

def busca_notificacao():
    try: 
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
    #responder
    campo_resposta = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p')
    campo_resposta.click()
    time.sleep(1)

    campo_resposta.send_keys(response, Keys.ENTER)
    time.sleep(1)

def obter_resposta(id_mensagem):
    #Retorna a mensagem correspondente ao ID fornecido.
    
    #Filtra a linha correspondente ao ID e pega a coluna 'Mensagem'
    resposta = df[df['ID'] == id_mensagem]['Mensagem']
    return resposta.iloc[0] if not resposta.empty else "Desculpe, não encontrei essa mensagem."


def salvar_contato(numero):
    arquivo = "ctt.csv"

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

def enviar_mensagem_numero(numero, mensagem):
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
    
    # sair da pesquisa com xpath: 
    cancel_search = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/span/button')
    cancel_search.click()
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

# Função para processar os agendamentos e enviar mensagens
def processar_agendamentos():
    arquivo = "agendamentos.xlsx"

    # Ler o arquivo Excel
    df = pd.read_excel(arquivo)

    # Obter a data atual no formato correto
    data_atual = datetime.now().strftime("%d/%m/%Y")

    # Percorrer as linhas
    for i, row in df.iterrows():
        contato = row["contato"]
        data_agendada = row["data"].strftime("%d/%m/%Y")
        mensagem = row["mensagem"]
        enviada = row["enviada"]

        # Verificar se a data agendada é hoje e se ainda não foi enviada
        if data_agendada == data_atual and not enviada:
            enviar_mensagem_numero(contato, mensagem)

            # Atualizar a coluna "enviada" para True
            df.at[i, "enviada"] = True

    # Salvar as alterações no arquivo Excel
    df.to_excel(arquivo, index=False)

    print("Processo concluído!")


while True:
    try:
        '''
          # Passo 1: Verificar notificações e abrir conversa
        busca_notificacao()

        # Passo 2: Capturar dados da conversa
        telefone = capturar_contato()
        salvar_contato(telefone)
        mensagem_recebida = capturar_mensagem()

        print(f"Telefone: {telefone}")
        print(f"Mensagem: {mensagem_recebida}")

        # Passo 3: Buscar resposta correspondente e enviar mensagem
        resposta = obter_resposta(mensagem_recebida)
        print(f"Resposta: {resposta}")
        enviar_mensagem(resposta)
        
        '''
      

        # Passo 4: Aguardar antes de verificar novas mensagens
        time.sleep(5)        

        processar_agendamentos() # Substitua pelo número desejado e pela mensagem        

    except KeyboardInterrupt:
        print("Fim do programa")
        driver.quit()
        exit()
    except Exception as e:
        print("aguardando carregamento...")
        time.sleep(20)
