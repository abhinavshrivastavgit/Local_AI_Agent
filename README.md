# 🚀 Local AI RAG System — Private Document Chatbot

A fully local **Retrieval-Augmented Generation (RAG)** system that allows you to chat with your own data using local LLMs — without sending any information to external APIs.

This project demonstrates how modern AI systems used in companies actually work internally.

---

# 🧠 What This Project Does

This system allows users to:

- Load a dataset or documents
- Convert them into embeddings
- Store them inside a vector database
- Retrieve relevant context
- Generate answers using a **local LLM**

Everything runs **completely offline**.

No OpenAI API.  
No external services.  
100% local AI.

---

# 🏗 System Architecture

User Question  
↓  
Retriever (Vector Search - ChromaDB)  
↓  
Relevant Context Retrieved  
↓  
Prompt Template  
↓  
Local LLM (Ollama - Llama Model)  
↓  
Generated Answer

This is the same architecture used in many production AI systems.

---

# 🔥 Why This Project Is Important

Most developers only use API-based AI tools.

But real AI engineers build systems that:

- Protect sensitive data
- Work offline
- Scale with internal datasets
- Use retrieval-based intelligence

This project demonstrates that workflow.

---

# ⚙️ Tech Stack

**LLM Runtime**  
Ollama

**LLM Model**  
Llama 3.2

**Embeddings Model**  
nomic-embed-text

**Vector Database**  
ChromaDB

**AI Framework**  
LangChain

**Programming Language**  
Python

**Dataset**  
Restaurant Reviews CSV

---

# 📂 Project Structure

```
Local_AI_AGENT
│
├── data/
│   └── realistic_restaurant_reviews.csv
│
├── vector.py
│   Handles:
│   - Data loading
│   - Document conversion
│   - Embeddings
│   - Vector database creation
│
├── main.py
│   Runs:
│   - Chat interface
│   - Retrieval system
│   - LLM responses
│
├── chroma_db/
│   Vector database storage
│
├── requirements.txt
│   Project dependencies
│
└── README.md
```

---

# 🧩 Core Components

### 1. Data Loader
Reads dataset from CSV file using Pandas.

### 2. Document Processor
Converts dataset rows into LangChain documents.

### 3. Embedding Generator
Creates semantic embeddings using:

```
nomic-embed-text
```

### 4. Vector Database
Stores embeddings using:

```
ChromaDB
```

### 5. Retriever
Searches for the most relevant context based on the user question.

### 6. Local LLM
Generates final answers using:

```
Llama 3.2
```

---

# 🛠 Installation

## Step 1 — Install Ollama

Download from:

https://ollama.com/

---

## Step 2 — Pull Required Models

Run this in terminal:

```
ollama pull llama3.2
ollama pull nomic-embed-text
```

---

## Step 3 — Install Python Dependencies

```
pip install -r requirements.txt
```

If requirements file is missing:

```
pip install chromadb
pip install langchain
pip install langchain-ollama
pip install langchain-community
pip install pandas
pip install pypdf
```

---

# ▶️ Running the Project

Start Ollama:

```
ollama serve
```

Run the chatbot:

```
python main.py
```

---

# 💬 Example Questions

You can ask:

- Which restaurant has the best reviews?
- What do customers complain about the most?
- Summarize customer feedback.
- Which place has the best pizza?

---

# 🧪 Learning Goals Behind This Project

This project helped me understand:

- How RAG systems actually work
- How embeddings power semantic search
- How vector databases store knowledge
- How local LLMs can replace cloud APIs
- How to structure real AI projects

---

# 🚀 Future Improvements

Planned upgrades:

- PDF document support
- Multi-dataset ingestion
- Web UI interface
- Conversation memory
- n8n automation integration
- API endpoint for deployment
- Docker containerization

---

# 👨‍💻 Author

Abhinav Shrivastav

Building projects in:
- AI
- Data Engineering
- Automation
- Local LLM Systems

---

# 🌟 Project Vision

The goal is to move from:

Using AI tools  
to  
Building AI systems.

---

If you found this interesting, feel free to connect or follow the journey.
