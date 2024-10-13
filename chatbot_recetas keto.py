# Variables sobre información del libro
title_ebook = "200 recetas keto"
price_ebook = 10.37 #precio en dolares
pages_ebook = 200
format_ebook = "PDF y EPUB"

# Función para obtener respuesta
def answer_question(answer):
    answer = answer.lower()
    
    if "hola" in answer:
        return "¡Hola! Bienvenido. ¿Cual es tu duda?"
    elif "precio" in answer:
        return f"El precio del libro '{title_ebook}' es de ${price_ebook}."
    elif "contenido" in answer:
        return f"El libro tiene {pages_ebook} páginas con recetas saludables y consejos nutricionales, orientado a la dieta keto."
    elif "paginas" in answer:
        return f"El libro tiene {pages_ebook} páginas con recetas saludables y consejos nutricionales"
    elif "formato" in answer:
        return f"El libro está disponible en formato {format_ebook}."
    elif "comprar" in answer:
        return "Para comprar, ve a nuestra página web y haz clic en 'Comprar ahora'."
    elif "gracias" in answer:
        return "¡De nada! Espero que te animes a comprar nuestro libro y te animes a probar todas las recetas que contiene para tu salud."
    else:
        return "Gracias con contactarte con nosotros, encantado de atenderte, te pedimos mantenerte a espera de respuesta con uno de nuestros asesores."

# Inicio del chat
print("Chatbot: ¡Hola! Pregúntame sobre nuestro libro de comida saludable.")

# Bucle principal
while True:
    user_question = input("Tú: ")
    if user_question.lower() == "adios":
        print("Chatbot: ¡Gracias por tu interés! Que tengas un buen día.")
        break
    answer = answer_question(user_question)
    print("Chatbot:", answer)