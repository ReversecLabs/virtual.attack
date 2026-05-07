# Add user to VMWare Admin group in AD

## Component
**AD**

## MITRE ATT&CK
- **ID:** T1098
- **Tactic:** Privilege Escalation

## Description
In environments where VMWare is integrated with AD, members of the relevant AD group will obtain privileged access to the VCF administration.

## Threat Actors
- UNC3944
- Scattered Spider
- Octo Tempest
- 0ktapus
- Muddled Libra
- SPRITE SPIDER

## Log Sources
- AD Security Event Log (Security.evtx)

## References
- https://cloud.google.com/blog/topics/threat-intelligence/vsphere-active-directory-integration-risks
https://cloud.google.com/blog/topics/threat-intelligence/defending-vsphere-from-unc3944
- https://www.crowdstrike.com/en-us/blog/carbon-spider-sprite-spider-target-esxi-servers-with-ransomware/

## Author
Leonidas Tsaousis (@laripping)
