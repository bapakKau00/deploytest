import streamlit as st
import streamlit.components.v1 as components

# Streamlit App Title
st.title("BankingBuddy with Animated Background")

# Custom HTML and CSS for Animated Background
background_html = """
<style>
body {
    margin: 0;
    overflow: hidden;
}

.animated-bg {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(45deg, #ff9a9e, #fad0c4, #fbc2eb, #a6c1ee);
    background-size: 400% 400%;
    animation: gradientAnimation 10s ease infinite;
    z-index: -1;
}

@keyframes gradientAnimation {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
</style>

<div class="animated-bg"></div>
"""

# Insert the animated background into the app
components.html(background_html, height=0)

# Main App Content
st.write("Welcome to BankingBuddy! Enjoy the animated background.")
