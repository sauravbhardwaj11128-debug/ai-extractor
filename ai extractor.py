import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("AI Powered Data Extraction")

text = st.text_area("Enter Customer Text")

if st.button("Extract"):

    prompt = f"""
Extract the following details from the text.

- customer_name
- travel_dates
- destination

Return only valid JSON.

Text:
{text}
"""

    response = model.generate_content(prompt)

    st.write(response.text)
