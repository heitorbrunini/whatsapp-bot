# Chatbot para WhatsApp com Selenium e IA

Este é um chatbot automatizado para WhatsApp Web que utiliza Selenium para detectar novas mensagens e responder automaticamente com IA via Ollama.

## 🚀 Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto
- **Selenium**: Automação do WhatsApp Web
- **Ollama**: Geração de respostas com IA
- **Requests**: Comunicação com API externa

## 📌 Funcionalidades

- Detecta mensagens não lidas no WhatsApp Web
- Coleta e processa as mensagens recebidas
- Gera respostas automáticas com IA
- Envia as respostas diretamente pelo WhatsApp Web

## 📂 Estrutura do Projeto

```
📂 chatbot-whatsapp
 ├── chatbot.py  # Código principal do chatbot
 ├── msedgedriver.exe  # WebDriver do Edge (coloque aqui)
 ├── profile/  # Perfil do usuário do navegador
 ├── README.md  # Documentação do projeto
```

## 🛠️ Configuração e Instalação

### 1️⃣ **Pré-requisitos**
- Python 3 instalado
- Microsoft Edge instalado
- WebDriver do Edge compatível com a versão do seu navegador ([Baixar aqui](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/))

### 2️⃣ **Instalar as Dependências**

```bash
pip install selenium requests ollama
```

### 3️⃣ **Configurar o WebDriver**
Coloque o arquivo `msedgedriver.exe` no mesmo diretório do script ou especifique o caminho correto no código.

### 4️⃣ **Executar o Chatbot**

```bash
python chatbot.py
```

> **Nota:** O WhatsApp Web será aberto automaticamente. Faça login manualmente na primeira execução.

## 🖥️ Como Funciona

1. O script acessa o WhatsApp Web e detecta novas mensagens.
2. Captura o número do contato e a mensagem recebida.
3. Usa a IA da Ollama para gerar uma resposta baseada no conteúdo recebido.
4. Envia a resposta automaticamente pelo WhatsApp Web.

## 🔄 Exemplo de Fluxo de Execução

```
[Bot] Aguardando notificação...
[Bot] Nova mensagem de +55 99999-9999
[Bot] Mensagem recebida: "Olá! Como funciona esse bot?"
[Bot] Respondendo...
[Bot] Resposta enviada!
```

## 🛑 Parar o Bot

Pressione `CTRL + C` para interromper a execução do bot.

## 📜 Licença

Este projeto é de código aberto e pode ser usado para estudos e aprimoramento de automação com Selenium e IA. Respeite as diretrizes do WhatsApp ao utilizá-lo.

---

Desenvolvido por **Heitor Brunini** 💻🤖
