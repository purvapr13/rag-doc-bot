# RAG-Doc-Bot: A Retrieval-Augmented Generation Document Bot

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
  - [API Endpoints](#api-endpoints)
- [Cache and Retrieval](#cache-and-retrieval)
- [Contributing](#contributing)
- [License](#license)

---

## About

**RAG-Doc-Bot** is designed to help organizations and individuals retrieve answers from a collection of documents using advanced document search and AI-based question answering. Using **ChromaDB** as a vector store and **Hugging Face's MiniLM model**, the bot performs efficient text search and integrates external knowledge sources (using models like **Ollama**) to provide accurate and contextual answers.

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
- **Document Embedding**: Hugging Face's MiniLM (all-MiniLM-L6-v2 model)
- **Retrieval**: LangChain
- **Language Model for Generation**: Ollama (or any other LLM)
- **Containerization**: Docker
- **Task Queue (for heavy processing)**: Threading and asyncio
- **Cache**: Cachetools (for caching answers)

---

## Setup

### Requirements

- Python >= 3.8
- Docker (for containerization)
- CUDA-enabled GPU (optional for Hugging Face model acceleration)

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/rag-doc-bot.git
   cd rag-doc-bot


<img width="587" alt="image" src="https://github.com/user-attachments/assets/7d12c6b5-4ed3-44f8-b4c6-3b70d5c6216d" />

