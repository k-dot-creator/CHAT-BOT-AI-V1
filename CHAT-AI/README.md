# Robbie-Jr-Bot v1

Robbie-Jr-Bot is a simple command-line chatbot powered by OpenAI's GPT-3.5-turbo model. It allows you to have natural conversations with an AI assistant directly from your terminal. This project is designed for learning, experimentation, and as a foundation for more advanced chatbot applications.

---

## Features

- **Conversational AI:** Uses OpenAI's ChatGPT API for intelligent, context-aware responses.
- **Conversation Memory:** Remembers the conversation history for more natural interactions.
- **Easy to Use:** Simple Python script, runs in any terminal.
- **Customizable:** Easily modify the system prompt or extend functionality.

---

## Requirements

- Python 3.6 or higher
- `requests` library (`pip install requests`)
- An OpenAI API key ([Get one here](https://platform.openai.com/account/api-keys))

---

## Installation

1. **Clone or Download the Repository**

   ```
   git clone https://github.com/k-dot-creator/CHAT-BOT-AI.git
   cd CHAT-BOT-AI
   ```

2. **Install Dependencies**

   ```
   pip install requests
   ```

3. **Set Your OpenAI API Key**

   Open `chatbot.py` and replace the `API_KEY` variable with your own OpenAI API key.

---

## Usage

Run the chatbot from your terminal:

```
python chatbot.py
```

You will see:

```
Robbiejr: Hello! Type 'bye' to exit.
```

Type your messages and interact with the bot. Type `bye` to end the conversation.

---

## Example Conversation

```
You: Hello!
Robbiejr: Hello! How can I assist you today?
You: Tell me a joke.
Robbiejr: Why don't scientists trust atoms? Because they make up everything!
You: bye
Robbiejr: Goodbye!
```

---

## How It Works

- The script maintains a list of messages (conversation history).
- Each user input is appended to this list and sent to the OpenAI API.
- The assistant's reply is also appended, allowing for context-aware conversations.

---

## Customization

- **Change the Assistant's Personality:**  
  Edit the `"system"` message in the `messages` list to set a different tone or role for the assistant.

- **Add Features:**  
  You can extend the script to support saving conversations, logging, or even a web interface.

---

## Troubleshooting

- **API Errors:**  
  If you see errors like "Sorry, I couldn't get a response from ChatGPT," check your API key, internet connection, and OpenAI account status.

- **requests not installed:**  
  Install it with `pip install requests`.

- **Rate Limits:**  
  Free OpenAI accounts have usage limits. Check your quota on the [OpenAI dashboard](https://platform.openai.com/).

---

## Security

**Never share your API key publicly.**  
For production or public projects, use environment variables or a secure secrets manager.

---

## License

This project is for educational purposes. See [LICENSE](LICENSE) for more information.

---

## Credits

- [OpenAI](https://openai.com/) for the GPT API
- Inspired by the open-source Python community
