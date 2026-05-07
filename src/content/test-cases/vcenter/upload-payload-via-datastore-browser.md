# Upload Payload via Datastore Browser

## Component
**vCenter**

## MITRE ATT&CK
- **ID:** T1105
- **Tactic:** Command and Control

## Description
With vCenter or ESXi access, the attacker uses the Datastore Browser to upload arbitrary binaries (e.g. ransomware encryptors, scripts) to a shared VMFS datastore. Files placed on a datastore are accessible from every host that mounts it, providing a stealthy delivery vector. UNC3944 used this to stage ESXi ransomware payloads.

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

## References
- https://cloud.google.com/blog/topics/threat-intelligence/defending-vsphere-from-unc3944
- https://www.crowdstrike.com/en-us/blog/carbon-spider-sprite-spider-target-esxi-servers-with-ransomware/

## Author
Leonidas Tsaousis (@laripping)
