from datetime import datetime

def get_response(user_input):

    greetings = ["hi", "hello", "hey"]

    if user_input in greetings:
        return "Hello! Nice to meet you."

    elif user_input == "help":
        return """
I can respond to:

• hello
• hi
• help
• about
• capabilities
• date
• time
• weather
• bye
"""

    elif user_input == "about":
        return "I am a traditional rule-based chatbot created using Python."

    elif user_input == "capabilities":
        return """
My capabilities include:

✓ Greetings
✓ Date
✓ Time
✓ FAQs
✓ Error handling
✓ Rule-based responses
"""

    elif user_input == "date":
        return datetime.now().strftime("%B %d, %Y")

    elif user_input == "time":
        return datetime.now().strftime("%I:%M %p")

    elif user_input == "weather":
        return "I cannot access live weather. Future versions could integrate weather APIs."

    elif user_input in ["bye", "goodbye"]:
        return "Goodbye! Thanks for chatting."

    else:
        return "Sorry, I don't understand that. Type 'help' to see available commands."