from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

from config import AZURE_ENDPOINT, AZURE_KEY


credential = AzureKeyCredential(AZURE_KEY)

client = TextAnalyticsClient(
    endpoint=AZURE_ENDPOINT,
    credential=credential
)


def analyze_sentiment(text):

    response = client.analyze_sentiment(documents=[text])[0]

    return {
        "sentiment": response.sentiment,
        "positive": round(response.confidence_scores.positive, 2),
        "neutral": round(response.confidence_scores.neutral, 2),
        "negative": round(response.confidence_scores.negative, 2)
    }