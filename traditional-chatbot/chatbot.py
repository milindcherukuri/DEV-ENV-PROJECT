from responses import get_response
from datetime import datetime

print("=" * 50)
print("Traditional Rule-Based Chatbot")
print("Type 'help' to see what I can do.")
print("Type 'exit' to quit.")
print("=" * 50)

while True:
    user_input = input("\nYou: ").strip().lower()

    if user_input == "exit":
        print("Bot: Goodbye! Have a great day.")
        break

    response = get_response(user_input)

    print("Bot:", response)