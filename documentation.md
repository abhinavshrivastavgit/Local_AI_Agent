# 🤖 Local AI RAG Chatbot — Private Document Intelligence

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![LLM](<https://img.shields.io/badge/LLM-Local%20(Ollama)-white.svg>)](https://ollama.com/)
[![VectorDB](https://img.shields.io/badge/VectorDB-ChromaDB-orange.svg)](https://www.trychroma.com/)
[![Framework](https://img.shields.io/badge/Framework-LangChain-green.svg)](https://www.langchain.com/)

---

# 🚀 Project Overview

Local AI RAG Chatbot is a fully local Retrieval-Augmented Generation (RAG) system that allows you to chat with your own data securely.

Instead of sending data to cloud-based AI services, this project runs completely on your local machine using Ollama. It indexes documents, converts them into embeddings, stores them in a vector database, and retrieves the most relevant context before generating responses.

This makes it ideal for:

- Private company documents
- Internal knowledge bases
- Research datasets
- Learning how real-world RAG systems work

The current version of this project demonstrates the system using a dataset of restaurant reviews, but the same architecture works for PDFs, TXT files, or internal company documents.

---

# 🎯 Key Features

- Local-first AI system
- No external API calls
- Runs completely offline
- Semantic search using embeddings
- Fast retrieval using vector database
- Scalable architecture for enterprise use cases
- Clean and modular Python structure

---

# 🧠 How the System Works

The chatbot follows a standard RAG pipeline:

1. Load dataset (CSV / documents)
2. Convert text into embeddings
3. Store embeddings in ChromaDB
4. Retrieve relevant context based on user query
5. Send context to local LLM
6. Generate accurate response

Flow:

User Question  
↓  
Retriever (ChromaDB)  
↓  
Relevant Context  
↓  
Local LLM (Ollama - Llama Model)  
↓  
Final Answer

---

# 🛠 Tech Stack

LLM Engine: Ollama (Local LLM runtime)  
Model Used: Llama 3.2  
Embeddings Model: nomic-embed-text  
Vector Database: ChromaDB  
Framework: LangChain  
Programming Language: Python  
Dataset Format: CSV

---

# 📂 Directory Structure

Local_AI_AGENT
│
├── data/
│ └── realistic_restaurant_reviews.csv
│
├── main.py # Runs the chatbot
├── vector.py # Handles embeddings and vector database
├── README.md # Project documentation
├── requirements.txt # Project dependencies
│
└── chroma_db/ # Auto-generated vector database

---

# ⚙️ Installation & Setup

## 1. Install Ollama

Download and install Ollama from:
https://ollama.com/

Then pull the required models:

ollama pull llama3.2  
ollama pull nomic-embed-text

---

## 2. Install Python Dependencies

pip install chromadb  
pip install langchain  
pip install langchain-ollama  
pip install langchain-community  
pip install pandas  
pip install pypdf

Or run:

pip install -r requirements.txt

---

# ▶️ Running the Project

Step 1 — Start Ollama

ollama serve

Step 2 — Run the chatbot

python main.py

The system will:

- Load the dataset
- Create embeddings
- Store them in ChromaDB
- Start the chat interface

---

# 💡 Example Queries

You can ask questions like:

- What are customers saying about food quality?
- Which restaurant has the best reviews?
- Summarize common complaints in the dataset.
- What do people think about service?

---

# 🔒 Why This Project Matters

Most AI systems today rely heavily on cloud APIs.

This project demonstrates how to build:

- Private AI systems
- Enterprise-ready architecture
- Secure document intelligence tools
- Production-style RAG pipelines

This is the same concept used in modern AI products inside companies.

---

# 📈 Future Improvements

- Add PDF document ingestion
- Add UI (Streamlit / Web App)
- Multi-document support
- Conversation memory
- Enterprise document search
- Deployment using Docker

---

# 👨‍💻 Author

Abhinav Shrivastav  
AI / Data Enthusiast  
Building Local AI Systems

---

# ⭐ Project Goal

The goal of this project is not just to build a chatbot, but to understand how real AI systems are designed and deployed locally without relying on external AI providers.
