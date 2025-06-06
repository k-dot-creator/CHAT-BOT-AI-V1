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