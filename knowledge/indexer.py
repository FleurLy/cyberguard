from mitre.mitre_data import techniques_attaque
import chromadb
from chromadb.utils import embedding_functions
import os
from dotenv import load_dotenv
load_dotenv()
path = os.getenv("CHROMA_DB_PATH")

pre_vectors = []
for key, value in techniques_attaque.items():
    vec = f"{key} {value['name']}: {value['description']} Detection: {value['detection']} Mitigation: {value['mitigation']}"
    pre_vectors.append(vec)

# ef = embedding_functions.DefaultEmbeddingFunction()


client = chromadb.PersistentClient(path=path)
collection = client.get_or_create_collection(name="mitre_techniques")

collection.add(
    documents=pre_vectors,        # liste de strings
    ids=list(techniques_attaque.keys())  # ["T1110", "T1059", "T1078"]
)

results = collection.query(
    query_texts=["ssh authentication failure"],
    n_results=2  # retourne les 2 techniques les plus proches
)

print(results)