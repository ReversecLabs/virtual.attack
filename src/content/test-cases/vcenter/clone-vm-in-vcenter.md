# Clone VM in vCenter

## Component
**vCenter**

## MITRE ATT&CK
- **ID:** T1005
- **Tactic:** Collection

## Description
Using compromised vCenter SSO credentials (typically VSPHERE.LOCAL\Administrator), the attacker clones high-value VMs (Domain Controllers, IdPs, secret vaults) without powering on the clone. The cloned VMDK is then mounted offline or downloaded to extract sensitive files such as NTDS.dit, registry hives or mailbox stores, bypassing in-guest EDR. Mandiant observed BRICKSTORM operators performing this between 01:00-10:00 UTC, deleting the clone immediately after extraction.

## Threat Actors
- UNC5221
- WARP PANDA

## Log Sources
- VPXD Logs (/var/log/vmware/vpxd/vpxd.log)

## References
- https://cloud.google.com/blog/topics/threat-intelligence/brickstorm-espionage-campaign

## Author
Leonidas Tsaousis (@laripping)
