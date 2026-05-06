import re 

class SecurityEvent:
    def __init__(self, timestamp, source_ip, event_type, severity):
        self.timestamp = timestamp
        self.source_ip = source_ip
        self.event_type = event_type
        self.severity = severity

class LogCollector:
    def __init__(self, text):
        self.text =  text

    def parse(self):
        match =  re.search(r"[A-Za-z]+\s+\d+\s+\d{2}:\d{2}:\d{2}", self.text)
        match2 = re.search(r"\d+\.\d+\.\d+\.\d+", self.text)
        match3 = re.search(r"Failed|Accepted", self.text)
        
        if not match or not match2 or not match3:
            raise ValueError("Log non reconnu : impossible de parser la ligne")

        event_type = "ssh_auth_failure" if "Failed" in match3.group() else "ssh_auth_success"
        return SecurityEvent(
                timestamp = str(match.group()),
                source_ip = str(match2.group()),
                event_type = event_type,
                severity = "medium" if "ssh_auth_failure" in event_type else "low"
                )
            

line = "May  3 14:22:01 server sshd[1234]: Failed password for root from 185.220.101.5"

collector = LogCollector(line)
event = collector.parse()

print(event.timestamp)
print(event.source_ip)
print(event.event_type)
print(event.severity)

collector2 = LogCollector("bonjour je suis une ligne quelconque")
event2 = collector2.parse()
print(event2)