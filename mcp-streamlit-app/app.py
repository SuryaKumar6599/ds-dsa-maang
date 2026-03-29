import streamlit as st
from llm.client import call_mcp

st.title("🧠 Local MCP AI App")

tool = st.selectbox("Select Tool", ["calculator", "summarize"])

if tool == "calculator":
    a = st.number_input("A", value=0)
    b = st.number_input("B", value=0)

    if st.button("Run"):
        result = call_mcp("calculator", {"a": a, "b": b})
        st.success(result)

elif tool == "summarize":
    text = st.text_area("Enter text")

    if st.button("Summarize"):
        result = call_mcp("summarize", {"text": text})
        st.success(result)