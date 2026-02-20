# 🤖 Private Policy Intel: Local RAG Chatbot

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Ollama](https://img.shields.io/badge/LLM-Ollama-white.svg)](https://ollama.com/)
[![VectorDB](https://img.shields.io/badge/VectorDB-Chroma-orange.svg)](https://www.trychroma.com/)
[![Automation](https://img.shields.io/badge/Workflow-n8n-red.svg)](https://n8n.io/)

### 🌟 Project Vision

**Rag Chatbot 1** is a privacy-first, enterprise-grade Retrieval-Augmented Generation (RAG) system. It allows firms to query "heavy" internal documentation (like Flipkart's corporate policies) with **100% data sovereignty**. Unlike cloud-based solutions, this system runs entirely on local hardware, ensuring that sensitive data never leaves the firm's private network.

---

### 🚀 Key Features

- **Zero-Cloud Privacy:** No data is sent to OpenAI or third-party servers. All processing is local.
- **Intelligent Retrieval:** Uses `nomic-embed-text` to understand semantic intent rather than simple keyword matching.
- **Visual Orchestration:** Integrated with **n8n** for easy workflow management and task automation.
- **Persistent Memory:** Powered by **ChromaDB**, ensuring fast and reliable access to indexed policy data.

---

### 🛠️ Tech Stack

- **LLM Engine:** [Ollama](https://ollama.com/) (running Llama 3.2)
- **Vector Database:** [ChromaDB](https://www.trychroma.com/)
- **Workflow Automation:** [n8n](https://n8n.io/)
- **Orchestration:** [LangChain](https://www.langchain.com/)
- **Data Format:** CSV, TXT, PDF

---

### 📂 Directory Structure

```text
Local_AI_AGENT
│
├── data/
│   └── realistic_restaurant_reviews.csv
│
├── main.py
├── vector.py
├── README.md
└── requirements.txt

```

---

### ⚙️ Installation & Setup

- **Pull Local Models**
  Ensure Ollama is installed and run:

```Bash
ollama pull llama3.2
ollama pull nomic-embed-text
```

- **Setup Python Environment**

```Bash
pip install chromadb langchain-ollama langchain-community pypdf pandas

```
