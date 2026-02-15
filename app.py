
# ---------------------------------------------------------------------------
# Project: 🌐 Pulse AI – Real-Time Global Sentiment Intelligence Engine
# File:    app.py
# Author:  AHMED ZARAI
#
# Copyright (c) 2026 Ahmed Zarai. All rights reserved.
# ---------------------------------------------------------------------------

import streamlit as st
from inference import SentimentEngine

# -------------------------------------------------
# 1. Page Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Pulse AI | Global Sentiment Intelligence",
    page_icon="🌐",
    layout="centered"
)

# -------------------------------------------------
# 2. Load Model (Cached)
# -------------------------------------------------
@st.cache_resource
def load_engine():
    return SentimentEngine()

engine = load_engine()

# -------------------------------------------------
# 3. UI
# -------------------------------------------------
st.title("🌐 Pulse AI – Global Sentiment Intelligence")
st.markdown(
    "Production-style Transformer-powered sentiment analysis "
    "built with Hugging Face DistilBERT."
)

user_text = st.text_area(
    "Enter customer feedback, review, or news text:",
    placeholder="The new tech release is absolutely game-changing!"
)

# -------------------------------------------------
# 4. Inference
# -------------------------------------------------
if st.button("Run Analysis"):

    if not user_text.strip():
        st.warning("Please enter some text before running analysis.")
    else:
        try:
            with st.spinner("Running Transformer inference..."):
                prediction = engine.predict(user_text)

            label = prediction["label"]
            confidence = prediction["confidence"]

            st.subheader(f"Sentiment: {label}")
            st.metric("Confidence Score", f"{confidence * 100:.2f}%")

            if label == "POSITIVE":
                st.success("Positive sentiment detected.")
            else:
                st.error("Negative sentiment detected.")

        except Exception as e:
            st.error("Inference failed.")
            st.exception(e)
