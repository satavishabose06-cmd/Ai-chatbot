from groq import Groq

client = Groq(
    api_key="YOUR_API_KEY"
)

messages = []

print("AI Chatbot (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    answer = response.choices[0].message.content

    print("Bot:", answer)

    messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )