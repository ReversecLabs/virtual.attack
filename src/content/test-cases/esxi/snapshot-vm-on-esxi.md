# Snapshot VM on ESXi

## Component
**ESXi**

## MITRE ATT&CK
- **ID:** T1003
- **Tactic:** Collection

## Description
Snapshots of running VMs can be taken from ESXi hosts, that capture the memory state and contain disk fragments. The snapshot artefacts are then stored in shared storage, allowing an attacker to exfiltrate them for analysis in an attempt to extract in-memory credentials. The vim-cmd native utility can be used for this purpose: vim-cmd /vmsvc/snapshot.create

## Threat Actors
- UNC5221
- WARP PANDA

## Log Sources
- HOSTD Logs (/var/log/hostd.log)
- ESXi Shell Logs (/var/log/shell.log)

## References
- https://www.crowdstrike.com/en-us/blog/warp-panda-cloud-threats/

## Author
Leonidas Tsaousis (@laripping)
