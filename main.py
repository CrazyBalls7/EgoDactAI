import ollama
Lang_model = 'llama3.2:1b'
question = input("Question: ")

def ask_ollama(question,model):
  stream = ollama.chat(
    model=Lang_model,
    messages=[{'role': 'user', 'content': question}],
    stream=True,
  )

  for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)



ask_ollama(question,Lang_model)