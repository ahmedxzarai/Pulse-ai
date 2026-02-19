<div align="center">
  <h1>🌐 Pulse AI</h1>
  <p><b>Real-Time Global Sentiment Intelligence Engine</b></p>

  ![Python](https://img.shields.io/badge/python-3.9+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
  ![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)
  ![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-Hugging%20Face-orange?style=for-the-badge)
  ![License](https://img.shields.io/badge/license-MIT-green.svg?style=for-the-badge)

  <p><i>Transforming unstructured customer feedback into actionable insights using Transformer-based NLP.</i></p>
  
  <a href="https://pulse-ai-jczcdcxtesbrnylreulvdk.streamlit.app/"><strong>Explore the Live Demo »</strong></a>
</div>

---

### 🚀 Overview
Pulse AI is a production-oriented NLP application leveraging *Transformer architecture* for real-time sentiment classification of global business reviews. This project demonstrates end-to-end ML system integration—from model inference to user-facing deployment.

### 🧠 System Architecture
```text
User Input ──▶ SentimentEngine (Inference) ──▶ DistilBERT Transformer ──▶ Softmax ──▶ Streamlit UI
```

### 🎯 Key Features
- Real-time Prediction: Instant single and batch sentiment analysis.
- Confidence Scoring: Probability-based metrics for every prediction.
- GPU-Aware: Automatic hardware detection for optimized performance.
- Brand Health Dashboard: Interactive Pie charts and summary tables.
- Batch Processing: Support for CSV upload/download for large-scale analysis.

### 🛠 Tech Stack
| Layer            | Technology                |
| ---------------- | ------------------------- |
| Model            | DistilBERT                |
| NLP Framework    | Hugging Face Transformers |
| Backend          | Python + PyTorch          |
| Frontend         | Streamlit                 |
| Hardware Support | CPU / GPU (auto-detected) |

### 📦 Project Structure
```text
Pulse-AI/
├── .gitignore
├── app.py                 # Streamlit UI & Dashboard
├── inference.py           # ML Inference Logic (Core Engine)
├── requirements.txt       # Project Dependencies
├── README.md              # Documentation
└── LICENSE                # MIT License
```

### 🖥 Getting Started
<details>
<summary><b>View Installation Steps</b></summary>
1. Clone the repository
```bash
git clone [https://github.com/ahmedxzarai/Pulse-ai.git](https://github.com/ahmedxzarai/Pulse-ai.git)
cd pulse-ai
```
2. Setup Environment
```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```
3. Install Dependencies
```bash
pip install -r requirements.txt
```
4. Run Application
```bash
streamlit run app.py
```
</details>

### 🔥 Engineering Highlights
- Modular Design: Clean separation between UI (Streamlit) and ML Logic (Inference).
- Caching Strategy: Production-style caching to prevent reloading the model on every interaction.
- Scalability: Logic is built to be "FastAPI-ready" for microservice conversion.

### 🚀 Roadmap & Future Improvements
- [ ] Multilingual model support (mBERT)
- [ ] REST API microservice layer (FastAPI)
- [ ] Docker containerization for cloud scaling
- [ ] CI/CD pipeline for automated testing


### 👤 Author
**AHMED ZARAI**<br>
*AI Systems & Biometric Intelligence Developer*





<div align="center">
<p>Copyright © 2026 AHMED ZARAI. Distributed under the MIT License.</p>
</div>