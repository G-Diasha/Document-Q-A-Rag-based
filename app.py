import os
import streamlit as st
from rag_utility import create_vector_db, question_answer

working_dir = os.path.dirname(os.path.abspath((__file__)))
st.set_page_config(
    page_title="RAG APP",
    page_icon="🛠️",
    layout="centered"
)
st.title("🌐 Document Q&A APP (RAG-based)")
uploaded_file = st.file_uploader("Please upload your PDF file", type=["pdf"])

if uploaded_file is not None:
    #define the save path
    save_path = os.path.join(working_dir, uploaded_file.name)
    #save the file
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    process_document = create_vector_db(save_path)
    st.info("Document processed successfully!")

user_question = st.text_area("Ask your question about the document below")
if st.button("Answer➤"):
    answer = question_answer(user_question)
    st.markdown("Response")
    st.markdown(answer)
