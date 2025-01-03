import streamlit as st
import streamlit.components.v1 as components

st.title("BankingBuddy Homepage")

# Embed Canva HTML with autoplay attempt
html_code = """
<div style="position: relative; width: 100%; height: 0; padding-top: 56.2225%;
 padding-bottom: 0; box-shadow: 0 2px 8px 0 rgba(63,69,81,0.16); margin-top: 1.6em; margin-bottom: 0.9em; overflow: hidden;
 border-radius: 8px; will-change: transform;">
  <iframe loading="lazy" style="position: absolute; width: 100%; height: 100%; top: 0; left: 0; border: none; padding: 0;margin: 0;"
    src="https://www.canva.com/design/DAGbFmi2_TI/7jAaNC635Y1VUdfGgl7aUg/view?embed&autoplay=1" allowfullscreen="allowfullscreen" allow="fullscreen">
  </iframe>
</div>
<a href="https://www.canva.com/design/DAGbFmi2_TI/7jAaNC635Y1VUdfGgl7aUg/view?utm_content=DAGbFmi2_TI&utm_campaign=designshare&utm_medium=embeds&utm_source=link" 
   target="_blank" rel="noopener">BankingBuddy</a> by Izat Hakimi
"""
components.html(html_code, height=600)
