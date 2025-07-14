# Reddit User Persona Analyzer

A Streamlit web app that analyzes a Reddit user's public posts and comments to generate a detailed persona profile using Google Gemini AI.

## 🚀 Features
- Enter any Reddit profile URL and generate a structured persona report
- Uses Google Gemini (Generative AI) for deep analysis
- Outputs persona in a consistent, human-readable format
- Download persona as TXT or PDF
- Clean, modern UI

## 🛠️ Tech Stack
- [Streamlit](https://streamlit.io/) (UI)
- [Google Gemini API](https://ai.google.dev/) (AI analysis)
- [Reddit API (PRAW)](https://praw.readthedocs.io/) (data scraping)
- [fpdf2](https://pypi.org/project/fpdf2/) (PDF export)

## 📦 Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/reddit_user_persona.git
   cd reddit_user_persona
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Keys:**
   - Create a `.streamlit/secrets.toml` file:
     ```toml
     REDDIT_CLIENT_ID = "your_reddit_client_id"
     REDDIT_CLIENT_SECRET = "your_reddit_client_secret"
     GEMINI_API_KEY = "your_gemini_api_key"
     ```
   - Get Reddit API keys from [Reddit Apps](https://www.reddit.com/prefs/apps)
   - Get Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

4. **Run the app:**
   ```bash
   streamlit run main.py
   ```

## 💡 Usage
- Enter a Reddit profile URL (e.g. `https://www.reddit.com/user/example_user/`)
- Click **Generate Persona**
- View the generated persona in the app
- Download the persona as TXT or PDF

## 📋 Example Output
```
NAME: example_user
AGE: Not specified
OCCUPATION: Not specified
STATUS: Not specified
LOCATION: Not specified
TIER: Not specified
ARCHETYPE: Not specified

MOTIVATIONS:
- Not specified

PERSONALITY:
- Not specified

BEHAVIOUR & HABITS:
- Not specified

FRUSTRATIONS:
- Not specified

GOALS & NEEDS:
- Not specified
```




