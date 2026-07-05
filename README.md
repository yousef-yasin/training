# AI Knowledge Base Assistant

## Overview

AI Knowledge Base Assistant is a Retrieval-Augmented Generation (RAG) system that answers user questions using only the documents stored in a local knowledge base.

The application processes multiple document formats, converts them into semantic embeddings, stores them in a Chroma Vector Database, retrieves the most relevant information based on semantic similarity, and generates accurate responses using Google's Gemini Large Language Model.

The system is designed to minimize hallucinations by restricting responses to the retrieved context only.

---

## Features

- Multi-format document support
- Automatic document ingestion
- Document chunking with overlap
- Semantic embeddings using Sentence Transformers
- ChromaDB vector database
- Semantic similarity search
- Google Gemini integration
- Hallucination prevention
- Modular project architecture

---

## Supported File Types

- PDF
- DOCX
- TXT
- Markdown
- CSV

---

## System Architecture

```
Knowledge Base
       │
       ▼
Document Reader
       │
       ▼
Text Chunking
       │
       ▼
Embedding Generation
       │
       ▼
ChromaDB
       │
       ▼
Semantic Retrieval
       │
       ▼
Google Gemini
       │
       ▼
Final Response
```

---

## Project Structure

```
training
│
├── app
│   ├── ingestion
│   │   ├── reader.py
│   │   └── chunker.py
│   │
│   ├── retrieval
│   │   ├── vector_store.py
│   │   └── retriever.py
│   │
│   ├── llm
│   │   └── gemini.py
│   │
│   ├── main.py
│   └── store.py
│
├── knowledge_base
├── chroma_db
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## Technologies

- Python
- Google Gemini API
- Google GenAI SDK
- ChromaDB
- Sentence Transformers
- HuggingFace Embedding Models
- PyPDF
- python-docx
- Pandas
- python-dotenv

---

## Workflow

### 1. Document Ingestion

The application scans all files inside the `knowledge_base` directory and extracts their textual content.

### 2. Chunking

Large documents are divided into overlapping chunks to improve retrieval quality and reduce language model context size.

### 3. Embedding Generation

Each chunk is transformed into a semantic vector using the Sentence Transformer model:

```
all-MiniLM-L6-v2
```

### 4. Vector Storage

Embeddings are stored inside ChromaDB together with metadata including:

- File name
- Chunk index
- Original text

### 5. Semantic Retrieval

User questions are converted into embeddings.

The system retrieves the most semantically similar chunks from the vector database.

### 6. Response Generation

Only the retrieved context is sent to Google Gemini.

The language model generates the final response without accessing external knowledge.

---

## Hallucination Prevention

If the retrieved similarity score is below the defined threshold, the assistant does not generate an answer and instead returns:

```
The information is not available in the Knowledge Base.
```

This prevents the model from generating unsupported information.

---

## Installation

Clone the repository

```bash
git clone https://github.com/your-username/training.git
```

Navigate to the project

```bash
cd training
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

Windows

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## Building the Vector Database

Place your documents inside the `knowledge_base` directory.

Run:

```bash
python app/store.py
```

This process:

- Reads all documents
- Splits text into chunks
- Generates embeddings
- Stores vectors inside ChromaDB

---

## Running the Application

Start the assistant:

```bash
python app/main.py
```

Example:

```
Ask your question:

What are the working hours?
```

Output:

```
Official working hours are from 9:00 AM to 5:00 PM.
```

Example:

```
Ask your question:

Who is the CEO of Apple?
```

Output:

```
The information is not available in the Knowledge Base.
```

---


## Author

Yousef Yasin


