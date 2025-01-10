import streamlit as st
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.agent_toolkits import create_sql_agent
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
)
import os
from dotenv import load_dotenv
load_dotenv()

openai_key=os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o", temperature=0, api_key=openai_key)
db = SQLDatabase.from_uri("sqlite:///tweets.db")

with open("prompt.txt", 'r') as file:
        system_prefix = file.read()

full_prompt = ChatPromptTemplate.from_messages(
    [
        ("system",system_prefix),
        ("human", "{input}"),
        MessagesPlaceholder("agent_scratchpad"),
    ]
)
agent = create_sql_agent(
    llm=llm,
    db=db,
    prompt=full_prompt,
    agent_type="openai-tools",
    verbose = True
)

if 'memory' not in st.session_state:
    st.session_state['memory'] = ChatMessageHistory(session_id="test-session")
if 'config' not in st.session_state:
    st.session_state['config'] = {"configurable": {"session_id": "test-session"}}

agent_with_chat_history = RunnableWithMessageHistory(
    agent,
    lambda session_id: st.session_state['memory'],
    input_messages_key="input",
    history_messages_key="chat_history",
)

st.set_page_config(
    page_title="Social Media Manager",
    page_icon="🤖",
    layout="wide"
)


st.title("Social Media Manager")


# check for messages in session and create if not exists
if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant", "content": "I am your social media manager who handles your twitter."}
    ]


# Display all messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


user_prompt = st.chat_input()

if user_prompt is not None:
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.write(user_prompt)


if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Loading..."):
            ai_response = agent_with_chat_history.invoke({"input": user_prompt},st.session_state['config'])["output"]
            print(ai_response)
            st.write(ai_response)
    new_ai_message = {"role": "assistant", "content": ai_response}
    st.session_state.messages.append(new_ai_message)