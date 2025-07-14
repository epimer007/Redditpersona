# Reddit User Persona Analyzer

A Streamlit web app that analyzes a Reddit user's public posts and comments to generate a detailed persona profile using Google Gemini AI.

## 🚀 Features
- Enter any Reddit profile URL and generate a structured persona report
- Uses Google Gemini (Generative AI) for deep analysis
- Outputs persona in a consistent, human-readable format
- Download persona as TXT file
- Clean, modern UI

## 🛠️ Tech Stack
- [Streamlit](https://streamlit.io/) (UI)
- [Google Gemini API](https://ai.google.dev/) (AI analysis)
- [Reddit API (PRAW)](https://praw.readthedocs.io/) (data scraping)


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
   - Add your api credentails to `.streamlit/secrets.toml` file:
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
- Download the persona as TXT file

## 📋 Example Output
```
NAME: kojied
AGE: Likely between 25 and 40 (inferred from "feeling old" at a bar frequented by interns and having some career experience)
OCCUPATION: iOS Developer, possibly with experience in environmental consulting (indicated by "Hey I’m an iOS developer building in visionOS." and "as someone who's worked in environmental consulting")
STATUS: Unclear
LOCATION: New York City (mentioned in "I've only been here for three years" and the bar story)
TIER: Upper middle class/Professional (indicated by ownership of Apple Vision Pro, interest in ESG investing, and mentions of option trading)
ARCHETYPE: The Tech-Savvy Idealist

MOTIVATIONS:
- To explore and understand new technologies, particularly spatial computing and its applications (mentioned in VisionOS development and interest in AVP).
- To make a positive impact through sustainable and ethical consumption (indicated by interest in ESG ratings and developing a purchase gratification tracker).
- To share knowledge and insights with others online (evident through posting questions, sharing ideas, and providing helpful responses).
- Desire for social connection and validation from peers (deduced from frequent posting and seeking opinions on diverse topics).

PERSONALITY:
- Introspective and reflective: Kojied analyzes their own feelings and motivations (e.g., comparing themselves to interns, reflecting on purchase gratification). "But then again, I thought to myself. Am I not the same as they are, just at a longer time horizon?"
- Idealistic and socially conscious: Concerned with individual impact on the world (ESG ratings), sustainability, and ethical consumption. (From multiple ESG-related posts).
- Curious and analytical: Asks questions and seeks information on diverse topics, from technology to investing to personal well-being. "I’m curious if people have been able to fully port their workflow into AVP."
- Knowledgeable and articulate: Shares insights and expertise in various areas, including iOS development, finance, and cultural observations. Evidenced by explanations related to trading and software development.
- Observant and detail-oriented: Notices subtle changes and inconsistencies (e.g., inconsistencies of refs in sports, character consistency in AI-generated images). "What needs to happen for the league to review the inconsistencies of the refs?"
- Humorous and self-aware: Makes witty comments and acknowledges personal biases or shortcomings. "I do too but I rarely finish a game haha. Too little late game content"

BEHAVIOUR & HABITS:
- Frequent Reddit user, active in various subreddits related to technology, finance, games, and lifestyle.
- Early adopter of new technologies, willing to invest in innovative products like Apple Vision Pro. "I already dropped $4k on this device..."
- Enjoys exploring the city's nightlife (mentioned in the bar story).
- Plays video games (mentions Project Zomboid, comments on game design). "Surprised I don’t see project zomboid. Graphics are retro but the game is so well made."
- Interested in investing and trading, specifically options. "I’ve been trading options for the past month or so, and have made good money."
- Seeks recommendations and advice from online communities.
- Contributes to online discussions by providing informative and helpful responses.

FRUSTRATIONS:
- Limitations of new technologies and lack of support for professional workflows (e.g., missing Xcode on AVP). "Also where’s Xcode? If Apple wants AVP to be a “work device”, they gotta have at least Xcode right?"
- Unsustainable practices and lack of consumer awareness regarding ESG impact.
- Inefficiencies and inconsistencies in systems (e.g., Robinhood transfer limits, confusing game mechanics). "I want to transfer from Robinhood, but WB only allows 50k transfers at a time."
- Difficulty achieving character consistency in AI-generated images. "It’s pretty hard to get consistent characters when they’re photorealistic tbh. I guess our eyes are more lenient when it’s cartoon."

GOALS & NEEDS:
- To integrate new technologies into their professional workflow to improve efficiency and productivity.
- To develop and promote sustainable consumption habits.
- To connect with others who share their interests and values.
- To find solutions to problems and challenges through collective knowledge and collaboration.
- To stay informed and up-to-date on the latest trends and developments in technology, finance, and culture.
- To create meaningful and impactful contributions to online communities.

```




