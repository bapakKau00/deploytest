import streamlit as st
import streamlit.components.v1 as components

st.title("BankingBuddy Homepage")

# Embed Canva HTML
html_code = """
<iframe src="https://www.canva.com/design/DAGbFmi2_TI/7jAaNC635Y1VUdfGgl7aUg/view" 
        width="800" height="600" style="border:none;"></iframe>
"""
components.html(html_code, height=600)


