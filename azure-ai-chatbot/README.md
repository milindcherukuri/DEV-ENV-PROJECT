# Azure AI Chatbot

## Overview

This project demonstrates a traditional Python chatbot integrated with Microsoft Azure AI Language Service. Unlike the previous rule-based chatbot, this implementation utilizes Azure AI to perform sentiment analysis on user input and generate conversational responses.

This project was developed for the University of the Cumberlands as part of the Human-Computer Interaction course.

---

## Features

- Traditional chatbot interface
- Azure AI Language integration
- Sentiment analysis
- Friendly chatbot responses
- Help command
- Exit command
- Error handling
- Environment variable configuration

---

## Technologies

- Python 3.x
- Azure AI Language Service
- Azure AI Text Analytics SDK
- python-dotenv

---

## Project Structure

```
azure-ai-chatbot/
│
├── app.py
├── ai_service.py
├── chatbot.py
├── config.py
├── requirements.txt
├── README.md
├── .env
└── screenshots/
```

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python app.py
```

---

## Azure Configuration

Create a `.env` file.

```
AZURE_LANGUAGE_ENDPOINT=YOUR_ENDPOINT
AZURE_LANGUAGE_KEY=YOUR_KEY
```

---

## Future Improvements

- Intent recognition
- Key phrase extraction
- Named Entity Recognition
- Speech input
- Azure Bot Service
- Azure OpenAI integration

---

## Author

Milind Cherukuri