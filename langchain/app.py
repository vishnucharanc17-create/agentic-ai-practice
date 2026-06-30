from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

#langsmith tracing
os.environ["LANCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY", "")
os.environ["OPENAI_API_KEY"]=os.getenv("open_router_key", "")


#prompt template

promp=ChatPromptTemplate.from_messages([
    ("system","You are a helpful assistant. please respond to the user queries"),
    ("user","Question: {question}"),
]) 

st.title("langchain learning journal")
user_input=st.text_input("ask me question")

llm=ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    model="gpt-oss-120b"
)
output_parser=StrOutputParser()
chain=promp|llm|output_parser

if user_input:
    st.write(chain.invoke({'question':user_input}))

