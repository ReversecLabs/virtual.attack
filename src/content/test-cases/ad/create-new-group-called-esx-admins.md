# Create new group called "ESX Admins"

## Component
**AD**

## MITRE ATT&CK
- **ID:** T1136.002
- **Tactic:** Privilege Escalation

## Description
Exploits CVE-2024-37085: AD-joined ESXi hosts auto-grant full admin to any member of an AD group named 'ESX Admins' (default value of Config.HostAgent.plugins.hostsvc.esxAdminsGroup). Test: net group "ESX Admins" /domain /add ; net group "ESX Admins" <user> /domain /add ; then verify the test user obtains root/full admin on a domain-joined ESXi host via DCUI/SSH/Host Client.

## Threat Actors
- Storm-0506
- Storm-1175
- Octo Tempest
- Manatee Tempest

## Log Sources
- AD Security Event Log (Security.evtx)
- HOSTD Logs (/var/log/hostd.log)
- Auth Logs (/var/log/auth.log)

## References
- https://www.microsoft.com/en-us/security/blog/2024/07/29/ransomware-operators-exploit-esxi-hypervisor-vulnerability-for-mass-encryption/

## Author
Leonidas Tsaousis (@laripping)
