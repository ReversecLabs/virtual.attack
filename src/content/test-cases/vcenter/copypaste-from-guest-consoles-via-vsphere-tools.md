# Copy/Paste from Guest Consoles via vSphere Tools

## Component
**vCenter**

## MITRE ATT&CK
- **ID:** T1005
- **Tactic:** Collection

## Description
Through vCenter, web or VMRC consoles can be launched into powered-on VMs. The latter method allows copy/paste subject to VM configuration, which could allow attackers to exfiltrate credentials or secrets through the clipboard

## Threat Actors
_None_

## Log Sources
- VPXD Logs (/var/log/vmware/vpxd/vpxd.log)
- HOSTD Logs (/var/log/hostd.log)
- Per-VM Logs (/vmfs/volumes/<datastore>/<vm>/vmware.log)

## References
- https://cloud.google.com/blog/topics/threat-intelligence/vsphere-active-directory-integration-risks

## Author
Leonidas Tsaousis (@laripping)
