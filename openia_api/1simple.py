from openai import OpenAI

from key import key

# Configura tu clave API de OpenAI
#api_key = "coloca tu api key de Openai"
api_key = key.key

client = OpenAI(api_key=api_key)

mensajes = [
        {"role":"system", "content": "Eres un asistente útil"},
        {"role": "user","content": "dime cual es la capital de México en pocas palabras"}
    ]

chat_completion = client.chat.completions.create(
    messages=mensajes,
    model="gpt-3.5-turbo",
    max_tokens=100, #palabras maximas
    n=1,# numero de respuestas 
    temperature=0.7, # que tan creativo va a ser (0 es nada creativo, 1 es muy cretivo)
)

print(chat_completion)

respuesta_asistente = chat_completion.choices[0].message.content
print("=============mensaje del asistente=============")
print(respuesta_asistente)



""" ChatCompletion(
                id='chatcmpl-9iwXwqaSZESsc3Lgv7JL5tMm3LSxE', 
                choices=[Choice(finish_reason='stop',  
                                index=0, 
                                logprobs=None, 
                                message=ChatCompletionMessage(
                                                                content='La capital de México es la Ciudad de México.', 
                                                                role='assistant', 
                                                                function_call=None, 
                                                                tool_calls=None
                                                            )
                                )
                        ], 
                created=1720498512, 
                model='gpt-3.5-turbo-0125', 
                object='chat.completion', 
                service_tier=None, 
                system_fingerprint=None, 
                usage=CompletionUsage(completion_tokens=10, prompt_tokens=31, total_tokens=41)
                ) """