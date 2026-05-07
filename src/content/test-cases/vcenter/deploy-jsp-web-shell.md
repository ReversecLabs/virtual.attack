# Deploy JSP Web Shell

## Component
**vCenter**

## MITRE ATT&CK
- **ID:** T1505.003
- **Tactic:** Persistence

## Description
Mandiant documented BRICKSTORM operators deploying a JavaServer Pages (JSP) web shell tracked as SLAYSTYLE (aka BEEFLUSH) into the Tomcat-hosted vCenter web interface to receive and execute arbitrary OS commands passed via HTTP requests. Test: drop a benign JSP file into a Tomcat webapp directory and confirm execution from a remote HTTP request.

## Threat Actors
- UNC5221
- WARP PANDA

## Log Sources
- vSphere UI Tomcat Logs (/var/log/vmware/vsphere-ui/logs/)
- rhttpproxy Logs (/var/log/vmware/rhttpproxy/rhttpproxy.log)

## References
- https://cloud.google.com/blog/topics/threat-intelligence/brickstorm-espionage-campaign

## Author
Leonidas Tsaousis (@laripping)
