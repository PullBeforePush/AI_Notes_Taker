import streamlit as st
import re
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found. Did you create a .env file?")

client = OpenAI(api_key=OPENAI_API_KEY)

st.title("Teams Meeting Transcript Summariser")
st.write("Upload a `.vtt` file from Microsoft Teams and get AI-generated meeting notes.")

uploaded_file = st.file_uploader("Upload Teams Transcript (.vtt)", type=["vtt"])

if uploaded_file:
    raw_text = uploaded_file.read().decode("utf-8")
    clean_text = re.sub(r"\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}", "", raw_text)
    clean_text = re.sub(r"WEBVTT|Kind: captions|Language: \w+", "", clean_text)
    clean_text = re.sub(r"\n+", "\n", clean_text).strip()

    if st.button("Summarise Meeting"):
        with st.spinner("Generating summary..."):
            prompt = f"""
            You are an AI meeting assistant. Summarise the following transcript and provide:
            1. Overall meeting summary
            2. Key decisions made
            3. Action items with responsible persons

            Transcript:
            {clean_text}
            """
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )
            result = response.choices[0].message.content
        st.success("Summary generated!")
        st.write(result)
