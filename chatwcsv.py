import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

# Initialize the LLM model
openai_key=os.getenv("OPENAI_API_KEY")
llm=OpenAI(api_token=openai_key)

def main():
    st.title("Chat with CSV")
    messages = []

    # File upload section
    uploaded_file = st.file_uploader("Choose a file to upload", type=["csv"]) 
    if uploaded_file is not None:
        # convert the data to a pandas smart DataFrame
        df = pd.read_csv(uploaded_file)
        chat_df = SmartDataframe(df,config={"llm": llm})

    user_input = st.chat_input(placeholder="Enter your message") 
    if user_input:
        messages.append({"role": "user", "content": user_input})
        response = chat_df.chat(user_input)  
        messages.append({"role": "assistant", "content": str(response)})

    # Display chat messages
    for message in messages:
        if message["role"] == "user":
            st.write(message["content"])
        else:
            st.write(message["content"])  # Add an avatar if desired
    
if __name__ == "__main__":
    main()