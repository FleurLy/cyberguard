techniques_attaque = {
    "T1110" : {
        "name": "Brute Force",
        "sub-techniques" : [ "T1110.001", "T1110.002", "T1110.003", "T1110.004" ],
        "description" : "Adversaries may use brute force techniques to gain access to accounts when passwords are unknown or when password hashes are obtained. Without knowledge of the password for an account or set of accounts, an adversary may systematically guess the password using a repetitive or iterative mechanism. Brute forcing passwords can take place via interaction with a service that will check the validity of those credentials or offline against previously acquired credential data, such as password hashes. Brute forcing credentials may take place at various points during a breach. For example, adversaries may attempt to brute force access to Valid Accounts within a victim environment leveraging knowledge gathered from other post-compromise behaviors such as OS Credential Dumping, Account Discovery, or Password Policy Discovery. Adversaries may also combine brute forcing activity with behaviors such as External Remote Services as part of Initial Access. If an adversary guesses the correct password but fails to login to a compromised account due to location-based conditional access policies, they may change their infrastructure until they match the victim’s location and therefore bypass those policies.",
        "detection" : "Brute Force Authentification Failures with Multi-Platform Log Correlation",
        "mitigation" : "Account Use Policies, Multi-factor Authentication, Password Policies,  	User Account Management"
    },
    "T1059" : {
        "name": "Command and Scripting Interpreter",
        "sub-techniques" : [ "T1059.001", "T1059.002", "T1059.003", "T1059.004", "T1059.005", "T1059.006", "T1059.007", "T1059.008" ,  "T1059.009", "T1059.010", "T1059.011", "T1059.012", "T1059.013"],
        "description" : "Adversaries may attempt to insert a code on the active terminal or a document trying to communicate directly with the OS- the system- so they can have a full control  or more power over commands. They can talk directly  with the system and give it commands to execute them, wich can be harmful  to the system, we can give the example of the command: rm -r ~/, altough this one is not usually a command given directly by  an attacker but it still too dangerous and can be communicated to the system in a secret way.",
        "detection" : "Behavioral Detection of Command and Scripting Interpreter Abuse",
        "mitigation" : " 	Antivirus/Antimalware, Audit, Behavior Prevention on Endpoint, Code Signing, Disable or Remove Feature or Program, Execution Prevention, Limit Software Installation, Privileged Account Management, Restrict Web-Based Content"
    },
    "T1078" : {
        "name": "Valid Accounts",
        "sub-techniques" : [ "T1078.001", "T1078.002", "T1078.003", "T1078.004" ],
        "description" : "dversaries may obtain and abuse credentials of existing accounts as a means of gaining Initial Access, Persistence, Privilege Escalation, or Defense Evasion. Compromised credentials may be used to bypass access controls placed on various resources on systems within the network and may even be used for persistent access to remote systems and externally available services, such as VPNs, Outlook Web Access, network devices, and remote desktop. Compromised credentials may also grant an adversary increased privilege to specific systems or access to restricted areas of the network. Adversaries may choose not to use malware or tools in conjunction with the legitimate access those credentials provide to make it harder to detect their presence.",
        "detection" : "Detection of Valid Account Abuse Across Platforms",
        "mitigation" : "Account Use Policies, Active Directory Configuration, Application Developer Guidance,  	Multi-factor Authentication, Password Policies, Privileged Account Management, User Account Management, User Training"
    }
}