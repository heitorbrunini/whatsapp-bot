from ollama import chat

def clean_response(content):
    # Remove blocos <think>...</think> e seu conteúdo
    import re
    return re.sub(r'<think>.*?</think>', '', content, flags=re.DOTALL)

def run_chat_interaction(model_name='pizzaria_gemma:latest'):
    print(f"Iniciando interação com o modelo: {model_name}. Digite 'sair' ou 'exit' para encerrar.")
    
    # Inicializa o histórico da conversa. Isso é importante para manter o contexto.
    messages = []

    while True:
        user_input = input("\nVocê: ")
        
        if user_input.lower() in ['sair', 'exit']:
            print("Encerrando a interação. Até mais!")
            break
        
        # Adiciona a mensagem do usuário ao histórico
        messages.append({'role': 'user', 'content': user_input})

        print("Modelo: ", end='', flush=True)
        try:
            stream = chat(
                model=model_name,
                messages=messages,
                stream=True,
            )

            current_response_content = ""
            for chunk in stream:
                content = chunk['message']['content']
                print(content, end='', flush=True)
                current_response_content += content
                
            #print (clean_response(current_response_content), flush=True)
            # Adiciona a resposta completa do modelo ao histórico para manter o contexto
            messages.append({'role': 'assistant', 'content': current_response_content})

        except Exception as e:
            print(f"\nOcorreu um erro ao interagir com o modelo: {e}")
            print("Por favor, verifique se o modelo está em execução e acessível.")
            break

def get_llm_response(user_message: str,conversation_history = [], model_name='pizzaria_gemma:latest') -> str:
    
    # Adiciona a mensagem do usuário ao histórico
    conversation_history.append({'role': 'user', 'content': user_message})
    
    # Armazena o conteúdo da resposta do Freddy
    freddy_full_response = ""
    try:
        stream = chat(
            model=model_name,
            messages=conversation_history, # Passa todo o histórico da conversa
            stream=True,
        )

        for chunk in stream:
            content = chunk['message']['content']
            freddy_full_response += content # Acumula todo o conteúdo do chunk

    except Exception as e:
        print(f"\n[ERRO] Ocorreu um erro ao interagir com o Freddy: {e}")
        print("Por favor, verifique se o modelo 'pizzariapersona' está em execução no Ollama e acessível.")
        # Em caso de erro, é bom retornar uma mensagem de erro ou levantar a exceção
        return f"Desculpe! Tivemos um problema para processar sua solicitação no momento. Por favor, tente novamente mais tarde. Erro: {e}"

    # Adiciona a resposta completa do modelo ao histórico
    conversation_history.append({'role': 'assistant', 'content': freddy_full_response})
    
    return freddy_full_response.strip() 

# Para iniciar a interação, chame a função:
if __name__ == "__main__":
    run_chat_interaction()