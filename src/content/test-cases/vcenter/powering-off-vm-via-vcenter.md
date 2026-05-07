# Powering Off VM via vCenter

## Component
**vCenter**

## MITRE ATT&CK
- **ID:** T1529
- **Tactic:** Impact

## Description
Attackers might proceed to power off VMs in vCenter in preparation for encryption or in order to detach virtual disks (vmdk) containing sensitive data such as Active Directory credential databases (NTDS)

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
- VMKernel Logs (/var/log/vmkernel.log)
- ESXi Shell Logs (/var/log/shell.log)

## References
- https://cloud.google.com/blog/topics/threat-intelligence/defending-vsphere-from-unc3944
- https://www.crowdstrike.com/en-us/blog/carbon-spider-sprite-spider-target-esxi-servers-with-ransomware/

## Author
Leonidas Tsaousis (@laripping)
