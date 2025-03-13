from ollama import chat

stream = chat(
    model='llama3.2',
    messages=[{'role': 'user', 'content': 'Why is the sky blue?'}],
    stream=True,
)

response = ""
for chunk in stream:
  response+= (chunk['message']['content'])
  #print(chunk['message']['content'], end='', flush=True)

print(var)