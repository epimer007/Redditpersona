import os
import google.generativeai as genai
import streamlit as st

api_key = st.secrets["GEMINI_API_KEY"] if "GEMINI_API_KEY" in st.secrets else "your_gemini_api_key"
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-flash")

def build_prompt(username, posts, comments):
    content = "\n\n".join(posts + comments)
    prompt = f"""
You are an expert persona profiler. Analyze the following Reddit posts and comments from the Reddit user {username}, and generate a detailed user persona.

STRICT INSTRUCTIONS:
- ALWAYS use the exact format below.
- DO NOT use Markdown formatting (no asterisks, bold, italics, or bullet points other than a single dash '-').
- ALWAYS use the same section order, headers, and spacing as shown.
- For each section, use dashes '-' for bullet points.
- DO NOT add or remove blank lines.

TEMPLATE (fill in as much as possible):

NAME: (If you can infer or find a real name from the content, provide it. Otherwise, use the Reddit username '{username}'—do NOT include 'u/' or any prefix.)
AGE: 
OCCUPATION: 
STATUS: 
LOCATION: 
TIER: 
ARCHETYPE: 

MOTIVATIONS:
- 

PERSONALITY:
- 

BEHAVIOUR & HABITS:
- 

FRUSTRATIONS:
- 

GOALS & NEEDS:
- 

For each trait, cite the exact post or comment that helped you derive it.

Reddit Content:
{content}
"""
    return prompt

def generate_user_persona(username, posts, comments):
    prompt = build_prompt(username, posts, comments)
    response = model.generate_content(prompt)

    # ✅ Save to file
    os.makedirs("outputs", exist_ok=True)  # Ensure folder exists
    with open(f"outputs/{username}_persona.txt", "w", encoding="utf-8") as f:
        f.write(response.text)

    return response.text
