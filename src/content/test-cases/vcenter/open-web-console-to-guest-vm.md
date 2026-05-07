# Open Web Console to Guest VM

## Component
**vCenter**

## MITRE ATT&CK
- **ID:** T1021
- **Tactic:** Lateral Movement

## Description
From the vCenter UI, an attacker can launch a web console to any Powered On guest, and attempt to authenticate using plaintext credentials, or abuse existing sessions

## Threat Actors
_None_

## Log Sources
- VPXD Logs (/var/log/vmware/vpxd/vpxd.log)

## References
- https://cloud.google.com/blog/topics/threat-intelligence/vsphere-active-directory-integration-risks
- https://williamlam.com/2016/07/how-to-audit-vsphere-standalone-vmrc-or-html5-vmrc-connections.html

## Author
Leonidas Tsaousis (@laripping)
