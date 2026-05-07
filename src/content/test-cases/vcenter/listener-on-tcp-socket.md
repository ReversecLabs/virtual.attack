# Listener on TCP Socket

## Component
**vCenter**

## MITRE ATT&CK
- **ID:** T1071
- **Tactic:** Command and Control

## Description
In the FireAnt incident, the threat actor deployed a persistent backdoor binary on vCenter servers that listened on TCP port 7475 and enabled remote command execution and file operations. To simulate this, a test ELF binary can be compiled that binds a TCP port which clients can then connect to. 

## Threat Actors
- UNC3886
- Fire Ant

## Log Sources
- custom Audit configuration needed (/var/log/audit/audit.log)

## References
- https://www.sygnia.co/blog/fire-ant-a-deep-dive-into-hypervisor-level-espionage/


## Author
Leonidas Tsaousis (@laripping)
