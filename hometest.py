import streamlit as st

# CSS for gradient animation
gradient_animation_css = """
<style>
.stApp > header {
  background-color: transparent;
}

.stApp {
  background: linear-gradient(45deg, #c28b99 10%, #435420 45%, #435420 55%, #c28b99 90%);
  animation: my_animation 20s ease infinite;
  background-size: 200% 200%;
  background-attachment: fixed;
}

@keyframes my_animation {
  0% {background-position: 0% 0%;}
  50% {background-position: 100% 100%;}
  100% {background-position: 0% 0%;}
}
</style>
"""

# Apply the CSS to Streamlit app
st.markdown(gradient_animation_css, unsafe_allow_html=True)

# Streamlit content
st.title("Gradient Background Animation")
st.write("This background changes smoothly, creating a dynamic, animated effect!")
