from openai import OpenAI

from key import key

# Configura tu clave API de OpenAI
#api_key = "coloca tu api key de Openai"
api_key = key.key

client = OpenAI(api_key=api_key)

mensajes = [
        {"role":"system", "content": "Eres un asistente útil"},
    ]

while True:
    user_input = input("Escribe Tu:")
    if user_input.lower() == "salir":
        break
    mensajes.append({"role":"user", "content":user_input})


    chat_completion = client.chat.completions.create(
        messages=mensajes,
        model="gpt-4o",
        max_tokens=100, #palabras maximas
        n=1,# numero de respuestas 
        temperature=0.7, # que tan creativo va a ser (0 es nada creativo, 1 es muy cretivo)
    )

    #print(chat_completion)

    respuesta_asistente = chat_completion.choices[0].message.content
    print("=============mensaje del Asistente=============")
    print(respuesta_asistente)
    print("===============================================")