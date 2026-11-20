from ingest import collection

question = input("Ask something: ")
results = collection.query(query_texts=[question], n_results=3)

for text, info in zip(results["documents"][0], results["metadatas"][0]):
    print("\n---", info["source"], "| page", info["page"], "---")
    print(text[:300])
