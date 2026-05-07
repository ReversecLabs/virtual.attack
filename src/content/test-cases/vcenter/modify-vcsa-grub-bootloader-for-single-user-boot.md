# Modify VCSA GRUB Bootloader for Single-User Boot

## Component
**vCenter**

## MITRE ATT&CK
- **ID:** T1542.003
- **Tactic:** Defense Evasion

## Description
With console access to the VCSA (via vSphere Web Console / MKS), the attacker reboots and edits the GRUB boot entry to append `init=/bin/bash` or `single` to the kernel command line. The VCSA then boots into a root shell without password authentication, granting "virtual physical access" equivalent. UNC3944 documented this against VCSA and other Linux appliances.

## Threat Actors
- UNC3944
- Scattered Spider
- Octo Tempest
- 0ktapus
- Muddled Libra

## Log Sources
- VPXD Logs (/var/log/vmware/vpxd/vpxd.log)
- System Messages (/var/log/messages)
- Auth Logs (/var/log/auth.log)

## References
- https://cloud.google.com/blog/topics/threat-intelligence/defending-vsphere-from-unc3944

## Author
Leonidas Tsaousis (@laripping)
