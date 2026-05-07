# Detach VMDK via vCenter

## Component
**vCenter**

## MITRE ATT&CK
- **ID:** T1005
- **Tactic:** Collection

## Description
Having identified critical VMs such as Active Directory Domain Controllers on vCenter, attackers might proceed to power them off, and then detach virtual disks (vmdk) containing sensitive data such as the NTDS database, which could then be attached to rogue VMs in their control, or exported.

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
