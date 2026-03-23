# 📄 Document QnA – RAG-Based Intelligent System

🔗 Live demo:  https://lnkd.in/euXp9UQF

An end-to-end **Retrieval-Augmented Generation (RAG)** system that enables users to ask natural-language questions over uploaded documents and receive context-aware, accurate answers powered by Large Language Models.

**🚀 Project Overview**

This project implements a **Document Question-Answering System** that bridges the gap between static documents and conversational AI.
Instead of relying on a language model’s parametric knowledge, this system:
* Ingests custom documents
* Transforms them into vector embeddings
* Stores them in a vector database
* Retrieves relevant context using semantic similarity
* Generates grounded answers using an LLM
  
This arechitecture ensures higher accuracy, reduced hallucinations

A simplified version of the system architecture is shown below:- 
<img width="1652" height="475" alt="github" src="https://github.com/user-attachments/assets/e2f2c1fa-13e2-42aa-8e41-a0e178c6c9cc" />

**✨ Key Features include:-**
 1) 📂 Multi-Document Ingestion
 2) 🔍 Semantic Search using Vector Similarity
 3) 🧠 Retrieval-Augmented Generation (RAG)
 4) ⚡ Fast Vector Storage with ChromaDB
 5) 🤗 Hugging Face Embedding Models
 6) 🧩 Modular LangChain Pipelines
 7) 🌐 Interactive Streamlit Deployment
 8) 🛡️ Reduced Hallucinations via Context Grounding

**📌 Project Workflow**

**1️⃣ Document Ingestion**
* Supports structured and unstructured documents
* Documents are loaded and split into semantic chunks
* Chunking improves retrieval accuracy and token efficiency

**2️⃣ Embedding Generation**
* Each document chunk is converted into a dense vector representation
* Uses Hugging Face embedding models
* Allows semantic understanding beyond keyword matching

**3️⃣ Vector Database Creation (ChromaDB)**
* Embeddings are stored in ChromaDB
* Enables fast similarity search using cosine distance
* Persistent and scalable vector storage

**4️⃣ Retrieval-Augmented Generation (RAG Pipeline)**
* User query is embedded
* Relevant document chunks are retrieved via similarity search
* Retrieved context is added into the LLM prompt
* The LLM generates context-aware responses

**5️⃣Streamlit Deployment**
* Clean and intuitive UI
* Upload documents
* Ask questions in real-time
* Receive instant AI-generated answers

**🛠️ Tech Stack**
* Python
* LangChain
* HuggingFace Transformers
* ChromaDB
* GROQ LLM
* Streamlit & Streamlit Cloud

**🧪 Use Cases**

* 📚 Research Paper QnA
* 🏢 Enterprise Document Search
* 📑 Legal & Financial Analysis
* 🧠 Knowledge Base Assistants
* 📖 Educational Tools


**🤝 Contributions**

Contributions are welcome!
Feel free to open issues, or suggest enhancements.
















