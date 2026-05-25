from agents import analyzer
from agents.collector import LogCollector 
from agents.knowledge import KnowledgeAgent
from agents.analyzer import Analyzer
from agents.reporter import Report

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

# line = "May  3 14:22:01 server sshd[1234]: Failed password for root from 185.220.101.5"



import streamlit as st

# Titre
st.title("CyberGuard AI")

# Zone de texte
logs = st.text_area("Colle tes logs ici")

# Bouton
if st.button("Analyser"):
    collector = LogCollector(logs)
    event = collector.parse()
    knowledge = KnowledgeAgent()
    analyzer = Analyzer(event)
    
    # Reporter génère le fichier
    reporter = Report(analyzer, knowledge)
    reporter.generate()
    
    # Afficher l'analyse
    st.markdown(reporter.reponse)
    
    # Lire le fichier généré et proposer le téléchargement
    with open("reports/output/report.md", "r") as f:
        contenu = f.read()
    
    st.download_button(
        label="Télécharger le rapport",
        data=contenu,
        file_name="report.md",
        mime="text/markdown"
    )