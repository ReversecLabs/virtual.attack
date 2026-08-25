# Add user to VMware admin group in vIDM

## Component
**vIDM**

## MITRE ATT&CK
- **ID:** T1098
- **Tactic:** Privilege Escalation

## Description
An alternate method of acquiring Administrative permissions could be through direct modification of the vIDM groups

## Threat Actors
_None_

## Log Sources
- Workspace ONE Audit Events (admin UI report)
- Workspace ONE Application Logs (/opt/vmware/horizon/workspace/logs/horizon.log)
- Workspace ONE Connector Logs (/opt/vmware/horizon/workspace/logs/connector.log)

## References
- https://knowledge.broadcom.com/external/article/367432/collecting-vmware-workspace-one-access-a.html

## Author
Leonidas Tsaousis (@laripping)
