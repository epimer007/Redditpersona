import praw
import streamlit as st

# Use secrets for Streamlit Cloud or fallback to manual config
client_id = st.secrets["REDDIT_CLIENT_ID"] if "REDDIT_CLIENT_ID" in st.secrets else "your_client_id"
client_secret = st.secrets["REDDIT_CLIENT_SECRET"] if "REDDIT_CLIENT_SECRET" in st.secrets else "your_client_secret"
user_agent = "reddit_persona_app"

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
)

def fetch_user_content(username: str, post_limit=30, comment_limit=30):
    user = reddit.redditor(username)
    posts = [f"Post Title: {post.title}\n{post.selftext}" for post in user.submissions.new(limit=post_limit)]
    comments = [f"Comment: {comment.body}" for comment in user.comments.new(limit=comment_limit)]
    return posts, comments
