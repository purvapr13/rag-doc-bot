# RAG-Doc-Bot: A Retrieval-Augmented Generation Document Bot

## About
**RAG-Doc-Bot** is an intelligent document retrieval and question-answering system built using **FastAPI**, **LangChain**, **ChromaDB**, and **Hugging Face** embeddings. It allows you to extract, store, and search document content efficiently to generate precise answers based on the context of the documents.

---

## Table of Contents

- [About](#about)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup](#setup)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [Testing](#testing)
  - [Docker](#docker)
- [Cache and Retrieval](#cache-and-retrieval)
- [License](#license)
  

---

## Features

- **Document Ingestion**: Supports PDF, DOCX, and other document types.
- **Searchable Vector Store**: ChromaDB is used to store document embeddings for fast retrieval.
- **Custom QA System**: LangChain framework helps retrieve relevant documents and generate answers.
- **Caching**: Implements caching for efficient answer retrieval.
- **FastAPI Backend**: A FastAPI-powered server to handle API requests.

---

## Tech Stack

- **Backend**: FastAPI
- **Vector Database**: ChromaDB
- **Document Embedding**: Hugging Face's Open Source MiniLM (all-MiniLM-L6-v2 model)
- **Retrieval**: LangChain
- **Language Model for Generation**: Mistral from Ollama (Open Source)
- **Containerization**: Docker
- **Cache**: Cachetools (for caching answers)

---

## Setup

### Requirements

- Python >= 3.8
- Docker (optional for containerization)
- CUDA-enabled GPU (optional for Hugging Face model acceleration)

### Local Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/purvapr13/rag-doc-bot.git
   cd rag-doc-bot

2. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
  ✅ If you're using CUDA, make sure to install PyTorch with GPU support

3. **📁 Create the `models/all-MiniLM-L6-v2/` folder manually inside the `app/` directory if it doesn't already exist.**

You need to manually download the [`all-MiniLM-L6-v2`](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) model and place it in the following directory:



## Running the Application

1. From the app folder run python main.py to start the application locally on port 8000:
     ```bash
        python main.py

2. To start streamlit UI, open another terminal and run: 
     ```bash
      streamlit run .\streamlit_app.py
It will start the streamlit UI as below, where you can ask questions.

<img width="587" alt="image" src="https://github.com/user-attachments/assets/7d12c6b5-4ed3-44f8-b4c6-3b70d5c6216d" />

 

## 🚢 Docker

### 🛠️ Build the Image

    ```bash
    docker-compose build

### ▶️ Start the App

    ```bash
    docker-compose up


> ⚠️ **Note**  
> 
> - The Hugging Face model (`all-MiniLM-L6-v2`) should be **downloaded manually and mounted locally** into the container.  
> - The `app/chroma_db` directory is **created at runtime** and is **not included** in the Docker image to keep it lightweight.
  

## Testing

Run automated tests using **pytest**:

pytest app/tests

### Tests include:

- ✅ **Valid and invalid API requests**
- 🚨 **Internal error handling**
- 📄 **Response content validation**

## Caching System

This app uses an **in-memory cache** (via [`cachetools`](https://pypi.org/project/cachetools/)) to store previously answered questions.

### Key Benefits

- 🧠 **Caches only successfully answered questions**
- ⚡ **Speeds up repeat queries significantly**
- 🔒 **Thread-safe and memory-efficient**







## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more information.

---

## Acknowledgements

- [**Hugging Face**](https://huggingface.co/) for transformer models  
- [**LangChain**](https://www.langchain.com/) for simplifying retrieval pipelines  
- [**Chroma**](https://www.trychroma.com/) as the vector database  
- [**Ollama**](https://ollama.ai/) for local language model integration  


