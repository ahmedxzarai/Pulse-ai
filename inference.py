from transformers import pipeline
import torch

class SentimentEngine:
    def __init__(self):
        # Hardware acceleration check
        self.device = 0 if torch.cuda.is_available() else -1
        self.classifier = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english",
            device=self.device
        )

    def predict(self, text: str) -> dict:
        """Analyze a single string."""
        result = self.classifier(text)[0]
        return {
            "label": result["label"],
            "confidence": float(result["score"])
        }

    def predict_batch(self, texts: list) -> list:
        """Analyze a list of strings efficiently."""
        results = self.classifier(texts)
        return [
            {"label": r["label"], "confidence": float(r["score"])} 
            for r in results
        ]
