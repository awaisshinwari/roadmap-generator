import streamlit as st
from groq import Groq

st.set_page_config(page_title="Roadmap Generator", page_icon="🗺️")
st.title("🗺️ AI Learning Roadmap Generator")

api_key = st.sidebar.text_input("Groq API Key", type="password")
field = st.text_input("Kya seekhna hai?", placeholder="e.g. Python, Web Development")
level = st.selectbox("Level", ["Beginner", "Intermediate", "Advanced"])
time = st.selectbox("Time", ["1 Week", "1 Month", "3 Months", "6 Months"])

if st.button("Generate Roadmap 🚀"):
    if not api_key:
        st.error("Pehle sidebar me API Key dalo!")
    else:
        with st.spinner("Roadmap ban raha hai..."):
            client = Groq(api_key=api_key)
            prompt = f"Make detailed learning roadmap for {field}, Level {level}, Time {time}. Give week by week topics, resources, practice tasks in Markdown."
            chat = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}]
            )
            st.markdown(chat.choices[0].message.content)
