# SmartDocsAI – Semantic Search using Endee
SmartDocs AI is an AI-powered semantic search system that retrieves documents based on meaning rather than exact keyword matches. Traditional search systems rely on keyword matching, which often fails to understand the intent behind user queries. This project uses transformer-based embeddings and vector similarity search to find the most relevant documents.

The system converts documents into vector embeddings and stores them in a vector index. When a user enters a query, the system converts the query into a vector and retrieves the most similar documents using semantic similarity.

This project demonstrates how vector databases such as Endee can be used in AI workflows for efficient semantic retrieval.


# Problem Statement
Organizations often manage large volumes of documents such as FAQs, manuals, and internal knowledge bases. Keyword-based search systems frequently fail to return the most relevant information.

This project solves that problem by implementing a semantic search system that understands the meaning of queries and retrieves relevant documents using vector embeddings.


# System Architecture
User Query
     │
     ▼
Embedding Model (Sentence Transformers)
     │
     ▼
Query Vector
     │
     ▼
Vector Database / Index
     │
     ▼
Similarity Search
     │
     ▼
Top Relevant Documents

# Technologies Used
Python, NumPy, Sentence Transformers, FAISS (for local vector indexing demonstration), Endee (conceptual vector database integration)

# How Endee is Used
In large-scale AI systems, embeddings are stored inside a vector database. This project demonstrates the workflow of generating embeddings and performing similarity search, which is the core functionality supported by Endee vector database.

For simplicity, FAISS is used locally to simulate the vector storage and search process. In production environments, Endee can replace the local vector index to provide scalable and efficient semantic search capabilities.

# Project Structure
endee-ai-semantic-search
│
├── app.py
├── embedder.py
├── endee_db.py
├── search.py
├── data.txt
├── requirements.txt
└── README.md

# Setup Instructions
1. Clone the repository - git clone 

2. Create virtual environment - python -m venv .venv
 
3. Activate it: Windows - .venv\Scripts\activate
 
4. Install dependencies - pip install -r requirements.txt

5. Run the application - python app.py

6. Enter your query: AI Technology 
 
Output: Artificial Intelligence is transforming industries.
Deep learning is widely used in computer vision.
Machine learning improves predictive analytics.

# Practical Use Cases
Enterprise knowledge base search
AI-powered FAQ retrieval
Customer support documentation search
Recommendation systems
Retrieval-Augmented Generation (RAG)

# Future Improvements
Integrate Endee as the production vector database
Add web interface using Streamlit
Integrate LLM for RAG-based answers
Support document uploads and large datasets

Author

Paikaray Sunil Bishnu Prasad |
B.Tech CSE | AI & Machine Learning Enthusiast


