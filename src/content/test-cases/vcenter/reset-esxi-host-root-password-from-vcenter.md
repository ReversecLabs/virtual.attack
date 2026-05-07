# Reset ESXi Host Root Password from vCenter

## Component
**vCenter**

## MITRE ATT&CK
- **ID:** T1098
- **Tactic:** Privilege Escalation

## Description
With sufficient vCenter privileges, the attacker resets the root password on managed ESXi hosts via the vSphere UI/API or host profiles, locking out legitimate administrators and pinning exclusive root access to the attacker-controlled credential. Mandiant documented UNC3944 doing this during ransomware operations.

## Threat Actors
- UNC3944
- Scattered Spider
- Octo Tempest
- 0ktapus
- Muddled Libra
- SPRITE SPIDER

## Log Sources
- VPXD Logs (/var/log/vmware/vpxd/vpxd.log)
- HOSTD Logs (/var/log/hostd.log)
- Auth Logs (/var/log/auth.log)

## References
- https://cloud.google.com/blog/topics/threat-intelligence/defending-vsphere-from-unc3944
- https://www.crowdstrike.com/en-us/blog/carbon-spider-sprite-spider-target-esxi-servers-with-ransomware/

## Author
Leonidas Tsaousis (@laripping)
