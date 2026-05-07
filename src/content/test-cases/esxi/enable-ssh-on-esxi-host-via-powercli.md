# Enable SSH on ESXi Host via PowerCLI

## Component
**ESXi**

## MITRE ATT&CK
- **ID:** T1021.004
- **Tactic:** Lateral Movement

## Description
Adversaries with valid vCenter credentials use VMware PowerCLI from a privileged session to enable the SSH service on a managed ESXi host. Test (from a PowerCLI session already connected to vCenter): `Connect-VIServer -Server <vc>; Get-VMHostService -VMHost <esxi> | Where-Object { $_.Key -eq "TSM-SSH" } | Start-VMHostService -Confirm:$false`. Distinct from "Enable SSH on ESXi Host from vCenter" because PowerCLI invocations leave a different log signature than UI/REST sessions, and from "Enable SSH on ESXi Host via vim-cmd" because this variant goes through vCenter rather than directly on the host.

## Threat Actors
- UNC3944
- Scattered Spider
- Octo Tempest
- 0ktapus
- Muddled Libra
- Abyss Locker

## Log Sources
- VPXD Logs (/var/log/vmware/vpxd/vpxd.log)
- HOSTD Logs (/var/log/hostd.log)
- Auth Logs (/var/log/auth.log)

## References
- https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1021.004/T1021.004.md
- https://www.sygnia.co/blog/abyss-locker-ransomware-targeting-esxi/

## Author
Atomic Red Team
