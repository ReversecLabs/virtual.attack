# Delete VM Snapshots on ESXi

## Component
**ESXi**

## MITRE ATT&CK
- **ID:** T1485
- **Tactic:** Impact

## Description
Adversaries delete VM snapshots on an ESXi host to prevent rollback as part of pre-encryption preparation, removing point-in-time recovery points before ransomware deployment. Test (from a privileged ESXi shell session): `for vm in $(vim-cmd vmsvc/getallvms | awk 'NR>1 {print $1}'); do vim-cmd vmsvc/snapshot.removeall $vm; done`. ATT&CK maps this to T1485 per ART; arguably overlaps with T1490 (Inhibit System Recovery).

## Threat Actors
- UNC3944
- Scattered Spider
- Octo Tempest
- 0ktapus
- Muddled Libra

## Log Sources
- HOSTD Logs (/var/log/hostd.log)
- ESXi Shell Logs (/var/log/shell.log)

## References
- https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1485/T1485.md
- https://lolesxi-project.github.io/LOLESXi/lolesxi/Binaries/vim-cmd/

## Author
AlbinoGazelle (Atomic Red Team)
