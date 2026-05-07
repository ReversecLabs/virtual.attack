# Backdoor Image ISO

## Component
**vCenter**

## MITRE ATT&CK
- **ID:** T1525
- **Tactic:** Persistence

## Description
Attacker with access to vCenter could upload backdoored ISO images for VMs in the vSphere Content Library, which would be used for future VM deployments.

## Threat Actors
_None_

## Log Sources
- VPXD Logs (/var/log/vmware/vpxd/vpxd.log)

## References
- https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/using-content-libraries.html
- https://cloud.google.com/blog/topics/threat-intelligence/defending-vsphere-from-unc3944

## Author
Leonidas Tsaousis (@laripping)
