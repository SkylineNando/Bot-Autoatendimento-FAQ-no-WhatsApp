from twilio.rest import Client

# Importar credenciais do arquivo config.py
from config import account_sid, auth_token, from_whatsapp_number, to_whatsapp_number

# Inicializa cliente Twilio
client = Client(account_sid, auth_token)

# Respostas FAQ
faq_responses = {
    "1": "Nosso horário de funcionamento é das 8h às 18h.",
    "2": "Os preços variam de R$100 a R$300.",
    "3": "Estamos localizados na Chapada dos Veadeiros."
}

# Mensagem inicial
initial_message = "Selecione uma opção:\n1. Horário\n2. Preços\n3. Localização"

# Enviar mensagem inicial
message = client.messages.create(
    body=initial_message,
    from_=from_whatsapp_number,
    to=to_whatsapp_number
)
print(f"Mensagem enviada: {message.sid}")
