import pytest
from agents.collector import LogCollector, SecurityEvent


LOG_VALIDE = "May  3 14:22:01 server sshd[1234]: Failed password for root from 185.220.101.5"
LOG_INVALIDE = "Ce texte ne contient pas les éléments nécessaires"
LOG_INVALIDE_IP = "May  3 14:22:01 server sshd[1234]: Failed password for root from "
LOG_INVALIDE_EVNT = "May  3 14:22:01 server sshd[1234]: for root from 185.220.101.5"
LOG_INVALIDE_TIME = " server sshd[1234]: Failed password for root from 185.220.101.5"

def test_erreur():
    with pytest.raises(ValueError):
        LogCollector(LOG_INVALIDE).parse()

def test_parse_retourne_security_event():
    event = LogCollector(LOG_VALIDE).parse()
    assert isinstance(event, SecurityEvent)

def test_source_ip():
    event = LogCollector(LOG_VALIDE).parse()
    assert (event != None) and (event.source_ip == "185.220.101.5")

def test_event_type():
    event = LogCollector(LOG_VALIDE).parse()
    assert (event != None) and (event.event_type == "ssh_auth_failure")

def test_severity():
    event = LogCollector(LOG_VALIDE).parse()
    assert (event != None) and (event.severity == "medium")

def test_erreur_source_ip():
    with pytest.raises(ValueError):
        LogCollector(LOG_INVALIDE_IP).parse()

def test_erreur_event_type():
    with pytest.raises(ValueError):
        LogCollector(LOG_INVALIDE_EVNT).parse()

def test_erreur_time():
    with pytest.raises(ValueError):
        LogCollector(LOG_INVALIDE_TIME).parse()