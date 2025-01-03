import nltk
from nltk.tokenize import word_tokenize

# Descarga los datos necesarios para NLTK
nltk.download('punkt_tab')

def soporte_tecnico():
    print("¡Hola! Soy tu asistente de soporte técnico. ¿En qué puedo ayudarte?")

    while True:
        pregunta = input("Tú: ").lower()
        palabras_clave = word_tokenize(pregunta)

        if "reiniciar" or "señal" in palabras_clave:
            print("Chatbot: Para reiniciar tu computadora, ve al menú de inicio y selecciona 'Reiniciar'.")
        elif "internet" in palabras_clave:
            print("Chatbot: Verifica tu conexión de red o reinicia el router.")
        elif "contraseña" in palabras_clave:
            print("Chatbot: Si necesitas cambiar tu contraseña, consulta la documentación del dispositivo.")
        elif "lento" in palabras_clave:
            print("Chatbot: Consulta la documentación del dispositivo o contacta a un profesional de soporte técnico")
        elif "salir" in palabras_clave:
            print("Chatbot: ¡Hasta luego!")
            break
        else:
            print("Chatbot: Lo siento, no entendí tu pregunta. Intenta algo como '¿Cómo reinicio mi computadora?'")
soporte_tecnico()
