# Change VIB Acceptance Level to CommunitySupported

## Component
**ESXi**

## MITRE ATT&CK
- **ID:** T1562.010
- **Tactic:** Defense Evasion

## Description
Adversaries downgrade the host VIB acceptance criteria from PartnerSupported (default) to CommunitySupported, opening the door to subsequent installation of unsigned community VIBs (see "Install Custom VIB on ESXi for Persistence"). Test (from a privileged ESXi shell): `esxcli software acceptance set --level=CommunitySupported`. Test (from a privileged PowerCLI session): `(Get-EsxCli -VMHost <host> -V2).software.acceptance.set.Invoke(@{level = "CommunitySupported"})`.

## Threat Actors
- UNC3886
- Fire Ant

## Log Sources
- esxupdate Logs (/var/log/esxupdate.log)
- HOSTD Logs (/var/log/hostd.log)
- ESXi Shell Logs (/var/log/shell.log)

## References
- https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.010/T1562.010.md
- https://www.sygnia.co/blog/fire-ant-a-deep-dive-into-hypervisor-level-espionage/
- https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence

## Author
Atomic Red Team
