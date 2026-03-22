import os
import streamlit as st
from dotenv import load_dotenv
#from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_classic.chains import RetrievalQA
from langchain_community.document_loaders import PyPDFLoader

load_dotenv()

working_dir = os.path.dirname(os.path.abspath((__file__)))

embed_model = HuggingFaceEmbeddings()

llm= ChatGroq(
    model = "llama-3.3-70b-versatile",
    temperature= 0.2
)

def create_vector_db(file_name):
    try: 
        loader =PyPDFLoader(f"{working_dir}/{file_name}")
        documents = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 2000,
        chunk_overlap = 200
    )
        text_chunks = text_splitter.split_documents(documents)
    #Store the document chunks in a Chroma vector database
        vector_db = Chroma.from_documents(
        embedding=embed_model,
        documents= text_chunks,
        persist_directory= f"{working_dir}/vector_store_db"
    )
        return "Vector store created successfully"
    except Exception as e:
        st.error(f"⚠️ Could not process this PDF. It may be corrupted or password-protected. Please try a different file.")
        st.stop()
def question_answer(user_question):
    vector_db = Chroma(
        embedding_function= embed_model,
        persist_directory= f"{working_dir}/vector_store_db"
    )
    #Create a retriever for document search
    retriever = vector_db.as_retriever()

    #Create a RetrievalQA chain to answer user question using Groq model

    qa_chain = RetrievalQA.from_chain_type(
        llm= llm,
        retriever = retriever,
        chain_type = "stuff",
    )
    response = qa_chain.invoke({"query": user_question})
    answer = response["result"]
    return answer
