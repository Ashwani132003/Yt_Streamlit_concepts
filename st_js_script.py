import streamlit as st
import streamlit.components.v1 as components

st.title("Run Local JS File in Streamlit")

# Read JS code from file
with open("my_script.js", "r") as js_file:
    js_code = js_file.read()

# Wrap in HTML <script> tag
html_code = f"""
    <script type="text/javascript">
      {js_code}
    </script>
  <body>
    <button onclick="showMessage()">Click to run JS from file</button>
  </body>
"""

components.html(html_code, height=200)
