# Timestomp via Touch

## Component
**ESXi**

## MITRE ATT&CK
- **ID:** T1070.006
- **Tactic:** Defense Evasion

## Description
Adversaries with shell access on an ESXi host modify the timestamps of files they have dropped, replaced, or edited. This can be achieved using the command `touch -r` available on PhotonOS. 

## Threat Actors
- ESXiArgs

## Log Sources
- ESXi Shell Logs (/var/log/shell.log)

## References
- https://www.elastic.co/guide/en/security/8.19/esxi-timestomping-using-touch-command.html
- https://trustedsec.com/blog/esxiargs-what-you-need-to-know-and-how-to-protect-your-data 
- https://blogs.juniper.net/en-us/threat-research/a-custom-python-backdoor-for-vmware-esxi-servers 
- https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-039a

## Author
Leonidas Tsaousis (@laripping)
