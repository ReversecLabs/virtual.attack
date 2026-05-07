# System Information Discovery on ESXi

## Component
**ESXi**

## MITRE ATT&CK
- **ID:** T1082
- **Tactic:** Discovery

## Description
Adversaries fingerprint an ESXi host via ESXCLI to gather build version, hostname, and patch level - feeding decisions about which CVEs (e.g. CVE-2023-20867, CVE-2024-37085) to attempt. Test (from a privileged shell session): `esxcli system hostname get; esxcli system version get; esxcli software profile get`. Documented as part of Darkside and other ESXi-targeting ransomware operations.

## Threat Actors
- DarkSide
- SPRITE SPIDER

## Log Sources
- ESXi Shell Logs (/var/log/shell.log)

## References
- https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.md
- https://www.crowdstrike.com/en-us/blog/carbon-spider-sprite-spider-target-esxi-servers-with-ransomware/

## Author
Atomic Red Team
