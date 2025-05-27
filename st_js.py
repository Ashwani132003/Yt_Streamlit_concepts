import streamlit as st
import streamlit.components.v1 as component

# Your javascript
js = """
alert("Hii there!!");
"""

# Wrapt the javascript as html code
html = f"<script>{js}</script>"

st.title("Javascript example")
component.html(html)