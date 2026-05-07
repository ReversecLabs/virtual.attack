# Snapshot VM in vCenter

## Component
**vCenter**

## MITRE ATT&CK
- **ID:** T1003
- **Tactic:** Collection

## Description
Snapshots of running VMs can be taken from vCenter, that capture the memory state and contain disk fragments. The snapshot artefacts are then stored in shared storage, allowing an attacker to Export them for analysis in an attempt to extract in-memory credentials.

## Threat Actors
- UNC5221
- WARP PANDA

## Log Sources
- VPXD Logs (/var/log/vmware/vpxd/vpxd.log)

## References
- https://www.crowdstrike.com/en-us/blog/warp-panda-cloud-threats/

## Author
Leonidas Tsaousis (@laripping)
