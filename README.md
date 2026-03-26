# SmartDocs AI 🔎

Semantic Document Search using AI embeddings and vector similarity search.

## Project Overview
SmartDocs AI is an AI-powered semantic search system that retrieves documents based on meaning rather than exact keyword matches. Traditional search systems rely heavily on keyword matching, which often fails to understand the intent behind user queries.

This project uses transformer-based embeddings to convert text into numerical vectors and performs similarity search to find the most relevant documents. By comparing vector embeddings, the system can retrieve information based on semantic meaning rather than exact words.

The project demonstrates an AI workflow involving embedding generation, vector storage, and semantic retrieval.

## Problem Statement
Organizations often manage large collections of documents such as knowledge bases, FAQs, manuals, and internal documentation. Traditional keyword-based search systems struggle to retrieve relevant information when queries are phrased differently.

This project solves that challenge by implemening semantic search using vector embeddings and similarity search.

## System Architecture

User Query  
↓  
Embedding Model (Sentence Transformers)  
↓  
Query Vector  
↓  
Vector Index / Vector Database  
↓  
Similarity Search  
↓  
Top Relevant Documents  

## Technologies Used

- **Python** – Core programming language used to build the project.
- **Sentence Transformers** – Used to generate semantic embeddings from text using the `all-MiniLM-L6-v2` model.
- **FAISS** – Used for local vector indexing and similarity search.
- **NumPy** – Used for numerical operations and vector handling.
- **Endee (Vector Database)** – Intended vector database for scalable storage and similarity search of embeddings in production environments.
- **Git & GitHub** – Used for version control and project hosting.

## How Endee is Used

Vector databases store high-dimensional embeddings and enable fast similarity search across large datasets. They are widely used in modern AI systems such as semantic search, recommendation engines, and Retrieval-Augmented Generation (RAG).

In this project, documents are converted into vector embeddings using the Sentence Transformers model `all-MiniLM-L6-v2`. These embeddings capture the semantic meaning of the text and allow the system to retrieve documents based on similarity instead of exact keyword matching.

For local execution and demonstration, FAISS is used as a lightweight vector index to store embeddings and perform similarity search. This allows the project to run easily on a local machine without requiring external infrastructure.

However, the system architecture is designed to be compatible with the **Endee vector database**. In a real production environment, document embeddings would be stored and queried using Endee, enabling scalable vector indexing, efficient similarity search, and integration with AI workflows such as semantic search and RAG pipelines.

## Project Structure
```
endee-ai-semantic-search
│
├── app.py
├── embedder.py
├── endee_db.py
├── search.py
├── data.txt
├── requirements.txt
└── README.md
```

## Setup Instructions

### Clone the repository
```
git clone https://https://github.com/19sunil/SmartDocsAI
cd SmartDocsAI
```

### Create virtual environment
```
python -m venv .venv
```

Activate environment

Windows
```
.venv\Scripts\activate
```

Linux / Mac
```
source .venv/bin/activate
```

### Install dependencies
```
pip install -r requirements.txt
```

### Run the application
```
python app.py
```

## Example Query
```
Enter your query: AI Technology
```

Example Output
```
Artificial Intelligence is transforming industries.
Deep learning is widely used in computer vision.
Machine learning improves predictive analytics.
```

## Practical Use Cases
- Enterprise knowledge base search  
- AI-powered FAQ systems  
- Customer support documentation retrieval  
- Recommendation systems  
- Retrieval-Augmented Generation (RAG)

## Future Improvements
- Integrate Endee as the primary vector database  
- Build a web interface using Streamlit  
- Add document upload support  
- Integrate large language models for RAG workflows  

## Author
Paikaray Sunil Bishnu Prasad |
B.Tech CSE | Artificial Intelligence & Machine Learning
