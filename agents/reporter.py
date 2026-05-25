
from agents.analyzer import Analyzer
from agents.knowledge import KnowledgeAgent
from datetime import datetime


class Report:
    def __init__(self, analyzer : Analyzer, knowledge_agent : KnowledgeAgent):
        self.analyzer = analyzer
        self.knowledge_agent = knowledge_agent
        self.reponse = self.analyzer.connexion_llm(self.knowledge_agent)

    def generate(self):
        with open('reports/output/report.md', 'w') as f:
            date = datetime.now().strftime("%Y-%m-%d")
            f.write(f"# Rapport d'incident — {date}\n\n")
            # f.close()

            # f = open('reports/output/report.md', 'a')
            f.write("## Résumé \n\n")
            chaine = ""
            chaine += "- Timestamp : " + self.analyzer.security_event.timestamp + "\n"
            chaine += "- IP source : " + self.analyzer.security_event.source_ip + "\n"
            chaine += "- Type : " + self.analyzer.security_event.event_type + "\n"
            chaine += "- Sévérité : " + self.analyzer.security_event.severity + "\n"
            f.write(chaine)
            f.write("\n\n## Analyse LLM \n\n")
            f.write(self.reponse)
            f.write("\n\n## Statut \n\n")
            f.write("Rapport généré automatiquement par CyberGuard AI")


from agents.collector import LogCollector
# from knowledge import KnowledgeAgent
# from analyzer import Analyzer

line = "May  3 14:22:01 server sshd[1234]: Failed password for root from 185.220.101.5"
event = LogCollector(line).parse()
knowledge = KnowledgeAgent()
analyzer = Analyzer(event)
reporter = Report(analyzer, knowledge)
reporter.generate()