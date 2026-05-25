from collector import SecurityEvent, LogCollector
import chromadb
import os
from dotenv import load_dotenv
load_dotenv()
path = os.getenv("CHROMA_DB_PATH")

class KnowledgeAgent:
    def __init__(self):
        client = chromadb.PersistentClient(path=path)
        self.collection = client.get_or_create_collection(name="mitre_techniques")
    
    def query(self, event: SecurityEvent):
        collection = self.collection
        requete = f"{event.timestamp}  {event.source_ip}  {event.event_type}  {event.severity}"
        

        results = collection.query(
            query_texts=[requete],
            n_results=2  # retourne les 2 techniques les plus proches
        )

        documents = results['documents'][0]
        return "\n".join(documents)

    
# from collector import LogCollector

# line = "May  3 14:22:01 server sshd[1234]: Failed password for root from 185.220.101.5"
# collector = LogCollector(line)
# event = collector.parse()

# agent = KnowledgeAgent()
# agent.query(event)