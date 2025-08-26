# Teams Meeting Transcript Summariser
A Streamlit web app that takes Microsoft Teams transcript files (.vtt) and generates AI-powered meeting notes, including:

📋 Overall summary

✅ Key decisions made

📝 Action items with responsible persons

You can also email the generated summary to multiple recipients directly from the app.

## Features

- Upload a Microsoft Teams .vtt transcript.

- Automatic cleaning & formatting of transcript text.

- Uses OpenAI GPT models to generate concise, structured meeting summaries.

- Option to send summary via email to one or more recipients.

- Works locally and when deployed on Streamlit Cloud.

## Installation
1. Clone the Repo
   ```
   git clone https://github.com/PullBeforePush/AI_Notes_Taker.git
   ```
2. Create a virtual environment & install dependencies
   ```
    python -m venv venv
    source venv/bin/activate   # Mac/Linux
    venv\Scripts\activate      # Windows

    pip install -r requirements.txt
   ```
3. Set up environment variables
   Create a .env file in the project root with:
   ```
   OPENAI_API_KEY=your_openai_api_key
   EMAIL_ADDRESS=your_email@gmail.com
   EMAIL_PASSWORD=your_email_password_or_app_password
   ```
4. Run the app
   ```
   streamlit run app.py
   ```

