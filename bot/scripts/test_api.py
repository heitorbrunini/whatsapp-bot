import requests

# Configuração do agente e token da API EDITACODIGO
agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
token_api = "Ezm597rhhnUH0zcnBhk772z1MZqhqgNC"

api = requests.get(f"https://editacodigo.com.br/index/api-whatsapp/{token_api}", headers=agent)
api = api.text
api = api.split('.n.')
bolinha_notificacao = api[3].strip()
contcaixa_msg = api[5].strip()
msg_cliente = api[6].strip()

print (f"msg_cliente: {msg_cliente}")
