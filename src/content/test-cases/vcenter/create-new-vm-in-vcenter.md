# Create New VM in vCenter

## Component
**vCenter**

## MITRE ATT&CK
- **ID:** T1564.006
- **Tactic:** Defense Evasion

## Description
Following successful vCenter breach, attackers might proceed to create new VMs through the UI in order to interact with other guests, establish long-term access, or move laterally through data-plane networking.
Can be combined with Defense Evasion techniques such as matching legitimate / existing names (T1036.005)

## Threat Actors
- UNC5221
- WARP PANDA

## Log Sources
- VPXD Logs (/var/log/vmware/vpxd/vpxd.log)

## References
- https://ctid.mitre.org/blog/2024/05/22/infiltrating-defenses-abusing-vmware-in-mitres-cyber-intrusion/

## Author
Leonidas Tsaousis (@laripping)
