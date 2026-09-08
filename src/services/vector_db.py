#https://docs.trychroma.com/docs/overview/getting-started
import chromadb
import uuid
from query_input import input_query
chroma_client = chromadb.PersistentClient(path="./Policy_data")
from extract_from_pdf import chunking,filepath
#from embeddings import embed
def retrieval(q):
    # switch \`create_collection\` to \`get_or_create_collection\` to avoid creating a new collection every time
    collection = chroma_client.get_or_create_collection(name="my_collection")

    # print(type(collection.peek()))
    # print(type(collection.get()))
    # if "documents" in collection.get():
    #     print(True)
    #     documents=collection.get()["documents"]
    # else:
    #     print(False)
    #     documents=chunking(filepath)
    documents=collection.get()['documents'] if collection.get()['documents'] else chunking(filepath)
    # switch \`add\` to \`upsert\` to avoid adding the same documents every time
    collection.upsert(
        #embeddings=embed(chunking(filepath)),
        documents=documents,
        ids=[str(uuid.uuid4()) for i in documents],
        metadatas=[{"line":line} for line in range(len(documents))]
    )

    results = collection.query(
        query_texts=[q], # Chroma will embed this for you
        n_results=1 # how many results to return
    )

    return results['documents'][0][0]

#print(retrieval())
        