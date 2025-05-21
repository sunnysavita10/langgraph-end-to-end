import streamlit as st
from langchain_core.messages import HumanMessage
from bot import chatbot

mybot=chatbot()
workflow=mybot()

# Set up the Streamlit app UI
st.title("ChatBot with LangGraph")
st.write("Ask any question, and I'll try to answer it!")

# Input text box for the question
question = st.text_input("Enter your question here:")

# Button to get the answer
if st.button("Get Answer"):
    if question:
        input={"messages": [HumanMessage(content=question)]}
        response=workflow.invoke(input)
        st.write("**Answer:**", response['messages'][-1].content)
    else:
        st.warning("Please enter a question to get an answer.")

# Additional styling (optional)
st.markdown("---")
st.caption("Powered by Streamlit and Transformers")
