# Local Account Discovery on ESXi

## Component
**ESXi**

## MITRE ATT&CK
- **ID:** T1087.001
- **Tactic:** Discovery

## Description
Adversaries enumerate local accounts on an ESXi host to identify additional principals (e.g. dcui, vpxuser, custom service accounts) for credential-targeted follow-on actions. Test (from a privileged shell session): `esxcli system account list`. Pairs with vpxuser extraction (see "Extract vpxuser Service Account Credentials from vCenter") for full principal mapping across the cluster.

## Threat Actors
_None_

## Log Sources
- ESXi Shell Logs (/var/log/shell.log)

## References
- https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.001/T1087.001.md

## Author
AlbinoGazelle (Atomic Red Team)
