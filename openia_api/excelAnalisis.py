import openai
import pandas as pd
from key import key

# Configura tu clave API de OpenAI
#openai.api_key = 'your-api-key-here'
openai.api_key = key.key

# Función para leer el archivo Excel y obtener una descripción del contenido
def analyze_excel(file_path):
    # Leer el archivo Excel
    df = pd.read_excel(file_path)

    # Generar una descripción del contenido del archivo Excel
    description = f"The Excel file contains the following columns: {', '.join(df.columns)}.\n"
    description += f"Here is a summary of the first few rows:\n{df.head().to_string(index=False)}"

    # Solicitar a OpenAI un análisis y sugerencias
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Analyze the following Excel data and provide suggestions for any potential issues:\n\n{description}\n\nSuggestions:",
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Obtener las sugerencias de la respuesta
    suggestions = response.choices[0].text.strip()

    return suggestions

# Ejemplo de uso
file_path = 'path/to/your/excel_file.xlsx'
suggestions = analyze_excel(file_path)
print(f"Suggestions for the Excel file:\n{suggestions}")
