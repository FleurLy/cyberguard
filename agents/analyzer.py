from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

load_dotenv()
ma_cle = os.getenv("GROQ_API_KEY")
class Analyzer:
    def __init__(self, security_event):
        self.security_event = security_event

    def prompt(self):
        chaine = "Tu es un expert en cybersécurité.\n"
        chaine += "Analyse cet événement de sécurité :\n"
        chaine += "- Timestamp : " + self.security_event.timestamp + "\n"
        chaine += "- IP source : " + self.security_event.source_ip + "\n"
        chaine += "- Type : " + self.security_event.event_type + "\n"
        chaine += "- Sévérité : " + self.security_event.severity + "\n"
        chaine += "Réponds avec :\n"
        chaine += "- Le type d'attaque détecté\n"
        chaine += "- Le niveau de sévérité (low/medium/high/critical)\n"
        chaine += "- Une explication courte"
        return chaine
    
    def connexion_llm(self):
        
        llm = ChatGroq(api_key=ma_cle, model="llama-3.1-8b-instant")
        response = llm.invoke([HumanMessage(content=self.prompt())])
        return response.content
    
import sys
sys.path.append("..")
from collector import LogCollector

line = "May  3 14:22:01 server sshd[1234]: Failed password for root from 185.220.101.5"
collector = LogCollector(line)
event = collector.parse()

analyzer = Analyzer(event)
print(analyzer.connexion_llm())