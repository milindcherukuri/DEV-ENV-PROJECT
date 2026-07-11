from ai_service import analyze_sentiment

print("=" * 60)
print("Azure AI Chatbot")
print("=" * 60)
print("Type 'help' to see my capabilities.")
print("Type 'exit' to quit.\n")


def chatbot_reply(sentiment):
    if sentiment == "positive":
        return (
            "😊 I'm happy to hear that! "
            "Azure AI detected a positive sentiment in your message."
        )

    elif sentiment == "negative":
        return (
            "😔 I'm sorry you're feeling that way. "
            "Azure AI detected a negative sentiment. "
            "I hope things improve."
        )

    elif sentiment == "neutral":
        return (
            "🙂 Thanks for sharing. "
            "Azure AI considers your message neutral."
        )

    return "I'm not sure how to respond."


while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye! Thanks for chatting.")
        break

    elif user_input.lower() == "help":

        print("""
Bot Capabilities
--------------------------
• Analyze sentiment
• Detect positive messages
• Detect negative messages
• Detect neutral messages
• Use Azure AI Language Service
• Exit with 'exit'
""")
        continue

    elif user_input.strip() == "":
        print("Bot: Please enter some text.")
        continue

    try:

        result = analyze_sentiment(user_input)

        print("\nAzure AI Analysis")
        print("-------------------------")
        print("Sentiment :", result["sentiment"])
        print("Positive  :", result["positive"])
        print("Neutral   :", result["neutral"])
        print("Negative  :", result["negative"])

        print("\nBot:")
        print(chatbot_reply(result["sentiment"]))
        print()

    except Exception as ex:
        print(f"\nBot: Something went wrong.\n{ex}\n")