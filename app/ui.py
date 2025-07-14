import streamlit as st
from app.utils import extract_username
from app.reddit_scraper import fetch_user_content
from app.gemini_analyzer import generate_user_persona

def run_ui():
    # Minimal CSS: only change title and button color
    st.markdown("""
    <style>
    .main-title {
        color: #2563eb !important;
        font-size: 2.5em !important;
        font-weight: 700 !important;
        text-align: center;
        margin-bottom: 0.2em;
    }
    .stButton>button {
        background: linear-gradient(90deg, #2563eb 0%, #38bdf8 100%) !important;
        color: #fff !important;
        border: none !important;
        border-radius: 6px !important;
        font-weight: 600 !important;
        font-size: 1.08em !important;
        padding: 0.5em 1.5em !important;
        margin-top: 0.5em;
    }
    .stButton>button:hover {
        filter: brightness(1.08);
    }
    </style>
    """, unsafe_allow_html=True)

    st.set_page_config(page_title="Reddit User Persona Generator", page_icon="🤖")
    st.markdown("<h1 class='main-title'>🤖 Reddit User Persona Generator</h1>", unsafe_allow_html=True)

    url = st.text_input("🔗 Enter Reddit Profile URL (e.g. https://www.reddit.com/user/example_user/)")

    if st.button("✨ Generate Persona") and url:
        username = extract_username(url)
        if not username:
            st.error("❌ Invalid Reddit profile URL.")
            return

        with st.spinner("⏳ Scraping Reddit data and analyzing with Gemini..."):
            try:
                posts, comments = fetch_user_content(username)
                persona_text = generate_user_persona(username, posts, comments)

                st.subheader("🧠 Generated User Persona:")
                st.text_area("Persona", persona_text, height=400)

                st.download_button(
                    label="📄 Download Persona Report",
                    data=persona_text,
                    file_name=f"{username}_persona.txt",
                    mime="text/plain"
                )
            except Exception as e:
                st.error(f"⚠️ Error: {e}")
