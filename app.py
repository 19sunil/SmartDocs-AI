from endee_db import load_documents
from search import semantic_search

def main():

    print("Loading documents into Endee...")
    load_documents()

    while True:

        query = input("\nEnter your query (or type exit): ")

        if query.lower() == "exit":
            break

        semantic_search(query)

if __name__ == "__main__":
    main()