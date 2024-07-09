import openai
from key import key

# Configura tu clave API de OpenAI
#openai.api_key = 'your-api-key-here'
openai.api_key = key.key

# Función para analizar la imagen
def analyze_image(image_path):
    # Cargar la imagen
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()

    # Enviar la solicitud a la API de OpenAI
    response = openai.Image.create(
        file=image_data,
        model="dall-e",  # Asegúrate de usar el modelo adecuado que soporte análisis de imágenes
        prompt="Describe this image",
        n=1,
        size="256x256"
    )

    # Obtener la descripción de la imagen
    description = response['data'][0]['text']

    return description

# Ejemplo de uso
image_path = 'path/to/your/image.jpg'
description = analyze_image(image_path)
print(f"Image description: {description}")
