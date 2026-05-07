# Process Discovery on ESXi

## Component
**ESXi**

## MITRE ATT&CK
- **ID:** T1057
- **Tactic:** Discovery

## Description
Adversaries enumerate processes running on an ESXi host to identify VM worker processes (vmx-*), management agents (hostd, vpxa), and security tooling. Test (from a privileged shell session): `ps -c | head` or `esxcli system process list`. Used by Sygnia-observed Fire Ant operators and ESXi-targeting ransomware to confirm host inventory before subsequent actions.

## Threat Actors
- Abyss Locker

## Log Sources
- ESXi Shell Logs (/var/log/shell.log)

## References
- https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1057/T1057.md

## Author
Atomic Red Team
