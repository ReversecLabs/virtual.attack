# Attach Cloned or Detached VMDK to Attacker-Controlled VM

## Component
**vCenter**

## MITRE ATT&CK
- **ID:** T1005
- **Tactic:** Collection

## Description
After cloning or detaching a VMDK from a high-value VM (e.g. an NTDS.dit-bearing DC disk; see "Detach VMDK via vCenter"), the attacker attaches that VMDK as a secondary disk to a VM they control - typically a temporary attacker-built Linux VM - and mounts the disk to extract files offline. This is the consumption step that turns disk theft into credential / data extraction.

## Threat Actors
- UNC3944
- Scattered Spider
- Octo Tempest
- 0ktapus
- Muddled Libra

## Log Sources
- VPXD Logs (/var/log/vmware/vpxd/vpxd.log)
- HOSTD Logs (/var/log/hostd.log)

## References
- https://cloud.google.com/blog/topics/threat-intelligence/defending-vsphere-from-unc3944

## Author
Leonidas Tsaousis (@laripping)
