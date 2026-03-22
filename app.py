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
    file_name = os.path.basename(uploaded_file.name)  # ✅ extract clean filename
    save_path = os.path.join(working_dir, file_name)   # ✅ build full path
    
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    with st.spinner("Processing document...⏳"):
        process_document = create_vector_db(uploaded_file.name)  # ✅ pass save_path not uploaded_file.name
    
    if process_document:
        st.success("Document processed successfully! ✅")
    else:
        st.error("⚠️ Could not process this PDF. Please try a different file.")

user_question = st.text_area("Ask your question about the document below")

if st.button("Answer➤"):
    answer = question_answer(user_question)
    st.markdown("Response")
    st.markdown(answer)
