

from google import genai 
import os 

# Configura client con API Key da variabile d'ambiente 
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"]) 

from google.genai import types

safety_settings = [    
        types.SafetySetting(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="BLOCK_NONE"),    
        types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="BLOCK_NONE"),    
        types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="BLOCK_NONE"),    
        types.SafetySetting(category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="BLOCK_NONE"),
]

config = types.GenerateContentConfig(
    temperature=0.3,                # 0=deterministico,  1=creativo
    max_output_tokens=1024,        # Lunghezza massima risposta
    system_instruction="""
    Sei un assistente amichevole per studenti di programmazione.    
    Rispondi in modo semplice e chiaro.    
    Usa esempi pratici quando possibile.
    """,
    safety_settings= safety_settings
)

# Loop per conversazione continua
while True:
    domanda = input("Fammi la tua domanda: ")
    
    if domanda.lower() == "esci":
        print("Arrivederci!")
        break

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=domanda,
        config=config
    )
    # Stampa output 
    print(f"AI: {response.text}\n")