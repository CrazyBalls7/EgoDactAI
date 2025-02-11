# Thanks to the random guy on youtube for this code!

import Main.ConfigEgoAI as ConfigEgoAI
import ollama

Lang_model = ConfigEgoAI.Lang_model


def ask_ollama(question,model):
  stream = ollama.chat(
    model=Lang_model,
    messages=[{'role': 'user', 'content': question}],
    stream=True,
  )

  for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)


# ask_ollama("HelloWorld",Lang_model)