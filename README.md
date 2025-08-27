# Teams Meeting Transcript Summariser
A Streamlit web app that takes Microsoft Teams transcript files (.vtt) and generates AI-powered meeting notes, including:

📋 Overall summary

✅ Key decisions made

📝 Action items with responsible persons

You can also email the generated summary to multiple recipients directly from the app. Here is the Link to [AI_Notes_Taker](https://aisummary2025.streamlit.app/) try it out it is deployed and ready to use.


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
   EMAIL_ADDRESS=example@gmail.com
   EMAIL_PASSWORD=your_email_password_or_app_password
   ```
   NB: The password for the sender gmail is not the one you use on daily basis but you must generate it on Gmail App Password under security settings.
4. Run the app
   ```
   streamlit run app.py
   ```
## Deployment
- So I have deployed this app on Streamlit Cloud for free. What you have to do is to make sure you push your code files in github excluding the .env file.
In StreamLit Cloud login with your github account. Click >> "New app" >> "Deploy". Then you can name the generated domain.
- Add your secrets under Settings → Secrets in this format:
   ```
   OPENAI_API_KEY="your_openai_api_key"
   EMAIL_ADDRESS="your_email@gmail.com"
   EMAIL_PASSWORD="your_email_password_or_app_password"
   ```
5. ## Requirements
   - Python 3.9+
   - [Streamlit](https://docs.streamlit.io/)
   - [OpenAI Python SDK](https://platform.openai.com/)
   - [python-dotenv](https://pypi.org/project/python-dotenv/)
6. ## Email Functionality
   - Emails are sent via Gmail’s SMTP server.
   - You can send summaries to multiple recipients (comma-separated).
7. ## Security Notes
   - Never commit your .env file or credentials.
   - Use environment variables or Streamlit Secrets Manager in production.
8. ## License
   - MIT License – feel free to use and adapt.

