# Enable SSH on ESXi Host from vCenter

## Component
**ESXi**

## MITRE ATT&CK
- **ID:** T1021.004
- **Tactic:** Lateral Movement

## Description
With vCenter privileges, the attacker enables the SSH service on managed ESXi hosts (Configure -> Services -> SSH -> Start) then SSH directly to the host using the vpxuser or freshly-reset root credential. UNC3944 documented enabling SSH on ESXi as a precursor to interactive shell access on the hypervisor for ransomware deployment.

## Threat Actors
- UNC3944
- Scattered Spider
- Octo Tempest
- 0ktapus
- Muddled Libra
- SPRITE SPIDER
- CARBON SPIDER

## Log Sources
- VPXD Logs (/var/log/vmware/vpxd/vpxd.log)
- HOSTD Logs (/var/log/hostd.log)
- Auth Logs (/var/log/auth.log)

## References
- https://cloud.google.com/blog/topics/threat-intelligence/defending-vsphere-from-unc3944
- https://www.crowdstrike.com/en-us/blog/carbon-spider-sprite-spider-target-esxi-servers-with-ransomware/
- https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/

## Author
Atomic Red Team
