from agents.collector import LogCollector 
from agents.knowledge import KnowledgeAgent
from agents.analyzer import Analyzer

class App:
    def __init__(self, collector : LogCollector, analyzer : Analyzer):
        self.collector = collector
        self.analyzer = analyzer
    
    def run(self):
        # -----------------------------
        # Etape 1 : Collecte de données
        # -----------------------------
        logs = self.collector.parse()

        # -----------------------------
        # Etape 2 : Connaissances
        # -----------------------------
        knowledge = KnowledgeAgent()

        # -----------------------------
        # Etape 3 : Analyse
        # -----------------------------
        analysis_result = self.analyzer.connexion_llm(knowledge)
        return analysis_result
    

from agents.collector import LogCollector
from agents.knowledge import KnowledgeAgent
from agents.analyzer import Analyzer

line = "May  3 14:22:01 server sshd[1234]: Failed password for root from 185.220.101.5"

# Étape 1 — Collecter
collector = LogCollector(line)
event = collector.parse()

# Étape 2 — Connaissances
knowledge = KnowledgeAgent()

# Étape 3 — Analyser
analyzer = Analyzer(event)
print(analyzer.connexion_llm(knowledge))