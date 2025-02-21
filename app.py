import streamlit as st
import openai
import json

# OpenAI API Key
openai.api_key = "your_openai_api_key"

def search_case_law(query):
    """Uses OpenAI's LLM to retrieve relevant case law summaries."""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a legal assistant providing case law summaries."},
            {"role": "user", "content": f"Find case laws related to: {query}"}
        ]
    )
    return response["choices"][0]["message"]["content"]

st.title("AI-Powered Case Law Research Assistant")

query = st.text_area("Enter Legal Query")
if st.button("Search Case Law"):
    if query.strip():
        case_law_summary = search_case_law(query)
        st.write("### Case Law Summary")
        st.write(case_law_summary)
    else:
        st.warning("Please enter a legal query to search.")
