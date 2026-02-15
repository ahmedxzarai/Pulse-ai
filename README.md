🌐 Pulse AI – Real-Time Global Sentiment Intelligence Engine

Transforming unstructured customer feedback into actionable insights using Transformer-based NLP.

🚀 Overview

Pulse AI is a production-oriented NLP application leveraging Transformer architecture for real-time sentiment classification of global business reviews.

Built using:

• Hugging Face Transformers
• DistilBERT (fine-tuned on SST-2)
• PyTorch backend
• Streamlit interactive dashboard
• This project demonstrates end-to-end ML system integration — from model inference to user-facing deployment.

🧠 System Architecture

User Input
    ↓
SentimentEngine (Inference Layer)
    ↓
DistilBERT Transformer
    ↓
Softmax Classification
    ↓
Confidence Score + Label
    ↓
Streamlit UI

🛠 Tech Stack

| Layer            | Technology                |
| ---------------- | ------------------------- |
| Model            | DistilBERT                |
| NLP Framework    | Hugging Face Transformers |
| Backend          | Python + PyTorch          |
| Frontend         | Streamlit                 |
| Hardware Support | CPU / GPU (auto-detected) |

🎯 Features

• Real-time sentiment prediction
• GPU-aware inference
• Confidence scoring
• Clean modular architecture
• Cached model loading
• Error-handled inference pipeline

📊 Model Details

• Model: distilbert-base-uncased-finetuned-sst-2-english
• Fine-tuned on SST-2 dataset
• Binary sentiment classification
• Lightweight compared to full BERT
• Optimized for CPU environments

📦 Project Structure

Pulse-AI/
│
├── app.py             # Streamlit UI
├── inference.py       # ML inference engine
├── requirements.txt
└── README.md

🖥 Run Locally

Clone the repository:
git clone https://github.com/ahmedxzarai/pulse-ai.git
cd pulse-ai

Create a virtual environment (recommended):
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux

Install dependencies:
pip install -r requirements.txt

Run the application:
streamlit run app.py

🌍 Business Applications

• Customer review intelligence
• Brand monitoring
• Market research automation
• E-commerce sentiment tracking
• SaaS product feedback analysis

🔥 Engineering Highlights

• Transformer integration in a modular system
• GPU-aware inference logic
• Production-style caching strategy
• Clean UI/ML separation
• Extensible for API integration (FastAPI-ready)

🚀 Future Improvements

• Multilingual model support
• REST API microservice layer
• Docker containerization
• Cloud deployment (AWS / GCP / Azure)
• Model benchmarking comparison
• CI/CD pipeline

💡 Why This Project Matters

• Pulse AI demonstrates practical application of modern Transformer architectures in a deployable system, showcasing:
• NLP engineering capability
• Production-aware design
• Real-world business alignment
• End-to-end ML workflow implementation



## 🌍 Live Demo
[Click here to try Pulse AI](https://pulse-ai-jczcdcxtesbrnylreulvdk.streamlit.app/)




📜 License \& Copyright
Copyright © 2026 AHMED ZARAI. Distributed under the MIT License. See LICENSE for more information.
