import requests

API_KEY = "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"

def ask_gpt(messages):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": messages
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"].strip()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return "Sorry, I couldn't get a response from ChatGPT."

print("Robbiejr: Hello! Type 'bye' to exit.")

messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Robbiejr: Goodbye!")
        break
    messages.append({"role": "user", "content": user_input})
    reply = ask_gpt(messages)
    print(f"Robbiejr: {reply}")
    messages.append({"role": "assistant", "content": reply})
