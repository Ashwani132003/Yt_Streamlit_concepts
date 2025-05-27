import streamlit as st
import streamlit.components.v1 as components

st.title("Streamlit Button Triggering JS Alert")

# Streamlit button
if st.button("Click Me"):
    # Inject JS alert via HTML on button press
    components.html(
        """
        <script type="text/javascript">
            alert("Hello from JavaScript!");
        </script>
        """,
        height=0,
    )

