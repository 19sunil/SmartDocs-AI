# SmartDocs AI 🔎

Semantic Document Search using AI embeddings and vector similarity search.

## Project Overview
SmartDocs AI is an AI-powered semantic search system that retrieves documents based on meaning rather than exact keyword matches. Traditional search systems rely heavily on keyword matching, which often fails to understand the intent behind user queries.

This project uses transformer-based embeddings to convert text into numerical vectors and performs similarity search to find the most relevant documents. By comparing vector embeddings, the system can retrieve information based on semantic meaning rather than exact words.

The project demonstrates an AI workflow involving embedding generation, vector storage, and semantic retrieval.

## Problem Statement
Organizations often manage large collections of documents such as knowledge bases, FAQs, manuals, and internal documentation. Traditional keyword-based search systems struggle to retrieve relevant information when queries are phrased differently.

This project solves that challenge by implementing semantic search using vector embeddings and similarity search.

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
- Python  
- Sentence Transformers  
- FAISS (vector similarity search), FAISS is used locally to simulate vector storage, while Endee would be used in production.
- NumPy  
- Endee (conceptual vector database integration)

## How Endee is Used
Vector databases store embeddings and allow fast similarity search across large datasets.

This project demonstrates the workflow used in systems that use vector databases like Endee. For simplicity, FAISS is used as a local vector index to simulate the embedding storage and search process.

In production systems, Endee can replace the local vector index to provide scalable and efficient semantic retrieval.

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
