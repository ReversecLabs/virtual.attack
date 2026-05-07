# Mass-Encrypt VMFS Datastore from ESXi Shell

## Component
**ESXi**

## MITRE ATT&CK
- **ID:** T1486
- **Tactic:** Impact

## Description
With root SSH on ESXi, the attacker stages and runs a Linux ransomware binary (e.g. Akira ESXi variant, Black Basta ESXi, RansomEXX) targeting .vmdk and .vmx files on mounted VMFS datastores, often after powering off all VMs. Encryption is performed in-place at hypervisor level, affecting all guests simultaneously without in-guest access.

## Threat Actors
- UNC3944
- Scattered Spider
- Octo Tempest
- 0ktapus
- Muddled Libra
- SPRITE SPIDER
- CARBON SPIDER
- FERAL SPIDER
- CYBORG SPIDER
- PINCHY SPIDER
- VIKING SPIDER
- ALPHA SPIDER
- BITWISE SPIDER
- Babuk Locker
- MichaelKors

## Log Sources
- HOSTD Logs (/var/log/hostd.log)
- ESXi Shell Logs (/var/log/shell.log)
- VMKernel Logs (/var/log/vmkernel.log)

## References
- https://cloud.google.com/blog/topics/threat-intelligence/defending-vsphere-from-unc3944
- https://www.crowdstrike.com/en-us/blog/carbon-spider-sprite-spider-target-esxi-servers-with-ransomware/
- https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/
- https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-lack-of-antivirus-support-opens-the-door-to-adversaries/

## Author
Leonidas Tsaousis (@laripping)
