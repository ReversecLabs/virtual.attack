# Rename existing group to "ESX Admins"

## Component
**AD**

## MITRE ATT&CK
- **ID:** T1098
- **Tactic:** Privilege Escalation

## Description
CVE-2024-37085 variant: rather than creating a new group, the attacker renames an existing AD group they already control members of to 'ESX Admins'. Because ESXi matches on group name only (not SID), the renamed group's existing members instantly inherit full admin on every joined ESXi host. Test: rename a benign group (e.g. HelpDesk-L1) containing a test user to 'ESX Admins' via Set-ADGroup/Rename-ADObject and verify root on the ESXi host.

## Threat Actors
_None_

## Log Sources
- AD Security Event Log (Security.evtx)
- HOSTD Logs (/var/log/hostd.log)

## References
- https://www.microsoft.com/en-us/security/blog/2024/07/29/ransomware-operators-exploit-esxi-hypervisor-vulnerability-for-mass-encryption/

## Author
Leonidas Tsaousis (@laripping)
