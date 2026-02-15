# ---------------------------------------------------------------------------
# Project: 🌐 Pulse AI – Real-Time Global Sentiment Intelligence Engine
# File:    app.py
# Author:  AHMED ZARAI
# ---------------------------------------------------------------------------

import streamlit as st
import pandas as pd
import plotly.express as px
from inference import SentimentEngine

# 1. Page Configuration
st.set_page_config(
    page_title="Pulse AI | Global Sentiment Intelligence",
    page_icon="🌐",
    layout="wide"
)

# 2. Load Model (Cached)
@st.cache_resource
def load_engine():
    return SentimentEngine()

engine = load_engine()

# 3. Sidebar
st.sidebar.title("About Pulse AI")
st.sidebar.info(
    "Pulse AI uses DistilBERT to classify global customer feedback. "
    "It is designed for high-scale Business Intelligence."
)

# 4. Main UI
st.title("🌐 Pulse AI – Global Sentiment Intelligence")

tab1, tab2 = st.tabs(["✨ Single Analysis", "📊 Batch Processing (CSV)"])

# --- TAB 1: Single Analysis ---
with tab1:
    user_text = st.text_area(
        "Enter customer feedback or news text:",
        placeholder="The new tech release is absolutely game-changing!",
        height=150
    )

    if st.button("Run Single Analysis"):
        if not user_text.strip():
            st.warning("Please enter some text first.")
        else:
            with st.spinner("Analyzing..."):
                prediction = engine.predict(user_text)
                label, conf = prediction["label"], prediction["confidence"]
                
                st.subheader(f"Sentiment: {label}")
                st.progress(int(conf * 100))
                st.write(f"Confidence: {conf * 100:.2f}%")
                
                if label == "POSITIVE":
                    st.success("The AI detects a positive tone! ✅")
                else:
                    st.error("The AI detects a negative tone. ⚠️")

# --- TAB 2: Batch Processing ---
with tab2:
    st.subheader("Upload a CSV for Bulk Analysis")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("Data Preview:", df.head(3))
        
        column = st.selectbox("Select the column containing text:", df.columns)
        
        if st.button("Start Batch Analysis"):
            with st.spinner("Processing large dataset..."):
                texts = df[column].astype(str).tolist()
                results = engine.predict_batch(texts)
                
                df['Sentiment'] = [r['label'] for r in results]
                df['Confidence'] = [r['confidence'] for r in results]

            st.success("Analysis Complete!")

            # Summary stats
            summary = df['Sentiment'].value_counts().reset_index()
            summary.columns = ['Sentiment', 'Count']

            # VISUALS
            col_chart, col_data = st.columns([1, 1])
            
            with col_chart:
                fig = px.pie(
                    summary, names='Sentiment', values='Count',
                    title='Overall Brand Health',
                    color='Sentiment',
                    color_discrete_map={'POSITIVE': '#2ca02c', 'NEGATIVE': '#d62728'},
                    hole=0.4
                )
                st.plotly_chart(fig)

            with col_data:
                st.write("Summary Table:")
                st.dataframe(df[[column, 'Sentiment', 'Confidence']].head(10))
                st.write("Sentiment Counts:")
                st.dataframe(summary)

            # Download Result
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Download Results CSV", csv, "pulse_ai_results.csv", "text/csv")
