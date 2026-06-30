from langsmith._openapi_client.types import OnlineLlmEvaluator
from langchain_openai import ChatOpenAI
from langchain_core import ChatPromptTemplate,StrOutputParser
# pyrefly: ignore [missing-import]
from langchain_community.llms import Ollama

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

llm=Ollama(model="llama2")
output_parser=StrOutputParser()
chain=promp|llm|output_parser


if user_input:
    st.write(chain.invoke({'question':user_input}))

