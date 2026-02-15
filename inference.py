
# ---------------------------------------------------------------------------
# Project: 🌐 Pulse AI – Real-Time Global Sentiment Intelligence Engine
# File:    inference.py
# Author:  AHMED ZARAI
#
# Copyright (c) 2026 Ahmed Zarai. All rights reserved.
# ---------------------------------------------------------------------------

from transformers import pipeline
import torch


class SentimentEngine:
    def __init__(self):
        self.device = 0 if torch.cuda.is_available() else -1
        self.classifier = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english",
            device=self.device
        )

    def predict(self, text: str) -> dict:
        result = self.classifier(text)[0]

        return {
            "label": result["label"],
            "confidence": float(result["score"])
        }
