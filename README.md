#Bot Autoatendimento FAQ no WhatsApp

## Visão Geral

Este projeto é um chatbot projetado para automatizar perguntas frequentes (FAQ) no WhatsApp. Os usuários podem enviar mensagens para o bot, e ele responderá com informações relevantes com base na seleção do usuário. O bot suporta respostas hierárquicas, permitindo que os usuários naveguem por várias opções para encontrar as informações necessárias.

## Recursos

- Respostas hierárquicas para FAQ.
- Opções e respostas personalizáveis.
- Integração com o WhatsApp via:
  - **WhatsApp Business API (Oficial)**.
  - **Bibliotecas open-source (e.g., Baileys, Venom)**.

---

## Instalação

### Pré-requisitos

1. **Python** (se usar a implementação baseada em Python) ou **Node.js** (para Baileys ou Venom).
2. Acesso à WhatsApp Business API (para integração oficial) ou uma conta WhatsApp.
3. (Opcional) Uma conta ativa no Twilio para a API do WhatsApp Business.

### Configuração

#### Configuração com Python (Usando Twilio)

1. Instale as bibliotecas necessárias:
   ```bash
   pip install twilio
   ```
2. Clone o repositório:
   ```bash
   git clone https://github.com/Skylinenando/whatsapp-faq-bot.git
   cd whatsapp-faq-bot
   ```
3. Configure as credenciais do Twilio no arquivo `config.py`:
   ```python
   account_sid = "SEU_ACCOUNT_SID"
   auth_token = "SEU_AUTH_TOKEN"
   from_whatsapp_number = 'whatsapp:+14155238886'  # Número Twilio
   to_whatsapp_number = 'whatsapp:+55XXXXXXXXXX'  # Seu número WhatsApp
   ```
4. Execute o bot:
   ```bash
   python bot.py
   ```

#### Configuração com Node.js (Usando Venom ou Baileys)

1. Instale as dependências:
   ```bash
   npm install venom-bot
   ```
2. Clone o repositório:
   ```bash
   git clone https://github.com/Skylinenando/whatsapp-faq-bot.git
   cd whatsapp-faq-bot
   ```
3. Execute o bot:
   ```bash
   node bot.js
   ```

---

## Configuração

### Estrutura de FAQ

Edite o arquivo `faq.json` para definir as respostas do bot:

```json
{
  "initial": "Selecione uma opção:\n1. Horário\n2. Preços\n3. Localização",
  "responses": {
    "1": "Nosso horário de funcionamento é das 8h às 18h.",
    "2": "Os preços variam de R$100 a R$300.",
    "3": "Estamos localizados na Chapada dos Veadeiros."
  }
}
```

### Variáveis de Ambiente

Use um arquivo `.env` para dados sensíveis:

```
TWILIO_ACCOUNT_SID=SEU_ACCOUNT_SID
TWILIO_AUTH_TOKEN=SEU_AUTH_TOKEN
FROM_WHATSAPP_NUMBER=whatsapp:+14155238886
TO_WHATSAPP_NUMBER=whatsapp:+55XXXXXXXXXX
```

---

## Uso

1. Inicie o bot usando o comando apropriado para sua configuração.
2. Envie uma mensagem para o número do WhatsApp vinculado ao bot.
3. Siga as instruções para navegar pelo FAQ.

---

## Limitações

- Bibliotecas open-source (e.g., Venom, Baileys) não são oficialmente suportadas pelo WhatsApp e podem levar ao bloqueio do número.
- A API do WhatsApp Business exige aprovação e pode envolver custos para uso em produção.

---

## Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do repositório.
2. Crie um novo branch para sua funcionalidade ou correção de bug.
3. Commit suas alterações e abra um pull request.

---

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

---

## Contato

Para dúvidas ou suporte, entre em contato com [Skylinenando no GitHub](https://github.com/Skylinenando).

